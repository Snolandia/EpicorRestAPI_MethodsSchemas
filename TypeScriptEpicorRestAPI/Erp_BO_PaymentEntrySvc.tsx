import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PaymentEntrySvc
// Description: Initialize
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/$metadata", {
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
   Description: Get PaymentEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PaymentEntries
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedRow
   */  
export function get_PaymentEntries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PaymentEntries
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CheckHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CheckHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PaymentEntries(requestBody:Erp_Tablesets_CheckHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries", {
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
   Summary: Calls GetByID to retrieve the PaymentEntry item
   Description: Calls GetByID to retrieve the PaymentEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PaymentEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CheckHedRow
   */  
export function get_PaymentEntries_Company_HeadNum(Company:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CheckHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries(" + Company + "," + HeadNum + ")", {
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
         resolve(data as Erp_Tablesets_CheckHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PaymentEntry for the service
   Description: Calls UpdateExt to update PaymentEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PaymentEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CheckHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PaymentEntries_Company_HeadNum(Company:string, HeadNum:string, requestBody:Erp_Tablesets_CheckHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries(" + Company + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete PaymentEntry item
   Description: Call UpdateExt to delete PaymentEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PaymentEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PaymentEntries_Company_HeadNum(Company:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries(" + Company + "," + HeadNum + ")", {
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
   Description: Get APTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APTrans1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranRow
   */  
export function get_PaymentEntries_Company_HeadNum_APTrans(Company:string, HeadNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries(" + Company + "," + HeadNum + ")/APTrans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APTran item
   Description: Calls GetByID to retrieve the APTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTran1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APTranRow
   */  
export function get_PaymentEntries_Company_HeadNum_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries(" + Company + "," + HeadNum + ")/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
         resolve(data as Erp_Tablesets_APTranRow)
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
      @param HeadNum Desc: HeadNum   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranRow
   */  
export function get_PaymentEntries_Company_HeadNum_BankTrans(Company:string, HeadNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries(" + Company + "," + HeadNum + ")/BankTrans", {
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
      @param HeadNum Desc: HeadNum   Required: True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BankTranRow
   */  
export function get_PaymentEntries_Company_HeadNum_BankTrans_Company_BankAcctID_TranNum_Voided(Company:string, HeadNum:string, BankAcctID:string, TranNum:string, Voided:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries(" + Company + "," + HeadNum + ")/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
         resolve(data as Erp_Tablesets_BankTranRow)
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
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxDtlRow
   */  
export function get_PaymentEntries_Company_HeadNum_TaxDtls(Company:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries(" + Company + "," + HeadNum + ")/TaxDtls", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaxDtlRow
   */  
export function get_PaymentEntries_Company_HeadNum_TaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, HeadNum:string, SourceModule:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries(" + Company + "," + HeadNum + ")/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_TaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CheckHedAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CheckHedAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedAttchRow
   */  
export function get_PaymentEntries_Company_HeadNum_CheckHedAttches(Company:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries(" + Company + "," + HeadNum + ")/CheckHedAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CheckHedAttch item
   Description: Calls GetByID to retrieve the CheckHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckHedAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CheckHedAttchRow
   */  
export function get_PaymentEntries_Company_HeadNum_CheckHedAttches_Company_HeadNum_DrawingSeq(Company:string, HeadNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CheckHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PaymentEntries(" + Company + "," + HeadNum + ")/CheckHedAttches(" + Company + "," + HeadNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_CheckHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get APTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APTrans
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranRow
   */  
export function get_APTrans(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTrans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APTrans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APTrans(requestBody:Erp_Tablesets_APTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTrans", {
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
   Summary: Calls GetByID to retrieve the APTran item
   Description: Calls GetByID to retrieve the APTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APTranRow
   */  
export function get_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
         resolve(data as Erp_Tablesets_APTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APTran for the service
   Description: Calls UpdateExt to update APTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, requestBody:Erp_Tablesets_APTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
   Summary: Call UpdateExt to delete APTran item
   Description: Call UpdateExt to delete APTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
   Description: Get APTTaxDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APTTaxDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTTaxDtlRow
   */  
export function get_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided_APTTaxDtls(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")/APTTaxDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APTTaxDtl item
   Description: Calls GetByID to retrieve the APTTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTTaxDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APTTaxDtlRow
   */  
export function get_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided_APTTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, SourceModule:string, InvoiceRef:string, BankAcctID:string, TranNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APTTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")/APTTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_APTTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get APTranTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APTranTGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranTGLCRow
   */  
export function get_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided_APTranTGLCs(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")/APTranTGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APTranTGLC item
   Description: Calls GetByID to retrieve the APTranTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTranTGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APTranTGLCRow
   */  
export function get_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided_APTranTGLCs_Company_HeadNum_APTranNo_InvoiceNum_Voided_SysRowID(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APTranTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")/APTranTGLCs(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + "," + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_APTranTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get APTTaxDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APTTaxDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTTaxDtlRow
   */  
export function get_APTTaxDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTTaxDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APTTaxDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APTTaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APTTaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APTTaxDtls(requestBody:Erp_Tablesets_APTTaxDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTTaxDtls", {
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
   Summary: Calls GetByID to retrieve the APTTaxDtl item
   Description: Calls GetByID to retrieve the APTTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTTaxDtl
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APTTaxDtlRow
   */  
export function get_APTTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APTTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_APTTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APTTaxDtl for the service
   Description: Calls UpdateExt to update APTTaxDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APTTaxDtl
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APTTaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APTTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:Erp_Tablesets_APTTaxDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete APTTaxDtl item
   Description: Call UpdateExt to delete APTTaxDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APTTaxDtl
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APTTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get APTranTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APTranTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranTGLCRow
   */  
export function get_APTranTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTranTGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APTranTGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APTranTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APTranTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APTranTGLCs(requestBody:Erp_Tablesets_APTranTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTranTGLCs", {
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
   Summary: Calls GetByID to retrieve the APTranTGLC item
   Description: Calls GetByID to retrieve the APTranTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTranTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APTranTGLCRow
   */  
export function get_APTranTGLCs_Company_HeadNum_APTranNo_InvoiceNum_Voided_SysRowID(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APTranTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTranTGLCs(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + "," + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_APTranTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APTranTGLC for the service
   Description: Calls UpdateExt to update APTranTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APTranTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APTranTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APTranTGLCs_Company_HeadNum_APTranNo_InvoiceNum_Voided_SysRowID(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, SysRowID:string, requestBody:Erp_Tablesets_APTranTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTranTGLCs(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + "," + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete APTranTGLC item
   Description: Call UpdateExt to delete APTranTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APTranTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APTranTGLCs_Company_HeadNum_APTranNo_InvoiceNum_Voided_SysRowID(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/APTranTGLCs(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + "," + SysRowID + ")", {
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
   Description: Get BankTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTrans
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranRow
   */  
export function get_BankTrans(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTrans", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BankTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankTrans(requestBody:Erp_Tablesets_BankTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTrans", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BankTranRow
   */  
export function get_BankTrans_Company_BankAcctID_TranNum_Voided(Company:string, BankAcctID:string, TranNum:string, Voided:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankTrans_Company_BankAcctID_TranNum_Voided(Company:string, BankAcctID:string, TranNum:string, Voided:string, requestBody:Erp_Tablesets_BankTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
   Summary: Call UpdateExt to delete BankTran item
   Description: Call UpdateExt to delete BankTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTaxDtlRow
   */  
export function get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTaxDtls(Company:string, BankAcctID:string, TranNum:string, Voided:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   */  
export function get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, BankAcctID:string, TranNum:string, Voided:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTGLCRow
   */  
export function get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTGLCs(Company:string, BankAcctID:string, TranNum:string, Voided:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BankTranTGLCRow
   */  
export function get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company:string, BankAcctID:string, TranNum:string, Voided:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTaxDtlRow
   */  
export function get_BankTranTaxDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTranTaxDtls", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankTranTaxDtls(requestBody:Erp_Tablesets_BankTranTaxDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTranTaxDtls", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   */  
export function get_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:Erp_Tablesets_BankTranTaxDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get BankTranTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTranTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTGLCRow
   */  
export function get_BankTranTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTranTGLCs", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BankTranTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankTranTGLCs(requestBody:Erp_Tablesets_BankTranTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTranTGLCs", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BankTranTGLCRow
   */  
export function get_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company:string, BankAcctID:string, TranNum:string, Voided:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company:string, BankAcctID:string, TranNum:string, Voided:string, SysRowID:string, requestBody:Erp_Tablesets_BankTranTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete BankTranTGLC item
   Description: Call UpdateExt to delete BankTranTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTranTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
   Description: Get TaxDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxDtlRow
   */  
export function get_TaxDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/TaxDtls", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxDtls(requestBody:Erp_Tablesets_TaxDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/TaxDtls", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaxDtlRow
   */  
export function get_TaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:Erp_Tablesets_TaxDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get CheckHedAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CheckHedAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedAttchRow
   */  
export function get_CheckHedAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CheckHedAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CheckHedAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CheckHedAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CheckHedAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckHedAttches(requestBody:Erp_Tablesets_CheckHedAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CheckHedAttches", {
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
   Summary: Calls GetByID to retrieve the CheckHedAttch item
   Description: Calls GetByID to retrieve the CheckHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CheckHedAttchRow
   */  
export function get_CheckHedAttches_Company_HeadNum_DrawingSeq(Company:string, HeadNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CheckHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CheckHedAttches(" + Company + "," + HeadNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_CheckHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CheckHedAttch for the service
   Description: Calls UpdateExt to update CheckHedAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CheckHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CheckHedAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CheckHedAttches_Company_HeadNum_DrawingSeq(Company:string, HeadNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_CheckHedAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CheckHedAttches(" + Company + "," + HeadNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete CheckHedAttch item
   Description: Call UpdateExt to delete CheckHedAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CheckHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CheckHedAttches_Company_HeadNum_DrawingSeq(Company:string, HeadNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CheckHedAttches(" + Company + "," + HeadNum + "," + DrawingSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCheckHed:string, whereClauseCheckHedAttch:string, whereClauseAPTran:string, whereClauseAPTranTGLC:string, whereClauseAPTTaxDtl:string, whereClauseBankTran:string, whereClauseBankTranTaxDtl:string, whereClauseBankTranTGLC:string, whereClauseTaxDtl:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCheckHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCheckHed=" + whereClauseCheckHed
   }
   if(typeof whereClauseCheckHedAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCheckHedAttch=" + whereClauseCheckHedAttch
   }
   if(typeof whereClauseAPTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPTran=" + whereClauseAPTran
   }
   if(typeof whereClauseAPTranTGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPTranTGLC=" + whereClauseAPTranTGLC
   }
   if(typeof whereClauseAPTTaxDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPTTaxDtl=" + whereClauseAPTTaxDtl
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
   if(typeof whereClauseTaxDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxDtl=" + whereClauseTaxDtl
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

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(headNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
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

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetList" + params, {
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
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the payment.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/AssignLegalNumber", {
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
   Summary: Invoke method GetTHWHTCertNoGenerationType
   Description: Gets the Generation Type of Thailand Withholding Tax Certificate Numbers
   OperationID: GetTHWHTCertNoGenerationType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTHWHTCertNoGenerationType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTHWHTCertNoGenerationType(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTHWHTCertNoGenerationType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetTHWHTCertNoGenerationType", {
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
         resolve(data as GetTHWHTCertNoGenerationType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTHWHTCertNoOpts
   Description: Returns a record in the LegalNumGenOpts datatable that will be used to generate a Withholding Tax Certificate Number
   OperationID: GetTHWHTCertNoOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTHWHTCertNoOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTHWHTCertNoOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTHWHTCertNoOpts(requestBody:GetTHWHTCertNoOpts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTHWHTCertNoOpts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetTHWHTCertNoOpts", {
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
         resolve(data as GetTHWHTCertNoOpts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignTHWHTCertNo
   Description: Assigns a Withholding Tax Certificate Number to the payment
   OperationID: AssignTHWHTCertNo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AssignTHWHTCertNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignTHWHTCertNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignTHWHTCertNo(requestBody:AssignTHWHTCertNo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AssignTHWHTCertNo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/AssignTHWHTCertNo", {
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
         resolve(data as AssignTHWHTCertNo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidTHWHTCertNo
   Description: Voids a Withholding Tax Certificate Number
   OperationID: VoidTHWHTCertNo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VoidTHWHTCertNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidTHWHTCertNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidTHWHTCertNo(requestBody:VoidTHWHTCertNo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VoidTHWHTCertNo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/VoidTHWHTCertNo", {
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
         resolve(data as VoidTHWHTCertNo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidSingleWHTCertificateNum
   Description: Void single WHT Certificate Number
   OperationID: VoidSingleWHTCertificateNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VoidSingleWHTCertificateNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidSingleWHTCertificateNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidSingleWHTCertificateNum(requestBody:VoidSingleWHTCertificateNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VoidSingleWHTCertificateNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/VoidSingleWHTCertificateNum", {
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
         resolve(data as VoidSingleWHTCertificateNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateTHWHTCertNoAssigned
   Description: Checks if all necessary Withholding Tax Certificate Numbers are assigned for manual method
   OperationID: ValidateTHWHTCertNoAssigned
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateTHWHTCertNoAssigned_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTHWHTCertNoAssigned_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateTHWHTCertNoAssigned(requestBody:ValidateTHWHTCertNoAssigned_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateTHWHTCertNoAssigned_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/ValidateTHWHTCertNoAssigned", {
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
         resolve(data as ValidateTHWHTCertNoAssigned_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalcTranAmtExt
   Description: CalcTranAmtExt
   OperationID: CalcTranAmtExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalcTranAmtExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcTranAmtExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcTranAmtExt(requestBody:CalcTranAmtExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalcTranAmtExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CalcTranAmtExt", {
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
         resolve(data as CalcTranAmtExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeVendorBankBranchCode
   Description: Check if the Bank Branch code changed.
   OperationID: OnChangeVendorBankBranchCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeVendorBankBranchCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorBankBranchCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendorBankBranchCode(requestBody:OnChangeVendorBankBranchCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeVendorBankBranchCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeVendorBankBranchCode", {
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
         resolve(data as OnChangeVendorBankBranchCode_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTranAmt(requestBody:ChangeTranAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTranAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/ChangeTranAmt", {
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
         resolve(data as ChangeTranAmt_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDocumentIsLocked(requestBody:CheckDocumentIsLocked_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDocumentIsLocked_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CheckDocumentIsLocked", {
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
         resolve(data as CheckDocumentIsLocked_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDocumentsInGroupLocked
   Description: Checking documents in the group if any document is locked
   OperationID: CheckDocumentsInGroupLocked
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDocumentsInGroupLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentsInGroupLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDocumentsInGroupLocked(requestBody:CheckDocumentsInGroupLocked_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDocumentsInGroupLocked_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CheckDocumentsInGroupLocked", {
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
         resolve(data as CheckDocumentsInGroupLocked_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VerifyBatchID
   Description: Pre-process batch id verification. This method verifies conditions and set a state to display dialog message on OU. UI gets user input and calls further methods depending on the input.
   OperationID: VerifyBatchID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VerifyBatchID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyBatchID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifyBatchID(requestBody:VerifyBatchID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VerifyBatchID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/VerifyBatchID", {
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
         resolve(data as VerifyBatchID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateChecks
   Description: Create Vendor Checks for selected invoices.
   OperationID: CreateChecks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateChecks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateChecks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateChecks(requestBody:CreateChecks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateChecks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CreateChecks", {
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
         resolve(data as CreateChecks_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateNewCheckHed
   Description: Create New CheckHed record.  To be used instead of GetNewCheckHed record.
   OperationID: CreateNewCheckHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateNewCheckHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewCheckHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateNewCheckHed(requestBody:CreateNewCheckHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateNewCheckHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CreateNewCheckHed", {
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
         resolve(data as CreateNewCheckHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteNegPayments
   Description: DeleteNegPayments.  Deletes all checks in the group that have negative check.
amounts. Works the same as MassDelete but only deletes negative balance checks.
   OperationID: DeleteNegPayments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteNegPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteNegPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteNegPayments(requestBody:DeleteNegPayments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteNegPayments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/DeleteNegPayments", {
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
         resolve(data as DeleteNegPayments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRegulatoryReportingCodeList
   Description: This method returns a list of valid Regulatory Reporting codes
   OperationID: GetRegulatoryReportingCodeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRegulatoryReportingCodeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRegulatoryReportingCodeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRegulatoryReportingCodeList(requestBody:GetRegulatoryReportingCodeList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRegulatoryReportingCodeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetRegulatoryReportingCodeList", {
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
         resolve(data as GetRegulatoryReportingCodeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAPTranReasonList
   Description: This method returns a list of valid AP Transaction Reason codes
   OperationID: GetAPTranReasonList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAPTranReasonList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPTranReasonList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAPTranReasonList(requestBody:GetAPTranReasonList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAPTranReasonList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetAPTranReasonList", {
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
         resolve(data as GetAPTranReasonList_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBankFeeDefaultAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankFeeDefaultAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankFeeDefaultAccount(requestBody:GetBankFeeDefaultAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBankFeeDefaultAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetBankFeeDefaultAccount", {
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
         resolve(data as GetBankFeeDefaultAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetElecInterface
   Description: Check if Payment Method is marked as Electronic Interface.
   OperationID: GetElecInterface
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetElecInterface_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetElecInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetElecInterface(requestBody:GetElecInterface_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetElecInterface_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetElecInterface", {
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
         resolve(data as GetElecInterface_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLegalNumberOpts
   Description: This method will return a record in the LegalNumGenOpts datatable that will
be used to generate a legal number.
   OperationID: GetLegalNumberOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLegalNumberOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumberOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLegalNumberOpts(requestBody:GetLegalNumberOpts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLegalNumberOpts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetLegalNumberOpts", {
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
         resolve(data as GetLegalNumberOpts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidLegalNumber
   Description: Method to void legal numbers
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/VoidLegalNumber", {
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
   Summary: Invoke method GetNewBankTranByHeadNum
   Description: Get New BankTran record for CheckHead
   OperationID: GetNewBankTranByHeadNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBankTranByHeadNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranByHeadNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankTranByHeadNum(requestBody:GetNewBankTranByHeadNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBankTranByHeadNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetNewBankTranByHeadNum", {
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
         resolve(data as GetNewBankTranByHeadNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMiscPayment
   Description: Create New Miscellaneous APTran record.
   OperationID: GetNewMiscPayment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMiscPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMiscPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMiscPayment(requestBody:GetNewMiscPayment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMiscPayment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetNewMiscPayment", {
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
         resolve(data as GetNewMiscPayment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPaymentRelationshipMap
   Description: Returns a serialized json string to show a Relationship Map for Payment
   OperationID: GetPaymentRelationshipMap
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPaymentRelationshipMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPaymentRelationshipMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPaymentRelationshipMap(requestBody:GetPaymentRelationshipMap_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPaymentRelationshipMap_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetPaymentRelationshipMap", {
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
         resolve(data as GetPaymentRelationshipMap_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRestartProcessPayment
   Description: Gets restart Process Payment
   OperationID: GetRestartProcessPayment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRestartProcessPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRestartProcessPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRestartProcessPayment(requestBody:GetRestartProcessPayment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRestartProcessPayment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetRestartProcessPayment", {
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
         resolve(data as GetRestartProcessPayment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MassDelete
   Description: Mass Delete.  Delete all checks in the Group.
   OperationID: MassDelete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MassDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassDelete(requestBody:MassDelete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MassDelete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/MassDelete", {
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
         resolve(data as MassDelete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MXCheckPaymentIsCheque
   Description: Method to call when it is necessary to check if Payment is Cheque.
   OperationID: MXCheckPaymentIsCheque
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MXCheckPaymentIsCheque_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MXCheckPaymentIsCheque_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MXCheckPaymentIsCheque(requestBody:MXCheckPaymentIsCheque_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MXCheckPaymentIsCheque_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/MXCheckPaymentIsCheque", {
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
         resolve(data as MXCheckPaymentIsCheque_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankFeeID
   OperationID: OnChangeBankFeeID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBankFeeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankFeeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankFeeID(requestBody:OnChangeBankFeeID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBankFeeID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeBankFeeID", {
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
         resolve(data as OnChangeBankFeeID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankTotalAmt
   Description: Call method when the user changes Bank Total Amount
   OperationID: OnChangeBankTotalAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBankTotalAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTotalAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankTotalAmt(requestBody:OnChangeBankTotalAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBankTotalAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeBankTotalAmt", {
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
         resolve(data as OnChangeBankTotalAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCheckDate
   Description: Call method when the user changes CheckHed.CheckDate.
   OperationID: OnChangeCheckDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCheckDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCheckDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCheckDate(requestBody:OnChangeCheckDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCheckDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeCheckDate", {
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
         resolve(data as OnChangeCheckDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCheckNum
   Description: Call method when the user changes CheckHed.CheckNum.
   OperationID: OnChangeCheckNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCheckNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCheckNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCheckNum(requestBody:OnChangeCheckNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCheckNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeCheckNum", {
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
         resolve(data as OnChangeCheckNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCurrency
   Description: Call method when the user changes flag CheckHed.IsEnterTotal
   OperationID: OnChangeCurrency
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCurrency(requestBody:OnChangeCurrency_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCurrency_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeCurrency", {
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
         resolve(data as OnChangeCurrency_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDocDiscAmt
   Description: Call method when the user changes the Doc Discount Amount changes in Pay Invoice.
Use this method with Payment Invoice screen for PaymentEntryDataSet.
   OperationID: OnChangeDocDiscAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDocDiscAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDocDiscAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDocDiscAmt(requestBody:OnChangeDocDiscAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDocDiscAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeDocDiscAmt", {
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
         resolve(data as OnChangeDocDiscAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDocPaymentTotal
   Description: Call method when the user changes Payment Total
   OperationID: OnChangeDocPaymentTotal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDocPaymentTotal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDocPaymentTotal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDocPaymentTotal(requestBody:OnChangeDocPaymentTotal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDocPaymentTotal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeDocPaymentTotal", {
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
         resolve(data as OnChangeDocPaymentTotal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDocTranAmt
   Description: Call method when the user changes the Doc Tran Amount changes in Pay Misc and Invoice.
   OperationID: OnChangeDocTranAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDocTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDocTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDocTranAmt(requestBody:OnChangeDocTranAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDocTranAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeDocTranAmt", {
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
         resolve(data as OnChangeDocTranAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeExchangeRate
   Description: Call method when the user changes Rate from Payment Currency to Bank Currency
   OperationID: OnChangeExchangeRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeExchangeRate(requestBody:OnChangeExchangeRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeExchangeRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeExchangeRate", {
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
         resolve(data as OnChangeExchangeRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDedTaxAmount
   Description: Call method when the user changes the FixedAmount in Tax screen.
Use this method with Misc. Payment screen for PaymentEntryDataSet.
   OperationID: OnChangeDedTaxAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDedTaxAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDedTaxAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDedTaxAmount(requestBody:OnChangeDedTaxAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDedTaxAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeDedTaxAmount", {
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
         resolve(data as OnChangeDedTaxAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFixedAmount
   Description: Call method when the user changes the FixedAmount in Tax screen.
Use this method with Misc. Payment screen for PaymentEntryDataSet.
   OperationID: OnChangeFixedAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFixedAmount(requestBody:OnChangeFixedAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFixedAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeFixedAmount", {
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
         resolve(data as OnChangeFixedAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeInvoiceNum
   Description: Call this method when the user enters the Invoice Number in Pay Invoice screen.
   OperationID: OnChangeInvoiceNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInvoiceNum(requestBody:OnChangeInvoiceNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeInvoiceNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeInvoiceNum", {
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
         resolve(data as OnChangeInvoiceNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeInvSelPayment
   Description: Call this method when the user changes either Gross Payment or Disc. Taken field.
Use this method with Payment maintenance screen for APInvSelDataSet.
   OperationID: OnChangeInvSelPayment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeInvSelPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInvSelPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInvSelPayment(requestBody:OnChangeInvSelPayment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeInvSelPayment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeInvSelPayment", {
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
         resolve(data as OnChangeInvSelPayment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeIsEnterTotal
   Description: Call method when the user changes flag CheckHed.IsEnterTotal
   OperationID: OnChangeIsEnterTotal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeIsEnterTotal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIsEnterTotal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeIsEnterTotal(requestBody:OnChangeIsEnterTotal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeIsEnterTotal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeIsEnterTotal", {
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
         resolve(data as OnChangeIsEnterTotal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeManualPrint
   Description: Call method when the user checks / unChecks the Manual Print flag.
   OperationID: OnChangeManualPrint
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeManualPrint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeManualPrint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeManualPrint(requestBody:OnChangeManualPrint_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeManualPrint_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeManualPrint", {
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
         resolve(data as OnChangeManualPrint_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePaymentBankRate
   Description: Call method when the user changes Rate from Payment Currency to Bank Currency
   OperationID: OnChangePaymentBankRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePaymentBankRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePaymentBankRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePaymentBankRate(requestBody:OnChangePaymentBankRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePaymentBankRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangePaymentBankRate", {
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
         resolve(data as OnChangePaymentBankRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePrePayment
   Description: Call this method when the user change flag PrePayment in Misc Payment screen.
   OperationID: OnChangePrePayment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePrePayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePrePayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePrePayment(requestBody:OnChangePrePayment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePrePayment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangePrePayment", {
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
         resolve(data as OnChangePrePayment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeRateCode
   Description: This method updates the dataset when the RateCode field changes
   OperationID: OnChangeRateCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRateCode(requestBody:OnChangeRateCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeRateCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeRateCode", {
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
         resolve(data as OnChangeRateCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeRefPONum
   Description: Call this method when the user enters the RefPONum for PrePayment
   OperationID: OnChangeRefPONum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeRefPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRefPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRefPONum(requestBody:OnChangeRefPONum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeRefPONum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeRefPONum", {
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
         resolve(data as OnChangeRefPONum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxableAmt
   Description: Call method when the user changes the Taxable Amt in Tax screen.
Use this method with Misc. Payment screen for PaymentEntryDataSet.
   OperationID: OnChangeTaxableAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxableAmt(requestBody:OnChangeTaxableAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxableAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeTaxableAmt", {
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
         resolve(data as OnChangeTaxableAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxAmt
   Description: Call method when the user changes the Tax Amt in Tax screen.
Use this method with Misc. Payment screen for PaymentEntryDataSet.
   OperationID: OnChangeTaxAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxAmt(requestBody:OnChangeTaxAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeTaxAmt", {
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
         resolve(data as OnChangeTaxAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxCode
   Description: Call method when the user changes the Tax ID in Tax maintainence.
Use this method with Misc. Payment screen for PaymentEntryDataSet.
   OperationID: OnChangeTaxCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxCode(requestBody:OnChangeTaxCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeTaxCode", {
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
         resolve(data as OnChangeTaxCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxPercent
   Description: Call method when the user changes the Tax Percent in Tax screen.
Use this method with Misc. Payment screen for PaymentEntryDataSet.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeTaxPercent", {
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
   Summary: Invoke method OnChangeVendor
   Description: Call this method when the user enters the ttCheckHed.VendorNum
   OperationID: OnChangeVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendor(requestBody:OnChangeVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeVendor", {
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
         resolve(data as OnChangeVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTHRefVendorID
   Description: Verify selected TH Reference Customer
   OperationID: OnChangeTHRefVendorID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTHRefVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTHRefVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTHRefVendorID(requestBody:OnChangeTHRefVendorID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTHRefVendorID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeTHRefVendorID", {
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
         resolve(data as OnChangeTHRefVendorID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTHRefInvoiceNum
   Description: Verify selected Reference Invoice NUmber
   OperationID: OnChangeTHRefInvoiceNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTHRefInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTHRefInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTHRefInvoiceNum(requestBody:OnChangeTHRefInvoiceNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTHRefInvoiceNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeTHRefInvoiceNum", {
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
         resolve(data as OnChangeTHRefInvoiceNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PostAllowed
   Description: Check if Post operation is available.
   OperationID: PostAllowed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PostAllowed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostAllowed(requestBody:PostAllowed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PostAllowed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PostAllowed", {
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
         resolve(data as PostAllowed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts datatable if
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/PreUpdate", {
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
   Summary: Invoke method RefreshBankInfo
   Description: Refresh bank info for selected invoices.
   OperationID: RefreshBankInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshBankInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshBankInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshBankInfo(requestBody:RefreshBankInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshBankInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/RefreshBankInfo", {
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
         resolve(data as RefreshBankInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResetProcessPayment
   Description: Clears out the check numbers from all checks in the CheckHed table and refreshes
the checks data (i.e. the Supplier information, etc.).
   OperationID: ResetProcessPayment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ResetProcessPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetProcessPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetProcessPayment(requestBody:ResetProcessPayment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ResetProcessPayment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/ResetProcessPayment", {
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
         resolve(data as ResetProcessPayment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectInvoices
   Description: Read ApInvHed records and create APInvSel records if they meet the selection criteria.
   OperationID: SelectInvoices
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectInvoices(requestBody:SelectInvoices_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectInvoices_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/SelectInvoices", {
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
         resolve(data as SelectInvoices_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectInvoicesMS
   Description: Read ApInvHed records and create APInvSel records if they meet the selection criteria.
   OperationID: SelectInvoicesMS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectInvoicesMS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectInvoicesMS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectInvoicesMS(requestBody:SelectInvoicesMS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectInvoicesMS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/SelectInvoicesMS", {
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
         resolve(data as SelectInvoicesMS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetCompleted
   Description: Sets all payments in group status to Completed.
   OperationID: SetCompleted
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetCompleted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCompleted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetCompleted(requestBody:SetCompleted_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetCompleted_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/SetCompleted", {
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
         resolve(data as SetCompleted_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetTransmitted
   Description: Sets all payments in group status to Trasmitted.
   OperationID: SetTransmitted
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetTransmitted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTransmitted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetTransmitted(requestBody:SetTransmitted_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetTransmitted_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/SetTransmitted", {
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
         resolve(data as SetTransmitted_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetReadyToCalc
   Description: Purpose: CALCULATE VANTAGE\TAX CONNECT TAX CALCULATIONS
UI NEEDS TO CALL A SAVE BEFORE CALLING THIS PROCEDURE
Parameters:  none
Notes:
<param name="ipGroupID">ipGroupID </param><param name="ipHeadNum">ipHeadNum </param><param name="ipAPTranNo">ipAPTranNo </param><param name="ipBankAcctID">ipBankAcctID </param><param name="ipTranNum">ipTranNum </param><param name="ipVoided">ipVoided </param><param name="ipCalcAll">ipCalcAll</param><param name="ds" type="Epicor.Mfg.BO.PaymentEntryDataSet">Payment dataset</param>
   OperationID: SetReadyToCalc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetReadyToCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetReadyToCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetReadyToCalc(requestBody:SetReadyToCalc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetReadyToCalc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/SetReadyToCalc", {
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
         resolve(data as SetReadyToCalc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePrintEditList
   Description: This method is called when the Print Group Edit List is selected
   OperationID: ValidatePrintEditList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePrintEditList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePrintEditList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePrintEditList(requestBody:ValidatePrintEditList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePrintEditList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/ValidatePrintEditList", {
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
         resolve(data as ValidatePrintEditList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDfltTranDocTypeID
   Description: Get Default Transaction document for AP Payments
   OperationID: GetDfltTranDocTypeID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDfltTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDfltTranDocTypeID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDfltTranDocTypeID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetDfltTranDocTypeID", {
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
         resolve(data as GetDfltTranDocTypeID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: Method to call to get a Code Description list.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetCodeDescList", {
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
   Summary: Invoke method ValidateAcctForGLControl
   Description: Validates an account has been entered for glcontrol
   OperationID: ValidateAcctForGLControl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateAcctForGLControl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAcctForGLControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateAcctForGLControl(requestBody:ValidateAcctForGLControl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateAcctForGLControl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/ValidateAcctForGLControl", {
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
         resolve(data as ValidateAcctForGLControl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Change1099Code
   Description: Method to call when changing the 1099 Code on a detail record, displays the correct description.
   OperationID: Change1099Code
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Change1099Code_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Change1099Code_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Change1099Code(requestBody:Change1099Code_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Change1099Code_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/Change1099Code", {
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
         resolve(data as Change1099Code_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method JPSelectPaymentStatements
   Description: Read JPAPPerBillStmtHead records and create APInvSel records if they meet the selection criteria.
   OperationID: JPSelectPaymentStatements
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/JPSelectPaymentStatements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/JPSelectPaymentStatements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JPSelectPaymentStatements(requestBody:JPSelectPaymentStatements_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JPSelectPaymentStatements_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/JPSelectPaymentStatements", {
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
         resolve(data as JPSelectPaymentStatements_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method JPCreateChecks
   Description: Create Vendor Checks for selected invoices.
   OperationID: JPCreateChecks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/JPCreateChecks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/JPCreateChecks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JPCreateChecks(requestBody:JPCreateChecks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JPCreateChecks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/JPCreateChecks", {
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
         resolve(data as JPCreateChecks_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefault1099Code
   Description: Method to call when changing the 1099 Code on a detail record, displays the correct description.
   OperationID: GetDefault1099Code
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefault1099Code_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefault1099Code_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefault1099Code(requestBody:GetDefault1099Code_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefault1099Code_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetDefault1099Code", {
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
         resolve(data as GetDefault1099Code_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFormType
   Description: Call this method when the user enters the ttAPTran.FormTypeID
   OperationID: OnChangeFormType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFormType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFormType(requestBody:OnChangeFormType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFormType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/OnChangeFormType", {
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
         resolve(data as OnChangeFormType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckVendorTaxID
   Description: Supplier Tax Id check
   OperationID: CheckVendorTaxID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckVendorTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckVendorTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckVendorTaxID(requestBody:CheckVendorTaxID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckVendorTaxID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CheckVendorTaxID", {
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
         resolve(data as CheckVendorTaxID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckGroupTaxID
   Description: Check for Vendor TaxId in Payments Group
   OperationID: CheckGroupTaxID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckGroupTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGroupTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckGroupTaxID(requestBody:CheckGroupTaxID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckGroupTaxID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CheckGroupTaxID", {
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
         resolve(data as CheckGroupTaxID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckNegPaymentExist
   Description: Check if Negative Payments exist
   OperationID: CheckNegPaymentExist
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckNegPaymentExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckNegPaymentExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckNegPaymentExist(requestBody:CheckNegPaymentExist_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckNegPaymentExist_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CheckNegPaymentExist", {
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
         resolve(data as CheckNegPaymentExist_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method composeNegPaymentMessage
   Description: compose a Negative Payment message
   OperationID: composeNegPaymentMessage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/composeNegPaymentMessage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/composeNegPaymentMessage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_composeNegPaymentMessage(requestBody:composeNegPaymentMessage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<composeNegPaymentMessage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/composeNegPaymentMessage", {
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
         resolve(data as composeNegPaymentMessage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckAllCheckNumsAssigned
   Description: Checks if there unassigned checknums in the group
   OperationID: CheckAllCheckNumsAssigned
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckAllCheckNumsAssigned_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAllCheckNumsAssigned_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAllCheckNumsAssigned(requestBody:CheckAllCheckNumsAssigned_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckAllCheckNumsAssigned_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/CheckAllCheckNumsAssigned", {
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
         resolve(data as CheckAllCheckNumsAssigned_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCheckHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCheckHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCheckHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCheckHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCheckHed(requestBody:GetNewCheckHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCheckHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetNewCheckHed", {
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
         resolve(data as GetNewCheckHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCheckHedAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCheckHedAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCheckHedAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCheckHedAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCheckHedAttch(requestBody:GetNewCheckHedAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCheckHedAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetNewCheckHedAttch", {
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
         resolve(data as GetNewCheckHedAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPTran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPTran(requestBody:GetNewAPTran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetNewAPTran", {
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
         resolve(data as GetNewAPTran_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPTranTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPTranTGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPTranTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPTranTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPTranTGLC(requestBody:GetNewAPTranTGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPTranTGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetNewAPTranTGLC", {
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
         resolve(data as GetNewAPTranTGLC_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPTTaxDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPTTaxDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPTTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPTTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPTTaxDtl(requestBody:GetNewAPTTaxDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPTTaxDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetNewAPTTaxDtl", {
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
         resolve(data as GetNewAPTTaxDtl_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBankTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankTran(requestBody:GetNewBankTran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBankTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetNewBankTran", {
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
         resolve(data as GetNewBankTran_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBankTranTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankTranTaxDtl(requestBody:GetNewBankTranTaxDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBankTranTaxDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetNewBankTranTaxDtl", {
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
         resolve(data as GetNewBankTranTaxDtl_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBankTranTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankTranTGLC(requestBody:GetNewBankTranTGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBankTranTGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetNewBankTranTGLC", {
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
         resolve(data as GetNewBankTranTGLC_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxDtl(requestBody:GetNewTaxDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTaxDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetNewTaxDtl", {
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
         resolve(data as GetNewTaxDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PaymentEntrySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTTaxDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APTTaxDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APTranRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APTranTGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankTranRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankTranTGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTaxDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankTranTaxDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CheckHedAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CheckHedListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CheckHedRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxDtlRow,
}

export interface Erp_Tablesets_APTTaxDtlRow{
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
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
      /**  Flag to indicate if Manual checkbos should be Read Only  */  
   "DisableManual":boolean,
   "GroupID":string,
      /**  The flag to indicate if the tax record for Invoice Payment could not be updated (Related to Withholding tax posted through Interim account option)  */  
   "DisableManUpdate":boolean,
      /**  The flag to indicate if system-assigned tax record is related to AP Invoice with 'Withholding tax posted to Interim Account' option.  */  
   "WhToInterim":boolean,
   "BitFlag":number,
   "RateCodeDescription":string,
   "SalesTaxDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APTranRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  */  
   "TranType":string,
      /**  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  */  
   "HeadNum":number,
      /**  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  */  
   "APTranNo":number,
      /**  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  */  
   "InvoiceNum":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  */  
   "Posted":boolean,
      /**  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   "TranAmt":number,
      /**  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   "DocTranAmt":number,
      /**  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   "DiscAmt":number,
      /**  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   "DocDiscAmt":number,
      /**  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  */  
   "Description":string,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**  Check number of the related CheckHed.  */  
   "CheckNum":number,
      /**  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  */  
   "TranDate":string,
      /**   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  */  
   "FiscalYear":number,
      /**  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  */  
   "FiscalPeriod":number,
      /**  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  */  
   "GLPosted":boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  */  
   "Voided":boolean,
      /**  UserID that created this APTran record.  */  
   "EntryPerson":string,
      /**  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  */  
   "VendorNum":number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  */  
   "Comment":string,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  Sales Tax Amount.  */  
   "TaxAmt":number,
      /**  Tax Amount in the vendors currency.  */  
   "DocTaxAmt":number,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "RefCodeDesc":string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   "RoundDiff":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  The Legal Number for the record.  */  
   "LegalNumber":string,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  Red Storno Flag  */  
   "RedStorno":boolean,
      /**  Indicates that this is prepayment.  */  
   "PrePayment":boolean,
      /**  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  */  
   "ContractRef":string,
      /**  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  */  
   "ContractRefDate":string,
      /**  Reference Purchase Order Number for Prepayments.  */  
   "RefPONum":number,
      /**  Tax Receipt Date (Thailand Localization)  */  
   "TaxReceiptDate":string,
      /**  Tax Receipt Number (Thailand Localization)  */  
   "TaxReceiptNo":string,
      /**  Withholding Tax Certificate Date (Thailand Localization)  */  
   "WHTCertificateDate":string,
      /**  Withholding Tax Certificate Number (Thailand Localization)  */  
   "WHTCertificateNo":string,
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
      /**  Invoice Balance at the time of revaluation  */  
   "RevalueBal":number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   "DocRevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt1RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt2RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt3RevalueBal":number,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Amount Bank Paid  */  
   "BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "DocBankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt1BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt2BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt3BankPaidAmt":number,
      /**  Legal Number for the adjustment.  */  
   "AdjLegalNumber":string,
      /**  Transaction Document Type for the adjustment.  */  
   "AdjTranDocTypeID":string,
      /**  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Remarks  */  
   "Remarks":string,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Card ID  */  
   "CardID":string,
      /**  Card Holder Tax ID  */  
   "CardHolderTaxID":string,
      /**  Card Member Name  */  
   "CardMemberName":string,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  UrgentPayment  */  
   "UrgentPayment":boolean,
      /**  InvoiceRef  */  
   "InvoiceRef":string,
      /**  Rate Group Code for transactions of type ADJ  */  
   "RateGrpCode":string,
      /**  CNCFICode  */  
   "CNCFICode":string,
      /**  Generation 1099 Date  */  
   "Gen1099Date":string,
      /**  NOTranReason  */  
   "NOTranReason":string,
      /**  PEIsDetractionPayment  */  
   "PEIsDetractionPayment":boolean,
      /**  Code1099ID  */  
   "Code1099ID":string,
      /**  FormTypeID  */  
   "FormTypeID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  DocWhManAddAmt  */  
   "DocWhManAddAmt":number,
      /**  WhManAddAmt  */  
   "WhManAddAmt":number,
      /**  Rpt1WhManAddAmt  */  
   "Rpt1WhManAddAmt":number,
      /**  Rpt2WhManAddAmt  */  
   "Rpt2WhManAddAmt":number,
      /**  Rpt3WhManAddAmt  */  
   "Rpt3WhManAddAmt":number,
   "BaseAdjustAmt":number,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
   "BaseCurrSymbolCurrDesc":string,
   "BaseCurrSymbolCurrName":string,
   "BaseCurrSymbolCurrSymbol":string,
   "BaseCurrSymbolDocumentDesc":string,
   "BaseSelfAssessedTax":number,
      /**  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  */  
   "ChangeExchangeRateResponse":string,
   "CNCFICodeDescription":string,
      /**  If Copy Rate is true then original AP Invoice exchange rates are used when Adjustmet is applied and no currency gain/loss are calculated  */  
   "CopyRate":boolean,
      /**  The flag to indicate if this payment line is realted to Correction invoice with negative amount  */  
   "CorrectionInv":boolean,
      /**  Indicates if the related invoice is linked to a Central Payment invoice  */  
   "CPayLinked":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencyGainLoss":number,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol from APInvHed  */  
   "CurrSymbol":string,
   "CurrSymbolCurrDesc":string,
   "CurrSymbolCurrName":string,
   "CurrSymbolCurrSymbol":string,
   "CurrSymbolDocumentDesc":string,
   "DebitMemo":boolean,
   "DisableFieldsForPCashDoc":boolean,
   "DiscountAvailable":boolean,
   "DiscountDate":string,
      /**  The display gl account.  */  
   "DispGLAcct":string,
   "DispTranAmt":number,
   "DocBaseSelfAssessedTax":number,
   "DocDispTranAmt":number,
   "DocExpenseAmount":number,
   "DocGainLossAmt":number,
   "DocInvoiceAmt":number,
   "DocInvoiceBal":number,
   "DocNetAmount":number,
   "DocNewBalance":number,
   "DocSelfAssessedTax":number,
   "DocUnPostedBal":number,
   "DocWithHoldTax":number,
      /**  If this flag is true then Copy Rate checkbox is Read Only  */  
   "DsblCopyRate":boolean,
   "DueDate":string,
   "ExchangeRate":number,
   "ExpenseAmount":number,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   "FullyPaid":boolean,
   "GainLossAmt":number,
      /**  This is the source Company of the Central Payment linked invoice  */  
   "GlbCompany":string,
   "GroupID":string,
      /**  CSF Switzerland - Initial value for Urgent Invoice Payment flag.  */  
   "InitUrgentPayment":boolean,
   "InvExchangeRate":number,
   "InvoiceAmt":number,
   "InvoiceBal":number,
   "isDiscountforDebitM":boolean,
   "LegalNumMessage":string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   "LegalNumStyle":string,
   "LockRate":boolean,
   "MiscPayment":boolean,
   "NetAmount":number,
   "NewBalance":number,
      /**  This field equals "Invoice" for Invoice payment, and "Misc" for Miscelleneous payment. This field  is used as label in tree.  */  
   "PaymentDesc":string,
      /**  Posting Error Message  */  
   "PostErrMess":string,
      /**  Indicates if posting GL transactions.  */  
   "PostToGL":boolean,
      /**  Print 1099  */  
   "Print1099":boolean,
   "RateGroupDescription":string,
   "RefCodeEnabled":boolean,
      /**  Delimited list of possible Ref codes.  */  
   "RefCodeList":string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   "RefCodeStatus":string,
   "Rpt1DispTranAmt":number,
   "Rpt1GainLossAmt":number,
   "Rpt1InvoiceAmt":number,
      /**  Invoice balance before adjustment in Rpt1 currency  */  
   "Rpt1InvoiceBal":number,
   "Rpt1NewBalance":number,
   "Rpt2DispTranAmt":number,
   "Rpt2GainLossAmt":number,
   "Rpt2InvoiceAmt":number,
      /**  Invoice balance before adjustment in Rpt2 currency  */  
   "Rpt2InvoiceBal":number,
   "Rpt2NewBalance":number,
   "Rpt3DispTranAmt":number,
   "Rpt3GainLossAmt":number,
   "Rpt3InvoiceAmt":number,
      /**  Report balance before adjustment in rpt3 currency  */  
   "Rpt3InvoiceBal":number,
   "Rpt3NewBalance":number,
   "SelfAssessedTax":number,
      /**  Indicates if tax records are created and posted for AP Invoice adjustment  */  
   "TaxableTransaction":boolean,
   "TaxLinesExist":boolean,
   "TermsCode":string,
   "TermsCodeDescription":string,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "UnPostedBal":number,
   "WithHoldTax":number,
   "XRateLabel":string,
   "AmtToAP":number,
   "ApplyDate":string,
   "InvoiceLegalNumber":string,
   "PLInvoiceReference":string,
      /**  The internal flag to indicate if Tax Liability assigned to the invoice being paid has Witholding taxes with Payment timing (WH taxes will be precalculated)  */  
   "isPrecalcTax":boolean,
      /**  The flag to indicate if the invoice being paid (applied)in Payment Entry/Invoice Payment is AP Invoice created for Misc. Payment / Prepayment by the system.  */  
   "PrepayApld":boolean,
      /**  The flag related to Misc. payment to indicate if Tax records created per Tax Liability assigned to Misc. payment are adjusted,  deleted,  or any tax records were added by the user  */  
   "ManualTaxAdj":boolean,
   "BitFlag":number,
   "BankAcctIDBankName":string,
   "BankAcctIDDescription":string,
   "Code1099Description":string,
   "FormTypeDescription":string,
   "InvoiceNumDescription":string,
   "TaxRegionCodeDescription":string,
   "VendorNumState":string,
   "VendorNumCity":string,
   "VendorNumAddress3":string,
   "VendorNumAddress2":string,
   "VendorNumCurrencyCode":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
   "VendorNumName":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCountry":string,
   "VendorNumAddress1":string,
   "VendorNumVendorID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APTranTGLCRow{
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
      /**  GroupID of APTran  */  
   "GroupID":string,
      /**  HeadNum of APTran  */  
   "HeadNum":number,
      /**  InvoiceNum of APTran  */  
   "InvoiceNum":string,
      /**  Voided of APTran  */  
   "Voided":boolean,
      /**  APTranNo of APTran  */  
   "APTranNo":number,
   "BitFlag":number,
   "COADescription":string,
   "GLAccountAccountDesc":string,
   "GLAccountGLAcctDisp":string,
   "GLAccountGLShortAcct":string,
   "GLBookCurrencyCode":string,
   "GLBookDescription":string,
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

export interface Erp_Tablesets_CheckHedAttchRow{
   "Company":string,
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

export interface Erp_Tablesets_CheckHedListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  */  
   "Posted":boolean,
      /**  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  */  
   "CheckNum":number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   "CheckDate":string,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   "FiscalYear":number,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  */  
   "CheckSrc":string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedCheck":boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Amount that the bank cleared the check for.  */  
   "ClearedAmt":number,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Person who cleared the check (System Set).  */  
   "ClearedPerson":string,
      /**  Date that the check was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  End Date of the Statement that the check was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  employee # for payroll checks  */  
   "EmployeeNum":string,
      /**  Check Amount. Base Currency.  */  
   "CheckAmt":number,
      /**  Check Amount. Document Currency.  */  
   "DocCheckAmt":number,
      /**  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  */  
   "ManualPrint":boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   "EntryPerson":string,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   "VendorNum":number,
      /**  Vendors name.  */  
   "Name":string,
      /**  First Address line  */  
   "Address1":string,
      /**  Second Address Line  */  
   "Address2":string,
      /**  Third Address Line  */  
   "Address3":string,
      /**  City portion of address  */  
   "City":string,
      /**  Can be blank.  */  
   "State":string,
      /**  Zip code or Postal code portion of address  */  
   "ZIP":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "Country":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   "BankSlip":string,
      /**  Payment by electronic funds transfer.  Default from the Vendor.  */  
   "ElecPayment":boolean,
      /**  ID of the vendor's bank.  */  
   "VendorBankID":string,
      /**  Supplier Bank Name  */  
   "VendorBankName":string,
      /**  Name on the Bank Account.  */  
   "VendorBankNameOnAccount":string,
      /**  First address line of supplier bank.  */  
   "VendorBankAddress1":string,
      /**  Second address line of supplier bank.  */  
   "VendorBankAddress2":string,
      /**  Third address line of supplier bank.  */  
   "VendorBankAddress3":string,
      /**  City portion of address of supplier bank.  */  
   "VendorBankCity":string,
      /**  Can be blank.  */  
   "VendorBankState":string,
      /**  Postal Code or zip code portion of address of supplier bank.  */  
   "VendorBankPostalCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "VendorBankCountryNum":number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   "VendorBankAcctNumber":string,
      /**  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  */  
   "VendorBankSwiftNum":string,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefCheckNum":string,
      /**  Reporting currency value of this field  */  
   "Rpt1CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Total paid amount in Base  */  
   "PaymentTotal":number,
      /**  Total paid amount in payment currency  */  
   "DocPaymentTotal":number,
      /**  Total paid amount in Rpt1 currency  */  
   "Rpt1PaymentTotal":number,
      /**  Total paid amount in Rpt2 currency  */  
   "Rpt2PaymentTotal":number,
      /**  Total paid amount in Rpt3 currency  */  
   "Rpt3PaymentTotal":number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   "Variance":number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   "DocVariance":number,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt1Variance":number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt2Variance":number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt3Variance":number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   "PaymentBankRate":number,
      /**  Total amount in Bank currency  */  
   "BankTotalAmt":number,
      /**  Total entered flag  */  
   "IsEnterTotal":boolean,
      /**  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  */  
   "LockRate":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  */  
   "UsePendAcct":boolean,
      /**  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  */  
   "ForceDiscount":boolean,
      /**  Reference to first checkhed  */  
   "FirstHeadNum":number,
      /**  Identifies that record is created by 'Apply Debit Memo'.  */  
   "ApplyingPayment":boolean,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**  AP Invoice Number for Apply Debit Memo Process.  */  
   "InvoiceNum":string,
      /**  Payment Method Unique Identifier  */  
   "PMUID":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Amount Bank Paid  */  
   "BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "DocBankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt1BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt2BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt3BankPaidAmt":number,
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  NOPaymentStatus  */  
   "NOPaymentStatus":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  PayLegalNumber  */  
   "PayLegalNumber":string,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  THPayerType  */  
   "THPayerType":number,
   "VoidDate":string,
   "BaseCurrSymbol":string,
      /**  Indicates if payment to a One-Time Vendor  */  
   "OneTimeVendor":boolean,
   "PaymentStatus":string,
   "PaymentAmount":number,
      /**  To be used by UI for entry  */  
   "VendorID":string,
      /**  Enable the Bank Account Search Button  */  
   "BankAccountEnabled":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   "FullyPaid":boolean,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   "TotalRoundDiff":number,
      /**  Bank Currency Code  */  
   "BankCurrCode":string,
      /**  Payment Total can be entered manually  */  
   "EnterPaymentTotal":boolean,
      /**  label <Payment Currency> -> <Bank Currency>  */  
   "XRateLabelPaymentBank":string,
      /**  label <Payment Currency> --> <Base Currency>  */  
   "XRateLabelPaymentBase":string,
   "BankCurrSymbol":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "ExchangeRateDisabled":boolean,
   "BaseExchRate":boolean,
      /**  It is used for Apply Debit Memo Process  */  
   "DocUnappliedAmt":number,
      /**  It is used for Apply Debit Memo Process  */  
   "UnappliedAmt":number,
      /**  It is used for Apply Debit Memo Process  */  
   "Rpt1UnappliedAmt":number,
      /**  It is used for Apply Debit Memo Process  */  
   "Rpt2UnappliedAmt":number,
      /**  It is used for Apply Debit Memo Process  */  
   "Rpt3UnappliedAmt":number,
      /**  It is used for Apply Debit Memo Process  */  
   "InvType":string,
      /**  DocUnpostedBal of Debit Memo or Pre-Payment Invoice.  */  
   "DocUnpostedBal":number,
   "HasLines":boolean,
   "BaseCurrencyCode":string,
   "EnableCurrency":boolean,
   "EnableIsEnterTotal":boolean,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Full description of the bank account.  */  
   "BankAcctIDDescription":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseCurrSymbolDocumentDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrSymbolCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrSymbolCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrSymbolCurrSymbol":string,
      /**  Description of the currency  */  
   "BaseCurrSymbolCurrDesc":string,
      /**  Description  */  
   "CashbookLineDescription":string,
      /**  Country name  */  
   "CountryNumDescription":string,
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
      /**  Country name  */  
   "VendorBankCountryNumDescription":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
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
      /**  CSF Switzerland - Indicate that Check has urgent Invoice payment  */  
   "UrgentCheck":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CheckHedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  */  
   "Posted":boolean,
      /**  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  */  
   "CheckNum":number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   "CheckDate":string,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   "FiscalYear":number,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  */  
   "CheckSrc":string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedCheck":boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Amount that the bank cleared the check for.  */  
   "ClearedAmt":number,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Person who cleared the check (System Set).  */  
   "ClearedPerson":string,
      /**  Date that the check was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  End Date of the Statement that the check was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  employee # for payroll checks  */  
   "EmployeeNum":string,
      /**  Check Amount. Base Currency.  */  
   "CheckAmt":number,
      /**  Check Amount. Document Currency.  */  
   "DocCheckAmt":number,
      /**  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  */  
   "ManualPrint":boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   "EntryPerson":string,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   "VendorNum":number,
      /**  Vendors name.  */  
   "Name":string,
      /**  First Address line  */  
   "Address1":string,
      /**  Second Address Line  */  
   "Address2":string,
      /**  Third Address Line  */  
   "Address3":string,
      /**  City portion of address  */  
   "City":string,
      /**  Can be blank.  */  
   "State":string,
      /**  Zip code or Postal code portion of address  */  
   "ZIP":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "Country":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   "BankSlip":string,
      /**  Payment by electronic funds transfer.  Default from the Vendor.  */  
   "ElecPayment":boolean,
      /**  ID of the vendor's bank.  */  
   "VendorBankID":string,
      /**  Supplier Bank Name  */  
   "VendorBankName":string,
      /**  Name on the Bank Account.  */  
   "VendorBankNameOnAccount":string,
      /**  First address line of supplier bank.  */  
   "VendorBankAddress1":string,
      /**  Second address line of supplier bank.  */  
   "VendorBankAddress2":string,
      /**  Third address line of supplier bank.  */  
   "VendorBankAddress3":string,
      /**  City portion of address of supplier bank.  */  
   "VendorBankCity":string,
      /**  Can be blank.  */  
   "VendorBankState":string,
      /**  Postal Code or zip code portion of address of supplier bank.  */  
   "VendorBankPostalCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "VendorBankCountryNum":number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   "VendorBankAcctNumber":string,
      /**  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  */  
   "VendorBankSwiftNum":string,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefCheckNum":string,
      /**  Reporting currency value of this field  */  
   "Rpt1CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Total paid amount in Base  */  
   "PaymentTotal":number,
      /**  Total paid amount in payment currency  */  
   "DocPaymentTotal":number,
      /**  Total paid amount in Rpt1 currency  */  
   "Rpt1PaymentTotal":number,
      /**  Total paid amount in Rpt2 currency  */  
   "Rpt2PaymentTotal":number,
      /**  Total paid amount in Rpt3 currency  */  
   "Rpt3PaymentTotal":number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   "Variance":number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   "DocVariance":number,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt1Variance":number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt2Variance":number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt3Variance":number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   "PaymentBankRate":number,
      /**  Total amount in Bank currency  */  
   "BankTotalAmt":number,
      /**  Total entered flag  */  
   "IsEnterTotal":boolean,
      /**  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  */  
   "LockRate":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  */  
   "UsePendAcct":boolean,
      /**  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  */  
   "ForceDiscount":boolean,
      /**  Reference to first checkhed  */  
   "FirstHeadNum":number,
      /**  Identifies that record is created by 'Apply Debit Memo'.  */  
   "ApplyingPayment":boolean,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**  AP Invoice Number for Apply Debit Memo Process.  */  
   "InvoiceNum":string,
      /**  Payment Method Unique Identifier  */  
   "PMUID":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Amount Bank Paid  */  
   "BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "DocBankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt1BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt2BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt3BankPaidAmt":number,
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  VendorBankIBANCode  */  
   "VendorBankIBANCode":string,
      /**  OwnReference  */  
   "OwnReference":string,
      /**  NOPaymentStatus  */  
   "NOPaymentStatus":number,
      /**  NOPaymentDirection  */  
   "NOPaymentDirection":string,
      /**  NOPaymentType  */  
   "NOPaymentType":string,
      /**  Norway CSF: The name of created payment file.  */  
   "NOTransferFileName":string,
      /**  Norway CSF: Transaction Reference Number assigned by bank.  */  
   "NOBankTransRef":string,
      /**  BalanceUpdate  */  
   "BalanceUpdate":number,
      /**  BankClearedAmt  */  
   "BankClearedAmt":number,
      /**  BankRecGainLoss  */  
   "BankRecGainLoss":number,
      /**  Bill of Exchange Invoice num this was generated from  */  
   "BOEInvoiceNum":string,
      /**  DocBankRecGainLoss  */  
   "DocBankRecGainLoss":number,
      /**  MsgId  */  
   "MsgId":string,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  PayLegalNumber  */  
   "PayLegalNumber":string,
      /**  PayTranDocTypeID  */  
   "PayTranDocTypeID":string,
      /**  Rpt1BankRecGainLoss  */  
   "Rpt1BankRecGainLoss":number,
      /**  Rpt2BankRecGainLoss  */  
   "Rpt2BankRecGainLoss":number,
      /**  Rpt3BankRecGainLoss  */  
   "Rpt3BankRecGainLoss":number,
      /**  TaxPaymInfo  */  
   "TaxPaymInfo":string,
      /**  VoidLegalNumber  */  
   "VoidLegalNumber":string,
      /**  VoidTranDocTypeID  */  
   "VoidTranDocTypeID":string,
      /**  SEGrpNum  */  
   "SEGrpNum":number,
      /**  SEReference  */  
   "SEReference":string,
      /**  SEISGroupedPO3  */  
   "SEISGroupedPO3":boolean,
      /**  SEISExported  */  
   "SEISExported":boolean,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  MXBankAcctNumber  */  
   "MXBankAcctNumber":string,
      /**  MXBankIdentifier  */  
   "MXBankIdentifier":string,
      /**  MXRFC  */  
   "MXRFC":string,
      /**  Indicates that payment is currently excluded from batch in Bank Statement Processing.  */  
   "BankBatchExcluded":boolean,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  ABTUID  */  
   "ABTUID":string,
      /**  SEPAPaymentDescription  */  
   "SEPAPaymentDescription":string,
      /**  THPayerType  */  
   "THPayerType":number,
      /**  TH Reference Invoice Num  */  
   "THRefInvoiceNum":string,
      /**  TH Reference Vendor Num  */  
   "THRefVendorNum":number,
      /**  Text entered by the user to indicate the reason a Payment  was voided.  */  
   "VoidedReason":string,
      /**  Regulatory Reporting Code  */  
   "RegulatoryReportingCode":string,
      /**  MXFiscalFolio  */  
   "MXFiscalFolio":string,
      /**  Tax Point Date  */  
   "TaxPointDate":string,
      /**  Standard Entry Class Code  */  
   "SEC":string,
      /**  ACH Transaction Code  */  
   "ACHTranCode":number,
      /**  Form 1099-K Merchant Category Code  */  
   "US1099KMerchCatCode":string,
      /**  US1099KGen  */  
   "US1099KGen":boolean,
      /**  Bank Branch Code of the Supplier Bank  */  
   "VendorBankBranchCode":string,
      /**  Id of the netting transaction that generated this document.  */  
   "NettingID":number,
      /**  Description  */  
   "Description":string,
      /**  GL Description for the Payment Voiding process  */  
   "VoidDescription":string,
      /**  GL Description for AP - Apply Debit Memo/Prepayment  */  
   "DMDescription":string,
      /**  CSF Mexico DIOT Transaction Type  */  
   "MXDIOTTranType":string,
      /**  ChildPlant  */  
   "ChildPlant":string,
   "BankBatchIDDsp":string,
      /**  Bank Check Amount  */  
   "BankCheckAmt":number,
      /**  Bank Currency Code  */  
   "BankCurrCode":string,
   "BankCurrSymbol":string,
   "BaseCurrencyCode":string,
   "BaseCurrSymbol":string,
   "BaseExchRate":boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   "DisableBankAmt":boolean,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in document currency.  */  
   "DocPreTaxTotal":number,
      /**  It is used for Apply Debit Memo Process  */  
   "DocUnappliedAmt":number,
      /**  DocUnpostedBal of Debit Memo or Pre-Payment Invoice.  */  
   "DocUnpostedBal":number,
      /**  Withholding taxes calcullated on applying Debit Memo in document currency  */  
   "DocWhldTotal":number,
   "EnableAssignLN":boolean,
   "EnableCurrency":boolean,
   "EnableIsEnterTotal":boolean,
   "EnableTranDocTypeID":boolean,
   "EnableVoidLN":boolean,
      /**  Payment Total can be entered manually  */  
   "EnterPaymentTotal":boolean,
   "ExchangeRateDisabled":boolean,
      /**  If Payment is created from Bank Reconcilation  */  
   "FromBankRec":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   "FullyPaid":boolean,
   "HasLines":boolean,
      /**  It is used for Apply Debit Memo Process  */  
   "InvType":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumberMessage":string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Indicates if the Payment (check) date was chagned by the user.  */  
   "ManualDateChange":boolean,
      /**  Indicates if Exchange rate was manually changed by the user.  */  
   "ManualExRateChange":boolean,
      /**  Indicates if payment to a One-Time Vendor  */  
   "OneTimeVendor":boolean,
   "PaymentAmount":number,
   "PaymentStatus":string,
   "PCReceipt":boolean,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in base currency.  */  
   "PreTaxTotal":number,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt1 currency.  */  
   "Rpt1PreTaxTotal":number,
      /**  It is used for Apply Debit Memo Process  */  
   "Rpt1UnappliedAmt":number,
      /**  Withholding taxes calcullated on applying Debit Memo in Rpt1 currency  */  
   "Rpt1WhldTotal":number,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt2 currency.  */  
   "Rpt2PreTaxTotal":number,
      /**  It is used for Apply Debit Memo Process  */  
   "Rpt2UnappliedAmt":number,
      /**  Withholding taxes calcullated on applying Debit Memo in Rpt2 currency  */  
   "Rpt2WhldTotal":number,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt3 currency  */  
   "Rpt3PreTaxTotal":number,
      /**  It is used for Apply Debit Memo Process  */  
   "Rpt3UnappliedAmt":number,
      /**  Withholding taxes calcullated on applying Debit Memo in Rpt3t currency  */  
   "Rpt3WhldTotal":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "SelectedForAction":boolean,
   "SEPAPaymentDescriptionEnabled":boolean,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   "TotalRoundDiff":number,
      /**  It is used for Apply Debit Memo Process  */  
   "UnappliedAmt":number,
      /**  CSF Switzerland - Indicate that Check has urgent Invoice payment  */  
   "UrgentCheck":boolean,
      /**  To be used by UI for entry  */  
   "VendorID":string,
   "VoidDate":string,
      /**  Withholding taxes calcullated on applying Debit Memo in base currency  */  
   "WhldTotal":number,
      /**  label <Payment Currency> -> <Bank Currency>  */  
   "XRateLabelPaymentBank":string,
      /**  label <Payment Currency> --> <Base Currency>  */  
   "XRateLabelPaymentBase":string,
      /**  Enable the Bank Account Search Button  */  
   "BankAccountEnabled":boolean,
      /**  Full address of Voided Payment  */  
   "FullAddress":string,
      /**  Check Misc Amount. Base Currency.  */  
   "CheckMiscAmt":number,
      /**  Check Misc Amount. Document Currency.  */  
   "DocCheckMiscAmt":number,
      /**  Check Invoice Amount. Document Currency.  */  
   "DocCheckInvAmt":number,
      /**  Check Invoice Amount. Base Currency.  */  
   "CheckInvAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1CheckMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2CheckMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3CheckMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1CheckInvAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2CheckInvAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3CheckInvAmt":number,
   "BitFlag":number,
   "BankAcctIDDescription":string,
   "BankAcctIDBankName":string,
   "BankBranchBankBranchCode":string,
   "BankBranchDescription":string,
   "BaseCurrSymbolCurrDesc":string,
   "BaseCurrSymbolCurrName":string,
   "BaseCurrSymbolCurrSymbol":string,
   "BaseCurrSymbolCurrencyID":string,
   "BaseCurrSymbolDocumentDesc":string,
   "CashbookLineDescription":string,
   "CountryNumDescription":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrName":string,
   "PMUIDName":string,
   "THRefVendorNumName":string,
   "THRefVendorNumVendorID":string,
   "VendorBankCountryNumDescription":string,
   "VendorNumCurrencyCode":string,
   "VendorNumName":string,
   "VendorNumAddress3":string,
   "VendorNumAddress1":string,
   "VendorNumVendorID":string,
   "VendorNumAddress2":string,
   "VendorNumTermsCode":string,
   "VendorNumCountry":string,
   "VendorNumState":string,
   "VendorNumCity":string,
   "VendorNumZIP":string,
   "VendorNumDefaultFOB":string,
   "XbSystSiteIsLegalEntity":boolean,
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
      @param ipHeadNum
      @param ds
   */  
export interface AssignLegalNumber_input{
      /**  Check Head Number  */  
   ipHeadNum:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface AssignLegalNumber_output{
parameters : {
      /**  output parameters  */  
   opLegalNumMsg:string,
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param ipHeadNum
      @param ds
   */  
export interface AssignTHWHTCertNo_input{
      /**  Check Head Number  */  
   ipHeadNum:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface AssignTHWHTCertNo_output{
parameters : {
      /**  output parameters  */  
   opLegalNumMsg:string,
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param cashDeskID
      @param referenceNum
      @param applyDate
      @param exchangeRateDate
   */  
export interface CalcTranAmtExt_input{
   cashDeskID:string,
   referenceNum:number,
   applyDate:string,
   exchangeRateDate:string,
}

export interface CalcTranAmtExt_output{
}

   /** Required : 
      @param ipFormType
      @param proposed1099Code
      @param ds
   */  
export interface Change1099Code_input{
      /**  The proposed 1099 Code  */  
   ipFormType:string,
      /**  The proposed 1099 Code  */  
   proposed1099Code:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface Change1099Code_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
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
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface ChangeTranAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param groupID
   */  
export interface CheckAllCheckNumsAssigned_input{
   groupID:string,
}

export interface CheckAllCheckNumsAssigned_output{
   returnObj:boolean,
}

   /** Required : 
      @param keyValue
   */  
export interface CheckDocumentIsLocked_input{
      /**  HeadNum  */  
   keyValue:string,
}

export interface CheckDocumentIsLocked_output{
}

   /** Required : 
      @param groupID
   */  
export interface CheckDocumentsInGroupLocked_input{
   groupID:string,
}

export interface CheckDocumentsInGroupLocked_output{
}

   /** Required : 
      @param groupID
   */  
export interface CheckGroupTaxID_input{
   groupID:string,
}

export interface CheckGroupTaxID_output{
parameters : {
      /**  output parameters  */  
   errMessage:string,
}
}

   /** Required : 
      @param bNetTotals
      @param currentGroupID
      @param bEFTAllowZeroNet
   */  
export interface CheckNegPaymentExist_input{
   bNetTotals:boolean,
   currentGroupID:string,
   bEFTAllowZeroNet:boolean,
}

export interface CheckNegPaymentExist_output{
   returnObj:boolean,
}

   /** Required : 
      @param vendorID
   */  
export interface CheckVendorTaxID_input{
   vendorID:string,
}

export interface CheckVendorTaxID_output{
parameters : {
      /**  output parameters  */  
   errMessage:string,
}
}

   /** Required : 
      @param pcGroupID
      @param ds
   */  
export interface CreateChecks_input{
      /**  AP Check Group ID  */  
   pcGroupID:string,
   ds:Erp_Tablesets_APInvSelTableset[],
}

export interface CreateChecks_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvSelTableset,
   outLNMsg:string,
   outVBMsg:string,
}
}

   /** Required : 
      @param pcGroupID
      @param ds
   */  
export interface CreateNewCheckHed_input{
      /**  AP Check Group ID  */  
   pcGroupID:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface CreateNewCheckHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param headNum
   */  
export interface DeleteByID_input{
   headNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param pcGroupID
      @param plIncludeZero
   */  
export interface DeleteNegPayments_input{
      /**  AP Check Group ID  */  
   pcGroupID:string,
      /**  Flag to include zero checks when deleting  */  
   plIncludeZero:boolean,
}

export interface DeleteNegPayments_output{
}

export interface Erp_Tablesets_APInvSelAttchRow{
   Company:string,
   Name:string,
   VendorNum:number,
   DueDate:string,
   InvoiceNum:string,
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

export interface Erp_Tablesets_APInvSelRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Logical flag indicating if this record is or is not selected to be written to the check files.  */  
   Selected:boolean,
      /**  Vendors name. Duplicated from the Vendor.Name. Used as part of the index to organize by name order.  */  
   Name:string,
      /**  VendorNum an element of the foreign key that relates this selection record to the Vendor and APInvHed master files. Duplicated from APInvHed.VendorNum. Also used as an element of  the unique file index.  */  
   VendorNum:number,
      /**  Invoice Number. An element of the foreign key  that relates this selection record back to the APInvHed record. Duplicated from the APInvHed.InvoiceNum.  */  
   InvoiceNum:string,
      /**  The Gross Payment that is to be paid against this invoice. When Selected this is set to APInvSel.AmtDue + APInvSel.DiscAvailable as the default.  */  
   GrossPay:number,
      /**  The Gross Payment that is to be paid against this invoice(Vendor Currency). When Selected this is set to APInvSel.AmtDue + APInvSel.DiscAvailable as the default.  */  
   DocGrossPay:number,
      /**  Prompt Payment discount to be taken. When selected this field is set to APInvSel.DiscAvailable as a default.  */  
   DiscAmt:number,
      /**  Prompt Payment discount to be taken(Vendor Currency). When selected this field is set to APInvSel.DiscAvailable as a default.  */  
   DocDiscAmt:number,
      /**  Payment due date of this invoice. Set to APInvHed.DueDate.  */  
   DueDate:string,
      /**  The Net Payment that is to be made against this invoice.  Set as GrossPay - DiscAmt.  */  
   NetPay:number,
      /**  The Net Payment that is to be made against this invoice(Vendor Currency).  Set as GrossPay - DiscAmt.  */  
   DocNetPay:number,
      /**   Total original  invoice Amount.
Duplicated from InvcHead.InvoiceAmt.  */  
   InvoiceAmt:number,
      /**   Total original  invoice Amount(Vendor Currency).
Duplicated from InvcHead.InvoiceAmt.  */  
   DocInvoiceAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative). Duplicated from InvcHead.InvoiceBal.  */  
   InvoiceBal:number,
      /**  Current outstanding balance(Vendor Currency). Carries a true sign. (Credit memos are negative). Duplicated from InvcHead.InvoiceBal.  */  
   DocInvoiceBal:number,
      /**  Current payment amount due. This is calculated as the payment schedule amounts that are due - prior payments.  */  
   AmtDue:number,
      /**  Current payment amount due(Vendor Currency). This is calulate as the payment schedule amounts that are due - prior payments.  */  
   DocAmtDue:number,
      /**  Last date that a payment was made against this invoice. This is set by finding the last APTran for this invoice.  */  
   LastPayDate:string,
      /**  Available Prompt Payment discount. Set during the build selection process. The system can be configured to "Always take discount" or allow the system to determine if discount is only taken when the APInvHed.DiscDate is <= the check date. In either case Discounts are only taken if this is the first payment against this invoice (APInvHed.InvoiceAmt = InvoiceBa). If Discounts are taken then this field is set to APInvHed.DiscAmt.  */  
   DiscAvailable:number,
      /**  Available Prompt Payment discount(Vendor Currency). Set during the build selection process. The system can be configured to "Always take discount" or allow the system to determine if discount is only taken when the APInvHed.DiscDate is <= the check date. In either case Discounts are only taken if this is the first payment against this invoice (APInvHed.InvoiceAmt = InvoiceBa). If Discounts are taken then this field is set to APInvHed.DiscAmt.  */  
   DocDiscAvailable:number,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   DebitMemo:boolean,
      /**  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  Copied from APInvHed.  */  
   DiscountDate:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AmtDue:number,
      /**  Reporting currency value of this field  */  
   Rpt2AmtDue:number,
      /**  Reporting currency value of this field  */  
   Rpt3AmtDue:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscAvailable:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscAvailable:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscAvailable:number,
      /**  Reporting currency value of this field  */  
   Rpt1GrossPay:number,
      /**  Reporting currency value of this field  */  
   Rpt2GrossPay:number,
      /**  Reporting currency value of this field  */  
   Rpt3GrossPay:number,
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
   Rpt1NetPay:number,
      /**  Reporting currency value of this field  */  
   Rpt2NetPay:number,
      /**  Reporting currency value of this field  */  
   Rpt3NetPay:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Prepayment flag  */  
   PrePayment:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PEIsDetractionPayment  */  
   PEIsDetractionPayment:boolean,
      /**  Indicates if the related invoice is linked to a Central Payment invoice  */  
   CPayLinked:boolean,
      /**  Used by UI to highlight the row if discount is available.  */  
   DiscountAvailable:boolean,
   DocNewBalance:number,
      /**  This is the source Company of the Central Payment linked invoice  */  
   GlbCompany:string,
   InvoiceDate:string,
   isDiscountforDebitM:boolean,
      /**  CSF Switzerland - Urgent Payment flag from Invoice.  */  
   IsUrgentPayment:boolean,
   LegalNumber:string,
   NewBalance:number,
      /**  Payment Method Name.  */  
   PayMethod:string,
   Rpt1NewBalance:number,
   Rpt2NewBalance:number,
   Rpt3NewBalance:number,
   TermsCode:string,
      /**  TermsCodeDescription  */  
   TermsCodeDescription:string,
   VendorBankID:string,
   VendorBankName:string,
   JPBillingNumber:string,
   JPProposalDate:string,
   JPSummarizationDate:string,
      /**  Invoice Has Withholdings  */  
   HasWithholdings:boolean,
   SourcePlant:string,
   BitFlag:number,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   VendorNumCurrencyCode:string,
   VendorNumCountry:string,
   VendorNumState:string,
   VendorNumCity:string,
   VendorNumName:string,
   VendorNumVendorID:string,
   VendorNumTermsCode:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
   VendorNumAddress1:string,
   VendorNumZIP:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APInvSelTableset{
   APInvSel:Erp_Tablesets_APInvSelRow[],
   APInvSelAttch:Erp_Tablesets_APInvSelAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APTTaxDtlRow{
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
   CurrencyCode:string,
   CurrencySwitch:boolean,
      /**  Flag to indicate if Manual checkbos should be Read Only  */  
   DisableManual:boolean,
   GroupID:string,
      /**  The flag to indicate if the tax record for Invoice Payment could not be updated (Related to Withholding tax posted through Interim account option)  */  
   DisableManUpdate:boolean,
      /**  The flag to indicate if system-assigned tax record is related to AP Invoice with 'Withholding tax posted to Interim Account' option.  */  
   WhToInterim:boolean,
   BitFlag:number,
   RateCodeDescription:string,
   SalesTaxDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  */  
   TranType:string,
      /**  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  */  
   HeadNum:number,
      /**  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  */  
   APTranNo:number,
      /**  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  */  
   InvoiceNum:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  */  
   Posted:boolean,
      /**  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   TranAmt:number,
      /**  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   DocTranAmt:number,
      /**  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   DiscAmt:number,
      /**  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   DocDiscAmt:number,
      /**  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  */  
   Description:string,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**  Check number of the related CheckHed.  */  
   CheckNum:number,
      /**  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  */  
   TranDate:string,
      /**   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  */  
   FiscalYear:number,
      /**  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  */  
   FiscalPeriod:number,
      /**  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  */  
   GLPosted:boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  */  
   Voided:boolean,
      /**  UserID that created this APTran record.  */  
   EntryPerson:string,
      /**  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  */  
   VendorNum:number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  */  
   Comment:string,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Sales Tax Amount.  */  
   TaxAmt:number,
      /**  Tax Amount in the vendors currency.  */  
   DocTaxAmt:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   RefCodeDesc:string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   RoundDiff:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  The Legal Number for the record.  */  
   LegalNumber:string,
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
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  Red Storno Flag  */  
   RedStorno:boolean,
      /**  Indicates that this is prepayment.  */  
   PrePayment:boolean,
      /**  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  */  
   ContractRef:string,
      /**  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  */  
   ContractRefDate:string,
      /**  Reference Purchase Order Number for Prepayments.  */  
   RefPONum:number,
      /**  Tax Receipt Date (Thailand Localization)  */  
   TaxReceiptDate:string,
      /**  Tax Receipt Number (Thailand Localization)  */  
   TaxReceiptNo:string,
      /**  Withholding Tax Certificate Date (Thailand Localization)  */  
   WHTCertificateDate:string,
      /**  Withholding Tax Certificate Number (Thailand Localization)  */  
   WHTCertificateNo:string,
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
      /**  Invoice Balance at the time of revaluation  */  
   RevalueBal:number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   DocRevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt1RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt2RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt3RevalueBal:number,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Amount Bank Paid  */  
   BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   DocBankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt1BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt2BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt3BankPaidAmt:number,
      /**  Legal Number for the adjustment.  */  
   AdjLegalNumber:string,
      /**  Transaction Document Type for the adjustment.  */  
   AdjTranDocTypeID:string,
      /**  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Remarks  */  
   Remarks:string,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Card ID  */  
   CardID:string,
      /**  Card Holder Tax ID  */  
   CardHolderTaxID:string,
      /**  Card Member Name  */  
   CardMemberName:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  UrgentPayment  */  
   UrgentPayment:boolean,
      /**  InvoiceRef  */  
   InvoiceRef:string,
      /**  Rate Group Code for transactions of type ADJ  */  
   RateGrpCode:string,
      /**  CNCFICode  */  
   CNCFICode:string,
      /**  Generation 1099 Date  */  
   Gen1099Date:string,
      /**  NOTranReason  */  
   NOTranReason:string,
      /**  PEIsDetractionPayment  */  
   PEIsDetractionPayment:boolean,
      /**  Code1099ID  */  
   Code1099ID:string,
      /**  FormTypeID  */  
   FormTypeID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  DocWhManAddAmt  */  
   DocWhManAddAmt:number,
      /**  WhManAddAmt  */  
   WhManAddAmt:number,
      /**  Rpt1WhManAddAmt  */  
   Rpt1WhManAddAmt:number,
      /**  Rpt2WhManAddAmt  */  
   Rpt2WhManAddAmt:number,
      /**  Rpt3WhManAddAmt  */  
   Rpt3WhManAddAmt:number,
   BaseAdjustAmt:number,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
   BaseCurrSymbolCurrDesc:string,
   BaseCurrSymbolCurrName:string,
   BaseCurrSymbolCurrSymbol:string,
   BaseCurrSymbolDocumentDesc:string,
   BaseSelfAssessedTax:number,
      /**  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  */  
   ChangeExchangeRateResponse:string,
   CNCFICodeDescription:string,
      /**  If Copy Rate is true then original AP Invoice exchange rates are used when Adjustmet is applied and no currency gain/loss are calculated  */  
   CopyRate:boolean,
      /**  The flag to indicate if this payment line is realted to Correction invoice with negative amount  */  
   CorrectionInv:boolean,
      /**  Indicates if the related invoice is linked to a Central Payment invoice  */  
   CPayLinked:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencyGainLoss:number,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol from APInvHed  */  
   CurrSymbol:string,
   CurrSymbolCurrDesc:string,
   CurrSymbolCurrName:string,
   CurrSymbolCurrSymbol:string,
   CurrSymbolDocumentDesc:string,
   DebitMemo:boolean,
   DisableFieldsForPCashDoc:boolean,
   DiscountAvailable:boolean,
   DiscountDate:string,
      /**  The display gl account.  */  
   DispGLAcct:string,
   DispTranAmt:number,
   DocBaseSelfAssessedTax:number,
   DocDispTranAmt:number,
   DocExpenseAmount:number,
   DocGainLossAmt:number,
   DocInvoiceAmt:number,
   DocInvoiceBal:number,
   DocNetAmount:number,
   DocNewBalance:number,
   DocSelfAssessedTax:number,
   DocUnPostedBal:number,
   DocWithHoldTax:number,
      /**  If this flag is true then Copy Rate checkbox is Read Only  */  
   DsblCopyRate:boolean,
   DueDate:string,
   ExchangeRate:number,
   ExpenseAmount:number,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   FullyPaid:boolean,
   GainLossAmt:number,
      /**  This is the source Company of the Central Payment linked invoice  */  
   GlbCompany:string,
   GroupID:string,
      /**  CSF Switzerland - Initial value for Urgent Invoice Payment flag.  */  
   InitUrgentPayment:boolean,
   InvExchangeRate:number,
   InvoiceAmt:number,
   InvoiceBal:number,
   isDiscountforDebitM:boolean,
   LegalNumMessage:string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   LegalNumStyle:string,
   LockRate:boolean,
   MiscPayment:boolean,
   NetAmount:number,
   NewBalance:number,
      /**  This field equals "Invoice" for Invoice payment, and "Misc" for Miscelleneous payment. This field  is used as label in tree.  */  
   PaymentDesc:string,
      /**  Posting Error Message  */  
   PostErrMess:string,
      /**  Indicates if posting GL transactions.  */  
   PostToGL:boolean,
      /**  Print 1099  */  
   Print1099:boolean,
   RateGroupDescription:string,
   RefCodeEnabled:boolean,
      /**  Delimited list of possible Ref codes.  */  
   RefCodeList:string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   RefCodeStatus:string,
   Rpt1DispTranAmt:number,
   Rpt1GainLossAmt:number,
   Rpt1InvoiceAmt:number,
      /**  Invoice balance before adjustment in Rpt1 currency  */  
   Rpt1InvoiceBal:number,
   Rpt1NewBalance:number,
   Rpt2DispTranAmt:number,
   Rpt2GainLossAmt:number,
   Rpt2InvoiceAmt:number,
      /**  Invoice balance before adjustment in Rpt2 currency  */  
   Rpt2InvoiceBal:number,
   Rpt2NewBalance:number,
   Rpt3DispTranAmt:number,
   Rpt3GainLossAmt:number,
   Rpt3InvoiceAmt:number,
      /**  Report balance before adjustment in rpt3 currency  */  
   Rpt3InvoiceBal:number,
   Rpt3NewBalance:number,
   SelfAssessedTax:number,
      /**  Indicates if tax records are created and posted for AP Invoice adjustment  */  
   TaxableTransaction:boolean,
   TaxLinesExist:boolean,
   TermsCode:string,
   TermsCodeDescription:string,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnPostedBal:number,
   WithHoldTax:number,
   XRateLabel:string,
   AmtToAP:number,
   ApplyDate:string,
   InvoiceLegalNumber:string,
   PLInvoiceReference:string,
      /**  The internal flag to indicate if Tax Liability assigned to the invoice being paid has Witholding taxes with Payment timing (WH taxes will be precalculated)  */  
   isPrecalcTax:boolean,
      /**  The flag to indicate if the invoice being paid (applied)in Payment Entry/Invoice Payment is AP Invoice created for Misc. Payment / Prepayment by the system.  */  
   PrepayApld:boolean,
      /**  The flag related to Misc. payment to indicate if Tax records created per Tax Liability assigned to Misc. payment are adjusted,  deleted,  or any tax records were added by the user  */  
   ManualTaxAdj:boolean,
   BitFlag:number,
   BankAcctIDBankName:string,
   BankAcctIDDescription:string,
   Code1099Description:string,
   FormTypeDescription:string,
   InvoiceNumDescription:string,
   TaxRegionCodeDescription:string,
   VendorNumState:string,
   VendorNumCity:string,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
   VendorNumCurrencyCode:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorNumName:string,
   VendorNumDefaultFOB:string,
   VendorNumCountry:string,
   VendorNumAddress1:string,
   VendorNumVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APTranTGLCRow{
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
      /**  GroupID of APTran  */  
   GroupID:string,
      /**  HeadNum of APTran  */  
   HeadNum:number,
      /**  InvoiceNum of APTran  */  
   InvoiceNum:string,
      /**  Voided of APTran  */  
   Voided:boolean,
      /**  APTranNo of APTran  */  
   APTranNo:number,
   BitFlag:number,
   COADescription:string,
   GLAccountAccountDesc:string,
   GLAccountGLAcctDisp:string,
   GLAccountGLShortAcct:string,
   GLBookCurrencyCode:string,
   GLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
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

export interface Erp_Tablesets_CheckHedAttchRow{
   Company:string,
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

export interface Erp_Tablesets_CheckHedListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  */  
   Posted:boolean,
      /**  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  */  
   CheckNum:number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   CheckDate:string,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   FiscalYear:number,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Voided flag  */  
   Voided:boolean,
      /**  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  */  
   CheckSrc:string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedCheck:boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Amount that the bank cleared the check for.  */  
   ClearedAmt:number,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Person who cleared the check (System Set).  */  
   ClearedPerson:string,
      /**  Date that the check was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  End Date of the Statement that the check was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  employee # for payroll checks  */  
   EmployeeNum:string,
      /**  Check Amount. Base Currency.  */  
   CheckAmt:number,
      /**  Check Amount. Document Currency.  */  
   DocCheckAmt:number,
      /**  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  */  
   ManualPrint:boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   EntryPerson:string,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   VendorNum:number,
      /**  Vendors name.  */  
   Name:string,
      /**  First Address line  */  
   Address1:string,
      /**  Second Address Line  */  
   Address2:string,
      /**  Third Address Line  */  
   Address3:string,
      /**  City portion of address  */  
   City:string,
      /**  Can be blank.  */  
   State:string,
      /**  Zip code or Postal code portion of address  */  
   ZIP:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   Country:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   BankSlip:string,
      /**  Payment by electronic funds transfer.  Default from the Vendor.  */  
   ElecPayment:boolean,
      /**  ID of the vendor's bank.  */  
   VendorBankID:string,
      /**  Supplier Bank Name  */  
   VendorBankName:string,
      /**  Name on the Bank Account.  */  
   VendorBankNameOnAccount:string,
      /**  First address line of supplier bank.  */  
   VendorBankAddress1:string,
      /**  Second address line of supplier bank.  */  
   VendorBankAddress2:string,
      /**  Third address line of supplier bank.  */  
   VendorBankAddress3:string,
      /**  City portion of address of supplier bank.  */  
   VendorBankCity:string,
      /**  Can be blank.  */  
   VendorBankState:string,
      /**  Postal Code or zip code portion of address of supplier bank.  */  
   VendorBankPostalCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   VendorBankCountryNum:number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   VendorBankAcctNumber:string,
      /**  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  */  
   VendorBankSwiftNum:string,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefCheckNum:string,
      /**  Reporting currency value of this field  */  
   Rpt1CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Total paid amount in Base  */  
   PaymentTotal:number,
      /**  Total paid amount in payment currency  */  
   DocPaymentTotal:number,
      /**  Total paid amount in Rpt1 currency  */  
   Rpt1PaymentTotal:number,
      /**  Total paid amount in Rpt2 currency  */  
   Rpt2PaymentTotal:number,
      /**  Total paid amount in Rpt3 currency  */  
   Rpt3PaymentTotal:number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   Variance:number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   DocVariance:number,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt1Variance:number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt2Variance:number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt3Variance:number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   PaymentBankRate:number,
      /**  Total amount in Bank currency  */  
   BankTotalAmt:number,
      /**  Total entered flag  */  
   IsEnterTotal:boolean,
      /**  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  */  
   LockRate:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  */  
   UsePendAcct:boolean,
      /**  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  */  
   ForceDiscount:boolean,
      /**  Reference to first checkhed  */  
   FirstHeadNum:number,
      /**  Identifies that record is created by 'Apply Debit Memo'.  */  
   ApplyingPayment:boolean,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  AP Invoice Number for Apply Debit Memo Process.  */  
   InvoiceNum:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Amount Bank Paid  */  
   BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   DocBankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt1BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt2BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt3BankPaidAmt:number,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  NOPaymentStatus  */  
   NOPaymentStatus:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  PayLegalNumber  */  
   PayLegalNumber:string,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  THPayerType  */  
   THPayerType:number,
   VoidDate:string,
   BaseCurrSymbol:string,
      /**  Indicates if payment to a One-Time Vendor  */  
   OneTimeVendor:boolean,
   PaymentStatus:string,
   PaymentAmount:number,
      /**  To be used by UI for entry  */  
   VendorID:string,
      /**  Enable the Bank Account Search Button  */  
   BankAccountEnabled:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   FullyPaid:boolean,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   TotalRoundDiff:number,
      /**  Bank Currency Code  */  
   BankCurrCode:string,
      /**  Payment Total can be entered manually  */  
   EnterPaymentTotal:boolean,
      /**  label <Payment Currency> -> <Bank Currency>  */  
   XRateLabelPaymentBank:string,
      /**  label <Payment Currency> --> <Base Currency>  */  
   XRateLabelPaymentBase:string,
   BankCurrSymbol:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   ExchangeRateDisabled:boolean,
   BaseExchRate:boolean,
      /**  It is used for Apply Debit Memo Process  */  
   DocUnappliedAmt:number,
      /**  It is used for Apply Debit Memo Process  */  
   UnappliedAmt:number,
      /**  It is used for Apply Debit Memo Process  */  
   Rpt1UnappliedAmt:number,
      /**  It is used for Apply Debit Memo Process  */  
   Rpt2UnappliedAmt:number,
      /**  It is used for Apply Debit Memo Process  */  
   Rpt3UnappliedAmt:number,
      /**  It is used for Apply Debit Memo Process  */  
   InvType:string,
      /**  DocUnpostedBal of Debit Memo or Pre-Payment Invoice.  */  
   DocUnpostedBal:number,
   HasLines:boolean,
   BaseCurrencyCode:string,
   EnableCurrency:boolean,
   EnableIsEnterTotal:boolean,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Full description of the bank account.  */  
   BankAcctIDDescription:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseCurrSymbolDocumentDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrSymbolCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrSymbolCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrSymbolCurrSymbol:string,
      /**  Description of the currency  */  
   BaseCurrSymbolCurrDesc:string,
      /**  Description  */  
   CashbookLineDescription:string,
      /**  Country name  */  
   CountryNumDescription:string,
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
      /**  Country name  */  
   VendorBankCountryNumDescription:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
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
      /**  CSF Switzerland - Indicate that Check has urgent Invoice payment  */  
   UrgentCheck:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CheckHedListTableset{
   CheckHedList:Erp_Tablesets_CheckHedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CheckHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  */  
   Posted:boolean,
      /**  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  */  
   CheckNum:number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   CheckDate:string,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   FiscalYear:number,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Voided flag  */  
   Voided:boolean,
      /**  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  */  
   CheckSrc:string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedCheck:boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Amount that the bank cleared the check for.  */  
   ClearedAmt:number,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Person who cleared the check (System Set).  */  
   ClearedPerson:string,
      /**  Date that the check was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  End Date of the Statement that the check was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  employee # for payroll checks  */  
   EmployeeNum:string,
      /**  Check Amount. Base Currency.  */  
   CheckAmt:number,
      /**  Check Amount. Document Currency.  */  
   DocCheckAmt:number,
      /**  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  */  
   ManualPrint:boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   EntryPerson:string,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   VendorNum:number,
      /**  Vendors name.  */  
   Name:string,
      /**  First Address line  */  
   Address1:string,
      /**  Second Address Line  */  
   Address2:string,
      /**  Third Address Line  */  
   Address3:string,
      /**  City portion of address  */  
   City:string,
      /**  Can be blank.  */  
   State:string,
      /**  Zip code or Postal code portion of address  */  
   ZIP:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   Country:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   BankSlip:string,
      /**  Payment by electronic funds transfer.  Default from the Vendor.  */  
   ElecPayment:boolean,
      /**  ID of the vendor's bank.  */  
   VendorBankID:string,
      /**  Supplier Bank Name  */  
   VendorBankName:string,
      /**  Name on the Bank Account.  */  
   VendorBankNameOnAccount:string,
      /**  First address line of supplier bank.  */  
   VendorBankAddress1:string,
      /**  Second address line of supplier bank.  */  
   VendorBankAddress2:string,
      /**  Third address line of supplier bank.  */  
   VendorBankAddress3:string,
      /**  City portion of address of supplier bank.  */  
   VendorBankCity:string,
      /**  Can be blank.  */  
   VendorBankState:string,
      /**  Postal Code or zip code portion of address of supplier bank.  */  
   VendorBankPostalCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   VendorBankCountryNum:number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   VendorBankAcctNumber:string,
      /**  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  */  
   VendorBankSwiftNum:string,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefCheckNum:string,
      /**  Reporting currency value of this field  */  
   Rpt1CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Total paid amount in Base  */  
   PaymentTotal:number,
      /**  Total paid amount in payment currency  */  
   DocPaymentTotal:number,
      /**  Total paid amount in Rpt1 currency  */  
   Rpt1PaymentTotal:number,
      /**  Total paid amount in Rpt2 currency  */  
   Rpt2PaymentTotal:number,
      /**  Total paid amount in Rpt3 currency  */  
   Rpt3PaymentTotal:number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   Variance:number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   DocVariance:number,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt1Variance:number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt2Variance:number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt3Variance:number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   PaymentBankRate:number,
      /**  Total amount in Bank currency  */  
   BankTotalAmt:number,
      /**  Total entered flag  */  
   IsEnterTotal:boolean,
      /**  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  */  
   LockRate:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  */  
   UsePendAcct:boolean,
      /**  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  */  
   ForceDiscount:boolean,
      /**  Reference to first checkhed  */  
   FirstHeadNum:number,
      /**  Identifies that record is created by 'Apply Debit Memo'.  */  
   ApplyingPayment:boolean,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  AP Invoice Number for Apply Debit Memo Process.  */  
   InvoiceNum:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Amount Bank Paid  */  
   BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   DocBankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt1BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt2BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt3BankPaidAmt:number,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  VendorBankIBANCode  */  
   VendorBankIBANCode:string,
      /**  OwnReference  */  
   OwnReference:string,
      /**  NOPaymentStatus  */  
   NOPaymentStatus:number,
      /**  NOPaymentDirection  */  
   NOPaymentDirection:string,
      /**  NOPaymentType  */  
   NOPaymentType:string,
      /**  Norway CSF: The name of created payment file.  */  
   NOTransferFileName:string,
      /**  Norway CSF: Transaction Reference Number assigned by bank.  */  
   NOBankTransRef:string,
      /**  BalanceUpdate  */  
   BalanceUpdate:number,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  BankRecGainLoss  */  
   BankRecGainLoss:number,
      /**  Bill of Exchange Invoice num this was generated from  */  
   BOEInvoiceNum:string,
      /**  DocBankRecGainLoss  */  
   DocBankRecGainLoss:number,
      /**  MsgId  */  
   MsgId:string,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  PayLegalNumber  */  
   PayLegalNumber:string,
      /**  PayTranDocTypeID  */  
   PayTranDocTypeID:string,
      /**  Rpt1BankRecGainLoss  */  
   Rpt1BankRecGainLoss:number,
      /**  Rpt2BankRecGainLoss  */  
   Rpt2BankRecGainLoss:number,
      /**  Rpt3BankRecGainLoss  */  
   Rpt3BankRecGainLoss:number,
      /**  TaxPaymInfo  */  
   TaxPaymInfo:string,
      /**  VoidLegalNumber  */  
   VoidLegalNumber:string,
      /**  VoidTranDocTypeID  */  
   VoidTranDocTypeID:string,
      /**  SEGrpNum  */  
   SEGrpNum:number,
      /**  SEReference  */  
   SEReference:string,
      /**  SEISGroupedPO3  */  
   SEISGroupedPO3:boolean,
      /**  SEISExported  */  
   SEISExported:boolean,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  MXBankAcctNumber  */  
   MXBankAcctNumber:string,
      /**  MXBankIdentifier  */  
   MXBankIdentifier:string,
      /**  MXRFC  */  
   MXRFC:string,
      /**  Indicates that payment is currently excluded from batch in Bank Statement Processing.  */  
   BankBatchExcluded:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  ABTUID  */  
   ABTUID:string,
      /**  SEPAPaymentDescription  */  
   SEPAPaymentDescription:string,
      /**  THPayerType  */  
   THPayerType:number,
      /**  TH Reference Invoice Num  */  
   THRefInvoiceNum:string,
      /**  TH Reference Vendor Num  */  
   THRefVendorNum:number,
      /**  Text entered by the user to indicate the reason a Payment  was voided.  */  
   VoidedReason:string,
      /**  Regulatory Reporting Code  */  
   RegulatoryReportingCode:string,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  Tax Point Date  */  
   TaxPointDate:string,
      /**  Standard Entry Class Code  */  
   SEC:string,
      /**  ACH Transaction Code  */  
   ACHTranCode:number,
      /**  Form 1099-K Merchant Category Code  */  
   US1099KMerchCatCode:string,
      /**  US1099KGen  */  
   US1099KGen:boolean,
      /**  Bank Branch Code of the Supplier Bank  */  
   VendorBankBranchCode:string,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  Description  */  
   Description:string,
      /**  GL Description for the Payment Voiding process  */  
   VoidDescription:string,
      /**  GL Description for AP - Apply Debit Memo/Prepayment  */  
   DMDescription:string,
      /**  CSF Mexico DIOT Transaction Type  */  
   MXDIOTTranType:string,
      /**  ChildPlant  */  
   ChildPlant:string,
   BankBatchIDDsp:string,
      /**  Bank Check Amount  */  
   BankCheckAmt:number,
      /**  Bank Currency Code  */  
   BankCurrCode:string,
   BankCurrSymbol:string,
   BaseCurrencyCode:string,
   BaseCurrSymbol:string,
   BaseExchRate:boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   DisableBankAmt:boolean,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in document currency.  */  
   DocPreTaxTotal:number,
      /**  It is used for Apply Debit Memo Process  */  
   DocUnappliedAmt:number,
      /**  DocUnpostedBal of Debit Memo or Pre-Payment Invoice.  */  
   DocUnpostedBal:number,
      /**  Withholding taxes calcullated on applying Debit Memo in document currency  */  
   DocWhldTotal:number,
   EnableAssignLN:boolean,
   EnableCurrency:boolean,
   EnableIsEnterTotal:boolean,
   EnableTranDocTypeID:boolean,
   EnableVoidLN:boolean,
      /**  Payment Total can be entered manually  */  
   EnterPaymentTotal:boolean,
   ExchangeRateDisabled:boolean,
      /**  If Payment is created from Bank Reconcilation  */  
   FromBankRec:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   FullyPaid:boolean,
   HasLines:boolean,
      /**  It is used for Apply Debit Memo Process  */  
   InvType:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumberMessage:string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Indicates if the Payment (check) date was chagned by the user.  */  
   ManualDateChange:boolean,
      /**  Indicates if Exchange rate was manually changed by the user.  */  
   ManualExRateChange:boolean,
      /**  Indicates if payment to a One-Time Vendor  */  
   OneTimeVendor:boolean,
   PaymentAmount:number,
   PaymentStatus:string,
   PCReceipt:boolean,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in base currency.  */  
   PreTaxTotal:number,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt1 currency.  */  
   Rpt1PreTaxTotal:number,
      /**  It is used for Apply Debit Memo Process  */  
   Rpt1UnappliedAmt:number,
      /**  Withholding taxes calcullated on applying Debit Memo in Rpt1 currency  */  
   Rpt1WhldTotal:number,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt2 currency.  */  
   Rpt2PreTaxTotal:number,
      /**  It is used for Apply Debit Memo Process  */  
   Rpt2UnappliedAmt:number,
      /**  Withholding taxes calcullated on applying Debit Memo in Rpt2 currency  */  
   Rpt2WhldTotal:number,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt3 currency  */  
   Rpt3PreTaxTotal:number,
      /**  It is used for Apply Debit Memo Process  */  
   Rpt3UnappliedAmt:number,
      /**  Withholding taxes calcullated on applying Debit Memo in Rpt3t currency  */  
   Rpt3WhldTotal:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   SelectedForAction:boolean,
   SEPAPaymentDescriptionEnabled:boolean,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   TotalRoundDiff:number,
      /**  It is used for Apply Debit Memo Process  */  
   UnappliedAmt:number,
      /**  CSF Switzerland - Indicate that Check has urgent Invoice payment  */  
   UrgentCheck:boolean,
      /**  To be used by UI for entry  */  
   VendorID:string,
   VoidDate:string,
      /**  Withholding taxes calcullated on applying Debit Memo in base currency  */  
   WhldTotal:number,
      /**  label <Payment Currency> -> <Bank Currency>  */  
   XRateLabelPaymentBank:string,
      /**  label <Payment Currency> --> <Base Currency>  */  
   XRateLabelPaymentBase:string,
      /**  Enable the Bank Account Search Button  */  
   BankAccountEnabled:boolean,
      /**  Full address of Voided Payment  */  
   FullAddress:string,
      /**  Check Misc Amount. Base Currency.  */  
   CheckMiscAmt:number,
      /**  Check Misc Amount. Document Currency.  */  
   DocCheckMiscAmt:number,
      /**  Check Invoice Amount. Document Currency.  */  
   DocCheckInvAmt:number,
      /**  Check Invoice Amount. Base Currency.  */  
   CheckInvAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1CheckMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2CheckMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3CheckMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1CheckInvAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2CheckInvAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3CheckInvAmt:number,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   BankBranchBankBranchCode:string,
   BankBranchDescription:string,
   BaseCurrSymbolCurrDesc:string,
   BaseCurrSymbolCurrName:string,
   BaseCurrSymbolCurrSymbol:string,
   BaseCurrSymbolCurrencyID:string,
   BaseCurrSymbolDocumentDesc:string,
   CashbookLineDescription:string,
   CountryNumDescription:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrName:string,
   PMUIDName:string,
   THRefVendorNumName:string,
   THRefVendorNumVendorID:string,
   VendorBankCountryNumDescription:string,
   VendorNumCurrencyCode:string,
   VendorNumName:string,
   VendorNumAddress3:string,
   VendorNumAddress1:string,
   VendorNumVendorID:string,
   VendorNumAddress2:string,
   VendorNumTermsCode:string,
   VendorNumCountry:string,
   VendorNumState:string,
   VendorNumCity:string,
   VendorNumZIP:string,
   VendorNumDefaultFOB:string,
   XbSystSiteIsLegalEntity:boolean,
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

export interface Erp_Tablesets_PaymentEntryTableset{
   CheckHed:Erp_Tablesets_CheckHedRow[],
   CheckHedAttch:Erp_Tablesets_CheckHedAttchRow[],
   APTran:Erp_Tablesets_APTranRow[],
   APTranTGLC:Erp_Tablesets_APTranTGLCRow[],
   APTTaxDtl:Erp_Tablesets_APTTaxDtlRow[],
   BankTran:Erp_Tablesets_BankTranRow[],
   BankTranTaxDtl:Erp_Tablesets_BankTranTaxDtlRow[],
   BankTranTGLC:Erp_Tablesets_BankTranTGLCRow[],
   TaxDtl:Erp_Tablesets_TaxDtlRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
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

export interface Erp_Tablesets_UpdExtPaymentEntryTableset{
   CheckHed:Erp_Tablesets_CheckHedRow[],
   CheckHedAttch:Erp_Tablesets_CheckHedAttchRow[],
   APTran:Erp_Tablesets_APTranRow[],
   APTranTGLC:Erp_Tablesets_APTranTGLCRow[],
   APTTaxDtl:Erp_Tablesets_APTTaxDtlRow[],
   BankTran:Erp_Tablesets_BankTranRow[],
   BankTranTaxDtl:Erp_Tablesets_BankTranTaxDtlRow[],
   BankTranTGLC:Erp_Tablesets_BankTranTGLCRow[],
   TaxDtl:Erp_Tablesets_TaxDtlRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param inAPTranReason
   */  
export interface GetAPTranReasonList_input{
      /**  AP Transaction Reason code to validate  */  
   inAPTranReason:string,
}

export interface GetAPTranReasonList_output{
parameters : {
      /**  output parameters  */  
   opAPTranReasonList:string,
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
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface GetBankFeeDefaultAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param headNum
   */  
export interface GetByID_input{
   headNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PaymentEntryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PaymentEntryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PaymentEntryTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  The table name  */  
   tableName:string,
      /**  The column name.  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface GetDefault1099Code_input{
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface GetDefault1099Code_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

export interface GetDfltTranDocTypeID_output{
      /**  Default Transaction document for AP Payments  */  
   returnObj:string,
}

   /** Required : 
      @param pcGroupID
   */  
export interface GetElecInterface_input{
      /**  AP Check Group ID  */  
   pcGroupID:string,
}

export interface GetElecInterface_output{
parameters : {
      /**  output parameters  */  
   opElecInt:boolean,
}
}

   /** Required : 
      @param inHeadNum
      @param ds
   */  
export interface GetLegalNumberOpts_input{
      /**  The check header number  */  
   inHeadNum:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface GetLegalNumberOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
   requiresUserInput:boolean,
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
   returnObj:Erp_Tablesets_CheckHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
export interface GetNewAPTTaxDtl_input{
   ds:Erp_Tablesets_PaymentEntryTableset[],
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

export interface GetNewAPTTaxDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param ds
      @param headNum
      @param apTranNo
      @param invoiceNum
      @param voided
   */  
export interface GetNewAPTranTGLC_input{
   ds:Erp_Tablesets_PaymentEntryTableset[],
   headNum:number,
   apTranNo:number,
   invoiceNum:string,
   voided:boolean,
}

export interface GetNewAPTranTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param ds
      @param headNum
      @param apTranNo
      @param invoiceNum
   */  
export interface GetNewAPTran_input{
   ds:Erp_Tablesets_PaymentEntryTableset[],
   headNum:number,
   apTranNo:number,
   invoiceNum:string,
}

export interface GetNewAPTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param lvHeadNum
      @param lvBankAcctID
      @param ds
   */  
export interface GetNewBankTranByHeadNum_input{
      /**  Headnum  */  
   lvHeadNum:number,
      /**  Bank Account ID  */  
   lvBankAcctID:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface GetNewBankTranByHeadNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param tranNum
      @param voided
   */  
export interface GetNewBankTranTGLC_input{
   ds:Erp_Tablesets_PaymentEntryTableset[],
   bankAcctID:string,
   tranNum:number,
   voided:boolean,
}

export interface GetNewBankTranTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
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
   ds:Erp_Tablesets_PaymentEntryTableset[],
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
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param tranNum
   */  
export interface GetNewBankTran_input{
   ds:Erp_Tablesets_PaymentEntryTableset[],
   bankAcctID:string,
   tranNum:number,
}

export interface GetNewBankTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param ds
      @param headNum
   */  
export interface GetNewCheckHedAttch_input{
   ds:Erp_Tablesets_PaymentEntryTableset[],
   headNum:number,
}

export interface GetNewCheckHedAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCheckHed_input{
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface GetNewCheckHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param piHeadNum
      @param ds
   */  
export interface GetNewMiscPayment_input{
      /**  value of CheckHed.HeadNum  */  
   piHeadNum:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface GetNewMiscPayment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
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
   ds:Erp_Tablesets_PaymentEntryTableset[],
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
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param headNum
      @param maxNumOfCards
   */  
export interface GetPaymentRelationshipMap_input{
   headNum:number,
   maxNumOfCards:number,
}

export interface GetPaymentRelationshipMap_output{
   returnObj:string,
}

   /** Required : 
      @param inRegulatoryRptCode
   */  
export interface GetRegulatoryReportingCodeList_input{
      /**  Regulatory Reporting code to validate  */  
   inRegulatoryRptCode:string,
}

export interface GetRegulatoryReportingCodeList_output{
parameters : {
      /**  output parameters  */  
   opRegulatoryRptCodeList:string,
}
}

   /** Required : 
      @param groupID
   */  
export interface GetRestartProcessPayment_input{
      /**  GroupID  */  
   groupID:string,
}

export interface GetRestartProcessPayment_output{
parameters : {
      /**  output parameters  */  
   restartProcessPayment:boolean,
}
}

   /** Required : 
      @param whereClauseCheckHed
      @param whereClauseCheckHedAttch
      @param whereClauseAPTran
      @param whereClauseAPTranTGLC
      @param whereClauseAPTTaxDtl
      @param whereClauseBankTran
      @param whereClauseBankTranTaxDtl
      @param whereClauseBankTranTGLC
      @param whereClauseTaxDtl
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCheckHed:string,
   whereClauseCheckHedAttch:string,
   whereClauseAPTran:string,
   whereClauseAPTranTGLC:string,
   whereClauseAPTTaxDtl:string,
   whereClauseBankTran:string,
   whereClauseBankTranTaxDtl:string,
   whereClauseBankTranTGLC:string,
   whereClauseTaxDtl:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PaymentEntryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetTHWHTCertNoGenerationType_output{
parameters : {
      /**  output parameters  */  
   generationType:string,
}
}

   /** Required : 
      @param ipHeadNum
      @param ds
   */  
export interface GetTHWHTCertNoOpts_input{
      /**  Check Head Number  */  
   ipHeadNum:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface GetTHWHTCertNoOpts_output{
parameters : {
      /**  output parameters  */  
   requiresUserInput:boolean,
   ds:Erp_Tablesets_PaymentEntryTableset,
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
      @param ipGroupID
      @param ds
   */  
export interface JPCreateChecks_input{
      /**  AP Check Group ID  */  
   ipGroupID:string,
   ds:Erp_Tablesets_APInvSelTableset[],
}

export interface JPCreateChecks_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvSelTableset,
   outLNMsg:string,
   outVBMsg:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipDueDateFrom
      @param ipDueDateTo
      @param ipSupplierList
      @param ipSupplierIDList
   */  
export interface JPSelectPaymentStatements_input{
      /**  Group ID  */  
   ipGroupID:string,
      /**  From Due date  */  
   ipDueDateFrom:string,
      /**  To Due date  */  
   ipDueDateTo:string,
      /**  Select invoices for the supplier list.  */  
   ipSupplierList:string,
      /**  Select invoices for the supplier ID list.  */  
   ipSupplierIDList:string,
}

export interface JPSelectPaymentStatements_output{
   returnObj:Erp_Tablesets_APInvSelTableset[],
}

   /** Required : 
      @param payMethodID
   */  
export interface MXCheckPaymentIsCheque_input{
      /**  payMethodID  */  
   payMethodID:number,
}

export interface MXCheckPaymentIsCheque_output{
   returnObj:boolean,
}

   /** Required : 
      @param pcGroupID
   */  
export interface MassDelete_input{
      /**  AP Check Group ID  */  
   pcGroupID:string,
}

export interface MassDelete_output{
}

   /** Required : 
      @param pcBankFeeID
      @param ds
   */  
export interface OnChangeBankFeeID_input{
   pcBankFeeID:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeBankFeeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param pBankTotalAmt
      @param pFirstTest
      @param ds
   */  
export interface OnChangeBankTotalAmt_input{
      /**  Propopsed Bank Total Amount  */  
   pBankTotalAmt:number,
      /**  First Run  */  
   pFirstTest:boolean,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeBankTotalAmt_output{
parameters : {
      /**  output parameters  */  
   pQuestion:string,
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param pdtCheckDate
      @param ds
   */  
export interface OnChangeCheckDate_input{
      /**  Propopsed CheckDate  */  
   pdtCheckDate:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeCheckDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param piCheckNum
      @param ds
   */  
export interface OnChangeCheckNum_input{
      /**  Propopsed check num  */  
   piCheckNum:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeCheckNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param pCurrencyCode
      @param ds
   */  
export interface OnChangeCurrency_input{
      /**  Propopsed Currency  */  
   pCurrencyCode:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeCurrency_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param plCurrencySwitch
      @param pdDedTax
      @param taxtbl
      @param ds
   */  
export interface OnChangeDedTaxAmount_input{
      /**  Currency switch  */  
   plCurrencySwitch:boolean,
      /**  Proposed taxable amount value  */  
   pdDedTax:number,
      /**  Tax temp-table name  */  
   taxtbl:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeDedTaxAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param pdDocDiscAmt
      @param ds
   */  
export interface OnChangeDocDiscAmt_input{
      /**  Proposed Document Amount value  */  
   pdDocDiscAmt:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeDocDiscAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param pDocPaymentTotal
      @param ds
   */  
export interface OnChangeDocPaymentTotal_input{
      /**  Propopsed DocPaymentTotal  */  
   pDocPaymentTotal:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeDocPaymentTotal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param pdDocTranAmt
      @param ds
   */  
export interface OnChangeDocTranAmt_input{
      /**  Proposed Document Amount value  */  
   pdDocTranAmt:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeDocTranAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param pExchangeRate
      @param ds
   */  
export interface OnChangeExchangeRate_input{
      /**  Propopsed ExchangeRate - Check Document currency - Base Currency  */  
   pExchangeRate:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeExchangeRate_output{
parameters : {
      /**  output parameters  */  
   pQuestion:string,
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param plCurrencySwitch
      @param pdFixed
      @param taxtbl
      @param ds
   */  
export interface OnChangeFixedAmount_input{
      /**  Currency switch  */  
   plCurrencySwitch:boolean,
      /**  Proposed taxable amount value  */  
   pdFixed:number,
      /**  Tax temp-table name  */  
   taxtbl:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeFixedAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param ipFormType
      @param ds
   */  
export interface OnChangeFormType_input{
      /**  1099 Form Type  */  
   ipFormType:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeFormType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param pdDocGrossPay
      @param pdDocDiscAmt
      @param pcRowIdent
      @param ds
   */  
export interface OnChangeInvSelPayment_input{
      /**  Proposeed Document Gross Payment value  */  
   pdDocGrossPay:number,
      /**  Proposeed Disc. Taken value.  Not applicable in Debit Memos  */  
   pdDocDiscAmt:number,
      /**  Pass ttAPInvSel.RowIdent value here to uniquely identify the record to change.  */  
   pcRowIdent:string,
   ds:Erp_Tablesets_APInvSelTableset[],
}

export interface OnChangeInvSelPayment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvSelTableset,
}
}

   /** Required : 
      @param pcInvoiceNum
      @param pcChangeExchangeRateResponse
      @param ds
   */  
export interface OnChangeInvoiceNum_input{
      /**  Invoice Num  */  
   pcInvoiceNum:string,
      /**  Response to the question pcChangeExchangeRateResponse. ? means question has not been asked.  Yes/No is considered a response.  */  
   pcChangeExchangeRateResponse:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
   pcQuestion:string,
}
}

   /** Required : 
      @param pIsEnterTotal
      @param pFirstTest
      @param pOrigLockRate
      @param pOrigExchangeRate
      @param pOrigPaymentBankRate
      @param pOrigBankTotalAmt
      @param ds
   */  
export interface OnChangeIsEnterTotal_input{
      /**  Propopsed IsEnterTotal  */  
   pIsEnterTotal:boolean,
      /**  First Run  */  
   pFirstTest:boolean,
      /**  Original Value of LockRate  */  
   pOrigLockRate:number,
      /**  Original Value of ExchangeRate  */  
   pOrigExchangeRate:number,
      /**  Original Value of PaymentBankRate  */  
   pOrigPaymentBankRate:number,
      /**  Original Value of BankTotalAmt  */  
   pOrigBankTotalAmt:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeIsEnterTotal_output{
parameters : {
      /**  output parameters  */  
   pQuestion:string,
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param plManualPrint
      @param ds
   */  
export interface OnChangeManualPrint_input{
      /**  Manual Print  */  
   plManualPrint:boolean,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeManualPrint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param pPaymentBankRate
      @param pFirstTest
      @param ds
   */  
export interface OnChangePaymentBankRate_input{
      /**  Propopsed Rate  */  
   pPaymentBankRate:number,
      /**  First Run  */  
   pFirstTest:boolean,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangePaymentBankRate_output{
parameters : {
      /**  output parameters  */  
   pQuestion:string,
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangePrePayment_input{
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangePrePayment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param rateCode
      @param taxtbl
      @param ds
   */  
export interface OnChangeRateCode_input{
      /**  Proposed RateCode value  */  
   rateCode:string,
      /**  Tax temp-table name  */  
   taxtbl:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeRateCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param piRefPONum
      @param ds
   */  
export interface OnChangeRefPONum_input{
      /**  Reference Purchase Order Number  */  
   piRefPONum:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeRefPONum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param apInvoiceNum
      @param ds
   */  
export interface OnChangeTHRefInvoiceNum_input{
      /**  Selected Invoice Number  */  
   apInvoiceNum:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeTHRefInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param vendorID
      @param ds
   */  
export interface OnChangeTHRefVendorID_input{
      /**  Selected Vendor ID  */  
   vendorID:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeTHRefVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param plCurrencySwitch
      @param pdTaxAmt
      @param taxtbl
      @param ds
   */  
export interface OnChangeTaxAmt_input{
      /**  Currency switch  */  
   plCurrencySwitch:boolean,
      /**  Proposed taxable amount value  */  
   pdTaxAmt:number,
      /**  Tax temp-table name  */  
   taxtbl:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeTaxAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param pcTaxCode
      @param taxtbl
      @param ds
   */  
export interface OnChangeTaxCode_input{
      /**  Proposed Tax ID  */  
   pcTaxCode:string,
      /**  Tax temp-table name  */  
   taxtbl:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeTaxCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param plCurrencySwitch
      @param pdPercent
      @param taxtbl
      @param ds
   */  
export interface OnChangeTaxPercent_input{
      /**  Currency switch  */  
   plCurrencySwitch:boolean,
      /**  Proposed taxable amount value  */  
   pdPercent:number,
      /**  Tax temp-table name  */  
   taxtbl:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeTaxPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param plCurrencySwitch
      @param pdTaxableAmt
      @param taxtbl
      @param ds
   */  
export interface OnChangeTaxableAmt_input{
      /**  Currency switch  */  
   plCurrencySwitch:boolean,
      /**  Proposed taxable amount value  */  
   pdTaxableAmt:number,
      /**  Tax temp-table name  */  
   taxtbl:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeTaxableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param vendorBankBranchCode
      @param ds
   */  
export interface OnChangeVendorBankBranchCode_input{
      /**  The proposed Bank Branch code  */  
   vendorBankBranchCode:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeVendorBankBranchCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param pcVendorID
      @param ds
   */  
export interface OnChangeVendor_input{
      /**  Vendor ID - character code for Vendor  */  
   pcVendorID:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface OnChangeVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param pcGroupID
   */  
export interface PostAllowed_input{
      /**  AP Check Group ID  */  
   pcGroupID:string,
}

export interface PostAllowed_output{
parameters : {
      /**  output parameters  */  
   allowed:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ds
   */  
export interface RefreshBankInfo_input{
      /**  AP Check Group ID  */  
   ipGroupID:string,
      /**  Check Head Number  */  
   ipHeadNum:number,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface RefreshBankInfo_output{
}

   /** Required : 
      @param pcGroupID
   */  
export interface ResetProcessPayment_input{
      /**  AP Check Group ID  */  
   pcGroupID:string,
}

export interface ResetProcessPayment_output{
   returnObj:Erp_Tablesets_PaymentEntryTableset[],
parameters : {
      /**  output parameters  */  
   isSomeReseted:boolean,
}
}

   /** Required : 
      @param pcGroupID
      @param pcPayableAccountsList
      @param pdtDueDate
      @param plConsiderDiscountDate
      @param pdtInvoicePM
      @param pdtInvoiceLC
      @param plOnlyDetractions
      @param pcSiteList
      @param pcSupplierList
      @param pcPaymentMethod
      @param pcCurrencyList
      @param pcSupplierIDList
      @param plFutureDebitMemos
      @param plIncludeUrgentInvoice
      @param plExcludeZeroDsc
      @param pdtDiscountHorizon
   */  
export interface SelectInvoicesMS_input{
      /**  AP Check Group ID  */  
   pcGroupID:string,
      /**  Delimited list of Payable Accounts  */  
   pcPayableAccountsList:string,
      /**  Select invoices due by this date.  */  
   pdtDueDate:string,
      /**  Consider discount date for invoice selection  */  
   plConsiderDiscountDate:boolean,
      /**  Select invoices without Payment Method.  */  
   pdtInvoicePM:boolean,
      /**  Select invoices with Letter of Credit.  */  
   pdtInvoiceLC:boolean,
      /**  Select only invoice with Detractions.  */  
   plOnlyDetractions:boolean,
      /**  Sites list for the selection  */  
   pcSiteList:string,
      /**  Select invoices for the supplier list.  */  
   pcSupplierList:string,
      /**  Select payment methods for the specific.  */  
   pcPaymentMethod:string,
      /**  Select invoices for the currency list.  */  
   pcCurrencyList:string,
      /**  Select invoices for the supplier ID list.  */  
   pcSupplierIDList:string,
      /**  Select with future due Debit Memos.  */  
   plFutureDebitMemos:boolean,
      /**  Select invoices with Urgent Payment flag.  */  
   plIncludeUrgentInvoice:boolean,
      /**  Exclude Invoices with Zero Discount  */  
   plExcludeZeroDsc:boolean,
      /**  If consider Discount Dates is true select invoices due by this date.  */  
   pdtDiscountHorizon:string,
}

export interface SelectInvoicesMS_output{
   returnObj:Erp_Tablesets_APInvSelTableset[],
}

   /** Required : 
      @param pcGroupID
      @param pcPayableAccountsList
      @param pdtDueDate
      @param plConsiderDiscountDate
      @param pdtInvoicePM
      @param pdtInvoiceLC
      @param plOnlyDetractions
      @param pcSupplierList
      @param pcPaymentMethod
      @param pcCurrencyList
      @param pcSupplierIDList
      @param plFutureDebitMemos
      @param plIncludeUrgentInvoice
      @param plExcludeZeroDsc
      @param pdtDiscountHorizon
   */  
export interface SelectInvoices_input{
      /**  AP Check Group ID  */  
   pcGroupID:string,
      /**  Delimited list of Payable Accounts  */  
   pcPayableAccountsList:string,
      /**  Select invoices due by this date.  */  
   pdtDueDate:string,
      /**  Consider discount date for invoice selection  */  
   plConsiderDiscountDate:boolean,
      /**  Select invoices without Payment Method.  */  
   pdtInvoicePM:boolean,
      /**  Select invoices with Letter of Credit.  */  
   pdtInvoiceLC:boolean,
      /**  Select only invoice with Detractions.  */  
   plOnlyDetractions:boolean,
      /**  Select invoices for the supplier list.  */  
   pcSupplierList:string,
      /**  Select payment methods for the specific.  */  
   pcPaymentMethod:string,
      /**  Select invoices for the currency list.  */  
   pcCurrencyList:string,
      /**  Select invoices for the supplier ID list.  */  
   pcSupplierIDList:string,
      /**  Select with future due Debit Memos.  */  
   plFutureDebitMemos:boolean,
      /**  Select invoices with Urgent Payment flag.  */  
   plIncludeUrgentInvoice:boolean,
      /**  Exclude Invoices with Zero Discount  */  
   plExcludeZeroDsc:boolean,
      /**  If consider Discount Dates is true select invoices due by this date.  */  
   pdtDiscountHorizon:string,
}

export interface SelectInvoices_output{
   returnObj:Erp_Tablesets_APInvSelTableset[],
}

   /** Required : 
      @param ipGroup
   */  
export interface SetCompleted_input{
      /**  AP Check Group ID  */  
   ipGroup:string,
}

export interface SetCompleted_output{
   returnObj:Erp_Tablesets_PaymentEntryTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ipAPTranNo
      @param ipBankAcctID
      @param ipTranNum
      @param ipVoided
      @param ipCalcAll
      @param ds
   */  
export interface SetReadyToCalc_input{
   ipGroupID:string,
   ipHeadNum:number,
   ipAPTranNo:number,
   ipBankAcctID:string,
   ipTranNum:number,
   ipVoided:boolean,
   ipCalcAll:boolean,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface SetReadyToCalc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param ipGroup
   */  
export interface SetTransmitted_input{
      /**  AP Check Group ID  */  
   ipGroup:string,
}

export interface SetTransmitted_output{
   returnObj:Erp_Tablesets_PaymentEntryTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPaymentEntryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPaymentEntryTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param ipHeadNum
   */  
export interface ValidateAcctForGLControl_input{
      /**  Check Head Number  */  
   ipHeadNum:number,
}

export interface ValidateAcctForGLControl_output{
parameters : {
      /**  output parameters  */  
   outMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
   */  
export interface ValidatePrintEditList_input{
      /**  Group ID  */  
   ipGroupID:string,
      /**  Head Num  */  
   ipHeadNum:number,
}

export interface ValidatePrintEditList_output{
parameters : {
      /**  output parameters  */  
   opWarningWithhold:string,
}
}

   /** Required : 
      @param groupID
   */  
export interface ValidateTHWHTCertNoAssigned_input{
      /**  Group ID  */  
   groupID:string,
}

export interface ValidateTHWHTCertNoAssigned_output{
}

   /** Required : 
      @param groupID
   */  
export interface VerifyBatchID_input{
   groupID:string,
}

export interface VerifyBatchID_output{
parameters : {
      /**  output parameters  */  
   state:number,
   firstBankBatchSysRowID:string,
   calculatedGroupBatchID:string,
}
}

   /** Required : 
      @param headnum
      @param voidReason
   */  
export interface VoidLegalNumber_input{
   headnum:number,
   voidReason:string,
}

export interface VoidLegalNumber_output{
   returnObj:Erp_Tablesets_PaymentEntryTableset[],
}

   /** Required : 
      @param whtCertificateNumToVoid
      @param voidedReason
   */  
export interface VoidSingleWHTCertificateNum_input{
      /**  WHT Certificate Num to void  */  
   whtCertificateNumToVoid:string,
      /**  Void Reason  */  
   voidedReason:string,
}

export interface VoidSingleWHTCertificateNum_output{
      /**  True if voiding completed; False if voiding failed  */  
   returnObj:boolean,
}

   /** Required : 
      @param ipHeadNum
      @param ipVoidedReason
      @param ds
   */  
export interface VoidTHWHTCertNo_input{
      /**  Check Head Number  */  
   ipHeadNum:number,
      /**  Reason for the void  */  
   ipVoidedReason:string,
   ds:Erp_Tablesets_PaymentEntryTableset[],
}

export interface VoidTHWHTCertNo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PaymentEntryTableset,
}
}

   /** Required : 
      @param messageID
      @param maxNames
      @param bNetTotals
      @param currentGroupID
      @param bEFTAllowZeroNet
   */  
export interface composeNegPaymentMessage_input{
   messageID:string,
   maxNames:number,
   bNetTotals:boolean,
   currentGroupID:string,
   bEFTAllowZeroNet:boolean,
}

export interface composeNegPaymentMessage_output{
parameters : {
      /**  output parameters  */  
   negPaymentMessage:string,
}
}

