import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ARPromissoryNotesSvc
// Description: The AR promissory note service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/$metadata", {
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
   Description: Get ARPromissoryNotes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPromissoryNotes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadRow
   */  
export function get_ARPromissoryNotes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPromissoryNotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARPromissoryNotes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARPromissoryNote item
   Description: Calls GetByID to retrieve the ARPromissoryNote item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPromissoryNote
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   */  
export function get_ARPromissoryNotes_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ARPNHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARPromissoryNote for the service
   Description: Calls UpdateExt to update ARPromissoryNote. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPromissoryNote
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARPromissoryNotes_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete ARPromissoryNote item
   Description: Call UpdateExt to delete ARPromissoryNote item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPromissoryNote
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARPromissoryNotes_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Description: Get BankTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTrans1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranRow
   */  
export function get_ARPromissoryNotes_Company_GroupID_HeadNum_BankTrans(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/BankTrans", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BankTran item
   Description: Calls GetByID to retrieve the BankTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTran1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranRow
   */  
export function get_ARPromissoryNotes_Company_GroupID_HeadNum_BankTrans_Company_BankAcctID_TranNum_Voided(Company:string, GroupID:string, HeadNum:string, BankAcctID:string, TranNum:string, Voided:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BankTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ARPNDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARPNDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNDtlRow
   */  
export function get_ARPromissoryNotes_Company_GroupID_HeadNum_ARPNDtls(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARPNDtl item
   Description: Calls GetByID to retrieve the ARPNDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   */  
export function get_ARPromissoryNotes_Company_GroupID_HeadNum_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ARPNDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TaxDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxDtlRow
   */  
export function get_ARPromissoryNotes_Company_GroupID_HeadNum_TaxDtls(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/TaxDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaxDtl item
   Description: Calls GetByID to retrieve the TaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxDtlRow
   */  
export function get_ARPromissoryNotes_Company_GroupID_HeadNum_TaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, GroupID:string, HeadNum:string, SourceModule:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ARPNHeadTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARPNHeadTGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadTGLCRow
   */  
export function get_ARPromissoryNotes_Company_GroupID_HeadNum_ARPNHeadTGLCs(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNHeadTGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARPNHeadTGLC item
   Description: Calls GetByID to retrieve the ARPNHeadTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNHeadTGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNHeadTGLCRow
   */  
export function get_ARPromissoryNotes_Company_GroupID_HeadNum_ARPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company:string, GroupID:string, HeadNum:string, TGLCTranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNHeadTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ARPNHeadTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ARPNHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARPNHeadAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadAttchRow
   */  
export function get_ARPromissoryNotes_Company_GroupID_HeadNum_ARPNHeadAttches(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARPNHeadAttch item
   Description: Calls GetByID to retrieve the ARPNHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNHeadAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNHeadAttchRow
   */  
export function get_ARPromissoryNotes_Company_GroupID_HeadNum_ARPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company:string, GroupID:string, HeadNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ARPNHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BankTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTrans
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranRow
   */  
export function get_BankTrans(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankTrans(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BankTran item
   Description: Calls GetByID to retrieve the BankTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranRow
   */  
export function get_BankTrans_Company_BankAcctID_TranNum_Voided(Company:string, BankAcctID:string, TranNum:string, Voided:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BankTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BankTran for the service
   Description: Calls UpdateExt to update BankTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankTrans_Company_BankAcctID_TranNum_Voided(Company:string, BankAcctID:string, TranNum:string, Voided:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
   Summary: Call UpdateExt to delete BankTran item
   Description: Call UpdateExt to delete BankTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BankTrans_Company_BankAcctID_TranNum_Voided(Company:string, BankAcctID:string, TranNum:string, Voided:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
   Description: Get BankTranTaxDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTranTaxDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTaxDtlRow
   */  
export function get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTaxDtls(Company:string, BankAcctID:string, TranNum:string, Voided:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BankTranTaxDtl item
   Description: Calls GetByID to retrieve the BankTranTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranTaxDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   */  
export function get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, BankAcctID:string, TranNum:string, Voided:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BankTranTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BankTranTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTranTGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTGLCRow
   */  
export function get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTGLCs(Company:string, BankAcctID:string, TranNum:string, Voided:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BankTranTGLC item
   Description: Calls GetByID to retrieve the BankTranTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranTGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   */  
export function get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company:string, BankAcctID:string, TranNum:string, Voided:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BankTranTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BankTranTaxDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTranTaxDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTaxDtlRow
   */  
export function get_BankTranTaxDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTaxDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankTranTaxDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankTranTaxDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTaxDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BankTranTaxDtl item
   Description: Calls GetByID to retrieve the BankTranTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranTaxDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   */  
export function get_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BankTranTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BankTranTaxDtl for the service
   Description: Calls UpdateExt to update BankTranTaxDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankTranTaxDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete BankTranTaxDtl item
   Description: Call UpdateExt to delete BankTranTaxDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTranTaxDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get BankTranTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTranTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTGLCRow
   */  
export function get_BankTranTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankTranTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankTranTGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BankTranTGLC item
   Description: Calls GetByID to retrieve the BankTranTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   */  
export function get_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company:string, BankAcctID:string, TranNum:string, Voided:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BankTranTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BankTranTGLC for the service
   Description: Calls UpdateExt to update BankTranTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankTranTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company:string, BankAcctID:string, TranNum:string, Voided:string, SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete BankTranTGLC item
   Description: Call UpdateExt to delete BankTranTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTranTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company:string, BankAcctID:string, TranNum:string, Voided:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
   Description: Get ARPNDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNDtlRow
   */  
export function get_ARPNDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARPNDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARPNDtl item
   Description: Calls GetByID to retrieve the ARPNDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   */  
export function get_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ARPNDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARPNDtl for the service
   Description: Calls UpdateExt to update ARPNDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
   Summary: Call UpdateExt to delete ARPNDtl item
   Description: Call UpdateExt to delete ARPNDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
   Description: Get TaxDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxDtlRow
   */  
export function get_TaxDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/TaxDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/TaxDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaxDtl item
   Description: Calls GetByID to retrieve the TaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxDtlRow
   */  
export function get_TaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxDtl for the service
   Description: Calls UpdateExt to update TaxDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete TaxDtl item
   Description: Call UpdateExt to delete TaxDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get ARPNHeadTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNHeadTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadTGLCRow
   */  
export function get_ARPNHeadTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadTGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNHeadTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNHeadTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNHeadTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARPNHeadTGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadTGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARPNHeadTGLC item
   Description: Calls GetByID to retrieve the ARPNHeadTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNHeadTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNHeadTGLCRow
   */  
export function get_ARPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company:string, GroupID:string, HeadNum:string, TGLCTranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNHeadTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ARPNHeadTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARPNHeadTGLC for the service
   Description: Calls UpdateExt to update ARPNHeadTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNHeadTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNHeadTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company:string, GroupID:string, HeadNum:string, TGLCTranNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")", {
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
   Summary: Call UpdateExt to delete ARPNHeadTGLC item
   Description: Call UpdateExt to delete ARPNHeadTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNHeadTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company:string, GroupID:string, HeadNum:string, TGLCTranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")", {
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
   Description: Get ARPNHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadAttchRow
   */  
export function get_ARPNHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARPNHeadAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARPNHeadAttch item
   Description: Calls GetByID to retrieve the ARPNHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNHeadAttchRow
   */  
export function get_ARPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company:string, GroupID:string, HeadNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ARPNHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARPNHeadAttch for the service
   Description: Calls UpdateExt to update ARPNHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company:string, GroupID:string, HeadNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ARPNHeadAttch item
   Description: Call UpdateExt to delete ARPNHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company:string, GroupID:string, HeadNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", {
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
   Description: Get ARPNLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNLists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNListRow
   */  
export function get_ARPNLists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNLists", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARPNLists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNLists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARPNList item
   Description: Calls GetByID to retrieve the ARPNList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNList
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNListRow
   */  
export function get_ARPNLists_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNLists(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ARPNListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARPNList for the service
   Description: Calls UpdateExt to update ARPNList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNList
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARPNLists_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNLists(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete ARPNList item
   Description: Call UpdateExt to delete ARPNList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNList
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARPNLists_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNLists(" + SysRowID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadListRow)
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
export function get_GetRows(whereClauseARPNHead:string, whereClauseARPNHeadAttch:string, whereClauseBankTran:string, whereClauseBankTranTaxDtl:string, whereClauseBankTranTGLC:string, whereClauseARPNDtl:string, whereClauseTaxDtl:string, whereClauseARPNHeadTGLC:string, whereClauseARPNList:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseARPNHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARPNHead=" + whereClauseARPNHead
   }
   if(typeof whereClauseARPNHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARPNHeadAttch=" + whereClauseARPNHeadAttch
   }
   if(typeof whereClauseBankTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBankTran=" + whereClauseBankTran
   }
   if(typeof whereClauseBankTranTaxDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBankTranTaxDtl=" + whereClauseBankTranTaxDtl
   }
   if(typeof whereClauseBankTranTGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBankTranTGLC=" + whereClauseBankTranTGLC
   }
   if(typeof whereClauseARPNDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARPNDtl=" + whereClauseARPNDtl
   }
   if(typeof whereClauseTaxDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxDtl=" + whereClauseTaxDtl
   }
   if(typeof whereClauseARPNHeadTGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARPNHeadTGLC=" + whereClauseARPNHeadTGLC
   }
   if(typeof whereClauseARPNList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARPNList=" + whereClauseARPNList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(groupID:string, headNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof groupID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupID=" + groupID
   }
   if(typeof headNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "headNum=" + headNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetAvailTranDocTypes", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BatchGenPIs
   OperationID: BatchGenPIs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BatchGenPIs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BatchGenPIs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BatchGenPIs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BatchGenPIs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CancelGenPI
   Description: CancelGenPI
   OperationID: CancelGenPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelGenPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelGenPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CancelGenPI(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/CancelGenPI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCurGroupID
   Description: ChangeCurGroupID
   OperationID: ChangeCurGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurGroupID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ChangeCurGroupID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTranAmt
   Description: This method updates the BankTran amounts when the adjustment amount changes or
the currency switch toggles.
   OperationID: ChangeTranAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTranAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ChangeTranAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDocumentIsLocked
   Description: Method to call when it is necessary to check if document is lock, before doing smth.
   OperationID: CheckDocumentIsLocked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDocumentIsLocked(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/CheckDocumentIsLocked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPNoteExisted
   Description: CheckPNoteExisted
   OperationID: CheckPNoteExisted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPNoteExisted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPNoteExisted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPNoteExisted(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/CheckPNoteExisted", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPNotesExistTracker
   Description: Checks to see if any AR Promissory Notes exist for a given promissory note ID
regardless of customer number or PI type
   OperationID: CheckPNotesExistTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPNotesExistTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPNotesExistTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPNotesExistTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/CheckPNotesExistTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateARPNMove
   Description: CreateARPNMove
   OperationID: CreateARPNMove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateARPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateARPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateARPNMove(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/CreateARPNMove", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DelARPNHead
   Description: Delete the AR Payment Instrument
   OperationID: DelARPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DelARPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DelARPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DelARPNHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/DelARPNHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeletePICashGroup
   Description: This method deletes a CashGrp from AR Invoice Entry
   OperationID: DeletePICashGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePICashGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePICashGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeletePICashGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/DeletePICashGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeletePNbyID
   Description: DeletePNbyID
   OperationID: DeletePNbyID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePNbyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePNbyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeletePNbyID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/DeletePNbyID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeletePNotes
   Description: DeletePNotes
   OperationID: DeletePNotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePNotes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePNotes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeletePNotes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/DeletePNotes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteZeroAmtTaxRec
   Description: This method deletes TaxDtl records which have zero amounts
Since Payments TAx logic calculates tax conditionally only for the first tax line the payment could have multiple zero tax records.
   OperationID: DeleteZeroAmtTaxRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteZeroAmtTaxRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteZeroAmtTaxRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteZeroAmtTaxRec(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/DeleteZeroAmtTaxRec", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method KineticFillPNSummary
   Description: Method to call when obtaining the payment schedule for the invoice header.
   OperationID: KineticFillPNSummary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KineticFillPNSummary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KineticFillPNSummary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KineticFillPNSummary(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/KineticFillPNSummary", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FillPNSummary
   Description: Method to call when obtaining the payment schedule for the invoice header.
   OperationID: FillPNSummary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillPNSummary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillPNSummary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FillPNSummary(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/FillPNSummary", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateARPNDtl
   Description: This method combines the GetNewARPNDtl and Update() method into one routine
so that the user can run an "Auto Apply" cash receipt function
   OperationID: GenerateARPNDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateARPNDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateARPNDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateARPNDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GenerateARPNDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateARPNDtls
   Description: This method combines the GetNewARPNDtl and Update() method into one routine
so that the user can run an "Auto Apply" cash receipt function
   OperationID: GenerateARPNDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateARPNDtls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateARPNDtls_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateARPNDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GenerateARPNDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetARPNList
   OperationID: GetARPNList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARPNList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARPNList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetARPNList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetARPNList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetARPNListTracker
   Description: Create a list of ARPN for a certail ARPromNoteID regardless of customer, type or post status
   OperationID: GetARPNListTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARPNListTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARPNListTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetARPNListTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetARPNListTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetARPNMove
   Description: Get the ARPNMove records for an ARPromissoryNote.
   OperationID: GetARPNMove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetARPNMove(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetARPNMove", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBankAcctInfo
   Description: This method is called when the BankAcctID field is modified
   OperationID: GetBankAcctInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankAcctInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankAcctInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankAcctInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetBankAcctInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBankFeeDefaultAccount
   Description: This method is used to get the default account(s) for a Bank Fee
   OperationID: GetBankFeeDefaultAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankFeeDefaultAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankFeeDefaultAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankFeeDefaultAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetBankFeeDefaultAccount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetById4PITracker
   Description: Procedure wrapper for procedure GetById for PI tracker to prevent removing ARPNHead when there is not
corresponded record in CashGrp table.(It was removed after posting in post_post file)
   OperationID: GetById4PITracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetById4PITracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetById4PITracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetById4PITracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetById4PITracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRows4Tracker
   Description: The method wrapper for the GetRows method for A/R Payment Instrument tracker to prevent removing ARPNHead when there is not
corresponded record in CashGrp table.
   OperationID: GetRows4Tracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRows4Tracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows4Tracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRows4Tracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetRows4Tracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrencyCodeForBatch
   OperationID: GetCurrencyCodeForBatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrencyCodeForBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyCodeForBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyCodeForBatch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetCurrencyCodeForBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrencyInfo
   Description: This method is used when the Currency Code changes for Invoice payments only
   OperationID: GetCurrencyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrencyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetCurrencyInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrencyInfoMaster
   Description: This method is used when the Currency Code changes for Invoice payments only
   OperationID: GetCurrencyInfoMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrencyInfoMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyInfoMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyInfoMaster(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetCurrencyInfoMaster", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCustomerInfo
   Description: This method is called when the CustID field is modified
   OperationID: GetCustomerInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomerInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomerInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustomerInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetCustomerInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCustPIFlags
   Description: This method gets the AutoGenPromNotes and DirectDebiting flags from the
Customer record. Also sets the flag hasBank to true if there are CustBank
records associated to the Customer and false if not.
   OperationID: GetCustPIFlags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustPIFlags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustPIFlags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustPIFlags(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetCustPIFlags", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlInvoiceInfo
   Description: This method is called when the InvoiceNum field is modified
   OperationID: GetDtlInvoiceInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlInvoiceInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlInvoiceInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlInvoiceInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetDtlInvoiceInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlLegalNumberInfo
   Description: This method is called when the InvLegalNumber field is modified
   OperationID: GetDtlLegalNumberInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlLegalNumberInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlLegalNumberInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlLegalNumberInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetDtlLegalNumberInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlTranAmtInfo
   Description: This method is run when the DocTranAmt field is modified
   OperationID: GetDtlTranAmtInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlTranAmtInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlTranAmtInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlTranAmtInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetDtlTranAmtInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExistingGenPI
   Description: This method is used to copy a generated ARPNHead
   OperationID: GetExistingGenPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExistingGenPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExistingGenPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExistingGenPI(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetExistingGenPI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGLJrnDtl
   Description: Get the GLJrnDtl records for an ARPromissoryNote.
   OperationID: GetGLJrnDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLJrnDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLJrnDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLJrnDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetGLJrnDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGroupIDForPIWithHeadNum
   Description: This method will retrieve the GroupID for an ARPNHead record that's for the
ARPromNoteID supplied.
   OperationID: GetGroupIDForPIWithHeadNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGroupIDForPIWithHeadNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupIDForPIWithHeadNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGroupIDForPIWithHeadNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetGroupIDForPIWithHeadNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGroupIDForPI
   Description: This method will retrieve the GroupID for an ARPNHead record that's for the
ARPromNoteID supplied.
   OperationID: GetGroupIDForPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGroupIDForPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupIDForPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGroupIDForPI(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetGroupIDForPI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetHdrInvoiceInfo
   Description: This method will default customer information from an invoice.
   OperationID: GetHdrInvoiceInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHdrInvoiceInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHdrInvoiceInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHdrInvoiceInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetHdrInvoiceInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetHdrLegalNumberInfo
   Description: This method will default customer information from an invoice.
   OperationID: GetHdrLegalNumberInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHdrLegalNumberInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHdrLegalNumberInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHdrLegalNumberInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetHdrLegalNumberInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetHeadNumForPI
   Description: This method will retrieve the HeadNum for an ARPNHead record that's for the
invoice number supplied.
   OperationID: GetHeadNumForPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHeadNumForPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHeadNumForPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHeadNumForPI(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetHeadNumForPI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvcsSinglGenPI
   Description: Retur list of open posted AR invoices for a specific Customer.
   OperationID: GetInvcsSinglGenPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvcsSinglGenPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcsSinglGenPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvcsSinglGenPI(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetInvcsSinglGenPI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLegalNumberInfo
   Description: This method is called when the InvLegalNumber field is modified
   OperationID: GetLegalNumberInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumberInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumberInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLegalNumberInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetLegalNumberInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNHeadByGroupID
   Description: GetNewARPNHeadByGroupID
   OperationID: GetNewARPNHeadByGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHeadByGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHeadByGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNHeadByGroupID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetNewARPNHeadByGroupID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNHeadByInvoiceNum
   Description: GetNewARPNHeadByInvoiceNum
   OperationID: GetNewARPNHeadByInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHeadByInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHeadByInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNHeadByInvoiceNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetNewARPNHeadByInvoiceNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNHeadByInvoiceAndAccount
   Description: GetNewARPNHeadByInvoiceNum
   OperationID: GetNewARPNHeadByInvoiceAndAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHeadByInvoiceAndAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHeadByInvoiceAndAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNHeadByInvoiceAndAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetNewARPNHeadByInvoiceAndAccount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBankTranByHeadNum
   Description: GetNewBankTranByHeadNum
   OperationID: GetNewBankTranByHeadNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTranByHeadNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranByHeadNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankTranByHeadNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetNewBankTranByHeadNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPITypePropByPMUID
   OperationID: GetPITypePropByPMUID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPITypePropByPMUID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPITypePropByPMUID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPITypePropByPMUID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetPITypePropByPMUID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPNotesByGroupID
   OperationID: GetPNotesByGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPNotesByGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPNotesByGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPNotesByGroupID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetPNotesByGroupID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPNotes
   OperationID: GetPNotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPNotes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPNotes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPNotes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetPNotes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRateCodeInfo
   Description: This method updates the dataset when the RateCode field changes
   OperationID: GetRateCodeInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRateCodeInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRateCodeInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRateCodeInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetRateCodeInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsByGrpID
   OperationID: GetRowsByGrpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsByGrpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsByGrpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsByGrpID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetRowsByGrpID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPNotesGenerated
   Description: Retrieves Payment Instruments which were created by Generation procedure.
   OperationID: GetPNotesGenerated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPNotesGenerated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPNotesGenerated_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPNotesGenerated(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetPNotesGenerated", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsByGrpIDExt
   Description: Retrieves list of Payment Instruments belong to gived Group
   OperationID: GetRowsByGrpIDExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsByGrpIDExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsByGrpIDExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsByGrpIDExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetRowsByGrpIDExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSalesTaxInfo
   Description: This method updates the dataset when the TaxCode field changes
   OperationID: GetSalesTaxInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSalesTaxInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSalesTaxInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSalesTaxInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetSalesTaxInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaxableInfo
   Description: This method is called when the Taxable Amount Tax Percent or Fixed Amount is changed to
recalculate the Tax Total
   OperationID: GetTaxableInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxableInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxableInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxableInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetTaxableInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTranAmt
   Description: This method upates the TranAmt/DocTranAmt field after the TranAmt, DocTranAmt or
ExchangeRate field is updated.  If BaseEntered flag is yes, the TranAmt and DocTranAmt
fields will be used to calculat the exchangeRate.  Otherwise, the TranAmt will be calculated
using the exchangeRate and DocTranAmt fields.
   OperationID: GetTranAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTranAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetTranAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUnapprovedPI
   Description: This function will retrived existing Unapproved Stage PIs and pull them into the group to
be converted to Portfolio Stage PIs.
   OperationID: GetUnapprovedPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUnapprovedPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUnapprovedPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUnapprovedPI(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetUnapprovedPI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUnapprovedPIwithCount
   Description: This function will retrived existing Unapproved Stage PIs and pull them into the group to
be converted to Portfolio Stage PIs.
   OperationID: GetUnapprovedPIwithCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUnapprovedPIwithCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUnapprovedPIwithCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUnapprovedPIwithCount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetUnapprovedPIwithCount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LeaveARPNHead
   Description: This method checks calculates the GainLoss Adjustment record when finally
leaving a ARPNHead record after adding/updating all the ARPNDtl records
   OperationID: LeaveARPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveARPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveARPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveARPNHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/LeaveARPNHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MarkSent
   Description: This method marks a Promissory Note as "Sent".
   OperationID: MarkSent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MarkSent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkSent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MarkSent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/MarkSent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MarkSigned
   Description: This method marks a Promissory Note as "Signed".
   OperationID: MarkSigned
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MarkSigned_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkSigned_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MarkSigned(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/MarkSigned", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankFeeID
   Description: OnChangeBankFeeID
   OperationID: OnChangeBankFeeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankFeeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankFeeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankFeeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/OnChangeBankFeeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankAcctID
   Description: OnChangeBankAcctID
   OperationID: OnChangeBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankAcctID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/OnChangeBankAcctID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeType
   Description: OnChangeType
   OperationID: OnChangeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/OnChangeType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PostPIGroupWithoutGL
   Description: PostPIGroupWithoutGL is to update ARPNMove records and delete CashGrp if all ARPNMove records were posted.
   OperationID: PostPIGroupWithoutGL
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostPIGroupWithoutGL_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostPIGroupWithoutGL_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostPIGroupWithoutGL(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/PostPIGroupWithoutGL", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PostPNWithoutGL
   OperationID: PostPNWithoutGL
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostPNWithoutGL_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostPNWithoutGL_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostPNWithoutGL(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/PostPNWithoutGL", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrePostCheck
   Description: PrePostCheck procedure checks if any related tax records have zero amounts.
   OperationID: PrePostCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePostCheck(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/PrePostCheck", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecalcBankTax
   Description: This method is called after the TaxAmt is changed to recalculate the doc or base tax amounts
   OperationID: RecalcBankTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcBankTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcBankTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecalcBankTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/RecalcBankTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetReadyToCalc
   Description: CALCULATE VANTAGE\TAX CONNECT TAX CALCULATIONS UI NEEDS TO CALL A SAVE BEFORE CALLING THIS PROCEDURE
   OperationID: SetReadyToCalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetReadyToCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetReadyToCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetReadyToCalc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/SetReadyToCalc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SingleGenPIExt
   Description: Generates Payment instruments for given invoises
   OperationID: SingleGenPIExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SingleGenPIExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SingleGenPIExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SingleGenPIExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/SingleGenPIExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEligibleInvcsForSinglGenPI
   Description: Returns list of open posted AR invoices for a specific Customer which are eligible to PI generation
   OperationID: GetEligibleInvcsForSinglGenPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEligibleInvcsForSinglGenPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEligibleInvcsForSinglGenPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEligibleInvcsForSinglGenPI(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetEligibleInvcsForSinglGenPI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SingleGenPI
   OperationID: SingleGenPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SingleGenPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SingleGenPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SingleGenPI(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/SingleGenPI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateARPIType
   Description: ValidateARPIType
Used to validate whether PI type exists and is valid for AR Payment instrument.
   OperationID: ValidateARPIType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateARPIType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateARPIType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateARPIType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ValidateARPIType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateDuplicatedARPromNoteID
   Description: This Method validates wheter a promissory note id is duplicated.
0 = ok, 1= duplicate for other cust, 2=duplicate for current customer
   OperationID: ValidateDuplicatedARPromNoteID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateDuplicatedARPromNoteID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDuplicatedARPromNoteID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateDuplicatedARPromNoteID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ValidateDuplicatedARPromNoteID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method WriteXMLFile
   Description: This method writes promissory note to file.
   OperationID: WriteXMLFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WriteXMLFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WriteXMLFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WriteXMLFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/WriteXMLFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Returns a list of rows that satisfy the where clause.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetListCustom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetLegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Assigns a legal number to the provided head number.
Validate header and legal number configuration exists, in other case throws an error.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/AssignLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/VoidLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts data table if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/PreUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetNewARPNHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNHeadAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetNewARPNHeadAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBankTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankTran(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetNewBankTran", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBankTranTaxDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankTranTaxDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTranTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankTranTaxDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetNewBankTranTaxDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBankTranTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankTranTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTranTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankTranTGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetNewBankTranTGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetNewARPNDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTaxDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetNewTaxDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNHeadTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNHeadTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHeadTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHeadTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNHeadTGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetNewARPNHeadTGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNHeadAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNHeadRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNHeadTGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankTranRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankTranTGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTaxDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankTranTaxDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxDtlRow[],
}

export interface Erp_Tablesets_ARPNDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Customer Number  */  
   "CustNum":number,
      /**  Discount Amount. Base Currency.  */  
   "DiscountAmt":number,
      /**  Discount Amount. Document Currency.  */  
   "DocDiscountAmount":number,
      /**  Transaction Amount. Document Currency.  */  
   "DocTranAmt":number,
      /**  Exchange Rate  */  
   "ExchangeRate":number,
      /**  Get Default Tax ID's flag.  */  
   "GetDfltTaxIds":boolean,
      /**  Posted to GL flag  */  
   "GLPosted":boolean,
      /**  Reference to  invchead  */  
   "InvoiceNum":number,
      /**  Legal Number  */  
   "LegalNumber":string,
      /**  Posted flag  */  
   "Posted":boolean,
      /**  Rate Group code  */  
   "RateGrpCode":string,
      /**  Rounding Difference  */  
   "RoundDiff":number,
      /**  Discount Amount. Report Currency 1.  */  
   "Rpt1DiscountAmt":number,
      /**  Transaction Amount. Report Currency 1.  */  
   "Rpt1TranAmt":number,
      /**  Discount Amount. Report Currency 2.  */  
   "Rpt2DiscountAmt":number,
      /**  Transaction Amount. Report Currency 2.  */  
   "Rpt2TranAmt":number,
      /**  Discount Amount. Report Currency 3.  */  
   "Rpt3DiscountAmt":number,
      /**  Transaction Amount. Report Currency 3.  */  
   "Rpt3TranAmt":number,
      /**  Tax Liability  */  
   "TaxRegionCode":string,
      /**  Transaction Amount  */  
   "TranAmt":number,
      /**  Transaction Date  */  
   "TranDate":string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   "GroupID":string,
      /**  The foreign key that relates this detail record to a ARPNHead record. Duplicated from ARPNHead.HeadNum when record is created. Not applicable to user interface.  */  
   "HeadNum":number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   "InvoiceRef":number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   "DNAmount":number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   "DocDnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DnAmount":number,
      /**   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  */  
   "TranType":string,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Tax Amount in the vendors currency.  */  
   "DocTaxAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  */  
   "FiscalPeriod":number,
      /**  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal Year Suffix.  */  
   "FiscalYearSuffix":string,
      /**  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  */  
   "Reference":string,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Total Tax Amount.  */  
   "TaxAmt":number,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   "GainLossType":string,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   "ReverseGL":boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   "RevalueDate":string,
      /**  PI Balance at the time of revaluation  */  
   "RevalueBal":number,
      /**  Document currency PI Balance at the time of revaluation  */  
   "DocRevalueBal":number,
      /**  Reporting currency PI Balance at the time of revaluation  */  
   "Rpt1RevalueBal":number,
      /**  Reporting currency PI Balance at the time of revaluation  */  
   "Rpt2RevalueBal":number,
      /**  Reporting currency PI Balance at the time of revaluation  */  
   "Rpt3RevalueBal":number,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "InvoiceDate":string,
   "DocInvoiceAmt":number,
   "CurrencyCode":string,
   "CurrencyDescription":string,
   "BaseCurrDesc":string,
   "BaseCurrSymbol":string,
   "DocInvoiceBal":number,
   "InvTermsCode":string,
   "InvDiscountDate":string,
   "InvDueDate":string,
   "DocNetCash":number,
   "DocNewBalance":number,
   "InvLockRate":boolean,
   "InvoiceBal":number,
   "NewBalance":number,
   "NetCash":number,
   "GainLossAmt":number,
   "ApplyDate":string,
   "BillConNumber":number,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
   "DispGLAcct":string,
   "DispTranAmt":number,
   "DocDispTranAmt":number,
   "DocSelfAssessTax":number,
   "DocWithholdTax":number,
   "FullyPaid":boolean,
   "InvExchRate":number,
   "InvLegalNumber":string,
   "InvoiceAmt":number,
   "InvXRateLabel":string,
   "LegalNumMessage":string,
   "LegalNumStyle":string,
   "OldGainLoss":number,
   "PostToGL":boolean,
   "SelfAssessTax":number,
   "SoldToCustID":string,
   "SoldToCustNum":number,
   "SoldToCustomerName":string,
   "WithholdTax":number,
   "XRateLabel":string,
   "Rpt1NewBalance":number,
   "Rpt3NewBalance":number,
   "Rpt1DispTranAmt":number,
   "Rpt2DispTranAmt":number,
   "Rpt3DispTranAmt":number,
   "Rpt1OldGainLoss":number,
   "Rpt2OldGainLoss":number,
   "Rpt3OldGainLoss":number,
   "Rpt1GainLossAmt":number,
   "Rpt2GainLossAmt":number,
   "Rpt3GainLossAmt":number,
   "Rpt1InvoiceAmt":number,
   "Rpt2InvoiceAmt":number,
   "Rpt3InvoiceAmt":number,
   "Rpt1InvoiceBal":number,
   "Rpt2InvoiceBal":number,
   "Rpt3InvoiceBal":number,
   "Rpt2NewBalance":number,
   "Rpt1NetCash":number,
   "Rpt2NetCash":number,
   "Rpt3NetCash":number,
   "InvoicePosted":boolean,
   "CurGroupID":string,
   "BitFlag":number,
   "CustNumName":string,
   "CustNumCustID":string,
   "CustNumBTName":string,
   "InvoiceNumTermsCode":string,
   "InvoiceNumCardMemberName":string,
   "TaxRgnDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARPNHeadAttchRow{
   "Company":string,
   "GroupID":string,
   "HeadNum":number,
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

export interface Erp_Tablesets_ARPNHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Transaction Amount  */  
   "TranAmt":number,
      /**  Applied Amount  */  
   "AppliedAmt":number,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Bank Amount  */  
   "BankAmount":number,
      /**  Bank Slip Number of the promissory note.  */  
   "BankSlip":string,
      /**  Base Amount  */  
   "BaseAmount":number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   "CashbookLine":number,
      /**  Company Bank Account ID  */  
   "CompBankAcctID":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Customer Bank Account ID  */  
   "CustBankAcctID":string,
      /**  Customer ID  */  
   "CustID":string,
      /**  Customer Number  */  
   "CustNum":number,
      /**  Description  */  
   "Description":string,
      /**  Discount Amount. Base Currency.  */  
   "DiscountAmt":number,
      /**  Applied Amount. Document Currency.  */  
   "DocAppliedAmt":number,
      /**  Unapplied Amount. Document Currency.  */  
   "DocUnAppliedAmt":number,
      /**  Tax Amount. Document Currency.  */  
   "DocTaxAmt":number,
      /**  Transaction Amount. Document Currency.  */  
   "DocTranAmt":number,
      /**  Withholding Amount. Document Currency.  */  
   "DocWithholdAmt":number,
      /**  Exchange Rate  */  
   "ExchangeRate":number,
      /**  Get Default Tax ID's flag.  */  
   "GetDfltTaxIds":boolean,
      /**  Posted to GL flag  */  
   "GLPosted":boolean,
      /**  Legal Number  */  
   "LegalNumber":string,
      /**  Paid flag  */  
   "Paid":boolean,
      /**  Posted flag  */  
   "Posted":boolean,
      /**  Process Card  */  
   "ProcessCard":string,
      /**  Rate Group code  */  
   "RateGrpCode":string,
      /**  Recalculated before posting.  */  
   "RecalcBeforePost":boolean,
      /**  Applied Amount. Report Currency 1.  */  
   "Rpt1AppliedAmt":number,
      /**  Tax Amount. Report Currency 1.  */  
   "Rpt1TaxAmt":number,
      /**  Transaction Amount. Report Currency 1.  */  
   "Rpt1TranAmt":number,
      /**  Unapplied Amount. Report Currency 1.  */  
   "Rpt1UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 1.  */  
   "Rpt1WithholdAmt":number,
      /**  Applied Amount. Report Currency 2.  */  
   "Rpt2AppliedAmt":number,
      /**  Tax Amount. Report Currency 2.  */  
   "Rpt2TaxAmt":number,
      /**  Transaction Amount. Report Currency 2.  */  
   "Rpt2TranAmt":number,
      /**  Unapplied Amount. Report Currency 2.  */  
   "Rpt2UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 2.  */  
   "Rpt2WithholdAmt":number,
      /**  Applied Amount. Report Currency 3.  */  
   "Rpt3AppliedAmt":number,
      /**  Tax Amount. Report Currency 3.  */  
   "Rpt3TaxAmt":number,
      /**  Transaction Amount. Report Currency 3.  */  
   "Rpt3TranAmt":number,
      /**  Unapplied Amount. Report Currency 3.  */  
   "Rpt3UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 3.  */  
   "Rpt3WithholdAmt":number,
      /**  Signed flag  */  
   "Signed":boolean,
      /**  Tax Amount. Base Currency.  */  
   "TaxAmt":number,
      /**  Tax Liability  */  
   "TaxRegionCode":string,
      /**  Total AR Amount  */  
   "TotalARAmt":number,
      /**  Transaction Date  */  
   "TransDate":string,
      /**  Unapplied Amount. Base Currency.  */  
   "UnappliedAmt":number,
      /**  Voided Flag  */  
   "Voided":boolean,
      /**  Withholding Amount. Base Currency.  */  
   "WithholdAmt":number,
      /**  Company Name  */  
   "CompanyName":string,
      /**  First company address line.  */  
   "CompanyAddr1":string,
      /**  Second company address line.  */  
   "CompanyAddr2":string,
      /**  Third company address line.  */  
   "CompanyAddr3":string,
      /**  Company City portion of the address.  */  
   "CompanyCity":string,
      /**  Company State portion of the address.  */  
   "CompanyState":string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   "CompanyPostalCode":string,
      /**  Company Country portion of the address.  */  
   "CompanyCountry":string,
      /**  Company Name  */  
   "CustomerName":string,
      /**  First customer address line.  */  
   "CustomerAddr1":string,
      /**  Second customer address line.  */  
   "CustomerAddr2":string,
      /**  Third customer address line.  */  
   "CustomerAddr3":string,
      /**  Customer Stateportion of the address.  */  
   "CustomerState":string,
      /**  Customer City portion of the address.  */  
   "CustomerPostalCode":string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   "CustomerCity":string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Reference to  invchead  */  
   "InvoiceNum":number,
      /**  AR Payment Instrument ID  */  
   "ARPromNoteID":string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   "FiscalPeriod":number,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  Transaction Type  */  
   "TranType":string,
      /**  Sent Flag  */  
   "Sent":boolean,
      /**  Type  */  
   "Type":string,
      /**  Issue Date  */  
   "IssueDate":string,
      /**  Due date of the promissory note.  */  
   "DueDate":string,
      /**  Bank/Branch Code for company's bank.  */  
   "CompBankBranchCode":string,
      /**  IBANCode for company's bank.  */  
   "CompIBANCode":string,
      /**  Bank/Branch Code for customer's bank.  */  
   "CustBankBranchCode":string,
      /**  IBAN Code for customer's bank.  */  
   "CustIBANCode":string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   "AutoGenerated":boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   "DirectDeposit":boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   "ClearedAmt":number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   "ClearedPerson":string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPI":boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Customer's country code  */  
   "CustCountryCode":number,
      /**  Customer country portion of the address.  */  
   "CustomerCountry":string,
      /**  Promissory Note Status  */  
   "PIStatus":string,
      /**  Current Group  */  
   "CurGroupID":string,
      /**  Stage  */  
   "PIStage":string,
      /**  Reason to change Company or Customer information  */  
   "ChgComment":string,
      /**  Hold from Application reason  */  
   "HoldReason":string,
      /**  Lock Exchange Rate  */  
   "LockRate":boolean,
      /**  Reference to reversed PI  */  
   "ReferseRef":number,
      /**  Reverse Date  */  
   "ReverseDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankClearedAmt  */  
   "BankClearedAmt":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  DiscountCashDate  */  
   "DiscountCashDate":string,
   "BaseCurrSymbol":string,
   "BaseCurrencyCode":string,
   "BaseCurrencyDesc":string,
   "TermsDesc":string,
   "CurrencyDesc":string,
   "TotalCashReceived":number,
   "CompanyBankName":string,
   "CompanyBankAcct":string,
   "CompanyBankIdentifier":string,
   "CustomerBankName":string,
   "CustomerBankAcct":string,
   "CustomerBankIdentifier":string,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   "calcRate":boolean,
   "ApplyDate":string,
   "BankCurrencyCode":string,
   "BankCurrSymbol":string,
   "BillToName":string,
      /**  Customer Credit Hold flag  */  
   "CreditHold":boolean,
   "CurrencySwitch":boolean,
      /**  Display GL Account  */  
   "DispGLAcct":string,
   "DocDiscount":number,
   "DocReceipt":number,
   "FullyPaid":boolean,
   "LegalNumMessage":string,
   "TotalRoundDiff":number,
   "TranTaxAmt":number,
   "XRateLabel":string,
      /**  Transaction Amount less Tax Amount  */  
   "DocTranTaxAmt":number,
   "Rpt1TranTaxAmt":number,
   "Rpt2TranTaxAmt":number,
   "Rpt3TranTaxAmt":number,
   "CompBankBranchCodeDesc":string,
   "CustBankBranchCodeDesc":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
   "PIStatusDesc":string,
      /**  like PIType.Initiation  */  
   "PITypeInitiation":string,
   "DocGainLossReal":number,
   "DocGainLossUnreal":number,
   "GainLossReal":number,
   "GainLossUnreal":number,
   "Rpt1GainLossReal":number,
   "Rpt1GainLossUnreal":number,
   "Rpt2GainLossReal":number,
   "Rpt2GainLossUnreal":number,
   "Rpt3GainLossReal":number,
   "Rpt3GainLossUnreal":number,
   "RevalueDate":string,
   "DocDiscountAmt":number,
   "Rpt1DiscountAmt":number,
   "Rpt2DiscountAmt":number,
   "Rpt3DiscountAmt":number,
   "Receipt":number,
   "Rpt1Receipt":number,
   "Rpt2Receipt":number,
   "Rpt3Receipt":number,
      /**  The Bank's full name.  */  
   "BankAcctBankName":string,
      /**  Full description of the bank account.  */  
   "BankAcctDescription":string,
      /**  Description  */  
   "CashbookLineDescription":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  Status Description  */  
   "PIStatusStatusDesc":string,
      /**  Type Description  */  
   "PITypeDescription":string,
      /**  Description  */  
   "RateGrpDescription":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionCodeDescription":string,
      /**  Description  */  
   "TranDocTypeDescription":string,
   "BankRecGainLoss":number,
   "DocBankRecGainLoss":number,
   "Rpt1BankRecGainLoss":number,
   "Rpt2BankRecGainLoss":number,
   "Rpt3BankRecGainLoss":number,
   "BankTotalAmount":number,
   "StatusChgTranDocType":string,
   "StatusChgLegalNum":string,
      /**  for kinetic purposes  */  
   "ARPNDtlExists":boolean,
      /**  for kinetic purposes  */  
   "ARPNDtlInvoicePosted":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARPNHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Transaction Amount  */  
   "TranAmt":number,
      /**  Applied Amount  */  
   "AppliedAmt":number,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Bank Amount  */  
   "BankAmount":number,
      /**  Bank Slip Number of the promissory note.  */  
   "BankSlip":string,
      /**  Base Amount  */  
   "BaseAmount":number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   "CashbookLine":number,
      /**  Company Bank Account ID  */  
   "CompBankAcctID":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Customer Bank Account ID  */  
   "CustBankAcctID":string,
      /**  Customer ID  */  
   "CustID":string,
      /**  Customer Number  */  
   "CustNum":number,
      /**  Description  */  
   "Description":string,
      /**  Discount Amount. Base Currency.  */  
   "DiscountAmt":number,
      /**  Applied Amount. Document Currency.  */  
   "DocAppliedAmt":number,
      /**  Unapplied Amount. Document Currency.  */  
   "DocUnAppliedAmt":number,
      /**  Tax Amount. Document Currency.  */  
   "DocTaxAmt":number,
      /**  Transaction Amount. Document Currency.  */  
   "DocTranAmt":number,
      /**  Withholding Amount. Document Currency.  */  
   "DocWithholdAmt":number,
      /**  Exchange Rate  */  
   "ExchangeRate":number,
      /**  Get Default Tax ID's flag.  */  
   "GetDfltTaxIds":boolean,
      /**  Posted to GL flag  */  
   "GLPosted":boolean,
      /**  Legal Number  */  
   "LegalNumber":string,
      /**  Paid flag  */  
   "Paid":boolean,
      /**  Posted flag  */  
   "Posted":boolean,
      /**  Process Card  */  
   "ProcessCard":string,
      /**  Rate Group code  */  
   "RateGrpCode":string,
      /**  Recalculated before posting.  */  
   "RecalcBeforePost":boolean,
      /**  Applied Amount. Report Currency 1.  */  
   "Rpt1AppliedAmt":number,
      /**  Tax Amount. Report Currency 1.  */  
   "Rpt1TaxAmt":number,
      /**  Transaction Amount. Report Currency 1.  */  
   "Rpt1TranAmt":number,
      /**  Unapplied Amount. Report Currency 1.  */  
   "Rpt1UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 1.  */  
   "Rpt1WithholdAmt":number,
      /**  Applied Amount. Report Currency 2.  */  
   "Rpt2AppliedAmt":number,
      /**  Tax Amount. Report Currency 2.  */  
   "Rpt2TaxAmt":number,
      /**  Transaction Amount. Report Currency 2.  */  
   "Rpt2TranAmt":number,
      /**  Unapplied Amount. Report Currency 2.  */  
   "Rpt2UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 2.  */  
   "Rpt2WithholdAmt":number,
      /**  Applied Amount. Report Currency 3.  */  
   "Rpt3AppliedAmt":number,
      /**  Tax Amount. Report Currency 3.  */  
   "Rpt3TaxAmt":number,
      /**  Transaction Amount. Report Currency 3.  */  
   "Rpt3TranAmt":number,
      /**  Unapplied Amount. Report Currency 3.  */  
   "Rpt3UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 3.  */  
   "Rpt3WithholdAmt":number,
      /**  Signed flag  */  
   "Signed":boolean,
      /**  Tax Amount. Base Currency.  */  
   "TaxAmt":number,
      /**  Tax Liability  */  
   "TaxRegionCode":string,
      /**  Total AR Amount  */  
   "TotalARAmt":number,
      /**  Transaction Date  */  
   "TransDate":string,
      /**  Unapplied Amount. Base Currency.  */  
   "UnappliedAmt":number,
      /**  Voided Flag  */  
   "Voided":boolean,
      /**  Withholding Amount. Base Currency.  */  
   "WithholdAmt":number,
      /**  Company Name  */  
   "CompanyName":string,
      /**  First company address line.  */  
   "CompanyAddr1":string,
      /**  Second company address line.  */  
   "CompanyAddr2":string,
      /**  Third company address line.  */  
   "CompanyAddr3":string,
      /**  Company City portion of the address.  */  
   "CompanyCity":string,
      /**  Company State portion of the address.  */  
   "CompanyState":string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   "CompanyPostalCode":string,
      /**  Company Country portion of the address.  */  
   "CompanyCountry":string,
      /**  Company Name  */  
   "CustomerName":string,
      /**  First customer address line.  */  
   "CustomerAddr1":string,
      /**  Second customer address line.  */  
   "CustomerAddr2":string,
      /**  Third customer address line.  */  
   "CustomerAddr3":string,
      /**  Customer Stateportion of the address.  */  
   "CustomerState":string,
      /**  Customer City portion of the address.  */  
   "CustomerPostalCode":string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   "CustomerCity":string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Reference to  invchead  */  
   "InvoiceNum":number,
      /**  AR Payment Instrument ID  */  
   "ARPromNoteID":string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   "FiscalPeriod":number,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  Transaction Type  */  
   "TranType":string,
      /**  Sent Flag  */  
   "Sent":boolean,
      /**  Type  */  
   "Type":string,
      /**  Issue Date  */  
   "IssueDate":string,
      /**  Due date of the promissory note.  */  
   "DueDate":string,
      /**  Bank/Branch Code for company's bank.  */  
   "CompBankBranchCode":string,
      /**  IBANCode for company's bank.  */  
   "CompIBANCode":string,
      /**  Bank/Branch Code for customer's bank.  */  
   "CustBankBranchCode":string,
      /**  IBAN Code for customer's bank.  */  
   "CustIBANCode":string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   "AutoGenerated":boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   "DirectDeposit":boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   "ClearedAmt":number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   "ClearedPerson":string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPI":boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Customer's country code  */  
   "CustCountryCode":number,
      /**  Customer country portion of the address.  */  
   "CustomerCountry":string,
      /**  Promissory Note Status  */  
   "PIStatus":string,
      /**  Current Group  */  
   "CurGroupID":string,
      /**  Stage  */  
   "PIStage":string,
      /**  Reason to change Company or Customer information  */  
   "ChgComment":string,
      /**  Hold from Application reason  */  
   "HoldReason":string,
      /**  Lock Exchange Rate  */  
   "LockRate":boolean,
      /**  Reference to reversed PI  */  
   "ReferseRef":number,
      /**  Reverse Date  */  
   "ReverseDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankClearedAmt  */  
   "BankClearedAmt":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  TotalBankFee  */  
   "TotalBankFee":number,
      /**  DocTotalBankFee  */  
   "DocTotalBankFee":number,
      /**  Rpt1TotalBankFee  */  
   "Rpt1TotalBankFee":number,
      /**  Rpt2TotalBankFee  */  
   "Rpt2TotalBankFee":number,
      /**  Rpt3TotalBankFee  */  
   "Rpt3TotalBankFee":number,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  Issuer Name  */  
   "IssuerName":string,
      /**  Signed By  */  
   "SignedBy":string,
      /**  Signed Date  */  
   "SignedDate":string,
      /**  Signee Address 1  */  
   "SigneeAddr1":string,
      /**  Signee Address 2  */  
   "SigneeAddr2":string,
      /**  Signee Address 3  */  
   "SigneeAddr3":string,
      /**  Signee City  */  
   "SigneeCity":string,
      /**  Signee State  */  
   "SigneeState":string,
      /**  Signee Postal Code  */  
   "SigneeZip":string,
      /**  Signee Country Number  */  
   "SigneeCountryNum":number,
      /**  Signee Phone  */  
   "SigneePhoneNum":string,
      /**  Signee Email Address  */  
   "SigneeEMailAddress":string,
      /**  Signee Comment  */  
   "SigneeComment":string,
      /**  DiscountChargeAmt  */  
   "DiscountChargeAmt":number,
      /**  DocDiscountChargeAmt  */  
   "DocDiscountChargeAmt":number,
      /**  Rpt1DiscountChargeAmt  */  
   "Rpt1DiscountChargeAmt":number,
      /**  Rpt2DiscountChargeAmt  */  
   "Rpt2DiscountChargeAmt":number,
      /**  Rpt3DiscountChargeAmt  */  
   "Rpt3DiscountChargeAmt":number,
      /**  Signee Bank Name  */  
   "SigneeBankName":string,
      /**  Signee Bank Account Number  */  
   "SigneeBankAcct":string,
      /**  Signee Bank Identifier  */  
   "SigneeBankIdentifier":string,
      /**  Signee IBAN Code  */  
   "SigneeIBANCode":string,
      /**  Signee Bank BranchCode  */  
   "SigneeBankBranchCode":string,
      /**  DiscountCashDate  */  
   "DiscountCashDate":string,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
   "ApplyDate":string,
   "BankCurrencyCode":string,
   "BankCurrSymbol":string,
   "BankRecGainLoss":number,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   "calcRate":boolean,
   "CompanyBankAcct":string,
   "CompanyBankIdentifier":string,
   "CompanyBankName":string,
   "CompBankBranchCodeDesc":string,
      /**  Customer Credit Hold flag  */  
   "CreditHold":boolean,
   "CurrencyDesc":string,
   "CurrencySwitch":boolean,
   "CustBankBranchCodeDesc":string,
   "CustomerBankAcct":string,
   "CustomerBankIdentifier":string,
   "CustomerBankName":string,
   "DisableBankAcctIDPI":boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   "DisableBankAmt":boolean,
      /**  Display GL Account  */  
   "DispGLAcct":string,
   "DocBankRecGainLoss":number,
   "DocDiscount":number,
   "DocDiscountAmt":number,
   "DocGainLossReal":number,
   "DocGainLossUnreal":number,
   "DocReceipt":number,
      /**  Transaction Amount less Tax Amount  */  
   "DocTranTaxAmt":number,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
   "FullyPaid":boolean,
   "GainLossReal":number,
   "GainLossUnreal":number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   "HasLegNumCnfg":boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumMessage":string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "PIStatusDesc":string,
      /**  like PIType.Initiation  */  
   "PITypeInitiation":string,
   "Receipt":number,
   "RevalueDate":string,
   "Rpt1BankRecGainLoss":number,
   "Rpt1DiscountAmt":number,
   "Rpt1GainLossReal":number,
   "Rpt1GainLossUnreal":number,
   "Rpt1Receipt":number,
   "Rpt1TranTaxAmt":number,
   "Rpt2BankRecGainLoss":number,
   "Rpt2DiscountAmt":number,
   "Rpt2GainLossReal":number,
   "Rpt2GainLossUnreal":number,
   "Rpt2Receipt":number,
   "Rpt2TranTaxAmt":number,
   "Rpt3BankRecGainLoss":number,
   "Rpt3DiscountAmt":number,
   "Rpt3GainLossReal":number,
   "Rpt3GainLossUnreal":number,
   "Rpt3Receipt":number,
   "Rpt3TranTaxAmt":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "StatusChgLegalNum":string,
   "StatusChgTranDocType":string,
   "TermsDesc":string,
   "TotalCashReceived":number,
   "TotalRoundDiff":number,
   "TranTaxAmt":number,
   "TypeDesc":string,
   "XRateLabel":string,
   "BankTotalAmount":number,
   "BaseCurrencyCode":string,
   "BaseCurrencyDesc":string,
   "BaseCurrSymbol":string,
   "BillToName":string,
   "DocDiscountedAmt":number,
      /**  for kinetic purposes  */  
   "ARPNDtlExists":boolean,
      /**  for kinetic purposes  */  
   "ARPNDtlInvoicePosted":boolean,
   "BitFlag":number,
   "BankAcctDescription":string,
   "BankAcctBankName":string,
   "CashbookLineDescription":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CustNumInactive":boolean,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "PIStatusStatusDesc":string,
   "PITypeDescription":string,
   "RateGrpDescription":string,
   "TaxRegionCodeDescription":string,
   "TranDocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARPNHeadTGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   "TGLCTranNum":number,
      /**  String identifier of the account context.  */  
   "GLAcctContext":string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   "BookID":string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   "COACode":string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   "GLAccount":string,
      /**  Indicates if the user can update or delete this record.  */  
   "UserCanModify":boolean,
      /**  Segement Value 1 of the account for this context.  */  
   "SegValue1":string,
      /**  Segement Value 2 of the account for this context.  */  
   "SegValue2":string,
      /**  Segement Value 3 of the account for this context.  */  
   "SegValue3":string,
      /**  Segement Value 4 of the account for this context.  */  
   "SegValue4":string,
      /**  Segement Value 5 of the account for this context.  */  
   "SegValue5":string,
      /**  Segement Value 6 of the account for this context.  */  
   "SegValue6":string,
      /**  Segement Value 7 of the account for this context.  */  
   "SegValue7":string,
      /**  Segement Value 8 of the account for this context.  */  
   "SegValue8":string,
      /**  Segement Value 9 of the account for this context.  */  
   "SegValue9":string,
      /**  Segement Value 10 of the account for this context.  */  
   "SegValue10":string,
      /**  Segement Value 11 of the account for this context.  */  
   "SegValue11":string,
      /**  Segement Value 12 of the account for this context.  */  
   "SegValue12":string,
      /**  Segement Value 13 of the account for this context.  */  
   "SegValue13":string,
      /**  Segement Value 14 of the account for this context.  */  
   "SegValue14":string,
      /**  Segement Value 15 of the account for this context.  */  
   "SegValue15":string,
      /**  Segement Value 16 of the account for this context.  */  
   "SegValue16":string,
      /**  Segement Value 17 of the account for this context.  */  
   "SegValue17":string,
      /**  Segement Value 18 of the account for this context.  */  
   "SegValue18":string,
      /**  Segement Value 19 of the account for this context.  */  
   "SegValue19":string,
      /**  Segement Value 20 of the account for this context.  */  
   "SegValue20":string,
      /**  Unique Identifier of the system GL Control Type.  */  
   "SysGLControlType":string,
      /**  System generated GL Control Identifier.  */  
   "SysGLControlCode":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   "FiscalYear":number,
      /**  JournalCode of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Journal number of the related GLJrnDtl.  */  
   "JournalNum":number,
      /**  JournalLine of the related GLJrnDtl.  */  
   "JournalLine":number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   "TranDate":string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   "TranSource":string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborDtlSeq":number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysDate":string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysTime":number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "TranNum":number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   "ARInvoiceNum":number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   "TransAmt":number,
      /**  Invoice Line Number associated with this GL Journal  */  
   "InvoiceLine":number,
      /**  The sequence number associated with this GL journal  */  
   "SeqNum":number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Credit Amount.  */  
   "CreditAmount":number,
      /**  Debit Amount.  */  
   "DebitAmount":number,
      /**  BookCreditAmount  */  
   "BookCreditAmount":number,
      /**  Book Debit Amount  */  
   "BookDebitAmount":number,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   "RecordType":string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   "CorrAccUID":number,
      /**  this field equals ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  Technical identifier.  */  
   "RuleUID":number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  IsModifiedByUser  */  
   "IsModifiedByUser":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  MovementType  */  
   "MovementType":string,
      /**  Plant  */  
   "Plant":string,
      /**  HeadNum of ARPNHead  */  
   "HeadNum":number,
      /**  GroupID of ARPNHead  */  
   "GroupID":string,
   "BitFlag":number,
   "COADescription":string,
   "GLAccountGLAcctDisp":string,
   "GLAccountAccountDesc":string,
   "GLAccountGLShortAcct":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARPNListRow{
   "ARPromNoteID":string,
   "Company":string,
   "CurGroupID":string,
   "CustID":string,
   "GroupID":string,
   "HeadNum":number,
   "PIStage":string,
   "PIStatus":string,
   "TranAmt":number,
   "Type":string,
   "Selected":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BankTranRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Relates record to a BankAcct.  */  
   "BankAcctID":string,
      /**  Unique ID of the Transaction.  */  
   "TranNum":number,
      /**  Date that the transaction took place.  */  
   "TranDate":string,
      /**  Amount of the Transaction  */  
   "TranAmt":number,
      /**  Transaction Reference  */  
   "TranRef":string,
      /**  Indicates that the Transaction (not cleared variance) has been posted to G/L.  When the Bank Statement is posted all Non-G/L Posted adjustments for the bank are posted to G/L using the Bank Account's Cash and Bank Fee Accounts. G/L Posted Transactions cannot be deleted. (System Set)  */  
   "GLPosted":boolean,
      /**  Person who entered the transaction (System Set).  */  
   "EntryPerson":string,
      /**  Date that the Transaction was entered into the system (System Set).  */  
   "EntryDate":string,
      /**  Time that the transaction was entered into the system - in HH:MM:SS format (System Set).  */  
   "EntryTime":string,
      /**  Indicates the transaction's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "TranCleared":boolean,
      /**  Indicates that the transaction is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "TranClearPending":boolean,
      /**  Amount that the Transaction was cleared for.  */  
   "TranClearedAmt":number,
      /**  Person who cleared the transaction (System Set).  */  
   "TranClearedPerson":string,
      /**  Date that the Transaction was cleared in the system (System Set).  */  
   "TranClearedDate":string,
      /**  Time that the transaction was cleared in the system - in HH:MM:SS format (System Set).  */  
   "TranClearedTime":string,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   "BankSlip":string,
      /**  Fiscal year that entry applies to.  */  
   "FiscalYear":number,
      /**  Fiscal period the transaction was posted to. Only pertains to when posted to GL.  */  
   "FiscalPeriod":number,
      /**  Journal Number of related GLJrnDtl.  */  
   "JournalNum":number,
      /**  Journal Code of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Document amount of the Transaction  */  
   "DocTranAmt":number,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Exchange rate that is used for this bank transaction.  */  
   "ExchangeRate":number,
      /**  Document amount that the Transaction was cleared for.  */  
   "DocTranClearedAmt":number,
      /**  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  */  
   "GroupID":string,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Link to the related GLRefTyp.RefType.  */  
   "GLRefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "GLRefCode":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "GLRefCodeDesc":string,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranClearedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Fiscal year suffix that entry applies to.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Unique ID of the Fee  */  
   "BankFeeID":string,
      /**  The Fee amount; this amount plus the Fee tax amount will compose the total of the charge on the statement  */  
   "BankFeeAmt":number,
      /**  The Tax Amount that has been charged to the fee  */  
   "BankFeeTaxAmt":number,
      /**  The Fee amount in Base Currency  */  
   "DocBankFeeAmt":number,
      /**  The Tax Amount that has been charged to the fee in Base Currency  */  
   "DocBankFeeTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1BankFeeAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2BankFeeAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3BankFeeAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1BankFeeTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2BankFeeTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3BankFeeTaxAmt":number,
      /**   Used for Bank Fee Functionality, indicates the module that created this BankFee.  This is assigned by the system.
Values can be; AR, AP and BA.  */  
   "SourceModule":string,
      /**  Consecutive from the AP and AR transactions, this field is used to identify the AP or AR transaction that created this Bank Fee  */  
   "HeadNum":number,
      /**  Indiates if the BankTran has been voided.  The TranNum field will be the same as the original transaction  */  
   "Voided":boolean,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   "GainLossType":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   "ReverseGL":boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   "RevalueDate":string,
      /**  Bank Balance at the time of revaluation  */  
   "RevalueBal":number,
      /**  Document currency Bank Balance at the time of revaluation  */  
   "DocRevalueBal":number,
      /**  Reporting currency Bank Balance at the time of revaluation  */  
   "Rpt1RevalueBal":number,
      /**  Reporting currency Bank Balance at the time of revaluation  */  
   "Rpt2RevalueBal":number,
      /**  Reporting currency Bank Balance at the time of revaluation  */  
   "Rpt3RevalueBal":number,
      /**  Legal Number for the record.  */  
   "LegalNumber":string,
      /**  Transaction Document for the record.  */  
   "TranDocTypeID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CNCFICode  */  
   "CNCFICode":string,
      /**  CNToCFICode  */  
   "CNToCFICode":string,
      /**  BankRecGainLoss  */  
   "BankRecGainLoss":number,
      /**  Rpt1BankRecGainLoss  */  
   "Rpt1BankRecGainLoss":number,
      /**  Rpt2BankRecGainLoss  */  
   "Rpt2BankRecGainLoss":number,
      /**  Rpt3BankRecGainLoss  */  
   "Rpt3BankRecGainLoss":number,
      /**  BalanceUpdated  */  
   "BalanceUpdated":number,
      /**  DocBankRecGainLoss  */  
   "DocBankRecGainLoss":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  Indicates that transaction is currently excluded from batch in Bank Statement Processing.  */  
   "BankBatchExcluded":boolean,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  ABTUID  */  
   "ABTUID":string,
      /**  Multi-Site related Site  */  
   "Plant":string,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
   "CNCFICodeDescription":string,
      /**  Cash Receipt currency code  */  
   "CRCurrCode":string,
      /**  Cash Receipt Rate group code  */  
   "CRRateGrpCode":string,
      /**  Cash Receipt Tran amount  */  
   "CRTranAmt":number,
      /**  Cash Receipt Transaction Cleared Amount  */  
   "CRTranClearedAmt":number,
      /**  Currency Switch  */  
   "CurrencySwitch":boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   "DisableBankAmt":boolean,
      /**  The flag to indicate if the Display amount is supposed to be reversed  */  
   "DispAmtReverse":boolean,
   "DispDocTranAmt":number,
   "DispDocTranClearedAmt":number,
   "DispTranAmt":number,
   "DispTranClearedAmt":number,
      /**  Used for tree structure/parent view definition in Petty Cash Entry  */  
   "InternalDate":string,
   "IsFiltered":boolean,
      /**  Indicates if the record is locked by review journal for bank reconciliation  */  
   "IsLockedBankRec":boolean,
   "LegalNumMessage":string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   "LegalNumStyle":string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   "RefCodeStatus":string,
   "Rpt1DispTranAmt":number,
   "Rpt1DispTranClearedAmt":number,
   "Rpt2DispTranAmt":number,
   "Rpt2DispTranClearedAmt":number,
   "Rpt3DispTranAmt":number,
   "Rpt3DispTranClearedAmt":number,
   "EnableAssignLegNum":boolean,
   "EnableTranDocType":boolean,
   "EnableVoidLegNum":boolean,
   "HasLegNumCnfg":boolean,
   "AllowChgAfterPrint":boolean,
      /**  Display GL Account  */  
   "GLAccount":string,
   "BitFlag":number,
   "BankAcctIDBankName":string,
   "BankAcctIDDescription":string,
   "BankFeeIDDescription":string,
   "BankFeeIDTaxCode":string,
   "CashbookLineDescription":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrName":string,
   "JournalCodeJrnlDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BankTranTGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   "TGLCTranNum":number,
      /**  String identifier of the account context.  */  
   "GLAcctContext":string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   "BookID":string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   "COACode":string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   "GLAccount":string,
      /**  Indicates if the user can update or delete this record.  */  
   "UserCanModify":boolean,
      /**  Segement Value 1 of the account for this context.  */  
   "SegValue1":string,
      /**  Segement Value 2 of the account for this context.  */  
   "SegValue2":string,
      /**  Segement Value 3 of the account for this context.  */  
   "SegValue3":string,
      /**  Segement Value 4 of the account for this context.  */  
   "SegValue4":string,
      /**  Segement Value 5 of the account for this context.  */  
   "SegValue5":string,
      /**  Segement Value 6 of the account for this context.  */  
   "SegValue6":string,
      /**  Segement Value 7 of the account for this context.  */  
   "SegValue7":string,
      /**  Segement Value 8 of the account for this context.  */  
   "SegValue8":string,
      /**  Segement Value 9 of the account for this context.  */  
   "SegValue9":string,
      /**  Segement Value 10 of the account for this context.  */  
   "SegValue10":string,
      /**  Segement Value 11 of the account for this context.  */  
   "SegValue11":string,
      /**  Segement Value 12 of the account for this context.  */  
   "SegValue12":string,
      /**  Segement Value 13 of the account for this context.  */  
   "SegValue13":string,
      /**  Segement Value 14 of the account for this context.  */  
   "SegValue14":string,
      /**  Segement Value 15 of the account for this context.  */  
   "SegValue15":string,
      /**  Segement Value 16 of the account for this context.  */  
   "SegValue16":string,
      /**  Segement Value 17 of the account for this context.  */  
   "SegValue17":string,
      /**  Segement Value 18 of the account for this context.  */  
   "SegValue18":string,
      /**  Segement Value 19 of the account for this context.  */  
   "SegValue19":string,
      /**  Segement Value 20 of the account for this context.  */  
   "SegValue20":string,
      /**  Unique Identifier of the system GL Control Type.  */  
   "SysGLControlType":string,
      /**  System generated GL Control Identifier.  */  
   "SysGLControlCode":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   "FiscalYear":number,
      /**  JournalCode of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Journal number of the related GLJrnDtl.  */  
   "JournalNum":number,
      /**  JournalLine of the related GLJrnDtl.  */  
   "JournalLine":number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   "TranDate":string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   "TranSource":string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborDtlSeq":number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysDate":string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysTime":number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "TranNum":number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   "ARInvoiceNum":number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   "TransAmt":number,
      /**  Invoice Line Number associated with this GL Journal  */  
   "InvoiceLine":number,
      /**  The sequence number associated with this GL journal  */  
   "SeqNum":number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Credit Amount.  */  
   "CreditAmount":number,
      /**  Debit Amount.  */  
   "DebitAmount":number,
      /**  BookCreditAmount  */  
   "BookCreditAmount":number,
      /**  Book Debit Amount  */  
   "BookDebitAmount":number,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   "RecordType":string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   "CorrAccUID":number,
      /**  this field equals ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  Technical identifier.  */  
   "RuleUID":number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  IsModifiedByUser  */  
   "IsModifiedByUser":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  MovementType  */  
   "MovementType":string,
      /**  Plant  */  
   "Plant":string,
      /**  GroupID for relation to BankTran  */  
   "GroupID":string,
   "HeadNum":number,
      /**  Used for tree structure/parent view definition in Petty Cash Entry  */  
   "InternalDate":string,
   "PCashDeskID":string,
   "PCashRefNum":number,
      /**  Voided flag for relation to BankTran  */  
   "Voided":boolean,
      /**  BankAcctID for relation to BankTran  */  
   "BankAcctID":string,
   "BitFlag":number,
   "COADescription":string,
   "GLAccountGLShortAcct":string,
   "GLAccountGLAcctDisp":string,
   "GLAccountAccountDesc":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BankTranTaxDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Indicates the module that created this tax detail.  This is assigned by the system.
Values can be; AR, AP.  */  
   "SourceModule":string,
      /**  HeadNum  */  
   "HeadNum":number,
      /**  Integer assigned by the system copied from APTran.  */  
   "APTranNo":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Taxable amount for this invoice. Manually entered if the currency is the base currency.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount. Manually entered if the currency is the base currency.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency. Manually entered.  */  
   "DocTaxAmt":number,
      /**  Reverse Charge.  */  
   "ReverseCharge":boolean,
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
      /**  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  */  
   "InvoiceNum":number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   "InvoiceRef":number,
      /**   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  */  
   "ECAcquisitionSeq":number,
      /**  Relates record to a BankAcct.  */  
   "BankAcctID":string,
      /**  Unique ID of the Transaction.  */  
   "TranNum":number,
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
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
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
      /**  Discount Tax Adjustment  */  
   "DiscTaxAdj":number,
      /**  Discount Tax Adjustment in foreign currency.  */  
   "DocDiscTaxAdj":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscTaxAdj":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscTaxAdj":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscTaxAdj":number,
      /**  Discount Taxable Adjustment  */  
   "DiscTaxableAdj":number,
      /**  Discount Taxable Adjustment in foreign currency.  */  
   "DocDiscTaxableAdj":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscTaxableAdj":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscTaxableAdj":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscTaxableAdj":number,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Indicates if transaction was voided.  The rest of the unique key will contain the original transaction values (like APTran)  */  
   "Voided":boolean,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "Rpt1TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "Rpt2TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "Rpt3TaxAmtVar":number,
      /**  Discount Tax Adjustment Variance  */  
   "DiscTaxAdjVar":number,
      /**  Discount Tax Adjustment Variance  */  
   "DocDiscTaxAdjVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscTaxAdjVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscTaxAdjVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscTaxAdjVar":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGOrigTaxableAmt  */  
   "AGOrigTaxableAmt":number,
      /**  GainLoss  */  
   "GainLoss":number,
      /**  DocGainLoss  */  
   "DocGainLoss":number,
      /**  Rpt1GainLoss  */  
   "Rpt1GainLoss":number,
      /**  Rpt2GainLoss  */  
   "Rpt2GainLoss":number,
      /**  Rpt3GainLoss  */  
   "Rpt3GainLoss":number,
      /**  CNCFICode  */  
   "CNCFICode":string,
      /**  APInvoiceNum  */  
   "APInvoiceNum":string,
      /**  TranType  */  
   "TranType":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
   "CNCFICodeDescription":string,
   "CTDescription":string,
      /**  Flag to indicate if Manual checkbox should be disabled  */  
   "DisableManual":boolean,
      /**  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  */  
   "GroupID":string,
      /**  Used for tree structure/parent view definition in Petty Cash Entry  */  
   "InternalDate":string,
   "IsFiltered":boolean,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
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

export interface Erp_Tablesets_TaxDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Indicates the module that created this tax detail.  This is assigned by the system.
Values can be; AR, AP.  */  
   "SourceModule":string,
      /**  HeadNum  */  
   "HeadNum":number,
      /**  Integer assigned by the system copied from APTran.  */  
   "APTranNo":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Taxable amount for this invoice. Manually entered if the currency is the base currency.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount. Manually entered if the currency is the base currency.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency. Manually entered.  */  
   "DocTaxAmt":number,
      /**  Reverse Charge.  */  
   "ReverseCharge":boolean,
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
      /**  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  */  
   "InvoiceNum":number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   "InvoiceRef":number,
      /**   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  */  
   "ECAcquisitionSeq":number,
      /**  Relates record to a BankAcct.  */  
   "BankAcctID":string,
      /**  Unique ID of the Transaction.  */  
   "TranNum":number,
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
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
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
      /**  Discount Tax Adjustment  */  
   "DiscTaxAdj":number,
      /**  Discount Tax Adjustment in foreign currency.  */  
   "DocDiscTaxAdj":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscTaxAdj":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscTaxAdj":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscTaxAdj":number,
      /**  Discount Taxable Adjustment  */  
   "DiscTaxableAdj":number,
      /**  Discount Taxable Adjustment in foreign currency.  */  
   "DocDiscTaxableAdj":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscTaxableAdj":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscTaxableAdj":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscTaxableAdj":number,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Indicates if transaction was voided.  The rest of the unique key will contain the original transaction values (like APTran)  */  
   "Voided":boolean,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "Rpt1TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "Rpt2TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "Rpt3TaxAmtVar":number,
      /**  Discount Tax Adjustment Variance  */  
   "DiscTaxAdjVar":number,
      /**  Discount Tax Adjustment Variance  */  
   "DocDiscTaxAdjVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscTaxAdjVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscTaxAdjVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscTaxAdjVar":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGOrigTaxableAmt  */  
   "AGOrigTaxableAmt":number,
      /**  GainLoss  */  
   "GainLoss":number,
      /**  DocGainLoss  */  
   "DocGainLoss":number,
      /**  Rpt1GainLoss  */  
   "Rpt1GainLoss":number,
      /**  Rpt2GainLoss  */  
   "Rpt2GainLoss":number,
      /**  Rpt3GainLoss  */  
   "Rpt3GainLoss":number,
      /**  CNCFICode  */  
   "CNCFICode":string,
      /**  APInvoiceNum  */  
   "APInvoiceNum":string,
      /**  TranType  */  
   "TranType":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
   "CNCFICodeDescription":string,
   "CTDescription":string,
      /**  Flag to indicate if Manual checkbos should be Read Only  */  
   "DisableManual":boolean,
      /**  Group ID - used to link to Cash Head  */  
   "GroupID":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
      /**  The flag to indicate if the user changed Deductible Tax amount on manually updated tax record  */  
   "DedTaxChanged":boolean,
   "EnableTax":boolean,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
      @param groupID
      @param headNum
   */  
export interface AssignLegalNumber_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
      /**  ARPN group identifier.  */  
   groupID:string,
      /**  ARPN header number.  */  
   headNum:number,
}

export interface AssignLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
   legalNumMsg:string,
}
}

   /** Required : 
      @param ipCutOffDate
      @param ipPIStatus
      @param ipPmntMeth
      @param ipGroupID
      @param ipCurrencyCode
   */  
export interface BatchGenPIs_input{
      /**  ipCutOffDate  */  
   ipCutOffDate:string,
      /**  ipPIStatus  */  
   ipPIStatus:string,
      /**  ipPmntMeth  */  
   ipPmntMeth:string,
      /**  ipGroupID  */  
   ipGroupID:string,
      /**  ipCurrencyCode  */  
   ipCurrencyCode:string,
}

export interface BatchGenPIs_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
}

   /** Required : 
      @param ipARPNID
      @param ipInvoiceNum
   */  
export interface CancelGenPI_input{
   ipARPNID:string,
   ipInvoiceNum:number,
}

export interface CancelGenPI_output{
}

   /** Required : 
      @param ipHeadNum
      @param ipID
      @param ipCustID
      @param ipCurGroupID
      @param ipNewPIType
   */  
export interface ChangeCurGroupID_input{
   ipHeadNum:number,
   ipID:string,
   ipCustID:string,
   ipCurGroupID:string,
   ipNewPIType:string,
}

export interface ChangeCurGroupID_output{
}

   /** Required : 
      @param ipTranAmtType
      @param proposedTranAmt
      @param ds
   */  
export interface ChangeTranAmt_input{
      /**  Indicate which of the transaction amount is changed.
            Valid values are: 'B' for Base Tran Amount and 'D' for Doc Tran Amount  */  
   ipTranAmtType:string,
      /**  The proposed Transaction Amount  */  
   proposedTranAmt:number,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface ChangeTranAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param keyValue
      @param keyValue2
   */  
export interface CheckDocumentIsLocked_input{
      /**  GroupID  */  
   keyValue:string,
      /**  HeadNum  */  
   keyValue2:string,
}

export interface CheckDocumentIsLocked_output{
}

   /** Required : 
      @param ipPIType
      @param ipID
      @param ipCustID
   */  
export interface CheckPNoteExisted_input{
   ipPIType:string,
   ipID:string,
   ipCustID:string,
}

export interface CheckPNoteExisted_output{
parameters : {
      /**  output parameters  */  
   opRet:string,
}
}

   /** Required : 
      @param ipID
      @param fromTracker
   */  
export interface CheckPNotesExistTracker_input{
      /**  ipID  */  
   ipID:string,
      /**  Indicates if the method was called from the Tracker or the Update program  */  
   fromTracker:boolean,
}

export interface CheckPNotesExistTracker_output{
parameters : {
      /**  output parameters  */  
   opRet:string,
   headNum:number,
   groupID:string,
   custID:string,
   type:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ipCurGroupID
      @param ipPIStatus
      @param ipPIType
      @param ipPIStage
   */  
export interface CreateARPNMove_input{
   ipGroupID:string,
   ipHeadNum:number,
   ipCurGroupID:string,
   ipPIStatus:string,
   ipPIType:string,
   ipPIStage:string,
}

export interface CreateARPNMove_output{
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ipdelHead
   */  
export interface DelARPNHead_input{
   ipGroupID:string,
   ipHeadNum:number,
   ipdelHead:boolean,
}

export interface DelARPNHead_output{
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface DeleteByID_input{
   groupID:string,
   headNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param groupID
   */  
export interface DeletePICashGroup_input{
      /**  Cash Group ID  */  
   groupID:string,
}

export interface DeletePICashGroup_output{
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
   */  
export interface DeletePNbyID_input{
   ipGroupID:string,
   ipHeadNum:number,
}

export interface DeletePNbyID_output{
}

   /** Required : 
      @param ipGroupID
   */  
export interface DeletePNotes_input{
   ipGroupID:string,
}

export interface DeletePNotes_output{
}

   /** Required : 
      @param postGroupID
   */  
export interface DeleteZeroAmtTaxRec_input{
      /**  The Group ID of the Group to post  */  
   postGroupID:string,
}

export interface DeleteZeroAmtTaxRec_output{
}

export interface Erp_Tablesets_ARPNDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Discount Amount. Base Currency.  */  
   DiscountAmt:number,
      /**  Discount Amount. Document Currency.  */  
   DocDiscountAmount:number,
      /**  Transaction Amount. Document Currency.  */  
   DocTranAmt:number,
      /**  Exchange Rate  */  
   ExchangeRate:number,
      /**  Get Default Tax ID's flag.  */  
   GetDfltTaxIds:boolean,
      /**  Posted to GL flag  */  
   GLPosted:boolean,
      /**  Reference to  invchead  */  
   InvoiceNum:number,
      /**  Legal Number  */  
   LegalNumber:string,
      /**  Posted flag  */  
   Posted:boolean,
      /**  Rate Group code  */  
   RateGrpCode:string,
      /**  Rounding Difference  */  
   RoundDiff:number,
      /**  Discount Amount. Report Currency 1.  */  
   Rpt1DiscountAmt:number,
      /**  Transaction Amount. Report Currency 1.  */  
   Rpt1TranAmt:number,
      /**  Discount Amount. Report Currency 2.  */  
   Rpt2DiscountAmt:number,
      /**  Transaction Amount. Report Currency 2.  */  
   Rpt2TranAmt:number,
      /**  Discount Amount. Report Currency 3.  */  
   Rpt3DiscountAmt:number,
      /**  Transaction Amount. Report Currency 3.  */  
   Rpt3TranAmt:number,
      /**  Tax Liability  */  
   TaxRegionCode:string,
      /**  Transaction Amount  */  
   TranAmt:number,
      /**  Transaction Date  */  
   TranDate:string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   GroupID:string,
      /**  The foreign key that relates this detail record to a ARPNHead record. Duplicated from ARPNHead.HeadNum when record is created. Not applicable to user interface.  */  
   HeadNum:number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   InvoiceRef:number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   DNAmount:number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   DocDnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3DnAmount:number,
      /**   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  */  
   TranType:string,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Tax Amount in the vendors currency.  */  
   DocTaxAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  */  
   FiscalPeriod:number,
      /**  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal Year Suffix.  */  
   FiscalYearSuffix:string,
      /**  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  */  
   Reference:string,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   GainLossType:string,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   ReverseGL:boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   RevalueDate:string,
      /**  PI Balance at the time of revaluation  */  
   RevalueBal:number,
      /**  Document currency PI Balance at the time of revaluation  */  
   DocRevalueBal:number,
      /**  Reporting currency PI Balance at the time of revaluation  */  
   Rpt1RevalueBal:number,
      /**  Reporting currency PI Balance at the time of revaluation  */  
   Rpt2RevalueBal:number,
      /**  Reporting currency PI Balance at the time of revaluation  */  
   Rpt3RevalueBal:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   InvoiceDate:string,
   DocInvoiceAmt:number,
   CurrencyCode:string,
   CurrencyDescription:string,
   BaseCurrDesc:string,
   BaseCurrSymbol:string,
   DocInvoiceBal:number,
   InvTermsCode:string,
   InvDiscountDate:string,
   InvDueDate:string,
   DocNetCash:number,
   DocNewBalance:number,
   InvLockRate:boolean,
   InvoiceBal:number,
   NewBalance:number,
   NetCash:number,
   GainLossAmt:number,
   ApplyDate:string,
   BillConNumber:number,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DispGLAcct:string,
   DispTranAmt:number,
   DocDispTranAmt:number,
   DocSelfAssessTax:number,
   DocWithholdTax:number,
   FullyPaid:boolean,
   InvExchRate:number,
   InvLegalNumber:string,
   InvoiceAmt:number,
   InvXRateLabel:string,
   LegalNumMessage:string,
   LegalNumStyle:string,
   OldGainLoss:number,
   PostToGL:boolean,
   SelfAssessTax:number,
   SoldToCustID:string,
   SoldToCustNum:number,
   SoldToCustomerName:string,
   WithholdTax:number,
   XRateLabel:string,
   Rpt1NewBalance:number,
   Rpt3NewBalance:number,
   Rpt1DispTranAmt:number,
   Rpt2DispTranAmt:number,
   Rpt3DispTranAmt:number,
   Rpt1OldGainLoss:number,
   Rpt2OldGainLoss:number,
   Rpt3OldGainLoss:number,
   Rpt1GainLossAmt:number,
   Rpt2GainLossAmt:number,
   Rpt3GainLossAmt:number,
   Rpt1InvoiceAmt:number,
   Rpt2InvoiceAmt:number,
   Rpt3InvoiceAmt:number,
   Rpt1InvoiceBal:number,
   Rpt2InvoiceBal:number,
   Rpt3InvoiceBal:number,
   Rpt2NewBalance:number,
   Rpt1NetCash:number,
   Rpt2NetCash:number,
   Rpt3NetCash:number,
   InvoicePosted:boolean,
   CurGroupID:string,
   BitFlag:number,
   CustNumName:string,
   CustNumCustID:string,
   CustNumBTName:string,
   InvoiceNumTermsCode:string,
   InvoiceNumCardMemberName:string,
   TaxRgnDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNHeadAttchRow{
   Company:string,
   GroupID:string,
   HeadNum:number,
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

export interface Erp_Tablesets_ARPNHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Transaction Amount  */  
   TranAmt:number,
      /**  Applied Amount  */  
   AppliedAmt:number,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Bank Amount  */  
   BankAmount:number,
      /**  Bank Slip Number of the promissory note.  */  
   BankSlip:string,
      /**  Base Amount  */  
   BaseAmount:number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   CashbookLine:number,
      /**  Company Bank Account ID  */  
   CompBankAcctID:string,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Customer Bank Account ID  */  
   CustBankAcctID:string,
      /**  Customer ID  */  
   CustID:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Description  */  
   Description:string,
      /**  Discount Amount. Base Currency.  */  
   DiscountAmt:number,
      /**  Applied Amount. Document Currency.  */  
   DocAppliedAmt:number,
      /**  Unapplied Amount. Document Currency.  */  
   DocUnAppliedAmt:number,
      /**  Tax Amount. Document Currency.  */  
   DocTaxAmt:number,
      /**  Transaction Amount. Document Currency.  */  
   DocTranAmt:number,
      /**  Withholding Amount. Document Currency.  */  
   DocWithholdAmt:number,
      /**  Exchange Rate  */  
   ExchangeRate:number,
      /**  Get Default Tax ID's flag.  */  
   GetDfltTaxIds:boolean,
      /**  Posted to GL flag  */  
   GLPosted:boolean,
      /**  Legal Number  */  
   LegalNumber:string,
      /**  Paid flag  */  
   Paid:boolean,
      /**  Posted flag  */  
   Posted:boolean,
      /**  Process Card  */  
   ProcessCard:string,
      /**  Rate Group code  */  
   RateGrpCode:string,
      /**  Recalculated before posting.  */  
   RecalcBeforePost:boolean,
      /**  Applied Amount. Report Currency 1.  */  
   Rpt1AppliedAmt:number,
      /**  Tax Amount. Report Currency 1.  */  
   Rpt1TaxAmt:number,
      /**  Transaction Amount. Report Currency 1.  */  
   Rpt1TranAmt:number,
      /**  Unapplied Amount. Report Currency 1.  */  
   Rpt1UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 1.  */  
   Rpt1WithholdAmt:number,
      /**  Applied Amount. Report Currency 2.  */  
   Rpt2AppliedAmt:number,
      /**  Tax Amount. Report Currency 2.  */  
   Rpt2TaxAmt:number,
      /**  Transaction Amount. Report Currency 2.  */  
   Rpt2TranAmt:number,
      /**  Unapplied Amount. Report Currency 2.  */  
   Rpt2UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 2.  */  
   Rpt2WithholdAmt:number,
      /**  Applied Amount. Report Currency 3.  */  
   Rpt3AppliedAmt:number,
      /**  Tax Amount. Report Currency 3.  */  
   Rpt3TaxAmt:number,
      /**  Transaction Amount. Report Currency 3.  */  
   Rpt3TranAmt:number,
      /**  Unapplied Amount. Report Currency 3.  */  
   Rpt3UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 3.  */  
   Rpt3WithholdAmt:number,
      /**  Signed flag  */  
   Signed:boolean,
      /**  Tax Amount. Base Currency.  */  
   TaxAmt:number,
      /**  Tax Liability  */  
   TaxRegionCode:string,
      /**  Total AR Amount  */  
   TotalARAmt:number,
      /**  Transaction Date  */  
   TransDate:string,
      /**  Unapplied Amount. Base Currency.  */  
   UnappliedAmt:number,
      /**  Voided Flag  */  
   Voided:boolean,
      /**  Withholding Amount. Base Currency.  */  
   WithholdAmt:number,
      /**  Company Name  */  
   CompanyName:string,
      /**  First company address line.  */  
   CompanyAddr1:string,
      /**  Second company address line.  */  
   CompanyAddr2:string,
      /**  Third company address line.  */  
   CompanyAddr3:string,
      /**  Company City portion of the address.  */  
   CompanyCity:string,
      /**  Company State portion of the address.  */  
   CompanyState:string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   CompanyPostalCode:string,
      /**  Company Country portion of the address.  */  
   CompanyCountry:string,
      /**  Company Name  */  
   CustomerName:string,
      /**  First customer address line.  */  
   CustomerAddr1:string,
      /**  Second customer address line.  */  
   CustomerAddr2:string,
      /**  Third customer address line.  */  
   CustomerAddr3:string,
      /**  Customer Stateportion of the address.  */  
   CustomerState:string,
      /**  Customer City portion of the address.  */  
   CustomerPostalCode:string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   CustomerCity:string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Reference to  invchead  */  
   InvoiceNum:number,
      /**  AR Payment Instrument ID  */  
   ARPromNoteID:string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   FiscalPeriod:number,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Transaction Type  */  
   TranType:string,
      /**  Sent Flag  */  
   Sent:boolean,
      /**  Type  */  
   Type:string,
      /**  Issue Date  */  
   IssueDate:string,
      /**  Due date of the promissory note.  */  
   DueDate:string,
      /**  Bank/Branch Code for company's bank.  */  
   CompBankBranchCode:string,
      /**  IBANCode for company's bank.  */  
   CompIBANCode:string,
      /**  Bank/Branch Code for customer's bank.  */  
   CustBankBranchCode:string,
      /**  IBAN Code for customer's bank.  */  
   CustIBANCode:string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   AutoGenerated:boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   DirectDeposit:boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   ClearedAmt:number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   ClearedPerson:string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPI:boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Customer's country code  */  
   CustCountryCode:number,
      /**  Customer country portion of the address.  */  
   CustomerCountry:string,
      /**  Promissory Note Status  */  
   PIStatus:string,
      /**  Current Group  */  
   CurGroupID:string,
      /**  Stage  */  
   PIStage:string,
      /**  Reason to change Company or Customer information  */  
   ChgComment:string,
      /**  Hold from Application reason  */  
   HoldReason:string,
      /**  Lock Exchange Rate  */  
   LockRate:boolean,
      /**  Reference to reversed PI  */  
   ReferseRef:number,
      /**  Reverse Date  */  
   ReverseDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  DiscountCashDate  */  
   DiscountCashDate:string,
   BaseCurrSymbol:string,
   BaseCurrencyCode:string,
   BaseCurrencyDesc:string,
   TermsDesc:string,
   CurrencyDesc:string,
   TotalCashReceived:number,
   CompanyBankName:string,
   CompanyBankAcct:string,
   CompanyBankIdentifier:string,
   CustomerBankName:string,
   CustomerBankAcct:string,
   CustomerBankIdentifier:string,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   calcRate:boolean,
   ApplyDate:string,
   BankCurrencyCode:string,
   BankCurrSymbol:string,
   BillToName:string,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
   CurrencySwitch:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocDiscount:number,
   DocReceipt:number,
   FullyPaid:boolean,
   LegalNumMessage:string,
   TotalRoundDiff:number,
   TranTaxAmt:number,
   XRateLabel:string,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
   Rpt1TranTaxAmt:number,
   Rpt2TranTaxAmt:number,
   Rpt3TranTaxAmt:number,
   CompBankBranchCodeDesc:string,
   CustBankBranchCodeDesc:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   HasLegNumCnfg:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
   PIStatusDesc:string,
      /**  like PIType.Initiation  */  
   PITypeInitiation:string,
   DocGainLossReal:number,
   DocGainLossUnreal:number,
   GainLossReal:number,
   GainLossUnreal:number,
   Rpt1GainLossReal:number,
   Rpt1GainLossUnreal:number,
   Rpt2GainLossReal:number,
   Rpt2GainLossUnreal:number,
   Rpt3GainLossReal:number,
   Rpt3GainLossUnreal:number,
   RevalueDate:string,
   DocDiscountAmt:number,
   Rpt1DiscountAmt:number,
   Rpt2DiscountAmt:number,
   Rpt3DiscountAmt:number,
   Receipt:number,
   Rpt1Receipt:number,
   Rpt2Receipt:number,
   Rpt3Receipt:number,
      /**  The Bank's full name.  */  
   BankAcctBankName:string,
      /**  Full description of the bank account.  */  
   BankAcctDescription:string,
      /**  Description  */  
   CashbookLineDescription:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  Status Description  */  
   PIStatusStatusDesc:string,
      /**  Type Description  */  
   PITypeDescription:string,
      /**  Description  */  
   RateGrpDescription:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionCodeDescription:string,
      /**  Description  */  
   TranDocTypeDescription:string,
   BankRecGainLoss:number,
   DocBankRecGainLoss:number,
   Rpt1BankRecGainLoss:number,
   Rpt2BankRecGainLoss:number,
   Rpt3BankRecGainLoss:number,
   BankTotalAmount:number,
   StatusChgTranDocType:string,
   StatusChgLegalNum:string,
      /**  for kinetic purposes  */  
   ARPNDtlExists:boolean,
      /**  for kinetic purposes  */  
   ARPNDtlInvoicePosted:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNHeadListTableset{
   ARPNHeadList:Erp_Tablesets_ARPNHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARPNHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Transaction Amount  */  
   TranAmt:number,
      /**  Applied Amount  */  
   AppliedAmt:number,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Bank Amount  */  
   BankAmount:number,
      /**  Bank Slip Number of the promissory note.  */  
   BankSlip:string,
      /**  Base Amount  */  
   BaseAmount:number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   CashbookLine:number,
      /**  Company Bank Account ID  */  
   CompBankAcctID:string,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Customer Bank Account ID  */  
   CustBankAcctID:string,
      /**  Customer ID  */  
   CustID:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Description  */  
   Description:string,
      /**  Discount Amount. Base Currency.  */  
   DiscountAmt:number,
      /**  Applied Amount. Document Currency.  */  
   DocAppliedAmt:number,
      /**  Unapplied Amount. Document Currency.  */  
   DocUnAppliedAmt:number,
      /**  Tax Amount. Document Currency.  */  
   DocTaxAmt:number,
      /**  Transaction Amount. Document Currency.  */  
   DocTranAmt:number,
      /**  Withholding Amount. Document Currency.  */  
   DocWithholdAmt:number,
      /**  Exchange Rate  */  
   ExchangeRate:number,
      /**  Get Default Tax ID's flag.  */  
   GetDfltTaxIds:boolean,
      /**  Posted to GL flag  */  
   GLPosted:boolean,
      /**  Legal Number  */  
   LegalNumber:string,
      /**  Paid flag  */  
   Paid:boolean,
      /**  Posted flag  */  
   Posted:boolean,
      /**  Process Card  */  
   ProcessCard:string,
      /**  Rate Group code  */  
   RateGrpCode:string,
      /**  Recalculated before posting.  */  
   RecalcBeforePost:boolean,
      /**  Applied Amount. Report Currency 1.  */  
   Rpt1AppliedAmt:number,
      /**  Tax Amount. Report Currency 1.  */  
   Rpt1TaxAmt:number,
      /**  Transaction Amount. Report Currency 1.  */  
   Rpt1TranAmt:number,
      /**  Unapplied Amount. Report Currency 1.  */  
   Rpt1UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 1.  */  
   Rpt1WithholdAmt:number,
      /**  Applied Amount. Report Currency 2.  */  
   Rpt2AppliedAmt:number,
      /**  Tax Amount. Report Currency 2.  */  
   Rpt2TaxAmt:number,
      /**  Transaction Amount. Report Currency 2.  */  
   Rpt2TranAmt:number,
      /**  Unapplied Amount. Report Currency 2.  */  
   Rpt2UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 2.  */  
   Rpt2WithholdAmt:number,
      /**  Applied Amount. Report Currency 3.  */  
   Rpt3AppliedAmt:number,
      /**  Tax Amount. Report Currency 3.  */  
   Rpt3TaxAmt:number,
      /**  Transaction Amount. Report Currency 3.  */  
   Rpt3TranAmt:number,
      /**  Unapplied Amount. Report Currency 3.  */  
   Rpt3UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 3.  */  
   Rpt3WithholdAmt:number,
      /**  Signed flag  */  
   Signed:boolean,
      /**  Tax Amount. Base Currency.  */  
   TaxAmt:number,
      /**  Tax Liability  */  
   TaxRegionCode:string,
      /**  Total AR Amount  */  
   TotalARAmt:number,
      /**  Transaction Date  */  
   TransDate:string,
      /**  Unapplied Amount. Base Currency.  */  
   UnappliedAmt:number,
      /**  Voided Flag  */  
   Voided:boolean,
      /**  Withholding Amount. Base Currency.  */  
   WithholdAmt:number,
      /**  Company Name  */  
   CompanyName:string,
      /**  First company address line.  */  
   CompanyAddr1:string,
      /**  Second company address line.  */  
   CompanyAddr2:string,
      /**  Third company address line.  */  
   CompanyAddr3:string,
      /**  Company City portion of the address.  */  
   CompanyCity:string,
      /**  Company State portion of the address.  */  
   CompanyState:string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   CompanyPostalCode:string,
      /**  Company Country portion of the address.  */  
   CompanyCountry:string,
      /**  Company Name  */  
   CustomerName:string,
      /**  First customer address line.  */  
   CustomerAddr1:string,
      /**  Second customer address line.  */  
   CustomerAddr2:string,
      /**  Third customer address line.  */  
   CustomerAddr3:string,
      /**  Customer Stateportion of the address.  */  
   CustomerState:string,
      /**  Customer City portion of the address.  */  
   CustomerPostalCode:string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   CustomerCity:string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Reference to  invchead  */  
   InvoiceNum:number,
      /**  AR Payment Instrument ID  */  
   ARPromNoteID:string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   FiscalPeriod:number,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Transaction Type  */  
   TranType:string,
      /**  Sent Flag  */  
   Sent:boolean,
      /**  Type  */  
   Type:string,
      /**  Issue Date  */  
   IssueDate:string,
      /**  Due date of the promissory note.  */  
   DueDate:string,
      /**  Bank/Branch Code for company's bank.  */  
   CompBankBranchCode:string,
      /**  IBANCode for company's bank.  */  
   CompIBANCode:string,
      /**  Bank/Branch Code for customer's bank.  */  
   CustBankBranchCode:string,
      /**  IBAN Code for customer's bank.  */  
   CustIBANCode:string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   AutoGenerated:boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   DirectDeposit:boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   ClearedAmt:number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   ClearedPerson:string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPI:boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Customer's country code  */  
   CustCountryCode:number,
      /**  Customer country portion of the address.  */  
   CustomerCountry:string,
      /**  Promissory Note Status  */  
   PIStatus:string,
      /**  Current Group  */  
   CurGroupID:string,
      /**  Stage  */  
   PIStage:string,
      /**  Reason to change Company or Customer information  */  
   ChgComment:string,
      /**  Hold from Application reason  */  
   HoldReason:string,
      /**  Lock Exchange Rate  */  
   LockRate:boolean,
      /**  Reference to reversed PI  */  
   ReferseRef:number,
      /**  Reverse Date  */  
   ReverseDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  TotalBankFee  */  
   TotalBankFee:number,
      /**  DocTotalBankFee  */  
   DocTotalBankFee:number,
      /**  Rpt1TotalBankFee  */  
   Rpt1TotalBankFee:number,
      /**  Rpt2TotalBankFee  */  
   Rpt2TotalBankFee:number,
      /**  Rpt3TotalBankFee  */  
   Rpt3TotalBankFee:number,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  Issuer Name  */  
   IssuerName:string,
      /**  Signed By  */  
   SignedBy:string,
      /**  Signed Date  */  
   SignedDate:string,
      /**  Signee Address 1  */  
   SigneeAddr1:string,
      /**  Signee Address 2  */  
   SigneeAddr2:string,
      /**  Signee Address 3  */  
   SigneeAddr3:string,
      /**  Signee City  */  
   SigneeCity:string,
      /**  Signee State  */  
   SigneeState:string,
      /**  Signee Postal Code  */  
   SigneeZip:string,
      /**  Signee Country Number  */  
   SigneeCountryNum:number,
      /**  Signee Phone  */  
   SigneePhoneNum:string,
      /**  Signee Email Address  */  
   SigneeEMailAddress:string,
      /**  Signee Comment  */  
   SigneeComment:string,
      /**  DiscountChargeAmt  */  
   DiscountChargeAmt:number,
      /**  DocDiscountChargeAmt  */  
   DocDiscountChargeAmt:number,
      /**  Rpt1DiscountChargeAmt  */  
   Rpt1DiscountChargeAmt:number,
      /**  Rpt2DiscountChargeAmt  */  
   Rpt2DiscountChargeAmt:number,
      /**  Rpt3DiscountChargeAmt  */  
   Rpt3DiscountChargeAmt:number,
      /**  Signee Bank Name  */  
   SigneeBankName:string,
      /**  Signee Bank Account Number  */  
   SigneeBankAcct:string,
      /**  Signee Bank Identifier  */  
   SigneeBankIdentifier:string,
      /**  Signee IBAN Code  */  
   SigneeIBANCode:string,
      /**  Signee Bank BranchCode  */  
   SigneeBankBranchCode:string,
      /**  DiscountCashDate  */  
   DiscountCashDate:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
   ApplyDate:string,
   BankCurrencyCode:string,
   BankCurrSymbol:string,
   BankRecGainLoss:number,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   calcRate:boolean,
   CompanyBankAcct:string,
   CompanyBankIdentifier:string,
   CompanyBankName:string,
   CompBankBranchCodeDesc:string,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
   CurrencyDesc:string,
   CurrencySwitch:boolean,
   CustBankBranchCodeDesc:string,
   CustomerBankAcct:string,
   CustomerBankIdentifier:string,
   CustomerBankName:string,
   DisableBankAcctIDPI:boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   DisableBankAmt:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocBankRecGainLoss:number,
   DocDiscount:number,
   DocDiscountAmt:number,
   DocGainLossReal:number,
   DocGainLossUnreal:number,
   DocReceipt:number,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
   FullyPaid:boolean,
   GainLossReal:number,
   GainLossUnreal:number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   HasLegNumCnfg:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumMessage:string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   PIStatusDesc:string,
      /**  like PIType.Initiation  */  
   PITypeInitiation:string,
   Receipt:number,
   RevalueDate:string,
   Rpt1BankRecGainLoss:number,
   Rpt1DiscountAmt:number,
   Rpt1GainLossReal:number,
   Rpt1GainLossUnreal:number,
   Rpt1Receipt:number,
   Rpt1TranTaxAmt:number,
   Rpt2BankRecGainLoss:number,
   Rpt2DiscountAmt:number,
   Rpt2GainLossReal:number,
   Rpt2GainLossUnreal:number,
   Rpt2Receipt:number,
   Rpt2TranTaxAmt:number,
   Rpt3BankRecGainLoss:number,
   Rpt3DiscountAmt:number,
   Rpt3GainLossReal:number,
   Rpt3GainLossUnreal:number,
   Rpt3Receipt:number,
   Rpt3TranTaxAmt:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   StatusChgLegalNum:string,
   StatusChgTranDocType:string,
   TermsDesc:string,
   TotalCashReceived:number,
   TotalRoundDiff:number,
   TranTaxAmt:number,
   TypeDesc:string,
   XRateLabel:string,
   BankTotalAmount:number,
   BaseCurrencyCode:string,
   BaseCurrencyDesc:string,
   BaseCurrSymbol:string,
   BillToName:string,
   DocDiscountedAmt:number,
      /**  for kinetic purposes  */  
   ARPNDtlExists:boolean,
      /**  for kinetic purposes  */  
   ARPNDtlInvoicePosted:boolean,
   BitFlag:number,
   BankAcctDescription:string,
   BankAcctBankName:string,
   CashbookLineDescription:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CustNumInactive:boolean,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   PIStatusStatusDesc:string,
   PITypeDescription:string,
   RateGrpDescription:string,
   TaxRegionCodeDescription:string,
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNHeadTGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   TGLCTranNum:number,
      /**  String identifier of the account context.  */  
   GLAcctContext:string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   BookID:string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   COACode:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Indicates if the user can update or delete this record.  */  
   UserCanModify:boolean,
      /**  Segement Value 1 of the account for this context.  */  
   SegValue1:string,
      /**  Segement Value 2 of the account for this context.  */  
   SegValue2:string,
      /**  Segement Value 3 of the account for this context.  */  
   SegValue3:string,
      /**  Segement Value 4 of the account for this context.  */  
   SegValue4:string,
      /**  Segement Value 5 of the account for this context.  */  
   SegValue5:string,
      /**  Segement Value 6 of the account for this context.  */  
   SegValue6:string,
      /**  Segement Value 7 of the account for this context.  */  
   SegValue7:string,
      /**  Segement Value 8 of the account for this context.  */  
   SegValue8:string,
      /**  Segement Value 9 of the account for this context.  */  
   SegValue9:string,
      /**  Segement Value 10 of the account for this context.  */  
   SegValue10:string,
      /**  Segement Value 11 of the account for this context.  */  
   SegValue11:string,
      /**  Segement Value 12 of the account for this context.  */  
   SegValue12:string,
      /**  Segement Value 13 of the account for this context.  */  
   SegValue13:string,
      /**  Segement Value 14 of the account for this context.  */  
   SegValue14:string,
      /**  Segement Value 15 of the account for this context.  */  
   SegValue15:string,
      /**  Segement Value 16 of the account for this context.  */  
   SegValue16:string,
      /**  Segement Value 17 of the account for this context.  */  
   SegValue17:string,
      /**  Segement Value 18 of the account for this context.  */  
   SegValue18:string,
      /**  Segement Value 19 of the account for this context.  */  
   SegValue19:string,
      /**  Segement Value 20 of the account for this context.  */  
   SegValue20:string,
      /**  Unique Identifier of the system GL Control Type.  */  
   SysGLControlType:string,
      /**  System generated GL Control Identifier.  */  
   SysGLControlCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   FiscalYear:number,
      /**  JournalCode of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Journal number of the related GLJrnDtl.  */  
   JournalNum:number,
      /**  JournalLine of the related GLJrnDtl.  */  
   JournalLine:number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   TranDate:string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   TranSource:string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborDtlSeq:number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysDate:string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysTime:number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   TranNum:number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   ARInvoiceNum:number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   TransAmt:number,
      /**  Invoice Line Number associated with this GL Journal  */  
   InvoiceLine:number,
      /**  The sequence number associated with this GL journal  */  
   SeqNum:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  BookCreditAmount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   RecordType:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  this field equals ABTUID which was created during posting  */  
   ABTUID:string,
      /**  Technical identifier.  */  
   RuleUID:number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  IsModifiedByUser  */  
   IsModifiedByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  MovementType  */  
   MovementType:string,
      /**  Plant  */  
   Plant:string,
      /**  HeadNum of ARPNHead  */  
   HeadNum:number,
      /**  GroupID of ARPNHead  */  
   GroupID:string,
   BitFlag:number,
   COADescription:string,
   GLAccountGLAcctDisp:string,
   GLAccountAccountDesc:string,
   GLAccountGLShortAcct:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNListRow{
   ARPromNoteID:string,
   Company:string,
   CurGroupID:string,
   CustID:string,
   GroupID:string,
   HeadNum:number,
   PIStage:string,
   PIStatus:string,
   TranAmt:number,
   Type:string,
   Selected:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNMoveRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  Movement Order  */  
   Seq:number,
      /**  Current Group ID  */  
   CurGroupID:string,
      /**  Status  */  
   PIStatus:string,
      /**  Stage  */  
   PIStage:string,
      /**  Posted  */  
   Posted:boolean,
      /**  Date created  */  
   CreateDate:string,
      /**  Created By User  */  
   CreateUser:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Move Type  */  
   Type:string,
      /**  Comment  */  
   Comment:string,
      /**  Transaction Date  */  
   TranDate:string,
      /**  Creation Time  */  
   CreateTime:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Reference to Endorsed AP PI GroupID.  */  
   EndorsedAPPNGroupID:string,
      /**  Reference to Endorsed AP PI HeadNum.  */  
   EndorsedAPPNHeadNum:number,
      /**  Description  */  
   Description:string,
      /**  PI status description  */  
   PIStatusDesc:string,
      /**  Posting Error Message  */  
   PostErrMess:string,
      /**  Indicates if posting GL transactions.  */  
   PostToGL:boolean,
      /**  PI Type description  */  
   TypeDesc:string,
   LegalNumMessage:string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   LegalNumStyle:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNMoveTableset{
   ARPNMove:Erp_Tablesets_ARPNMoveRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARPromissoryNotesTableset{
   ARPNHead:Erp_Tablesets_ARPNHeadRow[],
   ARPNHeadAttch:Erp_Tablesets_ARPNHeadAttchRow[],
   BankTran:Erp_Tablesets_BankTranRow[],
   BankTranTaxDtl:Erp_Tablesets_BankTranTaxDtlRow[],
   BankTranTGLC:Erp_Tablesets_BankTranTGLCRow[],
   ARPNDtl:Erp_Tablesets_ARPNDtlRow[],
   TaxDtl:Erp_Tablesets_TaxDtlRow[],
   ARPNHeadTGLC:Erp_Tablesets_ARPNHeadTGLCRow[],
   ARPNList:Erp_Tablesets_ARPNListRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BankTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Relates record to a BankAcct.  */  
   BankAcctID:string,
      /**  Unique ID of the Transaction.  */  
   TranNum:number,
      /**  Date that the transaction took place.  */  
   TranDate:string,
      /**  Amount of the Transaction  */  
   TranAmt:number,
      /**  Transaction Reference  */  
   TranRef:string,
      /**  Indicates that the Transaction (not cleared variance) has been posted to G/L.  When the Bank Statement is posted all Non-G/L Posted adjustments for the bank are posted to G/L using the Bank Account's Cash and Bank Fee Accounts. G/L Posted Transactions cannot be deleted. (System Set)  */  
   GLPosted:boolean,
      /**  Person who entered the transaction (System Set).  */  
   EntryPerson:string,
      /**  Date that the Transaction was entered into the system (System Set).  */  
   EntryDate:string,
      /**  Time that the transaction was entered into the system - in HH:MM:SS format (System Set).  */  
   EntryTime:string,
      /**  Indicates the transaction's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   TranCleared:boolean,
      /**  Indicates that the transaction is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   TranClearPending:boolean,
      /**  Amount that the Transaction was cleared for.  */  
   TranClearedAmt:number,
      /**  Person who cleared the transaction (System Set).  */  
   TranClearedPerson:string,
      /**  Date that the Transaction was cleared in the system (System Set).  */  
   TranClearedDate:string,
      /**  Time that the transaction was cleared in the system - in HH:MM:SS format (System Set).  */  
   TranClearedTime:string,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   BankSlip:string,
      /**  Fiscal year that entry applies to.  */  
   FiscalYear:number,
      /**  Fiscal period the transaction was posted to. Only pertains to when posted to GL.  */  
   FiscalPeriod:number,
      /**  Journal Number of related GLJrnDtl.  */  
   JournalNum:number,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Document amount of the Transaction  */  
   DocTranAmt:number,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Exchange rate that is used for this bank transaction.  */  
   ExchangeRate:number,
      /**  Document amount that the Transaction was cleared for.  */  
   DocTranClearedAmt:number,
      /**  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  */  
   GroupID:string,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   GLRefCodeDesc:string,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranClearedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Fiscal year suffix that entry applies to.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Unique ID of the Fee  */  
   BankFeeID:string,
      /**  The Fee amount; this amount plus the Fee tax amount will compose the total of the charge on the statement  */  
   BankFeeAmt:number,
      /**  The Tax Amount that has been charged to the fee  */  
   BankFeeTaxAmt:number,
      /**  The Fee amount in Base Currency  */  
   DocBankFeeAmt:number,
      /**  The Tax Amount that has been charged to the fee in Base Currency  */  
   DocBankFeeTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1BankFeeAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2BankFeeAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3BankFeeAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1BankFeeTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2BankFeeTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3BankFeeTaxAmt:number,
      /**   Used for Bank Fee Functionality, indicates the module that created this BankFee.  This is assigned by the system.
Values can be; AR, AP and BA.  */  
   SourceModule:string,
      /**  Consecutive from the AP and AR transactions, this field is used to identify the AP or AR transaction that created this Bank Fee  */  
   HeadNum:number,
      /**  Indiates if the BankTran has been voided.  The TranNum field will be the same as the original transaction  */  
   Voided:boolean,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   GainLossType:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   ReverseGL:boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   RevalueDate:string,
      /**  Bank Balance at the time of revaluation  */  
   RevalueBal:number,
      /**  Document currency Bank Balance at the time of revaluation  */  
   DocRevalueBal:number,
      /**  Reporting currency Bank Balance at the time of revaluation  */  
   Rpt1RevalueBal:number,
      /**  Reporting currency Bank Balance at the time of revaluation  */  
   Rpt2RevalueBal:number,
      /**  Reporting currency Bank Balance at the time of revaluation  */  
   Rpt3RevalueBal:number,
      /**  Legal Number for the record.  */  
   LegalNumber:string,
      /**  Transaction Document for the record.  */  
   TranDocTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CNCFICode  */  
   CNCFICode:string,
      /**  CNToCFICode  */  
   CNToCFICode:string,
      /**  BankRecGainLoss  */  
   BankRecGainLoss:number,
      /**  Rpt1BankRecGainLoss  */  
   Rpt1BankRecGainLoss:number,
      /**  Rpt2BankRecGainLoss  */  
   Rpt2BankRecGainLoss:number,
      /**  Rpt3BankRecGainLoss  */  
   Rpt3BankRecGainLoss:number,
      /**  BalanceUpdated  */  
   BalanceUpdated:number,
      /**  DocBankRecGainLoss  */  
   DocBankRecGainLoss:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  Indicates that transaction is currently excluded from batch in Bank Statement Processing.  */  
   BankBatchExcluded:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  ABTUID  */  
   ABTUID:string,
      /**  Multi-Site related Site  */  
   Plant:string,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
   CNCFICodeDescription:string,
      /**  Cash Receipt currency code  */  
   CRCurrCode:string,
      /**  Cash Receipt Rate group code  */  
   CRRateGrpCode:string,
      /**  Cash Receipt Tran amount  */  
   CRTranAmt:number,
      /**  Cash Receipt Transaction Cleared Amount  */  
   CRTranClearedAmt:number,
      /**  Currency Switch  */  
   CurrencySwitch:boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   DisableBankAmt:boolean,
      /**  The flag to indicate if the Display amount is supposed to be reversed  */  
   DispAmtReverse:boolean,
   DispDocTranAmt:number,
   DispDocTranClearedAmt:number,
   DispTranAmt:number,
   DispTranClearedAmt:number,
      /**  Used for tree structure/parent view definition in Petty Cash Entry  */  
   InternalDate:string,
   IsFiltered:boolean,
      /**  Indicates if the record is locked by review journal for bank reconciliation  */  
   IsLockedBankRec:boolean,
   LegalNumMessage:string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   LegalNumStyle:string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   RefCodeStatus:string,
   Rpt1DispTranAmt:number,
   Rpt1DispTranClearedAmt:number,
   Rpt2DispTranAmt:number,
   Rpt2DispTranClearedAmt:number,
   Rpt3DispTranAmt:number,
   Rpt3DispTranClearedAmt:number,
   EnableAssignLegNum:boolean,
   EnableTranDocType:boolean,
   EnableVoidLegNum:boolean,
   HasLegNumCnfg:boolean,
   AllowChgAfterPrint:boolean,
      /**  Display GL Account  */  
   GLAccount:string,
   BitFlag:number,
   BankAcctIDBankName:string,
   BankAcctIDDescription:string,
   BankFeeIDDescription:string,
   BankFeeIDTaxCode:string,
   CashbookLineDescription:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrName:string,
   JournalCodeJrnlDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BankTranTGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   TGLCTranNum:number,
      /**  String identifier of the account context.  */  
   GLAcctContext:string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   BookID:string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   COACode:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Indicates if the user can update or delete this record.  */  
   UserCanModify:boolean,
      /**  Segement Value 1 of the account for this context.  */  
   SegValue1:string,
      /**  Segement Value 2 of the account for this context.  */  
   SegValue2:string,
      /**  Segement Value 3 of the account for this context.  */  
   SegValue3:string,
      /**  Segement Value 4 of the account for this context.  */  
   SegValue4:string,
      /**  Segement Value 5 of the account for this context.  */  
   SegValue5:string,
      /**  Segement Value 6 of the account for this context.  */  
   SegValue6:string,
      /**  Segement Value 7 of the account for this context.  */  
   SegValue7:string,
      /**  Segement Value 8 of the account for this context.  */  
   SegValue8:string,
      /**  Segement Value 9 of the account for this context.  */  
   SegValue9:string,
      /**  Segement Value 10 of the account for this context.  */  
   SegValue10:string,
      /**  Segement Value 11 of the account for this context.  */  
   SegValue11:string,
      /**  Segement Value 12 of the account for this context.  */  
   SegValue12:string,
      /**  Segement Value 13 of the account for this context.  */  
   SegValue13:string,
      /**  Segement Value 14 of the account for this context.  */  
   SegValue14:string,
      /**  Segement Value 15 of the account for this context.  */  
   SegValue15:string,
      /**  Segement Value 16 of the account for this context.  */  
   SegValue16:string,
      /**  Segement Value 17 of the account for this context.  */  
   SegValue17:string,
      /**  Segement Value 18 of the account for this context.  */  
   SegValue18:string,
      /**  Segement Value 19 of the account for this context.  */  
   SegValue19:string,
      /**  Segement Value 20 of the account for this context.  */  
   SegValue20:string,
      /**  Unique Identifier of the system GL Control Type.  */  
   SysGLControlType:string,
      /**  System generated GL Control Identifier.  */  
   SysGLControlCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   FiscalYear:number,
      /**  JournalCode of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Journal number of the related GLJrnDtl.  */  
   JournalNum:number,
      /**  JournalLine of the related GLJrnDtl.  */  
   JournalLine:number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   TranDate:string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   TranSource:string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborDtlSeq:number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysDate:string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysTime:number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   TranNum:number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   ARInvoiceNum:number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   TransAmt:number,
      /**  Invoice Line Number associated with this GL Journal  */  
   InvoiceLine:number,
      /**  The sequence number associated with this GL journal  */  
   SeqNum:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  BookCreditAmount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   RecordType:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  this field equals ABTUID which was created during posting  */  
   ABTUID:string,
      /**  Technical identifier.  */  
   RuleUID:number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  IsModifiedByUser  */  
   IsModifiedByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  MovementType  */  
   MovementType:string,
      /**  Plant  */  
   Plant:string,
      /**  GroupID for relation to BankTran  */  
   GroupID:string,
   HeadNum:number,
      /**  Used for tree structure/parent view definition in Petty Cash Entry  */  
   InternalDate:string,
   PCashDeskID:string,
   PCashRefNum:number,
      /**  Voided flag for relation to BankTran  */  
   Voided:boolean,
      /**  BankAcctID for relation to BankTran  */  
   BankAcctID:string,
   BitFlag:number,
   COADescription:string,
   GLAccountGLShortAcct:string,
   GLAccountGLAcctDisp:string,
   GLAccountAccountDesc:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BankTranTaxDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Indicates the module that created this tax detail.  This is assigned by the system.
Values can be; AR, AP.  */  
   SourceModule:string,
      /**  HeadNum  */  
   HeadNum:number,
      /**  Integer assigned by the system copied from APTran.  */  
   APTranNo:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Taxable amount for this invoice. Manually entered if the currency is the base currency.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount. Manually entered if the currency is the base currency.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency. Manually entered.  */  
   DocTaxAmt:number,
      /**  Reverse Charge.  */  
   ReverseCharge:boolean,
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
      /**  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  */  
   InvoiceNum:number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   InvoiceRef:number,
      /**   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  */  
   ECAcquisitionSeq:number,
      /**  Relates record to a BankAcct.  */  
   BankAcctID:string,
      /**  Unique ID of the Transaction.  */  
   TranNum:number,
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
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
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
      /**  Discount Tax Adjustment  */  
   DiscTaxAdj:number,
      /**  Discount Tax Adjustment in foreign currency.  */  
   DocDiscTaxAdj:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscTaxAdj:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscTaxAdj:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscTaxAdj:number,
      /**  Discount Taxable Adjustment  */  
   DiscTaxableAdj:number,
      /**  Discount Taxable Adjustment in foreign currency.  */  
   DocDiscTaxableAdj:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscTaxableAdj:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscTaxableAdj:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscTaxableAdj:number,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Indicates if transaction was voided.  The rest of the unique key will contain the original transaction values (like APTran)  */  
   Voided:boolean,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   Rpt1TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   Rpt2TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   Rpt3TaxAmtVar:number,
      /**  Discount Tax Adjustment Variance  */  
   DiscTaxAdjVar:number,
      /**  Discount Tax Adjustment Variance  */  
   DocDiscTaxAdjVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscTaxAdjVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscTaxAdjVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscTaxAdjVar:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGOrigTaxableAmt  */  
   AGOrigTaxableAmt:number,
      /**  GainLoss  */  
   GainLoss:number,
      /**  DocGainLoss  */  
   DocGainLoss:number,
      /**  Rpt1GainLoss  */  
   Rpt1GainLoss:number,
      /**  Rpt2GainLoss  */  
   Rpt2GainLoss:number,
      /**  Rpt3GainLoss  */  
   Rpt3GainLoss:number,
      /**  CNCFICode  */  
   CNCFICode:string,
      /**  APInvoiceNum  */  
   APInvoiceNum:string,
      /**  TranType  */  
   TranType:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
   CNCFICodeDescription:string,
   CTDescription:string,
      /**  Flag to indicate if Manual checkbox should be disabled  */  
   DisableManual:boolean,
      /**  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  */  
   GroupID:string,
      /**  Used for tree structure/parent view definition in Petty Cash Entry  */  
   InternalDate:string,
   IsFiltered:boolean,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnDtlMovTableset{
   GLJrnDtl:Erp_Tablesets_GLJrnDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLJrnDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Fiscal year that entry applies to.  */  
   FiscalYear:number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   JournalNum:number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   JournalLine:number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   Description:string,
      /**  Date for this journal transaction entry.  */  
   JEDate:string,
      /**  Fiscal period that this journal entry applies to.  */  
   FiscalPeriod:number,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  User ID that posted this translation.  */  
   PostedBy:string,
      /**  Date that this transaction was posted to the G/L files.  */  
   PostedDate:string,
      /**  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  */  
   Posted:boolean,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   SourceModule:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   ARInvoiceNum:number,
      /**  BankAcctId of the BankAcct master that this check was drawn  against.  */  
   BankAcctID:string,
      /**  Check number.  */  
   CheckNum:number,
      /**  Cash Receipts reference field.  */  
   CRHeadNum:number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   Reverse:boolean,
      /**  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  */  
   BankTranNum:number,
      /**   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   BankSlip:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefType:string,
      /**  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefCode:string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalNum:number,
      /**  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalLine:number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   GlbJournalCode:string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   GlbVendorNum:number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   GlbAPInvoiceNum:string,
      /**  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  */  
   MultiCompany:boolean,
      /**  Linked to a Multi-Company Journal.  */  
   Linked:boolean,
      /**  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  */  
   CommentText:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   GlbCompanyID:string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   GlbFiscalYear:number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   GlbFiscalPeriod:number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   GlbGroupID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAccount:string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   SegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   SegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   SegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   SegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   SegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   SegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   SegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   SegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   SegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   SegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   SegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   SegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   SegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   SegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   SegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   SegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   SegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   SegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SegValue20:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   ExtGLAccount:string,
      /**  External Segment Value 1  */  
   ExtSegValue1:string,
      /**  External Segment Value 2  */  
   ExtSegValue2:string,
      /**  External Segment Value 3  */  
   ExtSegValue3:string,
      /**  External Segment Value 4  */  
   ExtSegValue4:string,
      /**  External Segment Value 5  */  
   ExtSegValue5:string,
      /**  External Segment Value 6  */  
   ExtSegValue6:string,
      /**  External Segment Value 7  */  
   ExtSegValue7:string,
      /**  External Segment Value 8  */  
   ExtSegValue8:string,
      /**  External Segment Value 9  */  
   ExtSegValue9:string,
      /**  External Segment Value 10  */  
   ExtSegValue10:string,
      /**  External Segment Value 11  */  
   ExtSegValue11:string,
      /**  External Segment Value 12  */  
   ExtSegValue12:string,
      /**  External Segment Value 13  */  
   ExtSegValue13:string,
      /**  External Segment Value 14  */  
   ExtSegValue14:string,
      /**  External Segment Value 15  */  
   ExtSegValue15:string,
      /**  External Segment Value 16  */  
   ExtSegValue16:string,
      /**  External Segment Value 17  */  
   ExtSegValue17:string,
      /**  External Segment Value 18  */  
   ExtSegValue18:string,
      /**  External Segment Value 19  */  
   ExtSegValue19:string,
      /**  External Segment Value 20  */  
   ExtSegValue20:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**  Legal Number of source document  */  
   LegalNumber:string,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   PerBalFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   TBFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   DailyBalFlag:boolean,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Fiscal year suffix.  */  
   GlbFiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   GlbFiscalCalendarID:string,
      /**  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  */  
   IntermediateProc:boolean,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  */  
   SrcCompany:string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SrcBook:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   SrcGLAccount:string,
      /**  Source Journal Code  */  
   SrcJrnlCode:string,
      /**  Source Journal Number  */  
   SrcJournalNum:number,
      /**  Source Journal Line  */  
   SrcJournalLine:number,
      /**   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  */  
   SrcType:string,
      /**  this field equas ABTUID which was created during posting  */  
   ABTUID:string,
      /**  This field shows Debit value of transaction  */  
   DebitAmount:number,
      /**  This field shows Credit value of transaction  */  
   CreditAmount:number,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   BookDebitAmount:number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   BookCreditAmount:number,
      /**  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  */  
   ParentRUID:string,
      /**  if has reverse line  */  
   HasReverseLine:boolean,
      /**  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  */  
   BalanceAcct:string,
      /**  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  */  
   TrialAcct:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  This is the last allocation stamp that affected this GLJrnDtl.  */  
   AllocationStamp:string,
      /**  Identifies the allocation batch this journal entry was processed under.  */  
   BatchID:string,
      /**  This is the allocation id that processed this journal entry.  */  
   AllocID:string,
      /**  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  */  
   RunNbr:number,
      /**  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  */  
   AllocRunNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtSeq:number,
      /**  External COA Code  */  
   ExtCOACode:string,
      /**  MatchCode is used to match two or more journal detail records together.  */  
   MatchCode:string,
      /**  MatchDate is set when the journal detail record is matched to other journal detail records.  */  
   MatchDate:string,
      /**  Indicates whether or not the transaction has been flagged as reconciled.  */  
   Reconciled:boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Journal Sequence Number  */  
   Sequence:number,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   CustNum:number,
      /**  CloseFiscalPeriod  */  
   CloseFiscalPeriod:number,
      /**  SourcePlant  */  
   SourcePlant:string,
      /**  Plant  */  
   Plant:string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   ExtSysType:string,
      /**  URL for drill back to an integrated external system  */  
   ExtSysURL:string,
      /**   Colombia Loc field            
This field is used as external calculated only.  */  
   COOneTimeDesc:string,
      /**   Colombia Loc field.           
This field is used as external calculated only.  */  
   COOneTimeID:string,
      /**  DEA Code  */  
   DEACodeDesc:string,
      /**  DEA End Date  */  
   DEAEndDate:string,
      /**  DEA Start Date  */  
   DEAStartDate:string,
      /**  Deferred Expense  */  
   DeferredExp:boolean,
      /**  DEA Distributed Amount  */  
   Distributed:number,
      /**  DEA Distributed Amount in Doc Currency  */  
   DocDistributed:number,
      /**  DEA Expense Amount in Doc Currency  */  
   DocExpense:number,
      /**  DEA Recognized Amount in Doc Currency  */  
   DocRecognized:number,
      /**  DEA Remaining Amount in Doc Currency  */  
   DocRemaining:number,
      /**  DEA Unrecognized Amount in Doc Currency  */  
   DocUnrecognized:number,
      /**  Flag to indicate if the MultiCompany check box needs to be enabled.  */  
   EnableMultiCompany:boolean,
      /**  DEA Expense Amount  */  
   Expense:number,
   ExtRefAcctChart:string,
   ExtRefAcctDept:string,
   ExtRefAcctDiv:string,
   ExtRefCodeStatus:string,
   GLAcctDisp:string,
      /**  External field used in Journal Tracker and Chart tracker. Journal Comments tab.  */  
   HeaderCommentText:string,
      /**  Manual GL Journal Line Reference.  */  
   LineReference:string,
      /**  Manual GL Journal Line Reference Holder.  */  
   LineReferenceHolder:string,
      /**  Manual GL Journal Line Reference Holder Name.  */  
   LineReferenceHolderName:string,
      /**  Manual GL Journal Line Reference Type.  */  
   LineReferenceType:string,
   MovementNum:number,
      /**  Apply Date of the Original Transaction  */  
   OrigApplyDate:string,
      /**  Journal line of the original transaction that was reversed.  */  
   OrigJrnlLine:number,
      /**  Journal number of the original transaction that was reversed.  */  
   OrigJrnlNbr:number,
      /**  Fiscal year of the original transaction that was reversed.  */  
   OrigJrnlYear:number,
      /**  Fiscal year suffix of the original transaction that was reversed.  */  
   OrigJrnlYearSuffix:string,
      /**  DEA Recognized Amount  */  
   Recognized:number,
   RefAcctChart:string,
   RefAcctDept:string,
   RefAcctDiv:string,
   RefCodeStatus:string,
      /**  DEA Remaining Amount  */  
   Remaining:number,
      /**  Apply date of the reversing transaction  */  
   RevApplyDate:string,
      /**  Journal line of the latest journal entry made to reverse a transaction.  */  
   RevJrnlLine:number,
      /**  Journal number of the latest journal entry made to reverse a transaction.  */  
   RevJrnlNbr:number,
      /**  Fiscal year of the latest journal entry made to reverse a transaction.  */  
   RevJrnlYear:number,
      /**  Fiscal year suffix of the latest journal entry made to reverse a transaction.  */  
   RevJrnlYearSuffix:string,
   StatAmount:number,
   TotCredit:number,
   TotDebit:number,
      /**  DEA Unrecognized Amount  */  
   Unrecognized:number,
   BookCurrencyCode:string,
   BookCurrencySymbol:string,
      /**  Description of the entity the journal detail is for  */  
   EntityDescription:string,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrName:string,
   CurrencyCurrencyID:string,
   CurrencyCurrSymbol:string,
   CurrencyCurrDesc:string,
   FiscalCalDescription:string,
   GLAccountGLAcctDisp:string,
   GLAccountAccountDesc:string,
   GLAccountGLAccount:string,
   JournalCodeJrnlDescription:string,
   SrcGLAccountGLShortAcct:string,
   SrcGLAccountAccountDesc:string,
   SrcGLAccountGLAcctDisp:string,
   StatUOMStatUOMDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if invoice is "open".  */  
   OpenInvoice:boolean,
      /**  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  */  
   ClosedDate:string,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   CreditMemo:boolean,
      /**  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  */  
   UnappliedCash:boolean,
      /**   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   CheckRef:string,
      /**  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  */  
   InvoiceSuffix:string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  */  
   GroupID:string,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   InvoiceType:string,
      /**  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  */  
   DeferredRevenue:boolean,
      /**  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  */  
   OrderNum:number,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   CustNum:number,
      /**  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  */  
   PONum:string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  Defaults from sales order ORderHed.FOB  */  
   FOB:string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   InvoiceDate:string,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  */  
   FiscalYear:number,
      /**  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  */  
   FiscalPeriod:number,
      /**  Once posted, maintenance is not allowed.  */  
   GLPosted:boolean,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnpostedBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   DocUnpostedBal:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DepositCredit:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DocDepositCredit:number,
      /**  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  */  
   SalesRepList:string,
      /**   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   InvoiceRef:number,
      /**  Value of this field is reference to invoice which has been cancelled by current invoice.  */  
   RefCancelled:number,
      /**  Value of this field is reference to invoice that cancelled this invoice.  */  
   RefCancelledBy:number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   StartUp:boolean,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDates:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   PayAmounts:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   DocPayAmounts:string,
      /**  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  */  
   PayDiscDate:string,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   PayDiscAmt:number,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   DocPayDiscAmt:number,
      /**  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  */  
   BillConNum:number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  */  
   InvoiceHeld:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Journal that invoice was posted to.  */  
   JournalCode:string,
      /**  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  */  
   LineType:string,
      /**   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**  The Site that the invoice is relate to.  */  
   Plant:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  External Identifier  */  
   ExternalID:string,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefInvoiceNum:string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   DepGainLoss:number,
      /**  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  */  
   DNComments:string,
      /**  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  */  
   DNCustNbr:string,
      /**   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  */  
   DebitNote:boolean,
      /**  This is populated from ShipHead.CustNum representing the Sold To customer.  */  
   SoldToCustNum:number,
      /**  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  */  
   Consolidated:boolean,
      /**  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  */  
   BillToInvoiceAddress:boolean,
      /**  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  */  
   SoldToInvoiceAddress:boolean,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm1:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm2:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm3:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm4:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm5:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate1:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate2:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate3:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate4:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate5:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales1:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales2:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales3:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales4:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales5:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit1:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit2:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit3:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit4:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit5:number,
      /**  Indicates if the Credit Memo is for a Rebate  */  
   CMType:string,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Rounding in Customer currency  */  
   DocRounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt1PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt2PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt3PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt1PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnpostedBal:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3DepGainLoss:number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Tax point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  The last date finance/late charges have been calculated for this invoice.  */  
   LastChrgCalcDate:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Total Finance Charge amount.  */  
   TotFinChrg:number,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDiscDays:string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   PayDiscPer:string,
      /**  Blocks certain invoice from generating finance/later charge.  */  
   BlockedFinChrg:boolean,
      /**  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  */  
   BlockedFinChrgReason:string,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Blocks certain invoice from being printed on reminder letters.  */  
   BlockedRemLetters:boolean,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PayDiscPartPay:boolean,
      /**  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  */  
   BlockedRemLettersReason:string,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  Currency Rate Date  */  
   CurrRateDate:string,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   PIPayment:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  */  
   UseAltBillTo:boolean,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  */  
   CorrectionInv:boolean,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden Finland Localization field - Banking Reference  */  
   SEBankRef:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Reversal Doucment Amount  */  
   ReversalDocAmount:number,
      /**  Original Due Date at posting time  */  
   OrigDueDate:string,
      /**  The reference to CashHead.HeadNum.Used in deposit invoices  */  
   HeadNum:number,
      /**  Letter of Credit ID.  */  
   ARLOCID:string,
      /**  The free text field which can contain reference (such as Contract)  */  
   ContractRef:string,
      /**  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  */  
   OurBank:string,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  If the invoice was generated in Project Billing then it is reference to the project.  */  
   PBProjectID:string,
      /**  Deposit amount is transaction amount of deposit payment  */  
   DepositAmt:number,
      /**   Taiwan Localization
Export Bill Number  */  
   GUIExportBillNumber:string,
      /**  Deposit amount is transaction amount of deposit payment in document currency  */  
   DocDepositAmt:number,
      /**   Taiwan Localization
Date of Export  */  
   GUIDateOfExport:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt1 currency  */  
   Rpt1DepositAmt:number,
      /**   Taiwan Localization
Export Type  */  
   GUIExportType:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt2 currency  */  
   Rpt2DepositAmt:number,
      /**   Taiwan Localization
Export Mark  */  
   GUIExportMark:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt23currency  */  
   Rpt3DepositAmt:number,
      /**   Taiwan Localization
Export Bill Type  */  
   GUIExportBillType:string,
      /**  Deposit unallocated amount in base currency  */  
   DepUnallocatedAmt:number,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   SummarizationDate:string,
      /**  Deposit unallocated amount in document currency  */  
   DocDepUnallocatedAmt:number,
      /**  Date when a company bills the customer  */  
   BillingDate:string,
      /**  Deposit unallocated amount in Rpt1 currency  */  
   Rpt1DepUnallocatedAmt:number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   BillingNumber:string,
      /**  Deposit unallocated amount in Rpt2 currency  */  
   Rpt2DepUnallocatedAmt:number,
      /**  Only records ready to bill will be printed in the Billing Statement  */  
   ReadyToBill:boolean,
      /**  Deposit unallocated amount in Rpt3 currency  */  
   Rpt3DepUnallocatedAmt:number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   OvrDefTaxDate:boolean,
      /**  Cross Reference Contract Number.  */  
   XRefContractNum:string,
      /**  Cross Reference Contract Date.  */  
   XRefContractDate:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Customer Agent Name  */  
   CustAgentName:string,
      /**  Customer Agent Tax Region Number  */  
   CustAgentTaxRegNo:string,
      /**  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  */  
   ExportType:string,
      /**  Export Report Number  */  
   ExportReportNo:string,
      /**  Real Estate Number  */  
   RealEstateNo:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  CycleCode  */  
   CycleCode:string,
      /**  Duration  */  
   Duration:number,
      /**  EndDate  */  
   EndDate:string,
      /**  MaxValueAmt  */  
   MaxValueAmt:number,
      /**  DocMaxValueAmt  */  
   DocMaxValueAmt:number,
      /**  Rpt1MaxValueAmt  */  
   Rpt1MaxValueAmt:number,
      /**  Rpt2MaxValueAmt  */  
   Rpt2MaxValueAmt:number,
      /**  Rpt3MaxValueAmt  */  
   Rpt3MaxValueAmt:number,
      /**  HoldInvoice  */  
   HoldInvoice:boolean,
      /**  CopyLatestInvoice  */  
   CopyLatestInvoice:boolean,
      /**  OverrideEndDate  */  
   OverrideEndDate:boolean,
      /**  CycleInactive  */  
   CycleInactive:boolean,
      /**  RecurSource  */  
   RecurSource:boolean,
      /**  InstanceNum  */  
   InstanceNum:number,
      /**  RecurBalance  */  
   RecurBalance:number,
      /**  DocRecurBalance  */  
   DocRecurBalance:number,
      /**  Rpt1RecurBalance  */  
   Rpt1RecurBalance:number,
      /**  Rpt2RecurBalance  */  
   Rpt2RecurBalance:number,
      /**  Rpt3RecurBalance  */  
   Rpt3RecurBalance:number,
      /**  LastDate  */  
   LastDate:string,
      /**  RecurringState  */  
   RecurringState:string,
      /**  IsRecurring  */  
   IsRecurring:boolean,
      /**  InvoiceNumList  */  
   InvoiceNumList:string,
      /**  IsAddedToGTI  */  
   IsAddedToGTI:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHISRCodeLine  */  
   CHISRCodeLine:string,
      /**  CMReason  */  
   CMReason:string,
      /**  THIsImmatAdjustment  */  
   THIsImmatAdjustment:boolean,
      /**  AGAuthorizationCode  */  
   AGAuthorizationCode:string,
      /**  AGAuthorizationDate  */  
   AGAuthorizationDate:string,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  AGDocumentLetter  */  
   AGDocumentLetter:string,
      /**  AGInvoicingPoint  */  
   AGInvoicingPoint:string,
      /**  AGLegalNumber  */  
   AGLegalNumber:string,
      /**  AGPrintingControlType  */  
   AGPrintingControlType:string,
      /**  RevisionDate  */  
   RevisionDate:string,
      /**  RevisionNum  */  
   RevisionNum:number,
      /**  TWDeclareYear  */  
   TWDeclareYear:number,
      /**  TWDeclarePeriod  */  
   TWDeclarePeriod:number,
      /**  TWGenerationType  */  
   TWGenerationType:string,
      /**  TWGUIGroup  */  
   TWGUIGroup:string,
      /**  TWPeriodPrefix  */  
   TWPeriodPrefix:string,
      /**  Indicates if the Invoice is in Collections status  */  
   InvInCollections:boolean,
      /**   Indicates if the Customer of the Invoice is in Collections
(Peru Localization)  */  
   CollectionsCust:boolean,
      /**  A counter of the number of times an AR Invoice has been transmitted via EDI.  The counter is automatically incremented each time the EDIReady flag changes from False to True.  */  
   CounterARForm:number,
      /**  flag indicates if Revenue of the invoice has been already posted  */  
   PostedRecog:boolean,
      /**  Confirmation Date  */  
   CNConfirmDate:string,
      /**  MXSATSeal  */  
   MXSATSeal:string,
      /**  MXSerie  */  
   MXSerie:string,
      /**  MXTaxRcptType  */  
   MXTaxRcptType:string,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  MXTotalPayments  */  
   MXTotalPayments:number,
      /**  MXFolio  */  
   MXFolio:string,
      /**  MXCertifiedTimestamp  */  
   MXCertifiedTimestamp:string,
      /**  MXSATCertificateSN  */  
   MXSATCertificateSN:string,
      /**  MXDigitalSeal  */  
   MXDigitalSeal:string,
      /**  MXPostedTimeStamp  */  
   MXPostedTimeStamp:string,
      /**  MXCertificate  */  
   MXCertificate:string,
      /**  MXApprovalYear  */  
   MXApprovalYear:number,
      /**  MXCBB  */  
   MXCBB:string,
      /**  MXApprovalNum  */  
   MXApprovalNum:number,
      /**  MXOriginalStringTFD  */  
   MXOriginalStringTFD:string,
      /**  MXPaymentNum  */  
   MXPaymentNum:number,
      /**  MXPaidAs  */  
   MXPaidAs:string,
      /**  MXCertificateSN  */  
   MXCertificateSN:string,
      /**  MXOriginalAmount  */  
   MXOriginalAmount:number,
      /**  MXAccountNumber  */  
   MXAccountNumber:string,
      /**  MXOriginalDate  */  
   MXOriginalDate:string,
      /**  MXOriginalSeries  */  
   MXOriginalSeries:string,
      /**  MXOriginalFolio  */  
   MXOriginalFolio:string,
      /**  MXTaxRegime  */  
   MXTaxRegime:string,
      /**  MXOriginalString  */  
   MXOriginalString:string,
      /**  MXPaymentName  */  
   MXPaymentName:string,
      /**  EInvoice  */  
   EInvoice:boolean,
      /**  EInvStatus  */  
   EInvStatus:number,
      /**  EInvTimestamp  */  
   EInvTimestamp:string,
      /**  EInvUpdatedBy  */  
   EInvUpdatedBy:string,
      /**  EInvException  */  
   EInvException:string,
      /**  Flagged that this invoice has taxes which were necessary or is necessary now.  */  
   WithTaxConfirm:boolean,
      /**  UseAltBillToID  */  
   UseAltBillToID:boolean,
      /**  MXCancelledDate  */  
   MXCancelledDate:string,
      /**  Overpaid  */  
   Overpaid:boolean,
      /**  OrdExchangeRate  */  
   OrdExchangeRate:number,
      /**  PEAPPayNum  */  
   PEAPPayNum:number,
      /**  PEBankNumber  */  
   PEBankNumber:string,
      /**  PECharges  */  
   PECharges:number,
      /**  PECommissions  */  
   PECommissions:number,
      /**  PEDetTaxAmt  */  
   PEDetTaxAmt:number,
      /**  PEDetTaxCurrencyCode  */  
   PEDetTaxCurrencyCode:string,
      /**  PEDischargeAmt  */  
   PEDischargeAmt:number,
      /**  PEDischargeDate  */  
   PEDischargeDate:string,
      /**  PEInterest  */  
   PEInterest:number,
      /**  PENoPayPenalty  */  
   PENoPayPenalty:number,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   PESUNATDepAmt:number,
      /**  CSF Peru - SUNAT Deposit Date  */  
   PESUNATDepDate:string,
      /**  CSF Peru -  SUNAT Deposit Number  */  
   PESUNATDepNum:string,
      /**  PEBOEPosted  */  
   PEBOEPosted:boolean,
      /**  DocPEInterest  */  
   DocPEInterest:number,
      /**  DocPECommissions  */  
   DocPECommissions:number,
      /**  DocPECharges  */  
   DocPECharges:number,
      /**  DocPENoPayPenalty  */  
   DocPENoPayPenalty:number,
      /**  DocPEDischargeAmt  */  
   DocPEDischargeAmt:number,
      /**  DocPEDetTaxAmt  */  
   DocPEDetTaxAmt:number,
      /**  Rpt1PEInterest  */  
   Rpt1PEInterest:number,
      /**  Rpt1PECommissions  */  
   Rpt1PECommissions:number,
      /**  Rpt1PECharges  */  
   Rpt1PECharges:number,
      /**  Rpt1PENoPayPenalty  */  
   Rpt1PENoPayPenalty:number,
      /**  Rpt1PEDischargeAmt  */  
   Rpt1PEDischargeAmt:number,
      /**  Rpt2PEInterest  */  
   Rpt2PEInterest:number,
      /**  Rpt2PECommissions  */  
   Rpt2PECommissions:number,
      /**  Rpt2PECharges  */  
   Rpt2PECharges:number,
      /**  Rpt2PENoPayPenalty  */  
   Rpt2PENoPayPenalty:number,
      /**  Rpt2PEDischargeAmt  */  
   Rpt2PEDischargeAmt:number,
      /**  Rpt3PEInterest  */  
   Rpt3PEInterest:number,
      /**  Rpt3PECommissions  */  
   Rpt3PECommissions:number,
      /**  Rpt3PECharges  */  
   Rpt3PECharges:number,
      /**  Rpt3PENoPayPenalty  */  
   Rpt3PENoPayPenalty:number,
      /**  Rpt3PEDischargeAmt  */  
   Rpt3PEDischargeAmt:number,
      /**  Our Supplier Code  */  
   OurSupplierCode:string,
      /**  PEGuaranteeName  */  
   PEGuaranteeName:string,
      /**  PEGuaranteeAddress1  */  
   PEGuaranteeAddress1:string,
      /**  PEGuaranteeAddress2  */  
   PEGuaranteeAddress2:string,
      /**  PEGuaranteeAddress3  */  
   PEGuaranteeAddress3:string,
      /**  PEGuaranteeCity  */  
   PEGuaranteeCity:string,
      /**  PEGuaranteeState  */  
   PEGuaranteeState:string,
      /**  PEGuaranteeZip  */  
   PEGuaranteeZip:string,
      /**  PEGuaranteeCountry  */  
   PEGuaranteeCountry:string,
      /**  PEGuaranteeTaxID  */  
   PEGuaranteeTaxID:string,
      /**  PEGuaranteePhoneNum  */  
   PEGuaranteePhoneNum:string,
      /**  PEBOEStatus  */  
   PEBOEStatus:string,
      /**  PEBOEIsMultiGen  */  
   PEBOEIsMultiGen:boolean,
      /**  PE Reference Document ID  */  
   PERefDocID:string,
      /**  PE Reason Code  */  
   PEReasonCode:string,
      /**  PE Reason Description  */  
   PEReasonDesc:string,
      /**  TW GUI Code Seller  */  
   TWGUIRegNumSeller:string,
      /**  TW GUI Code Buyer  */  
   TWGUIRegNumBuyer:string,
      /**  Document Name  */  
   TWGUIExportDocumentName:string,
      /**  Remarks  */  
   TWGUIExportRemarks:string,
      /**  Verification  */  
   TWGUIExportVerification:string,
      /**  PEDebitNoteReasonCode  */  
   PEDebitNoteReasonCode:string,
      /**  PEDebitNote  */  
   PEDebitNote:boolean,
      /**  MXPartPmt  */  
   MXPartPmt:boolean,
      /**  Tax Invoice Type  */  
   CNTaxInvoiceType:number,
      /**  MXExportOperationType  */  
   MXExportOperationType:string,
      /**  MXExportCustDocCode  */  
   MXExportCustDocCode:string,
      /**  MXExportCertOriginNum  */  
   MXExportCertOriginNum:string,
      /**  MXExportConfNum  */  
   MXExportConfNum:string,
      /**  MXExportCertOrigin  */  
   MXExportCertOrigin:boolean,
      /**  MXIncoterm  */  
   MXIncoterm:string,
      /**  AGDocConcept  */  
   AGDocConcept:number,
      /**  Electronic Invoice reference number  */  
   EInvRefNum:string,
      /**  Export document reference number  */  
   ExportDocRefNum:string,
      /**  Export document date  */  
   ExportDocDate:string,
      /**  Tax Transaction ID  */  
   INTaxTransactionID:string,
      /**  MXMovingReasonFlag  */  
   MXMovingReasonFlag:boolean,
      /**  MXMovingReason  */  
   MXMovingReason:string,
      /**  MXNumRegIdTrib  */  
   MXNumRegIdTrib:string,
      /**  MXResidenCountryNum  */  
   MXResidenCountryNum:number,
      /**  MXPurchaseType  */  
   MXPurchaseType:string,
      /**  MXConfirmationCode  */  
   MXConfirmationCode:string,
      /**  MXExternalCode  */  
   MXExternalCode:string,
      /**  This invoice was created via an integration with a third-party field service.  */  
   ServiceInvoice:boolean,
      /**  MXDomesticTransfer  */  
   MXDomesticTransfer:boolean,
      /**  MXCancellationMode  */  
   MXCancellationMode:string,
      /**  Shipping Port Code  */  
   INShippingPortCode:string,
      /**  Export Procedure  */  
   INExportProcedure:string,
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
      /**  DepositBalance  */  
   DepositBalance:number,
      /**  DocDepositBalance  */  
   DocDepositBalance:number,
      /**  Rpt1DepositBalance  */  
   Rpt1DepositBalance:number,
      /**  Rpt2DepositBalance  */  
   Rpt2DepositBalance:number,
      /**  Rpt3DepositBalance  */  
   Rpt3DepositBalance:number,
      /**  Quote number to which this invoice record is associated with.  */  
   QuoteNum:number,
      /**  The help desk case related to this invoice.  */  
   HDCaseNum:number,
      /**  Indicates that the credit hold was overridden for this invoice.  */  
   CreditOverride:boolean,
      /**  Description	Indicates that the credit hold was overridden for this invoice.	The date and time the user override the invoice credit hold.  */  
   CreditOverrideDate:string,
      /**  The user id that override the invoice credit hold.  */  
   CreditOverrideUserID:string,
      /**  Indicates the invoice is on credit hold.  Applicable to miscellaneous invoices only.  */  
   CreditHold:boolean,
      /**  Peru Electronic Invoice XML Type  */  
   PEXMLType:number,
      /**  COCreditMemoReasonCode  */  
   COCreditMemoReasonCode:string,
      /**  CODebitMemoReasonCode  */  
   CODebitMemoReasonCode:string,
      /**  COReasonDesc  */  
   COReasonDesc:string,
      /**  CODebitNote  */  
   CODebitNote:boolean,
      /**  PEDetractionTranNum  */  
   PEDetractionTranNum:number,
      /**  PEProductCode  */  
   PEProductCode:string,
      /**  PECollectionGroupID  */  
   PECollectionGroupID:string,
      /**  PE Caption Code  */  
   PECaptionCode:string,
      /**  PE Caption Code Description  */  
   PECaption:string,
      /**  PE Reference DocumentType 1  */  
   PERefDocumentType:string,
      /**  PE Reference Document Number 1  */  
   PERefDocumentNumber:string,
      /**  PE Detraction good or service code  */  
   PEDetrGoodServiceCode:string,
      /**  PE Reference DocumentType 2  */  
   PERefDocumentType2:string,
      /**  PE Reference DocumentType 3  */  
   PERefDocumentType3:string,
      /**  PE Reference DocumentType 4  */  
   PERefDocumentType4:string,
      /**  PE Reference DocumentType 5  */  
   PERefDocumentType5:string,
      /**  PE Reference Document Number 2  */  
   PERefDocumentNumber2:string,
      /**  PE Reference Document Number 3  */  
   PERefDocumentNumber3:string,
      /**  PE Reference Document Number 4  */  
   PERefDocumentNumber4:string,
      /**  PE Reference Document Number 5  */  
   PERefDocumentNumber5:string,
      /**  E-invoice  */  
   ELIEInvoice:boolean,
      /**  Status of E-invoice (1 - Open, 2 - Generated, 3 - Sent, 4 - Error).  */  
   ELIEInvStatus:number,
      /**  User Id of the person generated E-invoice.  */  
   ELIEInvUpdatedBy:string,
      /**  E-invoice error description.  */  
   ELIEInvException:string,
      /**  Date and Time of E-invoice generation.  */  
   ELIEInvUpdatedOn:string,
      /**  COOperType  */  
   COOperType:string,
      /**  Flag that indicates if the Invoice is for Central Collection.  */  
   CentralCollection:boolean,
      /**  Company that created this invoice.  */  
   CColChildCompany:string,
      /**  Central Collection company.  */  
   CColParentCompany:string,
      /**  Order number on the invoicing company.  */  
   CColOrderNum:number,
      /**  Invoice number on the invoicing company.  */  
   CColChildInvoiceNum:number,
      /**  Invoice number on central collection company  */  
   CColInvoiceNum:number,
      /**  Legal number on the invoicing company invoice.  */  
   CColChildLegalNumber:string,
      /**  Legal number on central collection company.  */  
   CColLegalNumber:string,
      /**  Invoice reference on the Invoicing Company.  */  
   CColInvoiceRef:number,
      /**  Invoice Balance in the Central Collection company.  */  
   CColInvBal:number,
      /**  Central Collection Doc Invoice Balance.  */  
   DocCColInvBal:number,
      /**  Invoice Amount on the Invoicing Company.  */  
   CColInvAmt:number,
      /**  Invoice Amount on the Invoicing Company.  */  
   DocCColInvAmt:number,
      /**  Rpt 1 Parent Invoice Balance  */  
   Rpt1CColInvBal:number,
      /**  Rpt 2 Parent Invoice Balance  */  
   Rpt2CColInvBal:number,
      /**  Rpt 3 Parent Invoice Balance  */  
   Rpt3CColInvBal:number,
      /**  Rpt 1 Child Invoice Amount  */  
   Rpt1CColInvAmt:number,
      /**  Rpt 2 Child Invoice Amount  */  
   Rpt2CColInvAmt:number,
      /**  Rpt 3 Child Invoice Amount  */  
   Rpt3CColInvAmt:number,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  User terminal name  */  
   ELIEInvTerminalName:string,
      /**  User terminal IP  */  
   ELIEInvTerminalIP:string,
      /**  GL Description  */  
   Description:string,
      /**  WithholdAcctToInterim  */  
   WithholdAcctToInterim:boolean,
      /**  Indicates if the Central Collection parent invoice is open.  */  
   CColOpenInvoice:boolean,
      /**  AGQRCodeData  */  
   AGQRCodeData:string,
      /**  Exempt Reason Code  */  
   ExemptReasonCode:string,
      /**  EInvoice ID  */  
   ELIEInvID:string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   CallNum:number,
      /**  this is a link to the service call line that this invoice is for.  Linetype = "CALL"  */  
   CallLine:number,
      /**  Associates the Call Line record back its linked jobnum  */  
   JobNum:string,
      /**  MXCancelReasonCode  */  
   MXCancelReasonCode:string,
      /**  MXSubstInvoiceNum  */  
   MXSubstInvoiceNum:number,
      /**  MXExportType  */  
   MXExportType:string,
      /**  MXGlobalInvoicePeriod  */  
   MXGlobalInvoicePeriod:string,
      /**  MXGlobalInvoiceMonth  */  
   MXGlobalInvoiceMonth:string,
      /**  ELIEInvServiceProviderStatus  */  
   ELIEInvServiceProviderStatus:number,
      /**  Incoterm Code  */  
   IncotermCode:string,
      /**  Incoterm Location  */  
   IncotermLocation:string,
      /**  CovenantDiscPercent  */  
   CovenantDiscPercent:number,
      /**  TotalCovenantDiscount  */  
   TotalCovenantDiscount:number,
      /**  DocCovenantDiscount  */  
   DocCovenantDiscount:number,
      /**  Rpt1CovenantDiscount  */  
   Rpt1CovenantDiscount:number,
      /**  Rpt2CovenantDiscount  */  
   Rpt2CovenantDiscount:number,
      /**  Rpt3CovenantDiscount  */  
   Rpt3CovenantDiscount:number,
      /**  TotalInCovenantDiscount  */  
   TotalInCovenantDiscount:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Total advanced billing amount.  */  
   ABAmt:number,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
      /**  ARPNHead's HeadNum  */  
   ARPNHeadNum:number,
      /**  when InvcHead.PIPayment = O then populate ARPaymentInstrumentID with a value of PI.  */  
   ARPromNoteID:string,
      /**  Auto generate payment instruments  */  
   AutoGenPN:boolean,
      /**  Delimited list of available bill to customers.  */  
   AvailBTCustList:string,
      /**  Used for Bill of Exchange.  Indicates the bank to use when a payment instrument for the invoice is created.  */  
   BankForPI:string,
   BankForPIName:string,
      /**  Customer ID for the bill to customer (InvcHead.CustNum).  */  
   BTCustID:string,
      /**  Bill to customer name.  */  
   BTCustomerName:string,
      /**  The date and time that the record was last changed  */  
   ChangeDateTime:string,
   CNGTIAction:string,
   CNGTIAddress:string,
   CNGTIBankAccount:string,
   CNGTIComment:string,
   CNGTICustomerName:string,
   CNGTIExportAddress:string,
      /**  CSF China, Gross Invoice Amount  */  
   CNGTIGrossInvcAmt:number,
      /**  CSF China, Total invoice amount = InvcHead.InvoiceAmt - InvcHead.WithholdAmt  */  
   CNGTIInvoiceAmt:number,
   CNGTINote:string,
   CNGTIShipToNum:string,
   CNGTIStatus1:string,
   CNGTIStatus2:boolean,
   CNGTITaxCode:string,
      /**  IFRS Calculation. If the checkbox is not checked then all the elements below are disabled. If the checkbox is checked, then some elements below become enabled showing default values so that the NPV can be calculated  */  
   COIFRSCalculation:boolean,
      /**  If true then Colombia IFRS Net Present Value calculation is enabled  */  
   COIFRSEnabled:boolean,
      /**  Financial Charge  */  
   COIFRSFinancialCharge:number,
   COIFRSInterestRate:number,
      /**  Number of Periods for payment  */  
   COIFRSNumberOfPeriods:number,
      /**  Present Value  */  
   COIFRSPresentValue:number,
      /**  Indicates if Invoice is in Collections (Peru localization)  */  
   CollectionsInv:boolean,
      /**  Contact email address.  */  
   ContactEmailAddr:string,
      /**  Contact fax number  */  
   ContactFaxNum:string,
      /**  Contact name  */  
   ContactName:string,
      /**  Contact phone number  */  
   ContactPhoneNum:string,
      /**  record converted from deposit  */  
   ConvertedFromDep:boolean,
   COOperTypeDesc:string,
      /**  True if the Country set for the current company contains an Intrastat code.  */  
   CountryIntrastat:boolean,
   CumulativeBalance:number,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   CurrencySwitch:boolean,
   CurrentInstanceNum:number,
   CustAllowOTS:boolean,
   CustOnCreditHold:boolean,
      /**  Deposit balance from CashHed  */  
   DepBal:number,
      /**  Deposit credit enabled flag.  */  
   DepositCreditEnabled:boolean,
   DirectDebiting:boolean,
      /**  The flag to indicate if Invoice Header Apply Date is supposed to be Read Only  */  
   DisableAplDate:boolean,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   DispBalDN:number,
      /**  Bill to address in list format.  */  
   DisplayBillAddr:string,
      /**  Display field for the masked credit card number  */  
   DisplayCreditCardNum:string,
   DisplayCurrencyID:string,
      /**  Currency display symbol  */  
   DisplaySymbol:string,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   DNPmtAmt:number,
      /**  Document Total advanced billing amount.  */  
   DocABAmt:number,
      /**  Financial Charge  */  
   DocCOIFRSFinancialCharge:number,
      /**  Present Value  */  
   DocCOIFRSPresentValue:number,
   DocCumulativeBalance:number,
      /**  Document deposit amount from cashhead.  */  
   DocDepBal:number,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   DocDispBalDN:number,
      /**  Document display symbol  */  
   DocDisplaySymbol:string,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   DocDNPmtAmt:number,
   DocDspPrepDeposit:number,
   DocDspTaxAmt:number,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   DocPESUNATDepAmt:number,
   DocRemainTaxAmt:number,
   DocReverseTaxAmt:number,
   DocSATaxAmt:number,
   DocSourceRecurBalance:number,
      /**  Document sub total  */  
   DocSubTotal:number,
      /**  Document Total tax amount from InvcTax for Collection type 'Invoice'  */  
   DocTaxAmt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in document currency.  */  
   DocVr:number,
   DocWHTaxAmt:number,
      /**  Display advance billing amount  */  
   DspABAmt:number,
      /**  Display deposit balance.  */  
   DspDepBal:number,
      /**  Display deposit credit.  */  
   DspDepCr:number,
   DspDigitalSignature:string,
      /**  Display document advance billing amount  */  
   DspDocABAmt:number,
      /**  Display document deposit balance  */  
   DspDocDepBal:number,
      /**  Display document deposit credit.  */  
   DspDocDepCr:number,
      /**  Display document invoice amount  */  
   DspDocInvoiceAmt:number,
      /**  Display document invoice balance  */  
   DspDocInvoiceBal:number,
      /**  Display Invoice Doc Rounding  */  
   DspDocRounding:number,
      /**  display document sub total  */  
   DspDocSubTotal:number,
      /**  Display invoice amount  */  
   DspInvoiceAmt:number,
      /**  Display Invoice Balance.  */  
   DspInvoiceBal:number,
      /**  Display invoice reference  */  
   DspInvoiceRef:number,
   DspPayDiscDays:string,
   DspPrepDeposit:number,
      /**  Display Rounding in Base  */  
   DspRounding:number,
      /**  If SoldTo and Alt-Bill to are the same, this displays as null.  */  
   dspSoldToCustID:string,
      /**  Display sub total  */  
   DspSubTotal:number,
   DspTaxAmt:number,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
   EnableCentralCollection:boolean,
      /**  Flag to determine if UseSOCCDefaults should be enabled.  */  
   EnableSOCCDefaults:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  It will be displayed to identify invoices automatically generated due ERS shipments.  */  
   ERSInvoice:boolean,
      /**  Indicates which date to be used to calculate the exchange rate, I for Invoice Date, A for Apply Date.  */  
   ExchangeRateDate:string,
      /**  Flag for update of InvcHead to allow when group id is "RMACRREQ"  */  
   GenedFromRMA:boolean,
      /**  CustBank record exists for customer  */  
   HasBank:boolean,
      /**  Indicates if a legal number configuration exists for ar invoices/credit memos  */  
   HasLegNumCnfg:boolean,
      /**  In case if Invoice Header Tax Liability is not assigned this flag indicates if any of Invoice lines has Tax inclusive Tax Liability assinged  */  
   InPriceLn:boolean,
      /**  Integration invoice type.  Used for setting of InvoiceType.  */  
   IntInvoiceType:string,
      /**  InvoiceType description  */  
   InvoiceTypeDesc:string,
      /**  Denmark localization external field  */  
   IsDK:boolean,
      /**  Set to true if intrastat is enabled.  */  
   IsIntrastatSensitive:boolean,
   IsLatestRecurrence:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Indicates if the UR Invoice was created from an On Account PI instead of an on account cash receipt.  */  
   IsPIUnappliedReceipt:boolean,
   IsPMForGenPIType:boolean,
   LatestInvoice:number,
      /**  Stores the message when a legal number is generated.  */  
   LegalNumberMessage:string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  MXCancellationID  */  
   MXCancellationID:string,
      /**  MXCancellationStatus  */  
   MXCancellationStatus:string,
      /**  It indicates that this Invoice has taxes, for which the confirmation is required.  */  
   NeedConfirmTaxes:boolean,
      /**  This field is to display in Cash Receipt Entry the Discount Date that the payment will take.  */  
   NextDiscDate:string,
      /**  NextInvoiceDate = InvcRecurringCycle.LastDate + RecurringCycle.Interval in RecurringCycle.Modifier units  */  
   NextInvoiceDate:string,
      /**  Pack slip number from the 1st line item.  */  
   PackSlipNum:number,
      /**  Pay schedule enabled flag  */  
   PaySchedEnabled:boolean,
      /**  Indicates what the user will change the status to  */  
   PEBOEChangeStatusTo:string,
   PEBOEStatusDesc:string,
      /**  Peru CSF: Collections date  */  
   PECollectionsDate:string,
      /**  PE Detraction good or service code description  */  
   PEDetrGoodServiceCodeDesc:string,
   PEDspCurrencySymbol:string,
      /**  Peru CSF: No if the invoice is moved out of collections, Yes if the invoice is moved into colletions.  */  
   PEInCollections:boolean,
      /**  PE Document Type Description  */  
   PERefDocumentTypeDesc:string,
      /**  PE Document Type Description 2  */  
   PERefDocumentTypeDesc2:string,
      /**  PE Document Type Description 3  */  
   PERefDocumentTypeDesc3:string,
      /**  PE Document Type Description 4  */  
   PERefDocumentTypeDesc4:string,
      /**  PE Document Type Description 5  */  
   PERefDocumentTypeDesc5:string,
      /**  PI - Bank account  */  
   PIBankAcctID:string,
      /**  PI Customer bank required  */  
   PICustBankDtl:boolean,
      /**  PI Initiation - generated or received  */  
   PIInitiation:string,
      /**  Prep Deposit enabled flag.  */  
   PrepDepositEnabled:boolean,
      /**  The description of the proposed Tax Region  */  
   ProposedTaxRgn:string,
      /**   This field indicates id all the amounts related to the invoice are supposed to be re-calculated on change of the Applate Date.
"R" - the user's answer is recalculate the amounts
"N" the user's answer is  do not recalculate the amount
Blank - user is not asked  */  
   RecalcAmts:string,
      /**  Recurring flag  */  
   Recurring:boolean,
   RemainTaxAmt:number,
   ReminderSeq:number,
      /**  Accumulate all reversal amounts of Credit Memos with the reference to the invoice  */  
   ReversalDocAmt:number,
   ReverseTaxAmt:number,
   Rpt1ABAmt:number,
      /**  Financial Charge  */  
   Rpt1COIFRSFinancialCharge:number,
      /**  Present Value  */  
   Rpt1COIFRSPresentValue:number,
   Rpt1CumulativeBalance:number,
   Rpt1DepBal:number,
   Rpt1DspABAmt:number,
   Rpt1DspDepBal:number,
   Rpt1DspDepCr:number,
   Rpt1DspInvoiceAmt:number,
   Rpt1DspInvoiceBal:number,
   Rpt1DspPrepDeposit:number,
   Rpt1DspRounding:number,
   Rpt1DspSubTotal:number,
   Rpt1DspTaxAmt:number,
   Rpt1RemainTaxAmt:number,
   Rpt1ReverseTaxAmt:number,
   Rpt1SATaxAmt:number,
   Rpt1SourceRecurBalance:number,
   Rpt1SubTotal:number,
   Rpt1TaxAmt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt1 currency.  */  
   Rpt1Vr:number,
   Rpt1WHTaxAmt:number,
   Rpt2ABAmt:number,
      /**  Financial Charge  */  
   Rpt2COIFRSFinancialCharge:number,
      /**  Present Value  */  
   Rpt2COIFRSPresentValue:number,
   Rpt2CumulativeBalance:number,
   Rpt2DepBal:number,
   Rpt2DspABAmt:number,
   Rpt2DspDepBal:number,
   Rpt2DspDepCr:number,
   Rpt2DspInvoiceAmt:number,
   Rpt2DspInvoiceBal:number,
   Rpt2DspPrepDeposit:number,
   Rpt2DspRounding:number,
   Rpt2DspSubTotal:number,
   Rpt2DspTaxAmt:number,
   Rpt2RemainTaxAmt:number,
   Rpt2ReverseTaxAmt:number,
   Rpt2SATaxAmt:number,
   Rpt2SourceRecurBalance:number,
   Rpt2SubTotal:number,
   Rpt2Taxamt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt2 currency.  */  
   Rpt2Vr:number,
   Rpt2WHTaxAmt:number,
   Rpt3ABAmt:number,
      /**  Financial Charge  */  
   Rpt3COIFRSFinancialCharge:number,
      /**  Present Value  */  
   Rpt3COIFRSPresentValue:number,
   Rpt3CumulativeBalance:number,
   Rpt3DepBal:number,
   Rpt3DspABAmt:number,
   Rpt3DspDepBal:number,
   Rpt3DspDepCr:number,
   Rpt3DspInvoiceAmt:number,
   Rpt3DspInvoiceBal:number,
   Rpt3DspPrepDeposit:number,
   Rpt3DspRounding:number,
   Rpt3DspSubTotal:number,
   Rpt3DspTaxAmt:number,
   Rpt3RemainTaxAmt:number,
   Rpt3ReverseTaxAmt:number,
   Rpt3SATaxAmt:number,
   Rpt3SourceRecurBalance:number,
   Rpt3SubTotal:number,
   Rpt3TaxAmt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt3 currency.  */  
   Rpt3Vr:number,
   Rpt3WHTaxAmt:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  1st entry in SalesRepList  */  
   SalesRepCode1:string,
      /**  2nd entry in SalesRepList  */  
   SalesRepCode2:string,
      /**  3rd entry in SalesRepList.  */  
   SalesRepCode3:string,
      /**  4th entry in SalesRepList  */  
   SalesRepCode4:string,
      /**  5th entry in SalesRepList  */  
   SalesRepCode5:string,
      /**  1st sales rep name  */  
   SalesRepName1:string,
      /**  2nd sales rep name  */  
   SalesRepName2:string,
      /**  3rd sales rep name  */  
   SalesRepName3:string,
      /**  4th sales rep name  */  
   SalesRepName4:string,
      /**  5th sales rep name  */  
   SalesRepName5:string,
   SATaxAmt:number,
      /**  Boolean for selection of invoices in grid  */  
   Selected:boolean,
   SkipRecurring:boolean,
      /**  Sold to address list.  */  
   SoldToAddressList:string,
      /**  Sold to customer id  */  
   SoldToCustID:string,
      /**  Sold to customer name.  */  
   SoldToCustomerName:string,
   SourceInvoiceNum:number,
   SourceLastDate:string,
   SourceRecurBalance:number,
      /**  Sub total for invoice  */  
   SubTotal:number,
      /**  The system transaction type - ARInvoice or CreditMemo.  Used to filter combo list for TranDocTypeID.  */  
   SystemTranType:string,
      /**  Total tax amount from InvcTax  */  
   TaxAmt:number,
   TaxExchangeRate:number,
      /**  The flag to indicate if the user is supposed to be asked about Tax Liability change  */  
   TaxRgnLineChange:boolean,
   TotalInstanceNum:number,
      /**  This field is used when invoice is transferred to another Invoice Group and the user has a chance to change the Apply date of the invoice transferred.  */  
   TransApplyDate:string,
      /**  If true, the credit card info will come from the sales order.  */  
   UseSOCCDefaults:boolean,
   UseTaxRate:boolean,
   VNInvDescription:string,
   VNInvoiceType:string,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in base currency.  */  
   Vr:number,
   WHTaxAmt:number,
      /**  Currency label  */  
   XRateLabel:string,
   zEnableCreditHold:boolean,
      /**  The number of days the invoice is past due.  */  
   AgingDays:number,
      /**   The list of prohibited statuses.for the Invoice
For examle, if contains 2 (EINVOICE_STATUS_GENERATED) then Generate E-invoice is not allowed.
if contains 2 (EINVOICE_STATUS_SENT) then Sending Invoice via Service provider is not allowed  */  
   ELIEInvProhibitedStatuses:string,
      /**  Flag indicating whether to enable Incoterm Location  */  
   EnableIncotermLocation:boolean,
   BitFlag:number,
   AGInvoicingPointDescription:string,
   ARSystLNReqForInvc:boolean,
   CardTypeDescription:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrRateGrpDescription:string,
   CustomerInactive:boolean,
   CustomerMXGeneralPublic:boolean,
   CustomerCustID:string,
   CustomerBTName:string,
   CustomerName:string,
   CustomerELISendingOption:number,
   FOBDescription:string,
   IncotermsDescription:string,
   JournalCodeJrnlDescription:string,
   MXPurchaseTypeCodeDesc:string,
   MXSubstInvoiceMXFiscalFolio:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   OurBankPayerRef:string,
   OurBankBankIdentifier:string,
   OurBankTypeCode:string,
   OurBankBankAcctID:string,
   OurBankCheckingAccount:string,
   OurBankBankName:string,
   OurBankIBANCode:string,
   OurBankLocalBIC:string,
   OurBankDescription:string,
   PayMethodName:string,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodType:number,
   PlantName:string,
   ProjectDescription:string,
   RecurringCycleMaximumValue:boolean,
   SoldToCustNumInactive:boolean,
   SoldToCustNumCustID:string,
   SoldToCustNumName:string,
   TaxRateGrpDescription:string,
   TaxRegionDescription:string,
   TermsCodeDescription:string,
   TranDocTypeDescription:string,
   XbSystOCRCalcType:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcsForCustTableset{
   InvcHead:Erp_Tablesets_InvcHeadRow[],
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

export interface Erp_Tablesets_PITotalsRow{
   CashRcv:number,
   DocCashRcv:number,
   DocDscTaken:number,
   DocGainReal:number,
   DocGainUnreal:number,
   DscTaken:number,
   GainReal:number,
   GainUnreal:number,
   RevalDate:string,
   Rpt1CashRcv:number,
   Rpt1DscTaken:number,
   Rpt1GainReal:number,
   Rpt1GainUnreal:number,
   Rpt2CashRcv:number,
   Rpt2DscTaken:number,
   Rpt2GainReal:number,
   Rpt2GainUnreal:number,
   Rpt3CashRcv:number,
   Rpt3DscTaken:number,
   Rpt3GainReal:number,
   Rpt3GainUnreal:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PNSummaryRow{
      /**  Company  */  
   Company:string,
      /**  Payment Instrument ID  */  
   PromNoteID:string,
      /**  Type  */  
   Type:string,
      /**  Status  */  
   PIStatus:string,
      /**  Stage  */  
   PIStage:string,
      /**  Currency Code  */  
   CurrencyCode:string,
   LegalNumber:string,
   IssueDate:string,
   DueDate:string,
   DiscountAmt:number,
   DocDiscountAmount:number,
   Rpt1DiscountAmt:number,
   Rpt2DiscountAmt:number,
   Rpt3DiscountAmt:number,
   TranAmt:number,
   DocTranAmt:number,
   Rpt1TranAmt:number,
   Rpt2TranAmt:number,
   Rpt3TranAmt:number,
   Posted:boolean,
   DNAmount:number,
   DocDNAmount:number,
   Rpt1DNAmount:number,
   Rpt2DNAmount:number,
   Rpt3DNAmount:number,
   TranDate:string,
   CustNum:number,
      /**  InvoiceNum  */  
   InvoiceNum:number,
   GainLossType:string,
   RevalueDate:string,
   RevalueBal:number,
   DocRevalueBal:number,
   Rpt1RevalueBal:number,
   Rpt2RevalueBal:number,
   Rpt3RevalueBal:number,
   TranType:string,
   Reference:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PNSummaryTableset{
   PNSummary:Erp_Tablesets_PNSummaryRow[],
   PITotals:Erp_Tablesets_PITotalsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TaxDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Indicates the module that created this tax detail.  This is assigned by the system.
Values can be; AR, AP.  */  
   SourceModule:string,
      /**  HeadNum  */  
   HeadNum:number,
      /**  Integer assigned by the system copied from APTran.  */  
   APTranNo:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Taxable amount for this invoice. Manually entered if the currency is the base currency.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount. Manually entered if the currency is the base currency.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency. Manually entered.  */  
   DocTaxAmt:number,
      /**  Reverse Charge.  */  
   ReverseCharge:boolean,
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
      /**  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  */  
   InvoiceNum:number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   InvoiceRef:number,
      /**   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  */  
   ECAcquisitionSeq:number,
      /**  Relates record to a BankAcct.  */  
   BankAcctID:string,
      /**  Unique ID of the Transaction.  */  
   TranNum:number,
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
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
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
      /**  Discount Tax Adjustment  */  
   DiscTaxAdj:number,
      /**  Discount Tax Adjustment in foreign currency.  */  
   DocDiscTaxAdj:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscTaxAdj:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscTaxAdj:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscTaxAdj:number,
      /**  Discount Taxable Adjustment  */  
   DiscTaxableAdj:number,
      /**  Discount Taxable Adjustment in foreign currency.  */  
   DocDiscTaxableAdj:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscTaxableAdj:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscTaxableAdj:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscTaxableAdj:number,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Indicates if transaction was voided.  The rest of the unique key will contain the original transaction values (like APTran)  */  
   Voided:boolean,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   Rpt1TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   Rpt2TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   Rpt3TaxAmtVar:number,
      /**  Discount Tax Adjustment Variance  */  
   DiscTaxAdjVar:number,
      /**  Discount Tax Adjustment Variance  */  
   DocDiscTaxAdjVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscTaxAdjVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscTaxAdjVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscTaxAdjVar:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGOrigTaxableAmt  */  
   AGOrigTaxableAmt:number,
      /**  GainLoss  */  
   GainLoss:number,
      /**  DocGainLoss  */  
   DocGainLoss:number,
      /**  Rpt1GainLoss  */  
   Rpt1GainLoss:number,
      /**  Rpt2GainLoss  */  
   Rpt2GainLoss:number,
      /**  Rpt3GainLoss  */  
   Rpt3GainLoss:number,
      /**  CNCFICode  */  
   CNCFICode:string,
      /**  APInvoiceNum  */  
   APInvoiceNum:string,
      /**  TranType  */  
   TranType:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
   CNCFICodeDescription:string,
   CTDescription:string,
      /**  Flag to indicate if Manual checkbos should be Read Only  */  
   DisableManual:boolean,
      /**  Group ID - used to link to Cash Head  */  
   GroupID:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
      /**  The flag to indicate if the user changed Deductible Tax amount on manually updated tax record  */  
   DedTaxChanged:boolean,
   EnableTax:boolean,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtARPromissoryNotesTableset{
   ARPNHead:Erp_Tablesets_ARPNHeadRow[],
   ARPNHeadAttch:Erp_Tablesets_ARPNHeadAttchRow[],
   BankTran:Erp_Tablesets_BankTranRow[],
   BankTranTaxDtl:Erp_Tablesets_BankTranTaxDtlRow[],
   BankTranTGLC:Erp_Tablesets_BankTranTGLCRow[],
   ARPNDtl:Erp_Tablesets_ARPNDtlRow[],
   TaxDtl:Erp_Tablesets_TaxDtlRow[],
   ARPNHeadTGLC:Erp_Tablesets_ARPNHeadTGLCRow[],
   ARPNList:Erp_Tablesets_ARPNListRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipcustNum
      @param ipStageFilter
      @param fromDays
      @param inRange
   */  
export interface FillPNSummary_input{
      /**  The customer number  */  
   ipcustNum:number,
      /**  All, Open, Closed, or New  */  
   ipStageFilter:string,
      /**  the amount of days to get a date from which the invoices will be selected.  */  
   fromDays:number,
      /**  if the invoices will be selected from an specific date.  */  
   inRange:boolean,
}

export interface FillPNSummary_output{
   returnObj:Erp_Tablesets_PNSummaryTableset[],
}

   /** Required : 
      @param groupID
      @param headNum
      @param invoiceNum
   */  
export interface GenerateARPNDtl_input{
      /**  Cash Group ID  */  
   groupID:string,
      /**  Promissory Note HeadNum  */  
   headNum:number,
      /**  Promissory Note Invoice Num  */  
   invoiceNum:number,
}

export interface GenerateARPNDtl_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
}

   /** Required : 
      @param groupID
      @param custNum
      @param currencyCode
      @param invoiceNum
   */  
export interface GenerateARPNDtls_input{
      /**  Cash Group ID  */  
   groupID:string,
      /**  Customer Number  */  
   custNum:number,
      /**  Currency Code Number  */  
   currencyCode:string,
      /**  Promissory Note Invoice Num  */  
   invoiceNum:number,
}

export interface GenerateARPNDtls_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
}

   /** Required : 
      @param ipPNID
      @param fromTracker
   */  
export interface GetARPNListTracker_input{
      /**  ipPNID  */  
   ipPNID:string,
      /**  Indicates if the method was called from the Tracker or the Update program  */  
   fromTracker:boolean,
}

export interface GetARPNListTracker_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
}

   /** Required : 
      @param ipType
      @param ipPNID
      @param ipCustID
   */  
export interface GetARPNList_input{
      /**  ipType  */  
   ipType:string,
      /**  ipPNID  */  
   ipPNID:string,
      /**  ipCustID  */  
   ipCustID:string,
}

export interface GetARPNList_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
}

   /** Required : 
      @param iGroupID
      @param iHeadNum
   */  
export interface GetARPNMove_input{
      /**  The Group Number  */  
   iGroupID:string,
      /**  The Header Number  */  
   iHeadNum:number,
}

export interface GetARPNMove_output{
   returnObj:Erp_Tablesets_ARPNMoveTableset[],
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   AvailTypes:string,
}
}

   /** Required : 
      @param bankAcctID
      @param ds
   */  
export interface GetBankAcctInfo_input{
      /**  Proposed BankAcctID  */  
   bankAcctID:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetBankAcctInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param bankAcctID
      @param tranNum
      @param voided
      @param ds
   */  
export interface GetBankFeeDefaultAccount_input{
      /**  The Bank Account ID  */  
   bankAcctID:string,
      /**  The Bank Fee Tran Num  */  
   tranNum:number,
      /**  voided  */  
   voided:boolean,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetBankFeeDefaultAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface GetByID_input{
   groupID:string,
   headNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ds
   */  
export interface GetById4PITracker_input{
      /**  Group ID  */  
   ipGroupID:string,
      /**  Head Num  */  
   ipHeadNum:number,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetById4PITracker_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
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
      @param ipGroupID
   */  
export interface GetCurrencyCodeForBatch_input{
      /**  ipGroupID  */  
   ipGroupID:string,
}

export interface GetCurrencyCodeForBatch_output{
parameters : {
      /**  output parameters  */  
   opCurrencyCode:string,
   opDefaultFound:boolean,
}
}

   /** Required : 
      @param currencyCode
      @param ds
   */  
export interface GetCurrencyInfoMaster_input{
      /**  Proposed Currency Code  */  
   currencyCode:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetCurrencyInfoMaster_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param currencyCode
      @param ds
   */  
export interface GetCurrencyInfo_input{
      /**  Proposed Currency Code  */  
   currencyCode:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetCurrencyInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param custID
   */  
export interface GetCustPIFlags_input{
      /**  CustID for Customer  */  
   custID:string,
}

export interface GetCustPIFlags_output{
parameters : {
      /**  output parameters  */  
   autoGenPromNotes:boolean,
   directDebiting:boolean,
   hasBank:boolean,
}
}

   /** Required : 
      @param custID
      @param ds
   */  
export interface GetCustomerInfo_input{
      /**  Proposed Customer ID  */  
   custID:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetCustomerInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param invoiceNum
      @param ds
   */  
export interface GetDtlInvoiceInfo_input{
      /**  Proposed Invoice Number  */  
   invoiceNum:number,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetDtlInvoiceInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param legalNumber
      @param ds
   */  
export interface GetDtlLegalNumberInfo_input{
      /**  Proposed Legal Number  */  
   legalNumber:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetDtlLegalNumberInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param docTranAmt
      @param ds
   */  
export interface GetDtlTranAmtInfo_input{
      /**  Proposed transaction amount  */  
   docTranAmt:number,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetDtlTranAmtInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ipCustID
      @param ipCurrencyCode
   */  
export interface GetEligibleInvcsForSinglGenPI_input{
      /**  customer ID  */  
   ipCustID:string,
      /**  currency code  */  
   ipCurrencyCode:string,
}

export interface GetEligibleInvcsForSinglGenPI_output{
   returnObj:Erp_Tablesets_InvcsForCustTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetExistingGenPI_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetExistingGenPI_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param iGroupID
      @param iHeadNum
   */  
export interface GetGLJrnDtl_input{
      /**  The Group Number  */  
   iGroupID:string,
      /**  The Header Number  */  
   iHeadNum:number,
}

export interface GetGLJrnDtl_output{
   returnObj:Erp_Tablesets_GLJrnDtlMovTableset[],
}

   /** Required : 
      @param arPromNoteID
      @param aHeadNum
   */  
export interface GetGroupIDForPIWithHeadNum_input{
      /**  AR Promissory Note ID  */  
   arPromNoteID:string,
      /**  HeadNum ID  */  
   aHeadNum:number,
}

export interface GetGroupIDForPIWithHeadNum_output{
parameters : {
      /**  output parameters  */  
   groupID:string,
   headNum:number,
}
}

   /** Required : 
      @param arPromNoteID
   */  
export interface GetGroupIDForPI_input{
      /**  AR Promissory Note ID  */  
   arPromNoteID:string,
}

export interface GetGroupIDForPI_output{
parameters : {
      /**  output parameters  */  
   groupID:string,
   headNum:number,
}
}

   /** Required : 
      @param invoiceNum
      @param ds
   */  
export interface GetHdrInvoiceInfo_input{
      /**  Invoice Number to get Customer information from  */  
   invoiceNum:number,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetHdrInvoiceInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param legalNumber
      @param ds
   */  
export interface GetHdrLegalNumberInfo_input{
      /**  Legal Number to get Customer information from  */  
   legalNumber:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetHdrLegalNumberInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param invoiceNum
   */  
export interface GetHeadNumForPI_input{
      /**  Invoice Number  */  
   invoiceNum:number,
}

export interface GetHeadNumForPI_output{
parameters : {
      /**  output parameters  */  
   headNum:number,
}
}

   /** Required : 
      @param ipCustID
      @param ipCurrencyCode
   */  
export interface GetInvcsSinglGenPI_input{
      /**  customer ID  */  
   ipCustID:string,
      /**  currency code  */  
   ipCurrencyCode:string,
}

export interface GetInvcsSinglGenPI_output{
   returnObj:Erp_Tablesets_InvcsForCustTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
   */  
export interface GetLegalNumGenOpts_input{
      /**  ARPN group identifier.  */  
   ipGroupID:string,
      /**  ARPN header number.  */  
   ipHeadNum:number,
}

export interface GetLegalNumGenOpts_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
parameters : {
      /**  output parameters  */  
   opPromptForNum:boolean,
}
}

   /** Required : 
      @param legalNumber
      @param ds
   */  
export interface GetLegalNumberInfo_input{
      /**  Proposed Legal Number  */  
   legalNumber:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetLegalNumberInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param type
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListCustom_input{
      /**  PI type  */  
   type:string,
      /**  Where clause from search  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetListCustom_output{
   returnObj:Erp_Tablesets_ARPNHeadListTableset[],
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
   returnObj:Erp_Tablesets_ARPNHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param headNum
      @param invoiceNum
   */  
export interface GetNewARPNDtl_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
   headNum:number,
   invoiceNum:number,
}

export interface GetNewARPNDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
   */  
export interface GetNewARPNHeadAttch_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
   groupID:string,
   headNum:number,
}

export interface GetNewARPNHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param piGroupID
      @param ds
   */  
export interface GetNewARPNHeadByGroupID_input{
   piGroupID:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetNewARPNHeadByGroupID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ipBankAcctID
      @param invoiceNum
      @param ds
   */  
export interface GetNewARPNHeadByInvoiceAndAccount_input{
   ipBankAcctID:string,
   invoiceNum:number,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetNewARPNHeadByInvoiceAndAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param invoiceNum
      @param ds
   */  
export interface GetNewARPNHeadByInvoiceNum_input{
   invoiceNum:number,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetNewARPNHeadByInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
   */  
export interface GetNewARPNHeadTGLC_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
   groupID:string,
   headNum:number,
}

export interface GetNewARPNHeadTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewARPNHead_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
   groupID:string,
}

export interface GetNewARPNHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param lvHeadNum
      @param lvBankAcctID
      @param ds
   */  
export interface GetNewBankTranByHeadNum_input{
   lvHeadNum:number,
   lvBankAcctID:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetNewBankTranByHeadNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param tranNum
      @param voided
   */  
export interface GetNewBankTranTGLC_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
   bankAcctID:string,
   tranNum:number,
   voided:boolean,
}

export interface GetNewBankTranTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ds
      @param sourceModule
      @param headNum
      @param apTranNo
      @param invoiceNum
      @param invoiceRef
      @param bankAcctID
      @param tranNum
      @param voided
      @param taxCode
      @param rateCode
   */  
export interface GetNewBankTranTaxDtl_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
   sourceModule:string,
   headNum:number,
   apTranNo:number,
   invoiceNum:number,
   invoiceRef:number,
   bankAcctID:string,
   tranNum:number,
   voided:boolean,
   taxCode:string,
   rateCode:string,
}

export interface GetNewBankTranTaxDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param tranNum
   */  
export interface GetNewBankTran_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
   bankAcctID:string,
   tranNum:number,
}

export interface GetNewBankTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ds
      @param sourceModule
      @param headNum
      @param apTranNo
      @param invoiceNum
      @param invoiceRef
      @param bankAcctID
      @param tranNum
      @param voided
      @param taxCode
      @param rateCode
   */  
export interface GetNewTaxDtl_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
   sourceModule:string,
   headNum:number,
   apTranNo:number,
   invoiceNum:number,
   invoiceRef:number,
   bankAcctID:string,
   tranNum:number,
   voided:boolean,
   taxCode:string,
   rateCode:string,
}

export interface GetNewTaxDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ipPMUID
   */  
export interface GetPITypePropByPMUID_input{
      /**  PMUID  */  
   ipPMUID:number,
}

export interface GetPITypePropByPMUID_output{
parameters : {
      /**  output parameters  */  
   opCustBankDtl:boolean,
   opInitiation:string,
   opBankAcctID:string,
}
}

   /** Required : 
      @param ipGroupID
   */  
export interface GetPNotesByGroupID_input{
      /**  ipGroupID  */  
   ipGroupID:string,
}

export interface GetPNotesByGroupID_output{
   returnObj:Erp_Tablesets_ARPNHeadListTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetPNotesGenerated_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetPNotesGenerated_output{
   returnObj:Erp_Tablesets_ARPNHeadListTableset[],
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
export interface GetPNotes_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetPNotes_output{
   returnObj:Erp_Tablesets_ARPNHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param rateCode
      @param taxtbl
      @param ds
   */  
export interface GetRateCodeInfo_input{
      /**  Proposed RateCode value  */  
   rateCode:string,
      /**  Tax temp-table name  */  
   taxtbl:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetRateCodeInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param whereClauseARPNHead
      @param whereClauseARPNHeadAttch
      @param whereClauseBankTran
      @param whereClauseBankTranTaxDtl
      @param whereClauseBankTranTGLC
      @param whereClauseARPNDtl
      @param whereClauseTaxDtl
      @param whereClauseARPNHeadTGLC
      @param whereClauseARPNList
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows4Tracker_input{
      /**  where condition for ARPNHead table  */  
   whereClauseARPNHead:string,
      /**  where condition for ARPNHeadAttch table  */  
   whereClauseARPNHeadAttch:string,
      /**  where condition for BankTran table  */  
   whereClauseBankTran:string,
      /**  where condition for ClauseBankTranTaxDtl  */  
   whereClauseBankTranTaxDtl:string,
      /**  where condition for ClauseBankTranTGLC  */  
   whereClauseBankTranTGLC:string,
      /**  where condition for ClauseARPNDtl  */  
   whereClauseARPNDtl:string,
      /**  where condition for ClauseTaxDtl  */  
   whereClauseTaxDtl:string,
      /**  where condition for ClauseARPNHeadTGLC  */  
   whereClauseARPNHeadTGLC:string,
      /**  where condition for ClauseARPNList  */  
   whereClauseARPNList:string,
      /**  where condition for ClauseLegalNumGenOpts  */  
   whereClauseLegalNumGenOpts:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetRows4Tracker_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipGroupiD
      @param dummy
   */  
export interface GetRowsByGrpIDExt_input{
      /**  GroupID  */  
   ipGroupiD:string,
      /**  dummy param which helps to refresh landing page on Kinetic  */  
   dummy:string,
}

export interface GetRowsByGrpIDExt_output{
   returnObj:Erp_Tablesets_ARPNHeadListTableset[],
}

   /** Required : 
      @param ipGroupiD
   */  
export interface GetRowsByGrpID_input{
      /**  Group ID  */  
   ipGroupiD:string,
}

export interface GetRowsByGrpID_output{
   returnObj:Erp_Tablesets_ARPNHeadListTableset[],
}

   /** Required : 
      @param whereClauseARPNHead
      @param whereClauseARPNHeadAttch
      @param whereClauseBankTran
      @param whereClauseBankTranTaxDtl
      @param whereClauseBankTranTGLC
      @param whereClauseARPNDtl
      @param whereClauseTaxDtl
      @param whereClauseARPNHeadTGLC
      @param whereClauseARPNList
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseARPNHead:string,
   whereClauseARPNHeadAttch:string,
   whereClauseBankTran:string,
   whereClauseBankTranTaxDtl:string,
   whereClauseBankTranTGLC:string,
   whereClauseARPNDtl:string,
   whereClauseTaxDtl:string,
   whereClauseARPNHeadTGLC:string,
   whereClauseARPNList:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param taxCode
      @param taxtbl
      @param ds
   */  
export interface GetSalesTaxInfo_input{
      /**  Proposed TaxCode value  */  
   taxCode:string,
      /**  Tax temp-table name  */  
   taxtbl:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetSalesTaxInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param taxableAmt
      @param taxPercent
      @param fixedAmount
      @param taxtbl
      @param ds
   */  
export interface GetTaxableInfo_input{
      /**  Proposed new taxable Amount  */  
   taxableAmt:number,
      /**  Proposed Tax Percent  */  
   taxPercent:number,
      /**  Propoed Fixed Amount  */  
   fixedAmount:number,
      /**  tax temp-table name  */  
   taxtbl:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetTaxableInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param baseEntered
      @param ds
   */  
export interface GetTranAmt_input{
      /**  If the TranAmt field was updated then value should be yes, otherwise no  */  
   baseEntered:boolean,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface GetTranAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param piGroup
      @param piPayMethodFilter
   */  
export interface GetUnapprovedPI_input{
      /**  Group ID  */  
   piGroup:string,
      /**  PayMethodFilter Filter  */  
   piPayMethodFilter:string,
}

export interface GetUnapprovedPI_output{
   returnObj:Erp_Tablesets_ARPNHeadListTableset[],
}

   /** Required : 
      @param piGroup
      @param piPayMethodFilter
   */  
export interface GetUnapprovedPIwithCount_input{
      /**  Group ID  */  
   piGroup:string,
      /**  PayMethodFilter Filter  */  
   piPayMethodFilter:string,
}

export interface GetUnapprovedPIwithCount_output{
   returnObj:Erp_Tablesets_ARPNHeadListTableset[],
parameters : {
      /**  output parameters  */  
   opCreatedRecCounter:number,
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
      @param ipcustNum
      @param ipStageFilter
      @param fromDays
      @param inRange
   */  
export interface KineticFillPNSummary_input{
      /**  The customer number  */  
   ipcustNum:number,
      /**  All, Open, Closed, or New  */  
   ipStageFilter:string,
      /**  the amount of days to get a date from which the invoices will be selected.  */  
   fromDays:number,
      /**  if the invoices will be selected from an specific date.  */  
   inRange:boolean,
}

export interface KineticFillPNSummary_output{
   returnObj:Erp_Tablesets_PNSummaryTableset[],
}

   /** Required : 
      @param groupID
      @param headNum
      @param onAccount
      @param ds
   */  
export interface LeaveARPNHead_input{
      /**  Cash Receipt Group ID  */  
   groupID:string,
      /**  Cash Receipt number  */  
   headNum:number,
      /**  Indicates if excess cash should go on account  */  
   onAccount:boolean,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface LeaveARPNHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface MarkSent_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface MarkSent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface MarkSigned_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface MarkSigned_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ipBankAcctID
      @param ds
   */  
export interface OnChangeBankAcctID_input{
   ipBankAcctID:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface OnChangeBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param pcBankFeeID
      @param ds
   */  
export interface OnChangeBankFeeID_input{
   pcBankFeeID:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface OnChangeBankFeeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param pcType
      @param ds
   */  
export interface OnChangeType_input{
   pcType:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface OnChangeType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ipGroupID
   */  
export interface PostPIGroupWithoutGL_input{
      /**  Group ID of PI  */  
   ipGroupID:string,
}

export interface PostPIGroupWithoutGL_output{
}

   /** Required : 
      @param ipGroupID
   */  
export interface PostPNWithoutGL_input{
      /**  ipGroupID  */  
   ipGroupID:string,
}

export interface PostPNWithoutGL_output{
}

   /** Required : 
      @param ipGroupID
   */  
export interface PrePostCheck_input{
      /**  Group ID of PI  */  
   ipGroupID:string,
}

export interface PrePostCheck_output{
parameters : {
      /**  output parameters  */  
   vTaxQuestion:string,
   legalNumberMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface RecalcBankTax_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface RecalcBankTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ipInvoiceNum
      @param ipInvoiceRef
      @param ipBankAcctID
      @param ipTranNum
      @param ipVoided
      @param ipCalcAll
      @param ds
   */  
export interface SetReadyToCalc_input{
      /**  ipGroupID  */  
   ipGroupID:string,
      /**  ipHeadNum  */  
   ipHeadNum:number,
      /**  ipInvoiceNum  */  
   ipInvoiceNum:number,
      /**  ipInvoiceRef  */  
   ipInvoiceRef:number,
      /**  ipBankAcctID  */  
   ipBankAcctID:string,
      /**  ipTranNum  */  
   ipTranNum:number,
      /**  ipVoided  */  
   ipVoided:boolean,
      /**  ipCalcAll  */  
   ipCalcAll:boolean,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface SetReadyToCalc_output{
}

   /** Required : 
      @param ipCustNum
      @param ipCustId
      @param ipPIStatus
      @param ipPIType
      @param ipGroupID
      @param ipCurrencyCode
      @param ds
   */  
export interface SingleGenPIExt_input{
   ipCustNum:number,
   ipCustId:string,
   ipPIStatus:string,
   ipPIType:string,
   ipGroupID:string,
   ipCurrencyCode:string,
   ds:Erp_Tablesets_InvcsForCustTableset[],
}

export interface SingleGenPIExt_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
}

   /** Required : 
      @param ipCustNum
      @param ipCustId
      @param ipPIStatus
      @param ipPIType
      @param ipInvcList
      @param ipGroupID
      @param ipCurrencyCode
   */  
export interface SingleGenPI_input{
      /**  ipCustNum  */  
   ipCustNum:number,
      /**  ipCustId  */  
   ipCustId:string,
      /**  ipPIStatus  */  
   ipPIStatus:string,
      /**  ipPIType  */  
   ipPIType:string,
      /**  ipInvcList  */  
   ipInvcList:string,
      /**  ipGroupID  */  
   ipGroupID:string,
      /**  ipCurrencyCode  */  
   ipCurrencyCode:string,
}

export interface SingleGenPI_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtARPromissoryNotesTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtARPromissoryNotesTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param PIType
   */  
export interface ValidateARPIType_input{
   PIType:string,
}

export interface ValidateARPIType_output{
      /**  Bool  */  
   returnObj:boolean,
}

   /** Required : 
      @param iARPromNoteID
      @param iPIType
      @param iCustID
      @param ds
   */  
export interface ValidateDuplicatedARPromNoteID_input{
   iARPromNoteID:string,
   iPIType:string,
   iCustID:string,
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}

export interface ValidateDuplicatedARPromNoteID_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPromissoryNotesTableset[],
}
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ipVoidedReason
   */  
export interface VoidLegalNumber_input{
      /**  ARPN group identifier.  */  
   ipGroupID:string,
      /**  ARPN header number.  */  
   ipHeadNum:number,
      /**  Indicates reason why legal number should be voided.  */  
   ipVoidedReason:string,
}

export interface VoidLegalNumber_output{
   returnObj:Erp_Tablesets_ARPromissoryNotesTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ipFileName
   */  
export interface WriteXMLFile_input{
   ipGroupID:string,
   ipHeadNum:number,
   ipFileName:string,
}

export interface WriteXMLFile_output{
      /**  File Path on server  */  
   returnObj:string,
}

