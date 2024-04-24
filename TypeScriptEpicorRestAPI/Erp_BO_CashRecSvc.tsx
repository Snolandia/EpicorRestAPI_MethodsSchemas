import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CashRecSvc
// Description: bo/CashRec/CashRec.p
           Cash Receipt Entry
           Jennifer Johnson
           01/22/04
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/$metadata", {
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
   Description: Get CashRecs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashRecs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadRow
   */  
export function get_CashRecs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashRecs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashRecs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashRec item
   Description: Calls GetByID to retrieve the CashRec item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashRec
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   */  
export function get_CashRecs_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashRec for the service
   Description: Calls UpdateExt to update CashRec. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashRec
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashRecs_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete CashRec item
   Description: Call UpdateExt to delete CashRec item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashRec
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashRecs_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
export function get_CashRecs_Company_GroupID_HeadNum_BankTrans(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")/BankTrans", {
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
export function get_CashRecs_Company_GroupID_HeadNum_BankTrans_Company_BankAcctID_TranNum_Voided(Company:string, GroupID:string, HeadNum:string, BankAcctID:string, TranNum:string, Voided:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
   Description: Get DebNotes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DebNotes1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DebNoteRow
   */  
export function get_CashRecs_Company_GroupID_HeadNum_DebNotes(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DebNoteRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")/DebNotes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DebNoteRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DebNote item
   Description: Calls GetByID to retrieve the DebNote item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DebNote1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DebitNoteID Desc: DebitNoteID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DebNoteRow
   */  
export function get_CashRecs_Company_GroupID_HeadNum_DebNotes_Company_DebitNoteID(Company:string, GroupID:string, HeadNum:string, DebitNoteID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DebNoteRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")/DebNotes(" + Company + "," + DebitNoteID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DebNoteRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CashDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashDtls1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlRow
   */  
export function get_CashRecs_Company_GroupID_HeadNum_CashDtls(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")/CashDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashDtl item
   Description: Calls GetByID to retrieve the CashDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   */  
export function get_CashRecs_Company_GroupID_HeadNum_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashDtlRow)
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
export function get_CashRecs_Company_GroupID_HeadNum_TaxDtls(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")/TaxDtls", {
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
export function get_CashRecs_Company_GroupID_HeadNum_TaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, GroupID:string, HeadNum:string, SourceModule:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get CashHeadTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashHeadTGLCs1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadTGLCRow
   */  
export function get_CashRecs_Company_GroupID_HeadNum_CashHeadTGLCs(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")/CashHeadTGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashHeadTGLC item
   Description: Calls GetByID to retrieve the CashHeadTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashHeadTGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashHeadTGLCRow
   */  
export function get_CashRecs_Company_GroupID_HeadNum_CashHeadTGLCs_SysRowID(Company:string, GroupID:string, HeadNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashHeadTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")/CashHeadTGLCs(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashHeadTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CashHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashHeadAttches1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadAttchRow
   */  
export function get_CashRecs_Company_GroupID_HeadNum_CashHeadAttches(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")/CashHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashHeadAttch item
   Description: Calls GetByID to retrieve the CashHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashHeadAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashHeadAttchRow
   */  
export function get_CashRecs_Company_GroupID_HeadNum_CashHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company:string, GroupID:string, HeadNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecs(" + Company + "," + GroupID + "," + HeadNum + ")/CashHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashHeadAttchRow)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTrans", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTrans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTranTaxDtls", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTranTaxDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTranTGLCs", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTranTGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
   Description: Get DebNotes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DebNotes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DebNoteRow
   */  
export function get_DebNotes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DebNoteRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DebNotes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DebNoteRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DebNotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DebNoteRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DebNoteRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DebNotes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DebNotes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DebNote item
   Description: Calls GetByID to retrieve the DebNote item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DebNote
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DebitNoteID Desc: DebitNoteID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DebNoteRow
   */  
export function get_DebNotes_Company_DebitNoteID(Company:string, DebitNoteID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DebNoteRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DebNotes(" + Company + "," + DebitNoteID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DebNoteRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DebNote for the service
   Description: Calls UpdateExt to update DebNote. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DebNote
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DebitNoteID Desc: DebitNoteID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DebNoteRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DebNotes_Company_DebitNoteID(Company:string, DebitNoteID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DebNotes(" + Company + "," + DebitNoteID + ")", {
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
   Summary: Call UpdateExt to delete DebNote item
   Description: Call UpdateExt to delete DebNote item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DebNote
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DebitNoteID Desc: DebitNoteID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DebNotes_Company_DebitNoteID(Company:string, DebitNoteID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DebNotes(" + Company + "," + DebitNoteID + ")", {
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
   Description: Get DebNoteAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DebNoteAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DebitNoteID Desc: DebitNoteID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DebNoteAttchRow
   */  
export function get_DebNotes_Company_DebitNoteID_DebNoteAttches(Company:string, DebitNoteID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DebNoteAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DebNotes(" + Company + "," + DebitNoteID + ")/DebNoteAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DebNoteAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DebNoteAttch item
   Description: Calls GetByID to retrieve the DebNoteAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DebNoteAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DebitNoteID Desc: DebitNoteID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DebNoteAttchRow
   */  
export function get_DebNotes_Company_DebitNoteID_DebNoteAttches_Company_DebitNoteID_DrawingSeq(Company:string, DebitNoteID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DebNoteAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DebNotes(" + Company + "," + DebitNoteID + ")/DebNoteAttches(" + Company + "," + DebitNoteID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DebNoteAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DebNoteAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DebNoteAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DebNoteAttchRow
   */  
export function get_DebNoteAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DebNoteAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DebNoteAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DebNoteAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DebNoteAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DebNoteAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DebNoteAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DebNoteAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DebNoteAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DebNoteAttch item
   Description: Calls GetByID to retrieve the DebNoteAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DebNoteAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DebitNoteID Desc: DebitNoteID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DebNoteAttchRow
   */  
export function get_DebNoteAttches_Company_DebitNoteID_DrawingSeq(Company:string, DebitNoteID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DebNoteAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DebNoteAttches(" + Company + "," + DebitNoteID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DebNoteAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DebNoteAttch for the service
   Description: Calls UpdateExt to update DebNoteAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DebNoteAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DebitNoteID Desc: DebitNoteID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DebNoteAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DebNoteAttches_Company_DebitNoteID_DrawingSeq(Company:string, DebitNoteID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DebNoteAttches(" + Company + "," + DebitNoteID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete DebNoteAttch item
   Description: Call UpdateExt to delete DebNoteAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DebNoteAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DebitNoteID Desc: DebitNoteID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DebNoteAttches_Company_DebitNoteID_DrawingSeq(Company:string, DebitNoteID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DebNoteAttches(" + Company + "," + DebitNoteID + "," + DrawingSeq + ")", {
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
   Description: Get CashDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlRow
   */  
export function get_CashDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashDtl item
   Description: Calls GetByID to retrieve the CashDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   */  
export function get_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashDtl for the service
   Description: Calls UpdateExt to update CashDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
   Summary: Call UpdateExt to delete CashDtl item
   Description: Call UpdateExt to delete CashDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
   Description: Get CDTaxDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CDTaxDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CDTaxDtlRow
   */  
export function get_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef_CDTaxDtls(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CDTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")/CDTaxDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CDTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CDTaxDtl item
   Description: Calls GetByID to retrieve the CDTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CDTaxDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param APTranNo Desc: APTranNo   Required: True
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CDTaxDtlRow
   */  
export function get_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef_CDTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, SourceModule:string, APTranNo:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CDTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")/CDTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CDTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CashDtlTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashDtlTGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlTGLCRow
   */  
export function get_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef_CashDtlTGLCs(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")/CashDtlTGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashDtlTGLC item
   Description: Calls GetByID to retrieve the CashDtlTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtlTGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlTGLCRow
   */  
export function get_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef_CashDtlTGLCs_SysRowID(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashDtlTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")/CashDtlTGLCs(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashDtlTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CDTaxDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CDTaxDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CDTaxDtlRow
   */  
export function get_CDTaxDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CDTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CDTaxDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CDTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CDTaxDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CDTaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CDTaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CDTaxDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CDTaxDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CDTaxDtl item
   Description: Calls GetByID to retrieve the CDTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CDTaxDtl
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CDTaxDtlRow
   */  
export function get_CDTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CDTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CDTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CDTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CDTaxDtl for the service
   Description: Calls UpdateExt to update CDTaxDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CDTaxDtl
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
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CDTaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CDTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CDTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete CDTaxDtl item
   Description: Call UpdateExt to delete CDTaxDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CDTaxDtl
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
export function delete_CDTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company:string, SourceModule:string, HeadNum:string, APTranNo:string, InvoiceNum:string, InvoiceRef:string, BankAcctID:string, TranNum:string, Voided:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CDTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get CashDtlTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashDtlTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlTGLCRow
   */  
export function get_CashDtlTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtlTGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashDtlTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashDtlTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashDtlTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashDtlTGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtlTGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashDtlTGLC item
   Description: Calls GetByID to retrieve the CashDtlTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtlTGLC
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlTGLCRow
   */  
export function get_CashDtlTGLCs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashDtlTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtlTGLCs(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashDtlTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashDtlTGLC for the service
   Description: Calls UpdateExt to update CashDtlTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashDtlTGLC
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashDtlTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashDtlTGLCs_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtlTGLCs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete CashDtlTGLC item
   Description: Call UpdateExt to delete CashDtlTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashDtlTGLC
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashDtlTGLCs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtlTGLCs(" + SysRowID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/TaxDtls", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/TaxDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get CashHeadTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashHeadTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadTGLCRow
   */  
export function get_CashHeadTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashHeadTGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashHeadTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashHeadTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashHeadTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashHeadTGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashHeadTGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashHeadTGLC item
   Description: Calls GetByID to retrieve the CashHeadTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashHeadTGLC
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashHeadTGLCRow
   */  
export function get_CashHeadTGLCs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashHeadTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashHeadTGLCs(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashHeadTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashHeadTGLC for the service
   Description: Calls UpdateExt to update CashHeadTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashHeadTGLC
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashHeadTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashHeadTGLCs_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashHeadTGLCs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete CashHeadTGLC item
   Description: Call UpdateExt to delete CashHeadTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashHeadTGLC
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashHeadTGLCs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashHeadTGLCs(" + SysRowID + ")", {
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
   Description: Get CashHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadAttchRow
   */  
export function get_CashHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashHeadAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashHeadAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashHeadAttch item
   Description: Calls GetByID to retrieve the CashHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashHeadAttchRow
   */  
export function get_CashHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company:string, GroupID:string, HeadNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashHeadAttch for the service
   Description: Calls UpdateExt to update CashHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company:string, GroupID:string, HeadNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete CashHeadAttch item
   Description: Call UpdateExt to delete CashHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashHeadAttch
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
export function delete_CashHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company:string, GroupID:string, HeadNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCashHead:string, whereClauseCashHeadAttch:string, whereClauseBankTran:string, whereClauseBankTranTaxDtl:string, whereClauseBankTranTGLC:string, whereClauseDebNote:string, whereClauseDebNoteAttch:string, whereClauseCashDtl:string, whereClauseCashDtlTGLC:string, whereClauseCDTaxDtl:string, whereClauseCashHeadTGLC:string, whereClauseTaxDtl:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCashHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashHead=" + whereClauseCashHead
   }
   if(typeof whereClauseCashHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashHeadAttch=" + whereClauseCashHeadAttch
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
   if(typeof whereClauseDebNote!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDebNote=" + whereClauseDebNote
   }
   if(typeof whereClauseDebNoteAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDebNoteAttch=" + whereClauseDebNoteAttch
   }
   if(typeof whereClauseCashDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashDtl=" + whereClauseCashDtl
   }
   if(typeof whereClauseCashDtlTGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashDtlTGLC=" + whereClauseCashDtlTGLC
   }
   if(typeof whereClauseCDTaxDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCDTaxDtl=" + whereClauseCDTaxDtl
   }
   if(typeof whereClauseCashHeadTGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashHeadTGLC=" + whereClauseCashHeadTGLC
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetRows" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewBankTran", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewBankTranTaxDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewBankTranTGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDebNote
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDebNote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDebNote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDebNote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDebNote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewDebNote", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDebNoteAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDebNoteAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDebNoteAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDebNoteAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDebNoteAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewDebNoteAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewCashDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashDtlTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashDtlTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashDtlTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashDtlTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashDtlTGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewCashDtlTGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCDTaxDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCDTaxDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCDTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCDTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCDTaxDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewCDTaxDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashHeadTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashHeadTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashHeadTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashHeadTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashHeadTGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewCashHeadTGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewTaxDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsUnAppliedDNExists
   Description: Check for unapplied DN present
   OperationID: IsUnAppliedDNExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsUnAppliedDNExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsUnAppliedDNExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsUnAppliedDNExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/IsUnAppliedDNExists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvcMiscWithoutTakeDiscount
   Description: Calculate amount of InvcMisc.MiscAmt where corresponding MiscChrg.TakeDiscount is false which means it should not be included when calculating discount amount
   OperationID: GetInvcMiscWithoutTakeDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvcMiscWithoutTakeDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcMiscWithoutTakeDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvcMiscWithoutTakeDiscount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetInvcMiscWithoutTakeDiscount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDCashRecAdjustment
   Description: Returns a DataSet when adjusting a cash receipt.
   OperationID: GetByIDCashRecAdjustment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDCashRecAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDCashRecAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDCashRecAdjustment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetByIDCashRecAdjustment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDTracker
   Description: Returns a DataSet given the primary key.
   OperationID: GetByIDTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetByIDTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDSetTrackerMobe
   Description: Called from Kinetic Tracker and Returns a DataSet given the primary key.
   OperationID: Get_GetByIDSetTrackerMobe
      @param groupID Desc: Group ID   Required: True   Allow empty value : True
      @param headNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDSetTrackerMobe_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByIDSetTrackerMobe(groupID:string, headNum:string, epicorHeaders?:Headers){
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetByIDSetTrackerMobe" + params, {
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
   Summary: Invoke method CalcTaxRecNumber
   Description: Assigns a legal number (Tax Receipt) to the selected invoice when apply With Holding Tax.
   OperationID: CalcTaxRecNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcTaxRecNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcTaxRecNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcTaxRecNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CalcTaxRecNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CashRecGetInvoices
   Description: This procedure returns the invoices to Cash Receipt Entry
   OperationID: CashRecGetInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CashRecGetInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CashRecGetInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashRecGetInvoices(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecGetInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CashRecGetInvoicesExt
   Description: This procedure returns the invoices to Cash Receipt Entry
   OperationID: CashRecGetInvoicesExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CashRecGetInvoicesExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CashRecGetInvoicesExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashRecGetInvoicesExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecGetInvoicesExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CashRecGetInvoicesCC
   Description: This procedure returns the invoices to Cash Receipt Entry
   OperationID: CashRecGetInvoicesCC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CashRecGetInvoicesCC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CashRecGetInvoicesCC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashRecGetInvoicesCC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecGetInvoicesCC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CashRecGetInvoicesCCExt
   Description: This procedure returns the invoices to Cash Receipt Entry
   OperationID: CashRecGetInvoicesCCExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CashRecGetInvoicesCCExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CashRecGetInvoicesCCExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashRecGetInvoicesCCExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashRecGetInvoicesCCExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvoiceBalance
   Description: Method to get Balance for selected Invoice.
   OperationID: GetInvoiceBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvoiceBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvoiceBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvoiceBalance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetInvoiceBalance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateInvoiceWriteOffAccount
   Description: Validate Write Off Account for Invoice selected for allocation
   OperationID: ValidateInvoiceWriteOffAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateInvoiceWriteOffAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInvoiceWriteOffAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateInvoiceWriteOffAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ValidateInvoiceWriteOffAccount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultWriteOffData
   Description: Method to get default Write Off Account and Write Off Amount for selected Invoice.
   OperationID: GetDefaultWriteOffData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultWriteOffData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultWriteOffData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultWriteOffData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetDefaultWriteOffData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWriteOffAmount
   Description: Method to validate Write Off Amount.
   OperationID: OnChangeWriteOffAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWriteOffAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWriteOffAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWriteOffAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangeWriteOffAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetWriteOff
   Description: This method called when Write Off CheckBox manually switched on Allocate tab
   OperationID: SetWriteOff
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetWriteOff_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetWriteOff_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetWriteOff(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/SetWriteOff", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CCClear
   Description: Procedure to Clear the Credit Card Information
   OperationID: CCClear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CCClear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CCClear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCClear(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CCClear", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CCLoadTranData
   Description: Procedure to be called when selecting a record in the Transaction
            history grid, the data selected is loaded in the CashHead table
   OperationID: CCLoadTranData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CCLoadTranData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CCLoadTranData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCLoadTranData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CCLoadTranData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CCLoadCardNumbers
   Description: Procedure to be called when selecting a record in the Credit Card Number grid
            the data selected is loaded in the Cash Head table
   OperationID: CCLoadCardNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CCLoadCardNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CCLoadCardNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCLoadCardNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CCLoadCardNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CCProcessCard
   Description: Procedure to attempt to process transaction for the amount specified in
            the "Total" field.
   OperationID: CCProcessCard
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CCProcessCard_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CCProcessCard_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCProcessCard(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CCProcessCard", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeBankAmount
   Description: This method upates the TranAmt, DocTranAmt, ReceiptAmount fields after
the BankAmount field is updated.
   OperationID: ChangeBankAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBankAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBankAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBankAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeBankAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeBankExchangeRate
   Description: This method upates the BaseAmount field after the BankExchangeRate
field is updated.
   OperationID: ChangeBankExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBankExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBankExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBankExchangeRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeBankExchangeRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeBankReceiptExgRate
   Description: This method upates the BankAmount field after the BankReceiptExchangeRate
field is updated.
   OperationID: ChangeBankReceiptExgRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBankReceiptExgRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBankReceiptExgRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBankReceiptExgRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeBankReceiptExgRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCCAmounts
   Description: This procedure should be called when any of the Credit Card
            amounts change (from the Column Changed event in the UI) to calculate the
            total to be charged to the credit card
   OperationID: ChangeCCAmounts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCCAmounts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCCAmounts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCCAmounts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeCCAmounts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCreditExp
   Description: Procedure to validate Credit Card Expiration Date
   OperationID: ChangeCreditExp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCreditExp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCreditExp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCreditExp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeCreditExp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDNAmount
   Description: This method is called when the Debit Note value field is modified
   OperationID: ChangeDNAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDNAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDNAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDNAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeDNAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeReceiptAmt
   Description: This method updates the TranAmt, DocTranAmt, BankAmount fields after
the ReceiptAmt field is updated.
   OperationID: ChangeReceiptAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeReceiptAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeReceiptAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeReceiptAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeReceiptAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeReceiptCurrency
   Description: This method upates the TranAmt, DocTranAmt, BankAmount fields after
the ReceiptCurrencyCode field is updated.
   OperationID: ChangeReceiptCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeReceiptCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeReceiptCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeReceiptCurrency(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeReceiptCurrency", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSettlementExgRate
   Description: This method upates the TranAmt, DocTranAmt fields after
the SettlementExchangeRate field is updated.
   OperationID: ChangeSettlementExgRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSettlementExgRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSettlementExgRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSettlementExgRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeSettlementExgRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaxWhld
   Description: This method upates the DocAppledAmt
if TaxWhld  field is updated.
   OperationID: ChangeTaxWhld
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxWhld_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxWhld_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxWhld(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeTaxWhld", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeTranAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTranAmtCashHead
   Description: This method updates the BankTran or DocTran amounts when the adjustment amount changes or
the currency switch toggles.
   OperationID: ChangeTranAmtCashHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranAmtCashHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranAmtCashHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTranAmtCashHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeTranAmtCashHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CheckDocumentIsLocked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateChecks
   Description: Create Customer Checks for selected invoices.
   OperationID: CreateChecks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateChecks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateChecks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateChecks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CreateChecks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateNewDebitNote
   Description: This method calls  GetNewCashDtl to create a new Debit Note record instead of the standard way
so DebNote.CashHeadNum and  DebNote.GroupID fields could be assigned .
   OperationID: CreateNewDebitNote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewDebitNote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewDebitNote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateNewDebitNote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CreateNewDebitNote", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteMaster
   OperationID: DeleteMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteMaster(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DeleteMaster", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteNegativeReceipts
   Description: Delete cash receipts whose receipt amount is negative.
   OperationID: DeleteNegativeReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteNegativeReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteNegativeReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteNegativeReceipts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DeleteNegativeReceipts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EnterCustDebNote
   Description: This method is called when the Debit Note number assigned by the customer is entered or modified
   OperationID: EnterCustDebNote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnterCustDebNote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnterCustDebNote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnterCustDebNote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/EnterCustDebNote", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateCashDtl
   Description: This method combines the GetNewCashDtl and Update() method into one routine
so that the user can run an "Auto Apply" cash receipt function
   OperationID: GenerateCashDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateCashDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateCashDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateCashDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GenerateCashDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAdjAmtTax
   Description: GetAdjAmtTax
   OperationID: GetAdjAmtTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAdjAmtTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAdjAmtTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAdjAmtTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetAdjAmtTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetBankFeeDefaultAccount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCashHeadDefaultAccount
   Description: This method is used to get the default account(s) for Deposit Cash Receipt
   OperationID: GetCashHeadDefaultAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashHeadDefaultAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashHeadDefaultAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCashHeadDefaultAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetCashHeadDefaultAccount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetCurrencyInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetCustomerInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDNInvInfo
   Description: This method is called when invoice number field (DNInvNbr) referenced by Debit Note is modified
   OperationID: GetDNInvInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDNInvInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDNInvInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDNInvInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetDNInvInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlDiscountInfo
   Description: This method is run when the DocDiscount field is modified
   OperationID: GetDtlDiscountInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlDiscountInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlDiscountInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlDiscountInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetDtlDiscountInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetDtlInvoiceInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetDtlLegalNumberInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPendingToPostAdjustments
   Description: Return ListMessage of Cash Receipt Adjustments pending to post and Invoice Unposted Balance
   OperationID: GetPendingToPostAdjustments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPendingToPostAdjustments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPendingToPostAdjustments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPendingToPostAdjustments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetPendingToPostAdjustments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsWriteOffOverpayment
   Description: This method called to check if WO overpayment question should be raised on UI
   OperationID: IsWriteOffOverpayment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsWriteOffOverpayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsWriteOffOverpayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsWriteOffOverpayment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/IsWriteOffOverpayment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: This method is run when the DocTranAmt field or WriteOffAmount is modified
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetDtlTranAmtInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlTranAmtInfoExt
   OperationID: GetDtlTranAmtInfoExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlTranAmtInfoExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlTranAmtInfoExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlTranAmtInfoExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetDtlTranAmtInfoExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetHdrInvoiceInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetHdrLegalNumberInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMXOriginalCheckRef
   Description: Set original CheckRef and depandent fields
   OperationID: GetMXOriginalCheckRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMXOriginalCheckRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMXOriginalCheckRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMXOriginalCheckRef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetMXOriginalCheckRef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMXTaxRcptType
   Description: Gets the current status of the Mexican Digital Tax Receipts, valid results can be
Disabled, CFD and CFDI
   OperationID: GetMXTaxRcptType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMXTaxRcptType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMXTaxRcptType(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetMXTaxRcptType", {
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
   Summary: Invoke method UpdateMXSubstitutionCashReceipt
   Description: Update CSF Mexico Substitution Cash Receipt fields, use from Cash Receipt Tracker
   OperationID: UpdateMXSubstitutionCashReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMXSubstitutionCashReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMXSubstitutionCashReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateMXSubstitutionCashReceipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/UpdateMXSubstitutionCashReceipt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewBankTranByHeadNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashHeadType
   Description: This method replaces the standard GetNewCashHead method.  The 3 Tran Types available
are "PAYINV":U for AR Receipt, "DEPOSIT":U for Deposits, or "MISPAY":U for Miscellaneous
   OperationID: GetNewCashHeadType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashHeadType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashHeadType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashHeadType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewCashHeadType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: This method is run when the OrderNum field is changing to validate/update dataset fields
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetOrderInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOrderInfo4DskCurr
   Description: This method is run when the OrderNum field is changing to validate/update dataset fields
   OperationID: GetOrderInfo4DskCurr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderInfo4DskCurr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderInfo4DskCurr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderInfo4DskCurr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetOrderInfo4DskCurr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetRateCodeInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetSalesTaxInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetTaxableInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetTranAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsDueDateHighLighted
   Description: This method checks whether the record should be highlighted
(customer should have a valid mandate and due date is less than either 2 or 5 days depending on payment type)
   OperationID: IsDueDateHighLighted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsDueDateHighLighted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsDueDateHighLighted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsDueDateHighLighted(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/IsDueDateHighLighted", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LeaveCashHead
   Description: This method checks calculates the GainLoss Adjustment record when finally
leaving a CashHead record after adding/updating all the CashDtl records
   OperationID: LeaveCashHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveCashHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveCashHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveCashHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/LeaveCashHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MassApplyDebitNotes
   Description: This procedure processes un-applied Debit Notes, ttDebNote records with RowMod = "U" is passed in, changed ttDebNote, ttCashDtl, ttCashHead are passed back.
   OperationID: MassApplyDebitNotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassApplyDebitNotes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassApplyDebitNotes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassApplyDebitNotes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/MassApplyDebitNotes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MassDelete
   Description: Delete cash receipts from group having electronic payment method.
   OperationID: MassDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassDelete(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/MassDelete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MassGenerateCashDtl
   Description: Create multiple CashDtl for a CashHead from multiple selected invoices. CahsHead and CashGrp must exist
   OperationID: MassGenerateCashDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassGenerateCashDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassGenerateCashDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassGenerateCashDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/MassGenerateCashDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangeBankFeeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTranDocTypeID
   Description: Purpose:  Sets default values when the TranDocTypeID changes
Parameters:  none
Notes:
   OperationID: OnChangeTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTranDocTypeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangeTranDocTypeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCreditCard
   Description: Purpose:  fills certain fields when Credit Card checkbox is set to true or clears certain fields when credit card checkbox is set to false
Parameters:
Notes:
   OperationID: OnChangeCreditCard
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCreditCard_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCreditCard_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCreditCard(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangeCreditCard", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessPayGateMessage
   Description: Purpose: Fills credit card information in CashHead with the CREProcess response message
Parameters: ref CashRecTableset ds
Notes:
   OperationID: ProcessPayGateMessage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessPayGateMessage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPayGateMessage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessPayGateMessage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ProcessPayGateMessage", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/RecalcBankTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecalcCDTax
   Description: This method is called after the TaxAmt is changed to recalculate the doc or base tax amounts
   OperationID: RecalcCDTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcCDTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcCDTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecalcCDTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/RecalcCDTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecalcTax
   Description: This method is called after the TaxAmt is changed to recalculate the doc or base tax amounts
   OperationID: RecalcTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecalcTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/RecalcTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReverseCashReceipt
   Description: Reverse Cash Receipt
   OperationID: ReverseCashReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReverseCashReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReverseCashReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReverseCashReceipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ReverseCashReceipt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectInvoices
   Description: Read InvcHead records and create ARInvSel records if they meet the selection criteria.
   OperationID: SelectInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectInvoices(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/SelectInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxableWriteOff
   Description: Validate That TaxableWriteOff flag can be selected for allocated Invoice
   OperationID: OnChangeTaxableWriteOff
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxableWriteOff_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxableWriteOff_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxableWriteOff(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangeTaxableWriteOff", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TakeDiscount
   Description: This method is run when the Take discount option is selected
   OperationID: TakeDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TakeDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TakeDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TakeDiscount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/TakeDiscount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateAutoGen
   Description: This method is called only when CashRec auto generated
Some validations will be ignored
   OperationID: UpdateAutoGen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAutoGen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAutoGen_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAutoGen(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/UpdateAutoGen", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: This method is called instead of the standard Update because several
actions in relation to the update might be required and it avoids
multiple BL calls from the UI.
This method will a create record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  And then this method will be called again.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/UpdateMaster", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePrintEditList
   OperationID: ValidatePrintEditList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePrintEditList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePrintEditList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePrintEditList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ValidatePrintEditList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteMasterBankRec
   OperationID: DeleteMasterBankRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteMasterBankRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteMasterBankRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteMasterBankRec(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/DeleteMasterBankRec", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
try to save the record but before the Update standard method is called.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/PreUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultLegalNumOpts
   Description: Create record in the LegalNumGenOpts datatable if
a legal number is required for this transaction. The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  And then this method will be called again.
   OperationID: GetDefaultLegalNumOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultLegalNumOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultLegalNumOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultLegalNumOpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetDefaultLegalNumOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignLegalNumberUserAction
   Description: Generate and assign a legal number when the creation of the legal number is initiated by the user
   OperationID: AssignLegalNumberUserAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumberUserAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumberUserAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignLegalNumberUserAction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/AssignLegalNumberUserAction", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignLegalNumberBankRec
   Description: Assign the legal number from Bank Receipt screen.
   OperationID: AssignLegalNumberBankRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumberBankRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumberBankRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignLegalNumberBankRec(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/AssignLegalNumberBankRec", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Voids the legal number for provider header number.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/VoidLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ParseCEPXml
   Description: Fill CashHead fields MXEPaymentCertificateNumber, MXEPaymentOriginalString, MXEPaymentDigitalSeal with values from CEP xml
   OperationID: ParseCEPXml
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ParseCEPXml_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseCEPXml_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ParseCEPXml(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ParseCEPXml", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ParseCEPXml2
   Description: Fill CashHead fields MXEPaymentCertificateNumber, MXEPaymentOriginalString, MXEPaymentDigitalSeal with values from CEP xml
   OperationID: ParseCEPXml2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ParseCEPXml2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseCEPXml2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ParseCEPXml2(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ParseCEPXml2", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCustomerTaxID
   Description: Customer Tax Id check
   OperationID: CheckCustomerTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCustomerTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCustomerTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCustomerTaxID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CheckCustomerTaxID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckGroupTaxID
   Description: Check for Customer TaxId in Cash Receipts Group
   OperationID: CheckGroupTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckGroupTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGroupTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckGroupTaxID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CheckGroupTaxID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAllocAmount
   OperationID: OnChangingAllocAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAllocAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAllocAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAllocAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangingAllocAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingCashApplied
   OperationID: OnChangingCashApplied
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingCashApplied_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingCashApplied_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingCashApplied(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangingCashApplied", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingDiscount
   OperationID: OnChangingDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingDiscount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangingDiscount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingWriteOffAmount
   OperationID: OnChangingWriteOffAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingWriteOffAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingWriteOffAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingWriteOffAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangingWriteOffAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedDiscount
   OperationID: OnChangedDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedDiscount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangedDiscount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedInvcSelected
   OperationID: OnChangedInvcSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedInvcSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedInvcSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedInvcSelected(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangedInvcSelected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedAllocAmount
   OperationID: OnChangedAllocAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedAllocAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedAllocAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedAllocAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangedAllocAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedCashApplied
   OperationID: OnChangedCashApplied
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedCashApplied_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedCashApplied_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedCashApplied(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/OnChangedCashApplied", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalcCashApDiscount
   OperationID: CalcCashApDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcCashApDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcCashApDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcCashApDiscount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CalcCashApDiscount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalcAllocAmount
   OperationID: CalcAllocAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcAllocAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcAllocAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcAllocAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CalcAllocAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalcDiscount
   OperationID: CalcDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcDiscount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CalcDiscount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalcSelectedInvcTotal
   Description: !!! At this time this method is not used becase of related procedure on the client side!!!
   OperationID: CalcSelectedInvcTotal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcSelectedInvcTotal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcSelectedInvcTotal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcSelectedInvcTotal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CalcSelectedInvcTotal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ForceTakeDiscount
   OperationID: ForceTakeDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ForceTakeDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ForceTakeDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ForceTakeDiscount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ForceTakeDiscount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AutomaticSelectInvoices
   OperationID: AutomaticSelectInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutomaticSelectInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutomaticSelectInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutomaticSelectInvoices(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/AutomaticSelectInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AutomaticSelectAndApply
   OperationID: AutomaticSelectAndApply
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutomaticSelectAndApply_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutomaticSelectAndApply_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutomaticSelectAndApply(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/AutomaticSelectAndApply", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MassGenerateCashDtlExt
   OperationID: MassGenerateCashDtlExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassGenerateCashDtlExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassGenerateCashDtlExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassGenerateCashDtlExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/MassGenerateCashDtlExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearInvoiceAlloc
   OperationID: ClearInvoiceAlloc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearInvoiceAlloc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearInvoiceAlloc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearInvoiceAlloc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ClearInvoiceAlloc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CashDtl_DocTranAmt_OnChanging
   OperationID: CashDtl_DocTranAmt_OnChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CashDtl_DocTranAmt_OnChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CashDtl_DocTranAmt_OnChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashDtl_DocTranAmt_OnChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CashDtl_DocTranAmt_OnChanging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCustomerBankID
   Description: Bank ID validation.
   OperationID: ValidateCustomerBankID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCustomerBankID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCustomerBankID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCustomerBankID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ValidateCustomerBankID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTransTypeComboList
   Description: Generate List of values for TransType combo-box.
   OperationID: GetTransTypeComboList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransTypeComboList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransTypeComboList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransTypeComboList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetTransTypeComboList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTranAmtCashHead2
   Description: This method updates the BankTran or DocTran amounts when the adjustment amount changes or
the currency switch toggles. Kinetic Version.
   OperationID: ChangeTranAmtCashHead2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranAmtCashHead2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranAmtCashHead2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTranAmtCashHead2(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ChangeTranAmtCashHead2", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateTotalCash
   OperationID: ValidateTotalCash
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTotalCash_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTotalCash_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateTotalCash(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ValidateTotalCash", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePaymentsWithUnappliedAmntInGroup
   OperationID: ValidatePaymentsWithUnappliedAmntInGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePaymentsWithUnappliedAmntInGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePaymentsWithUnappliedAmntInGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePaymentsWithUnappliedAmntInGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/ValidatePaymentsWithUnappliedAmntInGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CustListPayFor
   Description: Get list of related customers in whereClause format (for search purpose)
   OperationID: CustListPayFor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustListPayFor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustListPayFor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustListPayFor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CustListPayFor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckIfNonBusinessDay
   Description: Check that input date is not Saturday/Sunday.
   OperationID: CheckIfNonBusinessDay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIfNonBusinessDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfNonBusinessDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIfNonBusinessDay(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/CheckIfNonBusinessDay", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBankBatchIDFromGrpWithBBIDNotEqualsInpID
   OperationID: GetBankBatchIDFromGrpWithBBIDNotEqualsInpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankBatchIDFromGrpWithBBIDNotEqualsInpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankBatchIDFromGrpWithBBIDNotEqualsInpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankBatchIDFromGrpWithBBIDNotEqualsInpID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetBankBatchIDFromGrpWithBBIDNotEqualsInpID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCashHeadRowsByInvoiceNum
   Description: Method performing search by Invoice Number.
   OperationID: GetCashHeadRowsByInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashHeadRowsByInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashHeadRowsByInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCashHeadRowsByInvoiceNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetCashHeadRowsByInvoiceNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListForAdjustment
   OperationID: GetListForAdjustment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForAdjustment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetListForAdjustment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetEInvoiceStatusToSent
   Description: Set E-Invoice status to sent for Cash Receipt
   OperationID: SetEInvoiceStatusToSent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetEInvoiceStatusToSent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetEInvoiceStatusToSent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetEInvoiceStatusToSent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/SetEInvoiceStatusToSent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewCashHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashHeadAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashRecSvc/GetNewCashHeadAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CDTaxDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CDTaxDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashDtlTGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashHeadAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashHeadRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashHeadTGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DebNoteAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DebNoteAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DebNoteRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DebNoteRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxDtlRow[],
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

export interface Erp_Tablesets_CDTaxDtlRow{
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
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
      /**  Group ID - used to link to Cash Head  */  
   "GroupID":string,
   "CTDescription":string,
      /**  Flag to indicate if Manual checkbox should be Read Only  */  
   "DisableManual":boolean,
   "EnableTax":boolean,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  */  
   "GroupID":string,
      /**  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  */  
   "HeadNum":number,
      /**  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  */  
   "InvoiceNum":number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   "InvoiceRef":number,
      /**   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  */  
   "TranType":string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  */  
   "FiscalPeriod":number,
      /**  Indicates if this transaction has been posted to the General Ledger Module.  */  
   "GLPosted":boolean,
      /**  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  */  
   "TranDate":string,
      /**   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   "CheckRef":string,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  */  
   "TranAmt":number,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  */  
   "DocTranAmt":number,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   "CustNum":number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   "Discount":number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   "DocDiscount":number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  */  
   "Comment":string,
      /**  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  */  
   "Reference":string,
      /**   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "GLRefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "GLRefCode":string,
      /**  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  */  
   "DebitNote":boolean,
      /**  Debit Note Detail Comments.  */  
   "DNComments":string,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   "DNAmount":number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   "DocDnAmount":number,
      /**  The Debit Note Number assigned by the customer.  */  
   "DNCustNbr":string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   "RoundDiff":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Fiscal Year Suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
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
      /**  Total Tax Amount.  */  
   "TaxAmt":number,
      /**  Tax Amount in the vendors currency.  */  
   "DocTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Red Storno Flag  */  
   "RedStorno":boolean,
      /**  Tax Receipt Date (Thailand Localization)  */  
   "TaxReceiptDate":string,
      /**  Tax Receipt No. (Thailand Localization)  */  
   "TaxReceiptNo":string,
      /**  Withholding Tax Certificate Date  (Thailand Localization)  */  
   "WHTCertificateDate":string,
      /**  Withholding Tax Certificate No. (Thailand Localization)  */  
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
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Tax Remarks  */  
   "TaxRemarks":string,
      /**  Non Deductable Code  */  
   "NonDeductCode":string,
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
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  SEPADDMsgID  */  
   "SEPADDMsgID":string,
      /**  SEPADDPmtID  */  
   "SEPADDPmtID":string,
      /**  PmtDueDate  */  
   "PmtDueDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  MX Payment Number for AR Invoice  */  
   "MXPaymentNum":number,
      /**  Reference to HeadNum of main CashHead record.  */  
   "WriteOffHeadNumRef":number,
      /**  EpicorFSA  */  
   "EpicorFSA":boolean,
      /**  Taxable Adjustment  */  
   "TaxableAdjustment":boolean,
   "ApplyDate":string,
      /**  Adjustment amount in Base Currency  */  
   "BaseAdjAmt":number,
   "BaseCurrDesc":string,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
      /**  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  */  
   "BillConNum":number,
      /**  If this flag is true the AR Invoice exchange rates is used when the Adjustment is applied and no currency Gain/Loss is calculated  */  
   "CopyRate":boolean,
      /**  Indicates if invoice related to  this detail line is Correction invoice with negatice balance  */  
   "CorrectionInv":boolean,
   "CreditMemo":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencyDescription":string,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol  */  
   "CurrSymbol":string,
      /**  This field displays all Debit Note customer defined numbers applied.  */  
   "DebitNotesApplied":string,
   "DispDocSelfAssessAmt":number,
   "DispDocWithholdAmt":number,
      /**  Display gl account  */  
   "DispGLAcct":string,
   "DispSelfAssessAmt":number,
   "DispTranAmt":number,
   "DispWithholdAmt":number,
   "DocDispTranAmt":number,
      /**  Doc Invoice Amount  */  
   "DocInvoiceAmt":number,
      /**  Doc Invoice Balance  */  
   "DocInvoiceBal":number,
   "DocNetCash":number,
      /**  Doc New Invoice Balance  */  
   "DocNewBalance":number,
      /**  Write Off Amount  */  
   "DocWriteOffAmount":number,
      /**  If this flag is true then CopyRate checkbox is Read Only  */  
   "DsblCopyRate":boolean,
      /**  Legal Number Field  */  
   "EnableAssignLegNum":boolean,
   "EnableTranDocType":boolean,
      /**  Legal Number Field  */  
   "EnableVoidLegNum":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   "FullyPaid":boolean,
   "GainLossAmt":number,
      /**  G/L Reference Code Description  */  
   "GLRefCodeDesc":string,
      /**  Legal Number Field  */  
   "HasLegNumCnfg":boolean,
   "InvDiscountDate":string,
   "InvDueDate":string,
      /**  Invoice Exchange Rate  */  
   "InvExchRate":number,
   "InvLegalNumber":string,
   "InvLockRate":boolean,
      /**  Invoice Amount  */  
   "InvoiceAmt":number,
      /**  Invoice Balance  */  
   "InvoiceBal":number,
   "InvTermsCode":string,
   "InvXRateLabel":string,
      /**  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  */  
   "IsCreditPayment":boolean,
   "IsDiscountforCreditM":boolean,
   "LegalNumMessage":string,
   "LegalNumStyle":string,
   "NetCash":number,
      /**  New Invoice Balance  */  
   "NewBalance":number,
   "OldGainLoss":number,
      /**  The related order number (InvcHead.OrderNum)  */  
   "OrderNum":number,
      /**  Processing company's Reference ID, unique to each transaction  */  
   "PNRef":string,
      /**  Indicates if posting GL transactions  */  
   "PostToGL":boolean,
      /**  Whether to recalculate the CashDtl.TranAmt and all related columns prior to saving.  */  
   "RecalcTranAmt":boolean,
   "RedStornoOpt":string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   "RefCodeStatus":string,
      /**  This will indicate the information on this CashDtl record will not be included in the Cash Receipt Adjustment.  */  
   "RemoveForAdjustment":boolean,
   "Rpt1DispTranAmt":number,
   "Rpt1GainLossAmt":number,
   "Rpt1InvoiceAmt":number,
   "Rpt1InvoiceBal":number,
   "Rpt1NetCash":number,
   "Rpt1NewBalance":number,
   "Rpt1OldGainLoss":number,
      /**  Write Off Amount  */  
   "Rpt1WriteOffAmount":number,
      /**  Write Off Gain Loss Amount  */  
   "Rpt1WriteOffGainLossAmt":number,
   "Rpt2DispTranAmt":number,
   "Rpt2GainLossAmt":number,
   "Rpt2InvoiceAmt":number,
   "Rpt2InvoiceBal":number,
   "Rpt2NetCash":number,
   "Rpt2NewBalance":number,
   "Rpt2OldGainLoss":number,
      /**  Write Off Amount  */  
   "Rpt2WriteOffAmount":number,
      /**  Write Off Gain Loss Amount  */  
   "Rpt2WriteOffGainLossAmt":number,
   "Rpt3DispTranAmt":number,
   "Rpt3GainLossAmt":number,
   "Rpt3InvoiceAmt":number,
   "Rpt3InvoiceBal":number,
   "Rpt3NetCash":number,
   "Rpt3NewBalance":number,
   "Rpt3OldGainLoss":number,
      /**  Write Off Amount  */  
   "Rpt3WriteOffAmount":number,
      /**  Write Off Gain Loss Amount  */  
   "Rpt3WriteOffGainLossAmt":number,
      /**  CustID associated with CashDtl.SoldToCustNum  */  
   "SoldToCustID":string,
      /**  Populated from InvcHead.SoldToCustNum.  */  
   "SoldToCustNum":number,
      /**  CustName associated with CashDtl.SoldToCustNum  */  
   "SoldToCustomerName":string,
      /**  Legal Number Field  */  
   "SystemTranType":string,
      /**  Description of the Tran Type  */  
   "TranTypeDesc":string,
      /**  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  */  
   "Type":string,
      /**  Write Off  */  
   "WriteOff":boolean,
      /**  Write Off Account  */  
   "WriteOffAccount":string,
      /**  Write Off Account Description  */  
   "WriteOffAccountDesc":string,
      /**  Write Off Amount  */  
   "WriteOffAmount":number,
      /**  Write Off Gain Loss Amount  */  
   "WriteOffGainLossAmt":number,
   "XRateLabel":string,
      /**  Legal Number Field  */  
   "AllowChgAfterPrint":boolean,
      /**  Write Off Amount  */  
   "OldWriteOffAmount":number,
   "WriteOffAccountDisp":string,
   "TaxableWriteOff":boolean,
      /**  Total Gain Loss Amount  */  
   "TotalGainLossAmt":number,
      /**  Write Off Amount  */  
   "OldWriteOffGainLossAmt":number,
      /**  Write Off Amount  */  
   "Rpt1OldWriteOffGainLossAmt":number,
      /**  Write Off Amount  */  
   "Rpt2OldWriteOffGainLossAmt":number,
      /**  Write Off Amount  */  
   "Rpt3OldWriteOffGainLossAmt":number,
      /**  Total Gain Loss Amount  */  
   "Rpt1TotalGainLossAmt":number,
      /**  Total Gain Loss Amount  */  
   "Rpt2TotalGainLossAmt":number,
      /**  Total Gain Loss Amount  */  
   "Rpt3TotalGainLossAmt":number,
      /**  Write Off Amount  */  
   "DocOldWriteOffAmount":number,
      /**  Write Off Amount  */  
   "Rpt1OldWriteOffAmount":number,
      /**  Write Off Amount  */  
   "Rpt2OldWriteOffAmount":number,
      /**  Write Off Amount  */  
   "Rpt3OldWriteOffAmount":number,
      /**  Allows uset to enter comment for Write Off.  */  
   "WriteOffComment":string,
      /**  Id of the netting transaction that generated this document.  */  
   "NettingID":number,
   "ReferenceTranDate":string,
   "ReferenceTranNum":number,
   "ReferenceTranTime":number,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   "EnableManualWHTax":boolean,
      /**  Indicates if the withholding amount tax was manually modified.  */  
   "WHTaxManualChange":boolean,
   "BitFlag":number,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "InvoiceNumInvoiceType":string,
   "InvoiceNumCardMemberName":string,
   "InvoiceNumTermsCode":string,
   "RateGrpDescription":string,
   "TaxRgnDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashDtlTGLCRow{
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
      /**  HeadNum of CashDtl  */  
   "HeadNum":number,
      /**  InvoiceNum of CashDtl  */  
   "InvoiceNum":number,
      /**  InvoiceRef of CashDtl  */  
   "InvoiceRef":number,
      /**  GroupID of CashDtl  */  
   "GroupID":string,
   "CDSeqNum":number,
   "BitFlag":number,
   "COADescription":string,
   "GLAccountGLShortAcct":string,
   "GLAccountGLAcctDisp":string,
   "GLAccountAccountDesc":string,
   "GLBookCurrencyCode":string,
   "GLBookDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashHeadAttchRow{
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

export interface Erp_Tablesets_CashHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   "GroupID":string,
      /**  Displays the receipt header number used for internal reference.  */  
   "HeadNum":number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Displays the transaction type.  */  
   "TranType":string,
      /**  Displays the number of the check.  */  
   "CheckRef":string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   "OrderNum":number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   "InvoiceNum":number,
      /**  Displays the transaction amount.  */  
   "TranAmt":number,
      /**  Displays the transaction amount in customer currency.  */  
   "DocTranAmt":number,
      /**  Displays the customer ID.  */  
   "CustID":string,
      /**  Displays the date of the transaction.  */  
   "TranDate":string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   "CustNum":number,
      /**  Displays the unapplied amount.  */  
   "UnAppliedAmt":number,
      /**  Displays the unapplied amount in base currency.  */  
   "DocUnAppliedAmt":number,
      /**  Displays the amount applied to invoices.  */  
   "AppliedAmt":number,
      /**  Displays the amount in document currency applied to invoices.  */  
   "DocAppliedAmt":number,
      /**  Displays the fiscal year that the check is posted to.  */  
   "FiscalYear":number,
      /**  Displays the fiscal period that the check is posted to.  */  
   "FiscalPeriod":number,
      /**  Displays any reference.  */  
   "Reference":string,
      /**  Indicates if this transaction has been posted.  */  
   "GLPosted":boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   "CreditMemoNum":number,
      /**  Displays the customer currency.  */  
   "CurrencyCode":string,
      /**  Displays the exchange rate that is used for this check.  */  
   "ExchangeRate":number,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  Total Tax Amount.  */  
   "TaxAmt":number,
      /**  Displays the tax amount.  */  
   "DocTaxAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Displays the legal number of the check.  */  
   "LegalNumber":string,
      /**  External ID  */  
   "ExternalID":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "GLRefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "GLRefCode":string,
      /**  The member's name on the credit card.  */  
   "CardMemberName":string,
      /**  The credit card account identifier.  */  
   "CardNumber":string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   "CardType":string,
      /**  The expiration month of the credit card.  */  
   "ExpirationMonth":number,
      /**  The expiration year of the credit card.  */  
   "ExpirationYear":number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   "CardID":string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   "CardmemberReference":string,
      /**  Stores the encrypted credit card number  */  
   "ProcessCard":string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   "CCAmount":number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   "CCFreight":number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   "CCTax":number,
      /**  Total amount being sent to the credit card processor  */  
   "CCTotal":number,
      /**  See CCAmount  */  
   "CCDocAmount":number,
      /**  See CCFreight  */  
   "CCDocFreight":number,
      /**  See CCTax  */  
   "CCDocTax":number,
      /**  See CCTotal  */  
   "CCDocTotal":number,
      /**  Address used during AVS validation for credit transactions  */  
   "CCStreetAddr":string,
      /**  Zip used during AVS validation in credit transactions  */  
   "CCZip":string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   "DebNoteOnly":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AppliedAmt":number,
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
      /**  Reporting currency value of this field  */  
   "Rpt1UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnAppliedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Amount of deposit applied  */  
   "DocDepApplied":number,
      /**  See CCAmount  */  
   "Rpt1CCAmount":number,
      /**  See CCAmount  */  
   "Rpt2CCAmount":number,
      /**  See CCAmount  */  
   "Rpt3CCAmount":number,
      /**  See CCFreight  */  
   "Rpt1CCFreight":number,
      /**  See CCFreight  */  
   "Rpt2CCFreight":number,
      /**  See CCFreight  */  
   "Rpt3CCFreight":number,
      /**  See CCTax  */  
   "Rpt1CCTax":number,
      /**  See CCTax  */  
   "Rpt2CCTax":number,
      /**  See CCTax  */  
   "Rpt3CCTax":number,
      /**  See CCTotal  */  
   "Rpt1CCTotal":number,
      /**  See CCTotal  */  
   "Rpt2CCTotal":number,
      /**  See CCTotal  */  
   "Rpt3CCTotal":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
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
      /**  The unique code of Receipt Currency.  */  
   "ReceiptCurrencyCode":string,
      /**  Amount of Receipt in Receipt Currency.  */  
   "ReceiptAmt":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   "BankRcptExchangeRate":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   "SettlementExchangeRate":number,
      /**  The unique Currency code for Credit Memo.  */  
   "CMCurrencyCode":string,
      /**  Amount of Credit Memo in CM Currency.  */  
   "CMAmount":number,
      /**  Reference to cash receipt which had been reversed.  */  
   "ReverseRef":number,
      /**  Date when cash receipt had been reversed  */  
   "ReverseDate":string,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Withhold Tax  */  
   "TaxWhld":number,
      /**  Dsicount Date  */  
   "DiscountDate":string,
      /**  Calculate Withhold Tax  */  
   "TaxWhldCalc":number,
      /**  Addition to Contract  */  
   "ContractDate":string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   "UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   "DocUnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   "Rpt1UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   "Rpt2UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   "Rpt3UnallocatedAmt":number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   "ApplyHeadNum":number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   "AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   "DocAllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   "Rpt1AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   "Rpt2AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   "Rpt3AllocatedAmt":number,
      /**  Comments related to the cash receipt.  */  
   "Comment":string,
      /**  Payment Method Unique Identifier  */  
   "PMUID":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Tax Remarks  */  
   "TaxRemarks":string,
      /**  Non Deductable Code  */  
   "NonDeductCode":string,
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
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  Payee  */  
   "Payee":string,
      /**  AccountNumber  */  
   "AccountNumber":string,
      /**  OtherDetails  */  
   "OtherDetails":string,
      /**  MandateReference  */  
   "MandateReference":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SEPADDExportDate  */  
   "SEPADDExportDate":string,
      /**  BOE Invoice Number  */  
   "BOEInvoiceNum":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  OwnReference  */  
   "OwnReference":string,
      /**  DocumentType  */  
   "DocumentType":string,
      /**  ABTUID  */  
   "ABTUID":string,
      /**  BankRcptExchangeRate10D  */  
   "BankRcptExchangeRate10D":number,
      /**  SettlementExchangeRate10D  */  
   "SettlementExchangeRate10D":number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   "BankBatchExcluded":boolean,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  PayMethodReference  */  
   "PayMethodReference":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   "MXFiscalFolio":string,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   "AllowUpdSettlementCurr":boolean,
   "ApplyDate":string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSAddr":string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSZip":string,
   "BankAcctDesc":string,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Bank Currency Value  */  
   "BankAmount":number,
   "BankBaseXRateLabel":string,
   "BankCurrencyCode":string,
      /**  Bank Currency Symbol  */  
   "BankCurrSymbol":string,
   "BankExchangeRate":number,
   "BankRcptXRateLabel":string,
   "BaseCurrencyCode":string,
   "BaseCurrSymbol":string,
      /**  Bill To Name  */  
   "BillToName":string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   "calcRate":boolean,
      /**  Stored Credit Card Number  */  
   "CardStore":string,
      /**  The credit card description. For example, American Express, Visa, Master Card, Discover, etc.  */  
   "CardTypeDescription":string,
      /**  Description  */  
   "CashbookLineDescription":string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   "CCAllowSales":boolean,
   "CCApprovalNum":string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   "CCCSCID":string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   "CCEnableAddress":boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   "CCEnableCSC":boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   "CCResponse":string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   "CCTranID":string,
      /**  Credit Card Transaction Type  */  
   "CCTranType":string,
      /**  Description of the currency  */  
   "CMCurrencyCodeCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CMCurrencyCodeCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CMCurrencyCodeCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CMCurrencyCodeCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CMCurrencyCodeDocumentDesc":string,
      /**  Customer Credit Hold flag  */  
   "CreditHold":boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "CSCResult":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
   "CurrencySwitch":boolean,
   "CustFullAddr":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
   "CustomerName":string,
      /**  Display GL Account  */  
   "DispGLAcct":string,
   "DocDiscount":number,
   "DocReceipt":number,
      /**  Transaction Amount less Tax Amount  */  
   "DocTranTaxAmt":number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   "DocumentNum":number,
      /**  Amount of Credit Memo in CM Currency.  */  
   "DspCMAmount":number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user enters this amount and then it is used as a limit/control when applying it to the invoices.  */  
   "DspDocTranAmt":number,
   "DspSalesOrderValue":number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   "DspTranAmt":number,
   "EnableTransactionDate":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   "FullyPaid":boolean,
      /**  The InvcHead legal number  */  
   "InvcLegalNumber":string,
      /**  The member's name on the credit card.  */  
   "InvoiceNumCardMemberName":string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   "InvoiceNumTermsCode":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumberDsp":string,
   "LegalNumMessage":string,
      /**  Copied from OrderHed.LockRate  */  
   "LockRate":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
   "PaymentMethod":string,
      /**  Description  */  
   "RateGrpDescription":string,
      /**  Description of the currency  */  
   "RcptCurrencyCodeCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "RcptCurrencyCodeCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "RcptCurrencyCodeCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "RcptCurrencyCodeCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "RcptCurrencyCodeDocumentDesc":string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   "ReferencePNRef":string,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt1TranTaxAmt":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt2TranTaxAmt":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt3TranTaxAmt":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "SalesOrderValue":number,
   "SettlementXRateLabel":string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   "SoldToCustomerName":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionCodeDescription":string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   "TotalRoundDiff":number,
      /**  Transaction Amount less Tax Amount  */  
   "TranTaxAmt":number,
      /**  Description of TranType  */  
   "TranTypeDesc":string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   "UnappliedAmountApplied":boolean,
   "XRateLabel":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   "GroupID":string,
      /**  Displays the receipt header number used for internal reference.  */  
   "HeadNum":number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Displays the transaction type.  */  
   "TranType":string,
      /**  Displays the number of the check.  */  
   "CheckRef":string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   "OrderNum":number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   "InvoiceNum":number,
      /**  Displays the transaction amount.  */  
   "TranAmt":number,
      /**  Displays the transaction amount in customer currency.  */  
   "DocTranAmt":number,
      /**  Displays the customer ID.  */  
   "CustID":string,
      /**  Displays the date of the transaction.  */  
   "TranDate":string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   "CustNum":number,
      /**  Displays the unapplied amount.  */  
   "UnAppliedAmt":number,
      /**  Displays the unapplied amount in base currency.  */  
   "DocUnAppliedAmt":number,
      /**  Displays the amount applied to invoices.  */  
   "AppliedAmt":number,
      /**  Displays the amount in document currency applied to invoices.  */  
   "DocAppliedAmt":number,
      /**  Displays the fiscal year that the check is posted to.  */  
   "FiscalYear":number,
      /**  Displays the fiscal period that the check is posted to.  */  
   "FiscalPeriod":number,
      /**  Displays any reference.  */  
   "Reference":string,
      /**  Indicates if this transaction has been posted.  */  
   "GLPosted":boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   "CreditMemoNum":number,
      /**  Displays the customer currency.  */  
   "CurrencyCode":string,
      /**  Displays the exchange rate that is used for this check.  */  
   "ExchangeRate":number,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  Total Tax Amount.  */  
   "TaxAmt":number,
      /**  Displays the tax amount.  */  
   "DocTaxAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Displays the legal number of the check.  */  
   "LegalNumber":string,
      /**  External ID  */  
   "ExternalID":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "GLRefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "GLRefCode":string,
      /**  The member's name on the credit card.  */  
   "CardMemberName":string,
      /**  The credit card account identifier.  */  
   "CardNumber":string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   "CardType":string,
      /**  The expiration month of the credit card.  */  
   "ExpirationMonth":number,
      /**  The expiration year of the credit card.  */  
   "ExpirationYear":number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   "CardID":string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   "CardmemberReference":string,
      /**  Stores the encrypted credit card number  */  
   "ProcessCard":string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   "CCAmount":number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   "CCFreight":number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   "CCTax":number,
      /**  Total amount being sent to the credit card processor  */  
   "CCTotal":number,
      /**  See CCAmount  */  
   "CCDocAmount":number,
      /**  See CCFreight  */  
   "CCDocFreight":number,
      /**  See CCTax  */  
   "CCDocTax":number,
      /**  See CCTotal  */  
   "CCDocTotal":number,
      /**  Address used during AVS validation for credit transactions  */  
   "CCStreetAddr":string,
      /**  Zip used during AVS validation in credit transactions  */  
   "CCZip":string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   "DebNoteOnly":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AppliedAmt":number,
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
      /**  Reporting currency value of this field  */  
   "Rpt1UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnAppliedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Amount of deposit applied  */  
   "DocDepApplied":number,
      /**  See CCAmount  */  
   "Rpt1CCAmount":number,
      /**  See CCAmount  */  
   "Rpt2CCAmount":number,
      /**  See CCAmount  */  
   "Rpt3CCAmount":number,
      /**  See CCFreight  */  
   "Rpt1CCFreight":number,
      /**  See CCFreight  */  
   "Rpt2CCFreight":number,
      /**  See CCFreight  */  
   "Rpt3CCFreight":number,
      /**  See CCTax  */  
   "Rpt1CCTax":number,
      /**  See CCTax  */  
   "Rpt2CCTax":number,
      /**  See CCTax  */  
   "Rpt3CCTax":number,
      /**  See CCTotal  */  
   "Rpt1CCTotal":number,
      /**  See CCTotal  */  
   "Rpt2CCTotal":number,
      /**  See CCTotal  */  
   "Rpt3CCTotal":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
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
      /**  The unique code of Receipt Currency.  */  
   "ReceiptCurrencyCode":string,
      /**  Amount of Receipt in Receipt Currency.  */  
   "ReceiptAmt":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   "BankRcptExchangeRate":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   "SettlementExchangeRate":number,
      /**  The unique Currency code for Credit Memo.  */  
   "CMCurrencyCode":string,
      /**  Amount of Credit Memo in CM Currency.  */  
   "CMAmount":number,
      /**  Reference to cash receipt which had been reversed.  */  
   "ReverseRef":number,
      /**  Date when cash receipt had been reversed  */  
   "ReverseDate":string,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Withhold Tax  */  
   "TaxWhld":number,
      /**  Dsicount Date  */  
   "DiscountDate":string,
      /**  Calculate Withhold Tax  */  
   "TaxWhldCalc":number,
      /**  Addition to Contract  */  
   "ContractDate":string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   "UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   "DocUnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   "Rpt1UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   "Rpt2UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   "Rpt3UnallocatedAmt":number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   "ApplyHeadNum":number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   "AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   "DocAllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   "Rpt1AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   "Rpt2AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   "Rpt3AllocatedAmt":number,
      /**  Comments related to the cash receipt.  */  
   "Comment":string,
      /**  Payment Method Unique Identifier  */  
   "PMUID":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Tax Remarks  */  
   "TaxRemarks":string,
      /**  Non Deductable Code  */  
   "NonDeductCode":string,
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
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  Payee  */  
   "Payee":string,
      /**  AccountNumber  */  
   "AccountNumber":string,
      /**  OtherDetails  */  
   "OtherDetails":string,
      /**  MandateReference  */  
   "MandateReference":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SEPADDExportDate  */  
   "SEPADDExportDate":string,
      /**  BOE Invoice Number  */  
   "BOEInvoiceNum":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  OwnReference  */  
   "OwnReference":string,
      /**  DocumentType  */  
   "DocumentType":string,
      /**  ABTUID  */  
   "ABTUID":string,
      /**  BankRcptExchangeRate10D  */  
   "BankRcptExchangeRate10D":number,
      /**  SettlementExchangeRate10D  */  
   "SettlementExchangeRate10D":number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   "BankBatchExcluded":boolean,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  PayMethodReference  */  
   "PayMethodReference":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  The amount of the cash receipt applied to invoices in receipt currency  */  
   "RcptCurAppliedAmt":number,
      /**  The amount of the cash receipt that is unapplied in receipt currency  */  
   "RcptCurUnAppliedAmt":number,
      /**  MXAccountNumber  */  
   "MXAccountNumber":string,
      /**  MX Method of Payment: single, multiple, etc.  */  
   "MXPaidAs":string,
      /**  If TRUE then MX Electronic Payment XML is required  */  
   "MXPaySupplementFlag":boolean,
      /**  LockboxID  */  
   "LockboxID":string,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   "MXFiscalFolio":string,
      /**  MX UUID of the original Receipt being corrected  */  
   "MXOriginalCheckRef":string,
      /**  MX Confirmation Code for special Cash Receipts  */  
   "MXConfirmationCode":string,
      /**  MX Customer’s Bank ID  */  
   "MXBankID":string,
      /**  Text entered by the user to indicate the reason Cash receipt was Reversed.  */  
   "ReversedReason":string,
      /**  Credit Card Holder City.  */  
   "CCCity":string,
      /**  Credit Card Holder State.  */  
   "CCState":string,
      /**  ccToken  */  
   "ccToken":string,
      /**  DepositBalance  */  
   "DepositBalance":number,
      /**  DocDepositBalance  */  
   "DocDepositBalance":number,
      /**  Rpt1DepositBalance  */  
   "Rpt1DepositBalance":number,
      /**  Rpt2DepositBalance  */  
   "Rpt2DepositBalance":number,
      /**  Rpt3DepositBalance  */  
   "Rpt3DepositBalance":number,
      /**  Indicates this record is an adjustment CashHead.  */  
   "Adjustment":boolean,
      /**  Reference to cash receipt which had been adjusted.  */  
   "AdjustmentRef":number,
      /**  The reason for the adjustment entered by the user  */  
   "AdjustmentReason":string,
      /**  Total Check Write Off Amount  */  
   "WriteOffAmount":number,
      /**  DocWriteOffAmount  */  
   "DocWriteOffAmount":number,
      /**  Rpt1WriteOffAmount  */  
   "Rpt1WriteOffAmount":number,
      /**  Rpt2WriteOffAmount  */  
   "Rpt2WriteOffAmount":number,
      /**  Rpt3WriteOffAmount  */  
   "Rpt3WriteOffAmount":number,
      /**  Mexico Certified Timestamp  */  
   "MXCertifiedTimestamp":string,
      /**  Mexico SAT Seal  */  
   "MXSATSeal":string,
      /**  Mexico Digital Seal  */  
   "MXDigitalSeal":string,
      /**  Mexico SAT Certificate Serial Number  */  
   "MXSATCertificateSN":string,
      /**  Mexico Original String Timbre Fiscal Digital  */  
   "MXOriginalStringTFD":string,
      /**  Mexico Certificate  */  
   "MXCertificate":string,
      /**  Mexico Certificate Serial Number  */  
   "MXCertificateSN":string,
      /**  SourceGroupID  */  
   "SourceGroupID":string,
      /**  SourceHeadNum  */  
   "SourceHeadNum":number,
      /**  Standard Entry Class Code  */  
   "SEC":string,
      /**  ACH Transaction Code  */  
   "ACHTranCode":number,
      /**  ID of the Customer's bank.  */  
   "CustomerBankID":string,
      /**  The Bank account number for the Customer.  */  
   "CustomerBankAcctNumber":string,
      /**  CustomerBankSwiftNum  */  
   "CustomerBankSwiftNum":string,
      /**  The Bank account IBAN Code  */  
   "CustomerBankIBANCode":string,
      /**  Name on the Bank Account.  */  
   "CustomerBankNameOnAccount":string,
      /**  First address line of customer bank.  */  
   "CustomerBankAddress1":string,
      /**  Second address line of customer bank.  */  
   "CustomerBankAddress2":string,
      /**  Third address line of customer bank.  */  
   "CustomerBankAddress3":string,
      /**  Bank City  */  
   "CustomerBankCity":string,
      /**  Bank State/Prov  */  
   "CustomerBankState":string,
      /**  Postal Code or zip code  */  
   "CustomerBankPostalCode":string,
      /**  Bank account Country Number.  */  
   "CustomerBankCountryNum":number,
      /**  ARRemittanceSlipPrinted  */  
   "ARRemittanceSlipPrinted":boolean,
      /**  Customer Bank Name  */  
   "CustomerBankName":string,
      /**  MXPostedTimeStamp  */  
   "MXPostedTimeStamp":string,
      /**  MXSerie  */  
   "MXSerie":string,
      /**  MXFolio  */  
   "MXFolio":string,
      /**  MXEPaymentType  */  
   "MXEPaymentType":string,
      /**  MXEPaymentCertificateNumber  */  
   "MXEPaymentCertificateNumber":string,
      /**  MXEPaymentOriginalString  */  
   "MXEPaymentOriginalString":string,
      /**  MXEPaymentDigitalSeal  */  
   "MXEPaymentDigitalSeal":string,
      /**  Source  */  
   "Source":string,
      /**  Id of the netting transaction that generated this document.  */  
   "NettingID":number,
      /**  GL Description for the Reverse process  */  
   "RevDescription":string,
      /**  GL Description for AR - Apply Credit Memo  */  
   "CMDescription":string,
      /**  Receipt Amount in Bank Currency  */  
   "BankReceiptAmt":number,
      /**  MXCancelReasonCode  */  
   "MXCancelReasonCode":string,
      /**  MXSubstHeadNum  */  
   "MXSubstHeadNum":number,
      /**  MXCancellationMode  */  
   "MXCancellationMode":string,
      /**  E-invoice error description.  */  
   "ELIEInvException":string,
      /**  EInvoice ID  */  
   "ELIEInvID":string,
      /**  E-invoice  */  
   "ELIEInvoice":boolean,
      /**  E-invoice Service Provider Status  */  
   "ELIEInvServiceProviderStatus":number,
      /**  E-invoice Status  */  
   "ELIEInvStatus":number,
      /**  User Id of the person generated E-invoice.  */  
   "ELIEInvUpdatedBy":string,
      /**  E-invoice Updated On  */  
   "ELIEInvUpdatedOn":string,
      /**  Adjustment Customer Name  */  
   "AdjustmentCustName":string,
      /**  Customer to which the new invoices will be applied.  */  
   "AdjustmentCustNum":number,
      /**  Date the adjustment was made.  */  
   "AdjustmentDate":string,
      /**  Displays the amount available to apply to the invoices.  */  
   "AdjustmentDocUnAppliedAmt":number,
      /**  On Account  */  
   "AdjustmentOnAccount":boolean,
      /**  Temp TranDocTypeID used when adjusting a Cash Rececipt  */  
   "AdjustmentTranDocTypeID":string,
   "AllocDepBal":number,
   "AllowChgAfterPrint":boolean,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   "AllowUpdSettlementCurr":boolean,
      /**  Amount to Allocate  */  
   "AmtToAlloc":number,
   "ApplyDate":string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSAddr":string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSZip":string,
      /**  Bank Currency Value  */  
   "BankAmount":number,
   "BankBaseXRateLabel":string,
   "BankCurrencyCode":string,
      /**  Bank Currency Symbol  */  
   "BankCurrSymbol":string,
   "BankExchangeRate":number,
   "BankRcptXRateLabel":string,
   "BaseCurrencyCode":string,
      /**  Base Currency Symbol  */  
   "BaseCurrSymbol":string,
      /**  Bill To Name  */  
   "BillToName":string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   "calcRate":boolean,
      /**  Stored Credit Card Number  */  
   "CardStore":string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   "CCAllowSales":boolean,
   "CCApprovalNum":string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   "CCCSCID":string,
      /**  Tokenized value of CSCID  */  
   "CCCSCIDToken":string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   "CCEnableAddress":boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   "CCEnableCSC":boolean,
      /**   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  */  
   "CCIsTraining":boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   "CCResponse":string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   "CCTranID":string,
      /**  Credit Card Transaction Type  */  
   "CCTranType":string,
      /**  Check Box on the UI to filter records by Central Collection flag  */  
   "CentralCollectionCheck":boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Correction Invoice with negative amount  */  
   "CorrectionInv":boolean,
      /**  Customer Credit Hold flag  */  
   "CreditHold":boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Credit Memo  */  
   "CreditMemo":boolean,
      /**  CREProcessor is true when Credit Card Configuration is CRE Server.  */  
   "CREProcessor":boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "CSCResult":string,
      /**  Current Amount Selected on Invoice Select Tab  */  
   "CurrAmtSelected":number,
   "CurrencySwitch":boolean,
      /**  Displays the address of the customer that paid the receipt.  */  
   "CustFullAddr":string,
   "CustomerName":string,
   "DisableFieldsForPCashDoc":boolean,
      /**  Display GL Account  */  
   "DispGLAcct":string,
   "DocAllocDepBal":number,
      /**  Doc Amount to Allocate  */  
   "DocAmtToAlloc":number,
      /**  Displays the discount applied to the receipt.  */  
   "DocDiscount":number,
      /**  Displays the invoice amount paid by this receipt. The amount includes both discount and payment amounts.  */  
   "DocReceipt":number,
      /**  Transaction Amount less Tax Amount  */  
   "DocTranTaxAmt":number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   "DocumentNum":number,
   "DocWhldTax":number,
   "DspBankBatchID":string,
      /**  Amount of Credit Memo in CM Currency.  */  
   "DspCMAmount":number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   "DspDocTranAmt":number,
   "DspSalesOrderValue":number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   "DspTranAmt":number,
   "EnableAssignLegNum":boolean,
      /**  Indicates if the option to get the default account is enable.  */  
   "EnableGetDefaultAcct":boolean,
   "EnableTranDocType":boolean,
   "EnableTransactionDate":boolean,
   "EnableVoidLegNum":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   "FullyPaid":boolean,
   "GLRefCodeDescription":string,
   "HasLegNumCnfg":boolean,
      /**  The InvcHead legal number  */  
   "InvcLegalNumber":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumberDsp":string,
   "LegalNumMessage":string,
      /**  Copied from OrderHed.LockRate  */  
   "LockRate":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "ManualTaxAdj":boolean,
      /**  MXCancellationID  */  
   "MXCancellationID":string,
   "MXCancellationStatus":string,
      /**  MXECEPXml  */  
   "MXECEPXml":string,
      /**  Mexico Calculated field - shows Check Reference number of the original Receipt being corrected  */  
   "MXOriginalRefNum":string,
      /**  Host Address for the Paygate Hosted Token Service.  */  
   "PayGateHostAddress":string,
      /**  NameSpace for the Paygate Hosted Token Service.  */  
   "PayGateNameSpace":string,
      /**  Public Key for the Paygate Hosted Token Service EWA component.  */  
   "PayGatePublicKey":string,
      /**  This column is used within cash receipt tracker to show either the receipt date or the source/ original receipt date if the cash receipt has been adjusted.  */  
   "ReceiptDate":string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   "ReferencePNRef":string,
   "Rpt1AllocDepBal":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt1TranTaxAmt":number,
   "Rpt1WhldTax":number,
   "Rpt2AllocDepBal":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt2TranTaxAmt":number,
   "Rpt2WhldTax":number,
   "Rpt3AllocDepBal":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt3TranTaxAmt":number,
   "Rpt3WhldTax":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "SalesOrderValue":number,
   "SettlementXRateLabel":string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   "SoldToCustomerName":string,
   "SystemTranType":string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   "TotalRoundDiff":number,
      /**  Transaction Amount less Tax Amount  */  
   "TranTaxAmt":number,
      /**  Description of TranType  */  
   "TranTypeDesc":string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   "UnappliedAmountApplied":boolean,
   "WhldTax":number,
   "XRateLabel":string,
      /**  Displays the customer ID.  */  
   "AdjustmentCustID":string,
   "ReferenceTranDate":string,
   "ReferenceTranNum":number,
   "ReferenceTranTime":number,
      /**  Displays the address of the customer that paid the receipt with newline delimiter.  */  
   "CustFullAddrFormatted":string,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   "EnableManualWHTax":boolean,
      /**  Indicates if the withholding tax was manually modified.  */  
   "WHTaxManualChange":boolean,
      /**  Payment type description, displayed in the Details page header.  */  
   "TranTypeDescCaption":string,
   "AdjustmentCustAddress":string,
      /**  Substitution Cash Receipt Group ID  */  
   "MXSubstGroupId":string,
      /**  Substitution Cash Receipt CheckRef  */  
   "MXSubstCheckRef":string,
      /**  Substitution Cash Receipt UUID  */  
   "MXSubstFiscalFolio":string,
   "BitFlag":number,
   "BankAcctIDDescription":string,
   "BankAcctIDBankName":string,
   "CardTypeDescription":string,
   "CashBHedPosted":boolean,
   "CashBHedCashBookNum":number,
   "CashbookLineDescription":string,
   "CMCurrencyCodeDocumentDesc":string,
   "CMCurrencyCodeCurrName":string,
   "CMCurrencyCodeCurrSymbol":string,
   "CMCurrencyCodeCurrDesc":string,
   "CMCurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CustNumInactive":boolean,
   "CustNumName":string,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "InvoiceNumTermsCode":string,
   "InvoiceNumCardMemberName":string,
   "OrderNumCardMemberName":string,
   "OrderNumCurrencyCode":string,
   "PCashDocDirection":string,
   "PMUIDName":string,
   "PMUIDMXSATCode":string,
   "PMUIDSummarizePerCustomer":boolean,
   "PMUIDType":number,
   "RateGrpDescription":string,
   "RcptCurrencyCodeCurrencyID":string,
   "RcptCurrencyCodeDocumentDesc":string,
   "RcptCurrencyCodeCurrDesc":string,
   "RcptCurrencyCodeCurrSymbol":string,
   "RcptCurrencyCodeCurrName":string,
   "ReverseMXCancelReasonCode":string,
   "ReverseMXCancellationMode":string,
   "SourceTranDateTranDate":string,
   "TaxRegionCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashHeadTGLCRow{
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
      /**  HeadNum of CashHead  */  
   "HeadNum":number,
      /**  GroupID of CashHead  */  
   "GroupID":string,
   "BitFlag":number,
   "COADescription":string,
   "GLAccountAccountDesc":string,
   "GLAccountGLShortAcct":string,
   "GLAccountGLAcctDisp":string,
   "GLBookCurrencyCode":string,
   "GLBookDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DebNoteAttchRow{
   "Company":string,
   "DebitNoteID":number,
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

export interface Erp_Tablesets_DebNoteRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A  unique integer assigned by the system to new debit note  .  */  
   "DebitNoteID":number,
      /**  The customer number of the customer associated with this Debit Note.  */  
   "CustNum":number,
      /**   The Debit Note Number assigned by the customer.
This number is supposed to be unique for the customer.  */  
   "DNCustNbr":string,
      /**  The debit note value.  */  
   "DNAmount":number,
      /**  Customer Debit Note Amount.  */  
   "DocDNAmount":number,
      /**  The invoice number associated with this Debit Note.  */  
   "DNInvNbr":number,
      /**  A flag to indicate if this debit note was applied to Unapplied cash balance or invoice.  */  
   "DNApplied":boolean,
      /**  If a Debit Note was applied this field is "Cash" or "Invoice".  */  
   "DNAppliedTo":string,
      /**  The HeadNum of the CashHead record associated with this Debit Note.  */  
   "CashHeadNum":number,
      /**  The Group ID of the Cash Payment this Debit Note is associated with.  */  
   "GroupID":string,
      /**   If a Debit note is entered as a part of Cash Receipt payment this flag indicates if the Cash Receipts group is posted.
If this flag is yes the Debit Note can not be changed or deleted.  */  
   "PmtPosted":boolean,
      /**  Debit Note Comments  */  
   "DNComments":string,
      /**  Debit Note Due Date.  */  
   "DNDueDate":string,
      /**  Date when this Debit Note is entered.  */  
   "DNDate":string,
      /**  A flag to indicate if the invoice balance is supposed to be changed after the debit note is applied and posted.  */  
   "InvcChanged":boolean,
      /**  Invoice Number assigned to the Debit Note type invoice created when the Debit Note is posted with the Cash Receipt Group.  */  
   "InvNbrAssigned":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DNAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DNAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DNAmount":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The legal number of the invoice entered as debit note reference  */  
   "DNInvLegalNbr":string,
      /**  The flag to indicate if an infoice entered as debit note reference closed (or open).  */  
   "DNInvoiceClsd":boolean,
      /**  The open balance of the invoice entered as debit note reference.  */  
   "DNInvBalance":number,
      /**  The due date of the invoice entered as debit note reference  */  
   "DNInvDueDate":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
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
      @param inHeadNum
   */  
export interface AssignLegalNumberBankRec_input{
   ds:Erp_Tablesets_CashRecTableset[],
      /**  Header number.  */  
   inHeadNum:number,
}

export interface AssignLegalNumberBankRec_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
   msgLegalNumber:string,
}
}

   /** Required : 
      @param ds
      @param GroupID
      @param HeadNum
   */  
export interface AssignLegalNumberUserAction_input{
   ds:Erp_Tablesets_CashRecTableset[],
      /**  The check header group id  */  
   GroupID:string,
      /**  The check header number  */  
   HeadNum:number,
}

export interface AssignLegalNumberUserAction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
   LegalNumberMessage:string,
}
}

   /** Required : 
      @param groupID
      @param headNum
      @param DocUnAppliedAmt
      @param ds
   */  
export interface AutomaticSelectAndApply_input{
   groupID:string,
   headNum:number,
   DocUnAppliedAmt:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface AutomaticSelectAndApply_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
parameters : {
      /**  output parameters  */  
   massGenErrorMsg:string,
   opTotalCashReceived:number,
   opTotalApplied:number,
   opUnappliedBalance:number,
   opTotalMisc:number,
   opTotalDiscount:number,
   opTotalDeposit:number,
   opTotalARAmount:number,
   opTotalWithhold:number,
   opTotalWriteOff:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param groupID
      @param headNum
      @param unAppliedAmt
      @param ds
   */  
export interface AutomaticSelectInvoices_input{
   groupID:string,
   headNum:number,
   unAppliedAmt:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface AutomaticSelectInvoices_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CCClear_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface CCClear_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
      @param inTranDate
      @param inTranTime
      @param inTranNum
   */  
export interface CCLoadCardNumbers_input{
   ds:Erp_Tablesets_CashRecTableset[],
      /**  TranDate from the CreditTran table  */  
   inTranDate:string,
      /**  TranTime from the CreditTran table  */  
   inTranTime:number,
      /**  TranNum from the CreditTran table  */  
   inTranNum:number,
}

export interface CCLoadCardNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
      @param inTranDate
      @param inTranTime
      @param inTranNum
   */  
export interface CCLoadTranData_input{
   ds:Erp_Tablesets_CashRecTableset[],
      /**  TranDate from the CreditTran table  */  
   inTranDate:string,
      /**  TranTime from the CreditTran table  */  
   inTranTime:number,
      /**  TranNum from the CreditTran table  */  
   inTranNum:number,
}

export interface CCLoadTranData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param inTranType
      @param ds
   */  
export interface CCProcessCard_input{
      /**  The transaction type to apply to the credit card.
            Valid transaction types : D (Deposit), S (Sale), A (Authorize),
            C (Credit - 803), V (Void).  */  
   inTranType:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface CCProcessCard_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param unAppliedAmt
      @param forceDiscount
      @param ds
   */  
export interface CalcAllocAmount_input{
   unAppliedAmt:number,
   forceDiscount:boolean,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface CalcAllocAmount_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param ipAllocAmt
      @param ds
   */  
export interface CalcCashApDiscount_input{
   ipAllocAmt:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface CalcCashApDiscount_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param ipAmtToAlloc
      @param LastDiscount
      @param forceDiscount
      @param ds
   */  
export interface CalcDiscount_input{
   ipAmtToAlloc:number,
   LastDiscount:boolean,
   forceDiscount:boolean,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface CalcDiscount_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param docUnappliedAmount
      @param ds
   */  
export interface CalcSelectedInvcTotal_input{
   docUnappliedAmount:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface CalcSelectedInvcTotal_output{
parameters : {
      /**  output parameters  */  
   newUnappliedAmount:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param ipGroupID
      @param ds
   */  
export interface CalcTaxRecNumber_input{
      /**  Group ID  */  
   ipGroupID:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface CalcTaxRecNumber_output{
parameters : {
      /**  output parameters  */  
   opLegalNumMsg:string,
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param proposedDocTranAmt
      @param proposedDocWriteOffAmount
      @param fieldName
      @param answer
      @param ds
   */  
export interface CashDtl_DocTranAmt_OnChanging_input{
   proposedDocTranAmt:number,
   proposedDocWriteOffAmount:number,
   fieldName:string,
   answer:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface CashDtl_DocTranAmt_OnChanging_output{
parameters : {
      /**  output parameters  */  
   question:string,
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param payDay
      @param CustNum
      @param CurrencyCode
      @param tranDate
      @param CentralCollection
      @param headNum
      @param invoiceNum
      @param legalNumber
   */  
export interface CashRecGetInvoicesCCExt_input{
   payDay:string,
   CustNum:number,
   CurrencyCode:string,
   tranDate:string,
   CentralCollection:boolean,
   headNum:number,
   invoiceNum:number,
   legalNumber:string,
}

export interface CashRecGetInvoicesCCExt_output{
   returnObj:Erp_Tablesets_ARInvcAllocTableset[],
}

   /** Required : 
      @param payDay
      @param CustNum
      @param CurrencyCode
      @param tranDate
      @param CentralCollection
   */  
export interface CashRecGetInvoicesCC_input{
      /**  Payment date.  */  
   payDay:string,
      /**  CustNum to get Customer list  */  
   CustNum:number,
      /**  Currency Code used for the CashHed  */  
   CurrencyCode:string,
      /**  Transaction date.  */  
   tranDate:string,
      /**  Central Collection.  */  
   CentralCollection:boolean,
}

export interface CashRecGetInvoicesCC_output{
   returnObj:Erp_Tablesets_ARInvcAllocTableset[],
}

   /** Required : 
      @param payDay
      @param CustNum
      @param CurrencyCode
      @param tranDate
      @param headNum
      @param invoiceNum
      @param legalNumber
   */  
export interface CashRecGetInvoicesExt_input{
   payDay:string,
   CustNum:number,
   CurrencyCode:string,
   tranDate:string,
   headNum:number,
   invoiceNum:number,
   legalNumber:string,
}

export interface CashRecGetInvoicesExt_output{
   returnObj:Erp_Tablesets_ARInvcAllocTableset[],
}

   /** Required : 
      @param payDay
      @param CustNum
      @param CurrencyCode
      @param tranDate
   */  
export interface CashRecGetInvoices_input{
      /**  Payment date.  */  
   payDay:string,
      /**  CustNum to get Customer list if National Accounts are enabled  */  
   CustNum:number,
      /**  Currency Code used for the CashHed  */  
   CurrencyCode:string,
      /**  Transaction date.  */  
   tranDate:string,
}

export interface CashRecGetInvoices_output{
   returnObj:Erp_Tablesets_ARInvcAllocTableset[],
}

   /** Required : 
      @param ds
   */  
export interface ChangeBankAmount_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeBankAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param exchangeRate
      @param ds
   */  
export interface ChangeBankExchangeRate_input{
      /**  The exchange rate from Bank currency to Base currency  */  
   exchangeRate:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeBankExchangeRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param exchangeRate
      @param ds
   */  
export interface ChangeBankReceiptExgRate_input{
      /**  The exchange rate from Receipt currency to Bank currency  */  
   exchangeRate:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeBankReceiptExgRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeCCAmounts_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeCCAmounts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ipExpMonth
      @param ipExpYear
      @param ds
   */  
export interface ChangeCreditExp_input{
      /**  Expiration Month  */  
   ipExpMonth:number,
      /**  Expiration Year  */  
   ipExpYear:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeCreditExp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param dnAmount
      @param ds
   */  
export interface ChangeDNAmount_input{
      /**  Proposed Debit Note Value  */  
   dnAmount:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeDNAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeReceiptAmt_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeReceiptAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param currencyCode
      @param ds
   */  
export interface ChangeReceiptCurrency_input{
      /**  Proposed Currency Code  */  
   currencyCode:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeReceiptCurrency_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param exchangeRate
      @param ds
   */  
export interface ChangeSettlementExgRate_input{
      /**  The exchange rate from Receipt currency to settlement currency  */  
   exchangeRate:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeSettlementExgRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param taxWhld
      @param ds
   */  
export interface ChangeTaxWhld_input{
      /**  Withhold tax amount withheld by the customer  */  
   taxWhld:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeTaxWhld_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ipTranAmtType
      @param proposedTranAmt
      @param ds
   */  
export interface ChangeTranAmtCashHead2_input{
      /**  Indicate which of the transaction amount is changed.
            Valid values are: 'B' for Base Tran Amount and 'D' for Doc Tran Amount  */  
   ipTranAmtType:string,
      /**  The proposed Transaction Amount  */  
   proposedTranAmt:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeTranAmtCashHead2_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ipTranAmtType
      @param proposedTranAmt
      @param ds
   */  
export interface ChangeTranAmtCashHead_input{
      /**  Indicate which of the transaction amount is changed.
            Valid values are: 'B' for Base Tran Amount and 'D' for Doc Tran Amount  */  
   ipTranAmtType:string,
      /**  The proposed Transaction Amount  */  
   proposedTranAmt:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeTranAmtCashHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
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
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ChangeTranAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param custID
   */  
export interface CheckCustomerTaxID_input{
   custID:string,
}

export interface CheckCustomerTaxID_output{
parameters : {
      /**  output parameters  */  
   errMessage:string,
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
      @param ipDate
   */  
export interface CheckIfNonBusinessDay_input{
   ipDate:string,
}

export interface CheckIfNonBusinessDay_output{
parameters : {
      /**  output parameters  */  
   opIfBusinessDay:boolean,
}
}

   /** Required : 
      @param groupID
      @param headNum
      @param ds
   */  
export interface ClearInvoiceAlloc_input{
   groupID:string,
   headNum:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface ClearInvoiceAlloc_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param pcGroupID
      @param useDisc
      @param allowNegReceipts
      @param ds
   */  
export interface CreateChecks_input{
      /**  Cash Receipt Group ID  */  
   pcGroupID:string,
      /**  Yes or no  */  
   useDisc:boolean,
      /**  Yes or no  */  
   allowNegReceipts:boolean,
   ds:Erp_Tablesets_ARInvSelTableset[],
}

export interface CreateChecks_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvSelTableset[],
   opTotalCashReceived:number,
   opTotalApplied:number,
   opUnappliedBalance:number,
   opTotalMisc:number,
   opTotalDiscount:number,
   opTotalDeposit:number,
   opTotalARAmount:number,
   opTotalWithhold:number,
   opTotalWriteOff:number,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
   */  
export interface CreateNewDebitNote_input{
   ds:Erp_Tablesets_CashRecTableset[],
      /**  Cash Group ID  */  
   groupID:string,
      /**  Cash Receipt HeadNum  */  
   headNum:number,
}

export interface CreateNewDebitNote_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param custNum
   */  
export interface CustListPayFor_input{
   custNum:number,
}

export interface CustListPayFor_output{
parameters : {
      /**  output parameters  */  
   whereClauseForCustomers:string,
}
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
      @param ds
      @param inHeadNum
   */  
export interface DeleteMasterBankRec_input{
   ds:Erp_Tablesets_CashRecTableset[],
   inHeadNum:number,
}

export interface DeleteMasterBankRec_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
      @param pcGroupID
      @param ipHeadNum
   */  
export interface DeleteMaster_input{
   ds:Erp_Tablesets_CashRecTableset[],
      /**  current CashGrp GroupID  */  
   pcGroupID:string,
      /**  Cash Header HeadNum  */  
   ipHeadNum:string,
}

export interface DeleteMaster_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
   opTotalCashReceived:number,
   opTotalApplied:number,
   opUnappliedBalance:number,
   opTotalMisc:number,
   opTotalDiscount:number,
   opTotalDeposit:number,
   opTotalARAmount:number,
   opTotalWithhold:number,
   opTotalWriteOff:number,
}
}

   /** Required : 
      @param pcGroupID
   */  
export interface DeleteNegativeReceipts_input{
      /**  Cash Receipt Group ID  */  
   pcGroupID:string,
}

export interface DeleteNegativeReceipts_output{
}

   /** Required : 
      @param dnCustNbr
      @param ds
   */  
export interface EnterCustDebNote_input{
      /**  Proposed Debit Note Number  */  
   dnCustNbr:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface EnterCustDebNote_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

export interface Erp_Tablesets_ARInvSelRow{
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
      /**  Amount of the next schedule due. This amount is calculated based on the Cash Receipt Transaction Apply Date and the Due Dates of each payment of the Payment Schedule of the invoice.  */  
   AmountDue:number,
      /**  The amount of the payment to apply to the invoice  */  
   ApplyAmt:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
   BankNetPay:number,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  This external field captures the IMCashGrp.GroupID used in object BankFileImport.p  */  
   CashGroupID:string,
   DiscAmt:number,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
      /**  This new column should display payment discount amounts for invoices that are still within discount terms  */  
   Discount:number,
   DiscountAvailable:boolean,
      /**  Amount of the next schedule due. This amount is calculated based on the Cash Receipt Transaction Apply Date and the Due Dates of each payment of the Payment Schedule of the invoice.  */  
   DocAmountDue:number,
   DocDiscAmt:number,
   DocGrossPay:number,
   DocNetPay:number,
      /**  Due Date should be higthlighted if number of business days between selection date and invoice due date is less that 2 (for subsequent recurrent payment type) or 5 (for one-off or first recurrent payment types) days  */  
   DueDateHighLighted:boolean,
   GrossPay:number,
   IsCreditMemo:boolean,
      /**  DueDate from Select Invoices dialog.  */  
   PmtDueDate:string,
   Rpt1DiscAmt:number,
   Rpt1GrossPay:number,
   Rpt2DiscAmt:number,
   Rpt2GrossPay:number,
   Rpt3DiscAmt:number,
   Rpt3GrossPay:number,
   Selected:boolean,
      /**  Taxable Write Off  */  
   TaxableWriteOff:boolean,
      /**  Write Off  */  
   WriteOff:boolean,
      /**  Write Off Account  */  
   WriteOffAccount:string,
      /**  Write Off Account Description  */  
   WriteOffAccountDesc:string,
      /**  Write Off Amount  */  
   WriteOffAmount:number,
      /**  Allows uset to enter comment for Write Off.  */  
   WriteOffComment:string,
      /**  This new column should enable the user to enter a draft payment amount ? a part of the check amount that is to be allocated to the invoice  */  
   AllocAmount:number,
   BitFlag:number,
   CustomerCustID:string,
   CustomerBTName:string,
   CustomerName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARInvSelTGLCRow{
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
      /**  InvoiceNum of ARInvcSel  */  
   InvoiceNum:number,
   BitFlag:number,
   COADescription:string,
   GLAccountAccountDesc:string,
   GLAccountGLShortAcct:string,
   GLAccountGLAcctDisp:string,
   GLBookCurrencyCode:string,
   GLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARInvSelTableset{
   ARInvSel:Erp_Tablesets_ARInvSelRow[],
   ARInvSelTGLC:Erp_Tablesets_ARInvSelTGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARInvcAllocRow{
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
   AdjustAmtTax:number,
      /**  This new column should enable the user to enter a draft payment amount ? a part of the check amount that is to be allocated to the invoice  */  
   AllocAmount:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
      /**  Indicates that negative Write Off could be applied for AR Invoices.  */  
   AllowNegativeWriteOff:boolean,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Indicates that AR Invoices can be overpaid.  */  
   AllowOverpaidInv:boolean,
      /**  Amount of the next schedule due. This amount is calculated based on the Cash Receipt Transaction Apply Date and the Due Dates of each payment of the Payment Schedule of the invoice.  */  
   AmountDue:number,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
      /**  when InvcHead.PIPayment = O then populate ARPaymentInstrumentID with a value of PI.  */  
   ARPromNoteID:string,
      /**  Calculates the revised invoice balance after specifying an allocated amount.  */  
   CalcDocUnpostedBal:number,
      /**  This column should display the Allocated amount less Discount amount (automatically calculated).  */  
   CashApplied:number,
      /**  Currency Decimals General  */  
   CurrDecGeneral:number,
      /**  Deposit balance from CashHed  */  
   DepBal:number,
      /**  This new column should display payment discount amounts for invoices that are still within discount terms  */  
   Discount:number,
      /**  Flags in this new column should mark invoices that are still within discount terms  */  
   DiscountApplicable:boolean,
   DiscountPercent:number,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   DispBalDN:number,
   DisplayCurrencyID:string,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   DNPmtAmt:number,
      /**  Total Debit Notes applied  */  
   DocTotalDN:number,
      /**  Display deposit balance.  */  
   DspDepBal:number,
      /**  Display document deposit balance  */  
   DspDocDepBal:number,
      /**  Display document invoice amount  */  
   DspDocInvoiceAmt:number,
      /**  Display document invoice balance  */  
   DspDocInvoiceBal:number,
      /**  Display invoice amount  */  
   DspInvoiceAmt:number,
      /**  Display Invoice Balance.  */  
   DspInvoiceBal:number,
      /**  It will be displayed to identify invoices automatically generated due ERS shipments.  */  
   ERSInvoice:boolean,
      /**  Invoice with negative balance.  */  
   InvcNegBal:boolean,
      /**  Flags in this new column should mark invoices that are selected to be applied to the check  */  
   InvcSelected:boolean,
   IsDiscountforCreditM:boolean,
      /**  Set to true if Manually added taxes exist  */  
   ManAddTaxesExist:boolean,
      /**  This field is to display in Cash Receipt Entry the Discount Date that the payment will take.  */  
   NextDiscDate:string,
      /**  The original discount amount.  Used when manual taxes were added, in which case amounts cannot be changed.  The discount applied in this case must be the same as the orignal discoun  */  
   OriginalDiscount:number,
      /**  Pack slip number from the 1st line item.  */  
   PackSlipNum:number,
      /**  Sold to customer id  */  
   SoldToCustID:string,
      /**  Sold to customer name.  */  
   SoldToCustomerName:string,
      /**  Taxable Write Off  */  
   TaxableWriteOff:boolean,
      /**  Indicates if the invoice has withholding tax calculated at full or partial payment  */  
   WithholdTaxCalcPay:boolean,
      /**  Write Off  */  
   WriteOff:boolean,
      /**  Write Off Account  */  
   WriteOffAccount:string,
      /**  Write Off Account Description  */  
   WriteOffAccountDesc:string,
      /**  Write Off Amount  */  
   WriteOffAmount:number,
      /**  Allows uset to enter comment for Write Off.  */  
   WriteOffComment:string,
      /**  Document deposit amount from cashhead.  */  
   DocDepBal:number,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   DocDispBalDN:number,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   DocDNPmtAmt:number,
      /**  The adjustment  to  allocate amount  in case of WH taxes are posted through interim account for AR Invoice.  */  
   WhInterimAdj:number,
      /**  Technical field not for display. Flag determine applied invoice or not.  */  
   Apply:boolean,
   BitFlag:number,
   CustomerCustID:string,
   CustomerName:string,
   CustomerBTName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARInvcAllocTGLCRow{
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
      /**  InvoiceNum of ARInvcAlloc  */  
   InvoiceNum:number,
      /**  Technical field not for display. Flag determine applied invoice or not.  */  
   Apply:boolean,
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

export interface Erp_Tablesets_ARInvcAllocTableset{
   ARInvcAlloc:Erp_Tablesets_ARInvcAllocRow[],
   ARInvcAllocTGLC:Erp_Tablesets_ARInvcAllocTGLCRow[],
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

export interface Erp_Tablesets_CDTaxDtlRow{
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
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
      /**  Group ID - used to link to Cash Head  */  
   GroupID:string,
   CTDescription:string,
      /**  Flag to indicate if Manual checkbox should be Read Only  */  
   DisableManual:boolean,
   EnableTax:boolean,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  */  
   GroupID:string,
      /**  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  */  
   HeadNum:number,
      /**  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  */  
   InvoiceNum:number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   InvoiceRef:number,
      /**   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  */  
   TranType:string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  */  
   FiscalPeriod:number,
      /**  Indicates if this transaction has been posted to the General Ledger Module.  */  
   GLPosted:boolean,
      /**  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  */  
   TranDate:string,
      /**   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   CheckRef:string,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  */  
   TranAmt:number,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  */  
   DocTranAmt:number,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   CustNum:number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   Discount:number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   DocDiscount:number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  */  
   Comment:string,
      /**  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  */  
   Reference:string,
      /**   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
      /**  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  */  
   DebitNote:boolean,
      /**  Debit Note Detail Comments.  */  
   DNComments:string,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   DNAmount:number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   DocDnAmount:number,
      /**  The Debit Note Number assigned by the customer.  */  
   DNCustNbr:string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   RoundDiff:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Fiscal Year Suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
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
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Tax Amount in the vendors currency.  */  
   DocTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Red Storno Flag  */  
   RedStorno:boolean,
      /**  Tax Receipt Date (Thailand Localization)  */  
   TaxReceiptDate:string,
      /**  Tax Receipt No. (Thailand Localization)  */  
   TaxReceiptNo:string,
      /**  Withholding Tax Certificate Date  (Thailand Localization)  */  
   WHTCertificateDate:string,
      /**  Withholding Tax Certificate No. (Thailand Localization)  */  
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
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Tax Remarks  */  
   TaxRemarks:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
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
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  SEPADDMsgID  */  
   SEPADDMsgID:string,
      /**  SEPADDPmtID  */  
   SEPADDPmtID:string,
      /**  PmtDueDate  */  
   PmtDueDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  MX Payment Number for AR Invoice  */  
   MXPaymentNum:number,
      /**  Reference to HeadNum of main CashHead record.  */  
   WriteOffHeadNumRef:number,
      /**  EpicorFSA  */  
   EpicorFSA:boolean,
      /**  Taxable Adjustment  */  
   TaxableAdjustment:boolean,
   ApplyDate:string,
      /**  Adjustment amount in Base Currency  */  
   BaseAdjAmt:number,
   BaseCurrDesc:string,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  */  
   BillConNum:number,
      /**  If this flag is true the AR Invoice exchange rates is used when the Adjustment is applied and no currency Gain/Loss is calculated  */  
   CopyRate:boolean,
      /**  Indicates if invoice related to  this detail line is Correction invoice with negatice balance  */  
   CorrectionInv:boolean,
   CreditMemo:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencyDescription:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol  */  
   CurrSymbol:string,
      /**  This field displays all Debit Note customer defined numbers applied.  */  
   DebitNotesApplied:string,
   DispDocSelfAssessAmt:number,
   DispDocWithholdAmt:number,
      /**  Display gl account  */  
   DispGLAcct:string,
   DispSelfAssessAmt:number,
   DispTranAmt:number,
   DispWithholdAmt:number,
   DocDispTranAmt:number,
      /**  Doc Invoice Amount  */  
   DocInvoiceAmt:number,
      /**  Doc Invoice Balance  */  
   DocInvoiceBal:number,
   DocNetCash:number,
      /**  Doc New Invoice Balance  */  
   DocNewBalance:number,
      /**  Write Off Amount  */  
   DocWriteOffAmount:number,
      /**  If this flag is true then CopyRate checkbox is Read Only  */  
   DsblCopyRate:boolean,
      /**  Legal Number Field  */  
   EnableAssignLegNum:boolean,
   EnableTranDocType:boolean,
      /**  Legal Number Field  */  
   EnableVoidLegNum:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   FullyPaid:boolean,
   GainLossAmt:number,
      /**  G/L Reference Code Description  */  
   GLRefCodeDesc:string,
      /**  Legal Number Field  */  
   HasLegNumCnfg:boolean,
   InvDiscountDate:string,
   InvDueDate:string,
      /**  Invoice Exchange Rate  */  
   InvExchRate:number,
   InvLegalNumber:string,
   InvLockRate:boolean,
      /**  Invoice Amount  */  
   InvoiceAmt:number,
      /**  Invoice Balance  */  
   InvoiceBal:number,
   InvTermsCode:string,
   InvXRateLabel:string,
      /**  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  */  
   IsCreditPayment:boolean,
   IsDiscountforCreditM:boolean,
   LegalNumMessage:string,
   LegalNumStyle:string,
   NetCash:number,
      /**  New Invoice Balance  */  
   NewBalance:number,
   OldGainLoss:number,
      /**  The related order number (InvcHead.OrderNum)  */  
   OrderNum:number,
      /**  Processing company's Reference ID, unique to each transaction  */  
   PNRef:string,
      /**  Indicates if posting GL transactions  */  
   PostToGL:boolean,
      /**  Whether to recalculate the CashDtl.TranAmt and all related columns prior to saving.  */  
   RecalcTranAmt:boolean,
   RedStornoOpt:string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   RefCodeStatus:string,
      /**  This will indicate the information on this CashDtl record will not be included in the Cash Receipt Adjustment.  */  
   RemoveForAdjustment:boolean,
   Rpt1DispTranAmt:number,
   Rpt1GainLossAmt:number,
   Rpt1InvoiceAmt:number,
   Rpt1InvoiceBal:number,
   Rpt1NetCash:number,
   Rpt1NewBalance:number,
   Rpt1OldGainLoss:number,
      /**  Write Off Amount  */  
   Rpt1WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   Rpt1WriteOffGainLossAmt:number,
   Rpt2DispTranAmt:number,
   Rpt2GainLossAmt:number,
   Rpt2InvoiceAmt:number,
   Rpt2InvoiceBal:number,
   Rpt2NetCash:number,
   Rpt2NewBalance:number,
   Rpt2OldGainLoss:number,
      /**  Write Off Amount  */  
   Rpt2WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   Rpt2WriteOffGainLossAmt:number,
   Rpt3DispTranAmt:number,
   Rpt3GainLossAmt:number,
   Rpt3InvoiceAmt:number,
   Rpt3InvoiceBal:number,
   Rpt3NetCash:number,
   Rpt3NewBalance:number,
   Rpt3OldGainLoss:number,
      /**  Write Off Amount  */  
   Rpt3WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   Rpt3WriteOffGainLossAmt:number,
      /**  CustID associated with CashDtl.SoldToCustNum  */  
   SoldToCustID:string,
      /**  Populated from InvcHead.SoldToCustNum.  */  
   SoldToCustNum:number,
      /**  CustName associated with CashDtl.SoldToCustNum  */  
   SoldToCustomerName:string,
      /**  Legal Number Field  */  
   SystemTranType:string,
      /**  Description of the Tran Type  */  
   TranTypeDesc:string,
      /**  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  */  
   Type:string,
      /**  Write Off  */  
   WriteOff:boolean,
      /**  Write Off Account  */  
   WriteOffAccount:string,
      /**  Write Off Account Description  */  
   WriteOffAccountDesc:string,
      /**  Write Off Amount  */  
   WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   WriteOffGainLossAmt:number,
   XRateLabel:string,
      /**  Legal Number Field  */  
   AllowChgAfterPrint:boolean,
      /**  Write Off Amount  */  
   OldWriteOffAmount:number,
   WriteOffAccountDisp:string,
   TaxableWriteOff:boolean,
      /**  Total Gain Loss Amount  */  
   TotalGainLossAmt:number,
      /**  Write Off Amount  */  
   OldWriteOffGainLossAmt:number,
      /**  Write Off Amount  */  
   Rpt1OldWriteOffGainLossAmt:number,
      /**  Write Off Amount  */  
   Rpt2OldWriteOffGainLossAmt:number,
      /**  Write Off Amount  */  
   Rpt3OldWriteOffGainLossAmt:number,
      /**  Total Gain Loss Amount  */  
   Rpt1TotalGainLossAmt:number,
      /**  Total Gain Loss Amount  */  
   Rpt2TotalGainLossAmt:number,
      /**  Total Gain Loss Amount  */  
   Rpt3TotalGainLossAmt:number,
      /**  Write Off Amount  */  
   DocOldWriteOffAmount:number,
      /**  Write Off Amount  */  
   Rpt1OldWriteOffAmount:number,
      /**  Write Off Amount  */  
   Rpt2OldWriteOffAmount:number,
      /**  Write Off Amount  */  
   Rpt3OldWriteOffAmount:number,
      /**  Allows uset to enter comment for Write Off.  */  
   WriteOffComment:string,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
   ReferenceTranDate:string,
   ReferenceTranNum:number,
   ReferenceTranTime:number,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   EnableManualWHTax:boolean,
      /**  Indicates if the withholding amount tax was manually modified.  */  
   WHTaxManualChange:boolean,
   BitFlag:number,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   InvoiceNumInvoiceType:string,
   InvoiceNumCardMemberName:string,
   InvoiceNumTermsCode:string,
   RateGrpDescription:string,
   TaxRgnDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashDtlTGLCRow{
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
      /**  HeadNum of CashDtl  */  
   HeadNum:number,
      /**  InvoiceNum of CashDtl  */  
   InvoiceNum:number,
      /**  InvoiceRef of CashDtl  */  
   InvoiceRef:number,
      /**  GroupID of CashDtl  */  
   GroupID:string,
   CDSeqNum:number,
   BitFlag:number,
   COADescription:string,
   GLAccountGLShortAcct:string,
   GLAccountGLAcctDisp:string,
   GLAccountAccountDesc:string,
   GLBookCurrencyCode:string,
   GLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashHeadAttchRow{
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

export interface Erp_Tablesets_CashHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   GroupID:string,
      /**  Displays the receipt header number used for internal reference.  */  
   HeadNum:number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Displays the transaction type.  */  
   TranType:string,
      /**  Displays the number of the check.  */  
   CheckRef:string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   OrderNum:number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   InvoiceNum:number,
      /**  Displays the transaction amount.  */  
   TranAmt:number,
      /**  Displays the transaction amount in customer currency.  */  
   DocTranAmt:number,
      /**  Displays the customer ID.  */  
   CustID:string,
      /**  Displays the date of the transaction.  */  
   TranDate:string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   CustNum:number,
      /**  Displays the unapplied amount.  */  
   UnAppliedAmt:number,
      /**  Displays the unapplied amount in base currency.  */  
   DocUnAppliedAmt:number,
      /**  Displays the amount applied to invoices.  */  
   AppliedAmt:number,
      /**  Displays the amount in document currency applied to invoices.  */  
   DocAppliedAmt:number,
      /**  Displays the fiscal year that the check is posted to.  */  
   FiscalYear:number,
      /**  Displays the fiscal period that the check is posted to.  */  
   FiscalPeriod:number,
      /**  Displays any reference.  */  
   Reference:string,
      /**  Indicates if this transaction has been posted.  */  
   GLPosted:boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   CreditMemoNum:number,
      /**  Displays the customer currency.  */  
   CurrencyCode:string,
      /**  Displays the exchange rate that is used for this check.  */  
   ExchangeRate:number,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Displays the tax amount.  */  
   DocTaxAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Displays the legal number of the check.  */  
   LegalNumber:string,
      /**  External ID  */  
   ExternalID:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
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
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   CCAmount:number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   CCFreight:number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   CCTax:number,
      /**  Total amount being sent to the credit card processor  */  
   CCTotal:number,
      /**  See CCAmount  */  
   CCDocAmount:number,
      /**  See CCFreight  */  
   CCDocFreight:number,
      /**  See CCTax  */  
   CCDocTax:number,
      /**  See CCTotal  */  
   CCDocTotal:number,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   DebNoteOnly:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3AppliedAmt:number,
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
      /**  Reporting currency value of this field  */  
   Rpt1UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnAppliedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  See CCAmount  */  
   Rpt1CCAmount:number,
      /**  See CCAmount  */  
   Rpt2CCAmount:number,
      /**  See CCAmount  */  
   Rpt3CCAmount:number,
      /**  See CCFreight  */  
   Rpt1CCFreight:number,
      /**  See CCFreight  */  
   Rpt2CCFreight:number,
      /**  See CCFreight  */  
   Rpt3CCFreight:number,
      /**  See CCTax  */  
   Rpt1CCTax:number,
      /**  See CCTax  */  
   Rpt2CCTax:number,
      /**  See CCTax  */  
   Rpt3CCTax:number,
      /**  See CCTotal  */  
   Rpt1CCTotal:number,
      /**  See CCTotal  */  
   Rpt2CCTotal:number,
      /**  See CCTotal  */  
   Rpt3CCTotal:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
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
      /**  The unique code of Receipt Currency.  */  
   ReceiptCurrencyCode:string,
      /**  Amount of Receipt in Receipt Currency.  */  
   ReceiptAmt:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   BankRcptExchangeRate:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   SettlementExchangeRate:number,
      /**  The unique Currency code for Credit Memo.  */  
   CMCurrencyCode:string,
      /**  Amount of Credit Memo in CM Currency.  */  
   CMAmount:number,
      /**  Reference to cash receipt which had been reversed.  */  
   ReverseRef:number,
      /**  Date when cash receipt had been reversed  */  
   ReverseDate:string,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Withhold Tax  */  
   TaxWhld:number,
      /**  Dsicount Date  */  
   DiscountDate:string,
      /**  Calculate Withhold Tax  */  
   TaxWhldCalc:number,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   DocUnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   Rpt1UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   Rpt2UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   Rpt3UnallocatedAmt:number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   ApplyHeadNum:number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   DocAllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   Rpt1AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   Rpt2AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   Rpt3AllocatedAmt:number,
      /**  Comments related to the cash receipt.  */  
   Comment:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Tax Remarks  */  
   TaxRemarks:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
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
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  Payee  */  
   Payee:string,
      /**  AccountNumber  */  
   AccountNumber:string,
      /**  OtherDetails  */  
   OtherDetails:string,
      /**  MandateReference  */  
   MandateReference:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SEPADDExportDate  */  
   SEPADDExportDate:string,
      /**  BOE Invoice Number  */  
   BOEInvoiceNum:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  OwnReference  */  
   OwnReference:string,
      /**  DocumentType  */  
   DocumentType:string,
      /**  ABTUID  */  
   ABTUID:string,
      /**  BankRcptExchangeRate10D  */  
   BankRcptExchangeRate10D:number,
      /**  SettlementExchangeRate10D  */  
   SettlementExchangeRate10D:number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   BankBatchExcluded:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  PayMethodReference  */  
   PayMethodReference:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   MXFiscalFolio:string,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   AllowUpdSettlementCurr:boolean,
   ApplyDate:string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSAddr:string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSZip:string,
   BankAcctDesc:string,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Bank Currency Value  */  
   BankAmount:number,
   BankBaseXRateLabel:string,
   BankCurrencyCode:string,
      /**  Bank Currency Symbol  */  
   BankCurrSymbol:string,
   BankExchangeRate:number,
   BankRcptXRateLabel:string,
   BaseCurrencyCode:string,
   BaseCurrSymbol:string,
      /**  Bill To Name  */  
   BillToName:string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   calcRate:boolean,
      /**  Stored Credit Card Number  */  
   CardStore:string,
      /**  The credit card description. For example, American Express, Visa, Master Card, Discover, etc.  */  
   CardTypeDescription:string,
      /**  Description  */  
   CashbookLineDescription:string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   CCAllowSales:boolean,
   CCApprovalNum:string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   CCCSCID:string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   CCEnableAddress:boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   CCEnableCSC:boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   CCResponse:string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   CCTranID:string,
      /**  Credit Card Transaction Type  */  
   CCTranType:string,
      /**  Description of the currency  */  
   CMCurrencyCodeCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CMCurrencyCodeCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CMCurrencyCodeCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CMCurrencyCodeCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CMCurrencyCodeDocumentDesc:string,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   CSCResult:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
   CurrencySwitch:boolean,
   CustFullAddr:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
   CustomerName:string,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocDiscount:number,
   DocReceipt:number,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   DocumentNum:number,
      /**  Amount of Credit Memo in CM Currency.  */  
   DspCMAmount:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user enters this amount and then it is used as a limit/control when applying it to the invoices.  */  
   DspDocTranAmt:number,
   DspSalesOrderValue:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   DspTranAmt:number,
   EnableTransactionDate:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   FullyPaid:boolean,
      /**  The InvcHead legal number  */  
   InvcLegalNumber:string,
      /**  The member's name on the credit card.  */  
   InvoiceNumCardMemberName:string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   InvoiceNumTermsCode:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumberDsp:string,
   LegalNumMessage:string,
      /**  Copied from OrderHed.LockRate  */  
   LockRate:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
   PaymentMethod:string,
      /**  Description  */  
   RateGrpDescription:string,
      /**  Description of the currency  */  
   RcptCurrencyCodeCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   RcptCurrencyCodeCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   RcptCurrencyCodeCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   RcptCurrencyCodeCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   RcptCurrencyCodeDocumentDesc:string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   ReferencePNRef:string,
      /**  Transaction Amount less Tax Amount  */  
   Rpt1TranTaxAmt:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt2TranTaxAmt:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt3TranTaxAmt:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   SalesOrderValue:number,
   SettlementXRateLabel:string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   SoldToCustomerName:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionCodeDescription:string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   TotalRoundDiff:number,
      /**  Transaction Amount less Tax Amount  */  
   TranTaxAmt:number,
      /**  Description of TranType  */  
   TranTypeDesc:string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   UnappliedAmountApplied:boolean,
   XRateLabel:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashHeadListTableset{
   CashHeadList:Erp_Tablesets_CashHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   GroupID:string,
      /**  Displays the receipt header number used for internal reference.  */  
   HeadNum:number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Displays the transaction type.  */  
   TranType:string,
      /**  Displays the number of the check.  */  
   CheckRef:string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   OrderNum:number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   InvoiceNum:number,
      /**  Displays the transaction amount.  */  
   TranAmt:number,
      /**  Displays the transaction amount in customer currency.  */  
   DocTranAmt:number,
      /**  Displays the customer ID.  */  
   CustID:string,
      /**  Displays the date of the transaction.  */  
   TranDate:string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   CustNum:number,
      /**  Displays the unapplied amount.  */  
   UnAppliedAmt:number,
      /**  Displays the unapplied amount in base currency.  */  
   DocUnAppliedAmt:number,
      /**  Displays the amount applied to invoices.  */  
   AppliedAmt:number,
      /**  Displays the amount in document currency applied to invoices.  */  
   DocAppliedAmt:number,
      /**  Displays the fiscal year that the check is posted to.  */  
   FiscalYear:number,
      /**  Displays the fiscal period that the check is posted to.  */  
   FiscalPeriod:number,
      /**  Displays any reference.  */  
   Reference:string,
      /**  Indicates if this transaction has been posted.  */  
   GLPosted:boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   CreditMemoNum:number,
      /**  Displays the customer currency.  */  
   CurrencyCode:string,
      /**  Displays the exchange rate that is used for this check.  */  
   ExchangeRate:number,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Displays the tax amount.  */  
   DocTaxAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Displays the legal number of the check.  */  
   LegalNumber:string,
      /**  External ID  */  
   ExternalID:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
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
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   CCAmount:number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   CCFreight:number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   CCTax:number,
      /**  Total amount being sent to the credit card processor  */  
   CCTotal:number,
      /**  See CCAmount  */  
   CCDocAmount:number,
      /**  See CCFreight  */  
   CCDocFreight:number,
      /**  See CCTax  */  
   CCDocTax:number,
      /**  See CCTotal  */  
   CCDocTotal:number,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   DebNoteOnly:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3AppliedAmt:number,
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
      /**  Reporting currency value of this field  */  
   Rpt1UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnAppliedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  See CCAmount  */  
   Rpt1CCAmount:number,
      /**  See CCAmount  */  
   Rpt2CCAmount:number,
      /**  See CCAmount  */  
   Rpt3CCAmount:number,
      /**  See CCFreight  */  
   Rpt1CCFreight:number,
      /**  See CCFreight  */  
   Rpt2CCFreight:number,
      /**  See CCFreight  */  
   Rpt3CCFreight:number,
      /**  See CCTax  */  
   Rpt1CCTax:number,
      /**  See CCTax  */  
   Rpt2CCTax:number,
      /**  See CCTax  */  
   Rpt3CCTax:number,
      /**  See CCTotal  */  
   Rpt1CCTotal:number,
      /**  See CCTotal  */  
   Rpt2CCTotal:number,
      /**  See CCTotal  */  
   Rpt3CCTotal:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
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
      /**  The unique code of Receipt Currency.  */  
   ReceiptCurrencyCode:string,
      /**  Amount of Receipt in Receipt Currency.  */  
   ReceiptAmt:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   BankRcptExchangeRate:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   SettlementExchangeRate:number,
      /**  The unique Currency code for Credit Memo.  */  
   CMCurrencyCode:string,
      /**  Amount of Credit Memo in CM Currency.  */  
   CMAmount:number,
      /**  Reference to cash receipt which had been reversed.  */  
   ReverseRef:number,
      /**  Date when cash receipt had been reversed  */  
   ReverseDate:string,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Withhold Tax  */  
   TaxWhld:number,
      /**  Dsicount Date  */  
   DiscountDate:string,
      /**  Calculate Withhold Tax  */  
   TaxWhldCalc:number,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   DocUnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   Rpt1UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   Rpt2UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   Rpt3UnallocatedAmt:number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   ApplyHeadNum:number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   DocAllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   Rpt1AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   Rpt2AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   Rpt3AllocatedAmt:number,
      /**  Comments related to the cash receipt.  */  
   Comment:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Tax Remarks  */  
   TaxRemarks:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
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
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  Payee  */  
   Payee:string,
      /**  AccountNumber  */  
   AccountNumber:string,
      /**  OtherDetails  */  
   OtherDetails:string,
      /**  MandateReference  */  
   MandateReference:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SEPADDExportDate  */  
   SEPADDExportDate:string,
      /**  BOE Invoice Number  */  
   BOEInvoiceNum:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  OwnReference  */  
   OwnReference:string,
      /**  DocumentType  */  
   DocumentType:string,
      /**  ABTUID  */  
   ABTUID:string,
      /**  BankRcptExchangeRate10D  */  
   BankRcptExchangeRate10D:number,
      /**  SettlementExchangeRate10D  */  
   SettlementExchangeRate10D:number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   BankBatchExcluded:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  PayMethodReference  */  
   PayMethodReference:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  The amount of the cash receipt applied to invoices in receipt currency  */  
   RcptCurAppliedAmt:number,
      /**  The amount of the cash receipt that is unapplied in receipt currency  */  
   RcptCurUnAppliedAmt:number,
      /**  MXAccountNumber  */  
   MXAccountNumber:string,
      /**  MX Method of Payment: single, multiple, etc.  */  
   MXPaidAs:string,
      /**  If TRUE then MX Electronic Payment XML is required  */  
   MXPaySupplementFlag:boolean,
      /**  LockboxID  */  
   LockboxID:string,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   MXFiscalFolio:string,
      /**  MX UUID of the original Receipt being corrected  */  
   MXOriginalCheckRef:string,
      /**  MX Confirmation Code for special Cash Receipts  */  
   MXConfirmationCode:string,
      /**  MX Customer’s Bank ID  */  
   MXBankID:string,
      /**  Text entered by the user to indicate the reason Cash receipt was Reversed.  */  
   ReversedReason:string,
      /**  Credit Card Holder City.  */  
   CCCity:string,
      /**  Credit Card Holder State.  */  
   CCState:string,
      /**  ccToken  */  
   ccToken:string,
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
      /**  Indicates this record is an adjustment CashHead.  */  
   Adjustment:boolean,
      /**  Reference to cash receipt which had been adjusted.  */  
   AdjustmentRef:number,
      /**  The reason for the adjustment entered by the user  */  
   AdjustmentReason:string,
      /**  Total Check Write Off Amount  */  
   WriteOffAmount:number,
      /**  DocWriteOffAmount  */  
   DocWriteOffAmount:number,
      /**  Rpt1WriteOffAmount  */  
   Rpt1WriteOffAmount:number,
      /**  Rpt2WriteOffAmount  */  
   Rpt2WriteOffAmount:number,
      /**  Rpt3WriteOffAmount  */  
   Rpt3WriteOffAmount:number,
      /**  Mexico Certified Timestamp  */  
   MXCertifiedTimestamp:string,
      /**  Mexico SAT Seal  */  
   MXSATSeal:string,
      /**  Mexico Digital Seal  */  
   MXDigitalSeal:string,
      /**  Mexico SAT Certificate Serial Number  */  
   MXSATCertificateSN:string,
      /**  Mexico Original String Timbre Fiscal Digital  */  
   MXOriginalStringTFD:string,
      /**  Mexico Certificate  */  
   MXCertificate:string,
      /**  Mexico Certificate Serial Number  */  
   MXCertificateSN:string,
      /**  SourceGroupID  */  
   SourceGroupID:string,
      /**  SourceHeadNum  */  
   SourceHeadNum:number,
      /**  Standard Entry Class Code  */  
   SEC:string,
      /**  ACH Transaction Code  */  
   ACHTranCode:number,
      /**  ID of the Customer's bank.  */  
   CustomerBankID:string,
      /**  The Bank account number for the Customer.  */  
   CustomerBankAcctNumber:string,
      /**  CustomerBankSwiftNum  */  
   CustomerBankSwiftNum:string,
      /**  The Bank account IBAN Code  */  
   CustomerBankIBANCode:string,
      /**  Name on the Bank Account.  */  
   CustomerBankNameOnAccount:string,
      /**  First address line of customer bank.  */  
   CustomerBankAddress1:string,
      /**  Second address line of customer bank.  */  
   CustomerBankAddress2:string,
      /**  Third address line of customer bank.  */  
   CustomerBankAddress3:string,
      /**  Bank City  */  
   CustomerBankCity:string,
      /**  Bank State/Prov  */  
   CustomerBankState:string,
      /**  Postal Code or zip code  */  
   CustomerBankPostalCode:string,
      /**  Bank account Country Number.  */  
   CustomerBankCountryNum:number,
      /**  ARRemittanceSlipPrinted  */  
   ARRemittanceSlipPrinted:boolean,
      /**  Customer Bank Name  */  
   CustomerBankName:string,
      /**  MXPostedTimeStamp  */  
   MXPostedTimeStamp:string,
      /**  MXSerie  */  
   MXSerie:string,
      /**  MXFolio  */  
   MXFolio:string,
      /**  MXEPaymentType  */  
   MXEPaymentType:string,
      /**  MXEPaymentCertificateNumber  */  
   MXEPaymentCertificateNumber:string,
      /**  MXEPaymentOriginalString  */  
   MXEPaymentOriginalString:string,
      /**  MXEPaymentDigitalSeal  */  
   MXEPaymentDigitalSeal:string,
      /**  Source  */  
   Source:string,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  GL Description for the Reverse process  */  
   RevDescription:string,
      /**  GL Description for AR - Apply Credit Memo  */  
   CMDescription:string,
      /**  Receipt Amount in Bank Currency  */  
   BankReceiptAmt:number,
      /**  MXCancelReasonCode  */  
   MXCancelReasonCode:string,
      /**  MXSubstHeadNum  */  
   MXSubstHeadNum:number,
      /**  MXCancellationMode  */  
   MXCancellationMode:string,
      /**  E-invoice error description.  */  
   ELIEInvException:string,
      /**  EInvoice ID  */  
   ELIEInvID:string,
      /**  E-invoice  */  
   ELIEInvoice:boolean,
      /**  E-invoice Service Provider Status  */  
   ELIEInvServiceProviderStatus:number,
      /**  E-invoice Status  */  
   ELIEInvStatus:number,
      /**  User Id of the person generated E-invoice.  */  
   ELIEInvUpdatedBy:string,
      /**  E-invoice Updated On  */  
   ELIEInvUpdatedOn:string,
      /**  Adjustment Customer Name  */  
   AdjustmentCustName:string,
      /**  Customer to which the new invoices will be applied.  */  
   AdjustmentCustNum:number,
      /**  Date the adjustment was made.  */  
   AdjustmentDate:string,
      /**  Displays the amount available to apply to the invoices.  */  
   AdjustmentDocUnAppliedAmt:number,
      /**  On Account  */  
   AdjustmentOnAccount:boolean,
      /**  Temp TranDocTypeID used when adjusting a Cash Rececipt  */  
   AdjustmentTranDocTypeID:string,
   AllocDepBal:number,
   AllowChgAfterPrint:boolean,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   AllowUpdSettlementCurr:boolean,
      /**  Amount to Allocate  */  
   AmtToAlloc:number,
   ApplyDate:string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSAddr:string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSZip:string,
      /**  Bank Currency Value  */  
   BankAmount:number,
   BankBaseXRateLabel:string,
   BankCurrencyCode:string,
      /**  Bank Currency Symbol  */  
   BankCurrSymbol:string,
   BankExchangeRate:number,
   BankRcptXRateLabel:string,
   BaseCurrencyCode:string,
      /**  Base Currency Symbol  */  
   BaseCurrSymbol:string,
      /**  Bill To Name  */  
   BillToName:string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   calcRate:boolean,
      /**  Stored Credit Card Number  */  
   CardStore:string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   CCAllowSales:boolean,
   CCApprovalNum:string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   CCCSCID:string,
      /**  Tokenized value of CSCID  */  
   CCCSCIDToken:string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   CCEnableAddress:boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   CCEnableCSC:boolean,
      /**   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  */  
   CCIsTraining:boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   CCResponse:string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   CCTranID:string,
      /**  Credit Card Transaction Type  */  
   CCTranType:string,
      /**  Check Box on the UI to filter records by Central Collection flag  */  
   CentralCollectionCheck:boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Correction Invoice with negative amount  */  
   CorrectionInv:boolean,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Credit Memo  */  
   CreditMemo:boolean,
      /**  CREProcessor is true when Credit Card Configuration is CRE Server.  */  
   CREProcessor:boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   CSCResult:string,
      /**  Current Amount Selected on Invoice Select Tab  */  
   CurrAmtSelected:number,
   CurrencySwitch:boolean,
      /**  Displays the address of the customer that paid the receipt.  */  
   CustFullAddr:string,
   CustomerName:string,
   DisableFieldsForPCashDoc:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocAllocDepBal:number,
      /**  Doc Amount to Allocate  */  
   DocAmtToAlloc:number,
      /**  Displays the discount applied to the receipt.  */  
   DocDiscount:number,
      /**  Displays the invoice amount paid by this receipt. The amount includes both discount and payment amounts.  */  
   DocReceipt:number,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   DocumentNum:number,
   DocWhldTax:number,
   DspBankBatchID:string,
      /**  Amount of Credit Memo in CM Currency.  */  
   DspCMAmount:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   DspDocTranAmt:number,
   DspSalesOrderValue:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   DspTranAmt:number,
   EnableAssignLegNum:boolean,
      /**  Indicates if the option to get the default account is enable.  */  
   EnableGetDefaultAcct:boolean,
   EnableTranDocType:boolean,
   EnableTransactionDate:boolean,
   EnableVoidLegNum:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   FullyPaid:boolean,
   GLRefCodeDescription:string,
   HasLegNumCnfg:boolean,
      /**  The InvcHead legal number  */  
   InvcLegalNumber:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumberDsp:string,
   LegalNumMessage:string,
      /**  Copied from OrderHed.LockRate  */  
   LockRate:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   ManualTaxAdj:boolean,
      /**  MXCancellationID  */  
   MXCancellationID:string,
   MXCancellationStatus:string,
      /**  MXECEPXml  */  
   MXECEPXml:string,
      /**  Mexico Calculated field - shows Check Reference number of the original Receipt being corrected  */  
   MXOriginalRefNum:string,
      /**  Host Address for the Paygate Hosted Token Service.  */  
   PayGateHostAddress:string,
      /**  NameSpace for the Paygate Hosted Token Service.  */  
   PayGateNameSpace:string,
      /**  Public Key for the Paygate Hosted Token Service EWA component.  */  
   PayGatePublicKey:string,
      /**  This column is used within cash receipt tracker to show either the receipt date or the source/ original receipt date if the cash receipt has been adjusted.  */  
   ReceiptDate:string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   ReferencePNRef:string,
   Rpt1AllocDepBal:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt1TranTaxAmt:number,
   Rpt1WhldTax:number,
   Rpt2AllocDepBal:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt2TranTaxAmt:number,
   Rpt2WhldTax:number,
   Rpt3AllocDepBal:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt3TranTaxAmt:number,
   Rpt3WhldTax:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   SalesOrderValue:number,
   SettlementXRateLabel:string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   SoldToCustomerName:string,
   SystemTranType:string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   TotalRoundDiff:number,
      /**  Transaction Amount less Tax Amount  */  
   TranTaxAmt:number,
      /**  Description of TranType  */  
   TranTypeDesc:string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   UnappliedAmountApplied:boolean,
   WhldTax:number,
   XRateLabel:string,
      /**  Displays the customer ID.  */  
   AdjustmentCustID:string,
   ReferenceTranDate:string,
   ReferenceTranNum:number,
   ReferenceTranTime:number,
      /**  Displays the address of the customer that paid the receipt with newline delimiter.  */  
   CustFullAddrFormatted:string,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   EnableManualWHTax:boolean,
      /**  Indicates if the withholding tax was manually modified.  */  
   WHTaxManualChange:boolean,
      /**  Payment type description, displayed in the Details page header.  */  
   TranTypeDescCaption:string,
   AdjustmentCustAddress:string,
      /**  Substitution Cash Receipt Group ID  */  
   MXSubstGroupId:string,
      /**  Substitution Cash Receipt CheckRef  */  
   MXSubstCheckRef:string,
      /**  Substitution Cash Receipt UUID  */  
   MXSubstFiscalFolio:string,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   CardTypeDescription:string,
   CashBHedPosted:boolean,
   CashBHedCashBookNum:number,
   CashbookLineDescription:string,
   CMCurrencyCodeDocumentDesc:string,
   CMCurrencyCodeCurrName:string,
   CMCurrencyCodeCurrSymbol:string,
   CMCurrencyCodeCurrDesc:string,
   CMCurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CustNumInactive:boolean,
   CustNumName:string,
   CustNumBTName:string,
   CustNumCustID:string,
   InvoiceNumTermsCode:string,
   InvoiceNumCardMemberName:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PCashDocDirection:string,
   PMUIDName:string,
   PMUIDMXSATCode:string,
   PMUIDSummarizePerCustomer:boolean,
   PMUIDType:number,
   RateGrpDescription:string,
   RcptCurrencyCodeCurrencyID:string,
   RcptCurrencyCodeDocumentDesc:string,
   RcptCurrencyCodeCurrDesc:string,
   RcptCurrencyCodeCurrSymbol:string,
   RcptCurrencyCodeCurrName:string,
   ReverseMXCancelReasonCode:string,
   ReverseMXCancellationMode:string,
   SourceTranDateTranDate:string,
   TaxRegionCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashHeadTGLCRow{
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
      /**  HeadNum of CashHead  */  
   HeadNum:number,
      /**  GroupID of CashHead  */  
   GroupID:string,
   BitFlag:number,
   COADescription:string,
   GLAccountAccountDesc:string,
   GLAccountGLShortAcct:string,
   GLAccountGLAcctDisp:string,
   GLBookCurrencyCode:string,
   GLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashRecTableset{
   CashHead:Erp_Tablesets_CashHeadRow[],
   CashHeadAttch:Erp_Tablesets_CashHeadAttchRow[],
   BankTran:Erp_Tablesets_BankTranRow[],
   BankTranTaxDtl:Erp_Tablesets_BankTranTaxDtlRow[],
   BankTranTGLC:Erp_Tablesets_BankTranTGLCRow[],
   DebNote:Erp_Tablesets_DebNoteRow[],
   DebNoteAttch:Erp_Tablesets_DebNoteAttchRow[],
   CashDtl:Erp_Tablesets_CashDtlRow[],
   CashDtlTGLC:Erp_Tablesets_CashDtlTGLCRow[],
   CDTaxDtl:Erp_Tablesets_CDTaxDtlRow[],
   CashHeadTGLC:Erp_Tablesets_CashHeadTGLCRow[],
   TaxDtl:Erp_Tablesets_TaxDtlRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DebNoteAttchRow{
   Company:string,
   DebitNoteID:number,
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

export interface Erp_Tablesets_DebNoteRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A  unique integer assigned by the system to new debit note  .  */  
   DebitNoteID:number,
      /**  The customer number of the customer associated with this Debit Note.  */  
   CustNum:number,
      /**   The Debit Note Number assigned by the customer.
This number is supposed to be unique for the customer.  */  
   DNCustNbr:string,
      /**  The debit note value.  */  
   DNAmount:number,
      /**  Customer Debit Note Amount.  */  
   DocDNAmount:number,
      /**  The invoice number associated with this Debit Note.  */  
   DNInvNbr:number,
      /**  A flag to indicate if this debit note was applied to Unapplied cash balance or invoice.  */  
   DNApplied:boolean,
      /**  If a Debit Note was applied this field is "Cash" or "Invoice".  */  
   DNAppliedTo:string,
      /**  The HeadNum of the CashHead record associated with this Debit Note.  */  
   CashHeadNum:number,
      /**  The Group ID of the Cash Payment this Debit Note is associated with.  */  
   GroupID:string,
      /**   If a Debit note is entered as a part of Cash Receipt payment this flag indicates if the Cash Receipts group is posted.
If this flag is yes the Debit Note can not be changed or deleted.  */  
   PmtPosted:boolean,
      /**  Debit Note Comments  */  
   DNComments:string,
      /**  Debit Note Due Date.  */  
   DNDueDate:string,
      /**  Date when this Debit Note is entered.  */  
   DNDate:string,
      /**  A flag to indicate if the invoice balance is supposed to be changed after the debit note is applied and posted.  */  
   InvcChanged:boolean,
      /**  Invoice Number assigned to the Debit Note type invoice created when the Debit Note is posted with the Cash Receipt Group.  */  
   InvNbrAssigned:number,
      /**  Reporting currency value of this field  */  
   Rpt1DNAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2DNAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3DNAmount:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The legal number of the invoice entered as debit note reference  */  
   DNInvLegalNbr:string,
      /**  The flag to indicate if an infoice entered as debit note reference closed (or open).  */  
   DNInvoiceClsd:boolean,
      /**  The open balance of the invoice entered as debit note reference.  */  
   DNInvBalance:number,
      /**  The due date of the invoice entered as debit note reference  */  
   DNInvDueDate:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
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

export interface Erp_Tablesets_UpdExtCashRecTableset{
   CashHead:Erp_Tablesets_CashHeadRow[],
   CashHeadAttch:Erp_Tablesets_CashHeadAttchRow[],
   BankTran:Erp_Tablesets_BankTranRow[],
   BankTranTaxDtl:Erp_Tablesets_BankTranTaxDtlRow[],
   BankTranTGLC:Erp_Tablesets_BankTranTGLCRow[],
   DebNote:Erp_Tablesets_DebNoteRow[],
   DebNoteAttch:Erp_Tablesets_DebNoteAttchRow[],
   CashDtl:Erp_Tablesets_CashDtlRow[],
   CashDtlTGLC:Erp_Tablesets_CashDtlTGLCRow[],
   CDTaxDtl:Erp_Tablesets_CDTaxDtlRow[],
   CashHeadTGLC:Erp_Tablesets_CashHeadTGLCRow[],
   TaxDtl:Erp_Tablesets_TaxDtlRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param headNum
      @param ds
   */  
export interface ForceTakeDiscount_input{
   headNum:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface ForceTakeDiscount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param groupID
      @param headNum
      @param invoiceNum
      @param takeDiscount
   */  
export interface GenerateCashDtl_input{
      /**  Cash Group ID  */  
   groupID:string,
      /**  Cash Receipt HeadNum  */  
   headNum:number,
      /**  Cash Receipt Invoice Num  */  
   invoiceNum:number,
      /**  If yes, force the line to take the discount.  If no, the discount will be taken only if within the discount parameters  */  
   takeDiscount:boolean,
}

export interface GenerateCashDtl_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
}

   /** Required : 
      @param invoiceNum
   */  
export interface GetAdjAmtTax_input{
   invoiceNum:number,
}

export interface GetAdjAmtTax_output{
parameters : {
      /**  output parameters  */  
   adjustAmtTax:number,
}
}

   /** Required : 
      @param ipGroupID
      @param ipBankBatchID
   */  
export interface GetBankBatchIDFromGrpWithBBIDNotEqualsInpID_input{
   ipGroupID:string,
   ipBankBatchID:string,
}

export interface GetBankBatchIDFromGrpWithBBIDNotEqualsInpID_output{
parameters : {
      /**  output parameters  */  
   opIfAnyRecordsFound:boolean,
   opBankBatchID:string,
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
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetBankFeeDefaultAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param groupID
      @param headNum
      @param ds
   */  
export interface GetByIDCashRecAdjustment_input{
   groupID:string,
   headNum:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetByIDCashRecAdjustment_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface GetByIDSetTrackerMobe_input{
      /**  Group ID  */  
   groupID:string,
      /**  HeadNum  */  
   headNum:number,
}

export interface GetByIDSetTrackerMobe_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
}

   /** Required : 
      @param groupID
      @param headNum
      @param ds
   */  
export interface GetByIDTracker_input{
      /**  Group ID  */  
   groupID:string,
      /**  HeadNum  */  
   headNum:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetByIDTracker_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
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
   returnObj:Erp_Tablesets_CashRecTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
}

   /** Required : 
      @param groupID
      @param headNum
      @param ds
   */  
export interface GetCashHeadDefaultAccount_input{
      /**  Group ID  */  
   groupID:string,
      /**  Head Num  */  
   headNum:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetCashHeadDefaultAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ipInvoiceNum
      @param whereClauseCashHead
      @param whereClauseCashHeadAttch
      @param whereClauseBankTran
      @param whereClauseBankTranTaxDtl
      @param whereClauseBankTranTGLC
      @param whereClauseDebNote
      @param whereClauseDebNoteAttch
      @param whereClauseCashDtl
      @param whereClauseCashDtlTGLC
      @param whereClauseCDTaxDtl
      @param whereClauseCashHeadTGLC
      @param whereClauseTaxDtl
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetCashHeadRowsByInvoiceNum_input{
   ipInvoiceNum:string,
   whereClauseCashHead:string,
   whereClauseCashHeadAttch:string,
   whereClauseBankTran:string,
   whereClauseBankTranTaxDtl:string,
   whereClauseBankTranTGLC:string,
   whereClauseDebNote:string,
   whereClauseDebNoteAttch:string,
   whereClauseCashDtl:string,
   whereClauseCashDtlTGLC:string,
   whereClauseCDTaxDtl:string,
   whereClauseCashHeadTGLC:string,
   whereClauseTaxDtl:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetCashHeadRowsByInvoiceNum_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
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
      @param currencyCode
      @param ds
   */  
export interface GetCurrencyInfo_input{
      /**  Proposed Currency Code  */  
   currencyCode:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetCurrencyInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param custID
      @param ds
   */  
export interface GetCustomerInfo_input{
      /**  Proposed Customer ID  */  
   custID:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetCustomerInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param dnInvNbr
      @param ds
   */  
export interface GetDNInvInfo_input{
      /**  Proposed Invoice Number  */  
   dnInvNbr:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetDNInvInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
      @param inHeadNum
   */  
export interface GetDefaultLegalNumOpts_input{
   ds:Erp_Tablesets_CashRecTableset[],
      /**  Header Number  */  
   inHeadNum:number,
}

export interface GetDefaultLegalNumOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
   RequiresUserInput:boolean,
}
}

   /** Required : 
      @param cashHeadNum
      @param invoiceNum
      @param calcAccount
      @param ds
   */  
export interface GetDefaultWriteOffData_input{
   cashHeadNum:number,
   invoiceNum:number,
   calcAccount:boolean,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface GetDefaultWriteOffData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param docDiscount
      @param ds
   */  
export interface GetDtlDiscountInfo_input{
      /**  Proposed discount amount  */  
   docDiscount:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetDtlDiscountInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param invoiceNum
      @param ds
   */  
export interface GetDtlInvoiceInfo_input{
      /**  Proposed Invoice Number  */  
   invoiceNum:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetDtlInvoiceInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param legalNumber
      @param ds
   */  
export interface GetDtlLegalNumberInfo_input{
      /**  Proposed Legal Number  */  
   legalNumber:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetDtlLegalNumberInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param cashDeskID
      @param referenceNum
      @param applyDate
      @param exchangeRateDate
   */  
export interface GetDtlTranAmtInfoExt_input{
   cashDeskID:string,
   referenceNum:number,
   applyDate:string,
   exchangeRateDate:string,
}

export interface GetDtlTranAmtInfoExt_output{
}

   /** Required : 
      @param docTranAmt
      @param docWriteOffAmount
      @param ds
   */  
export interface GetDtlTranAmtInfo_input{
      /**  Proposed Customer applied amount  */  
   docTranAmt:number,
      /**  Proposed Write Off amount  */  
   docWriteOffAmount:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetDtlTranAmtInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param invoiceNum
      @param ds
   */  
export interface GetHdrInvoiceInfo_input{
      /**  Invoice Number to get Customer information from  */  
   invoiceNum:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetHdrInvoiceInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param legalNumber
      @param ds
   */  
export interface GetHdrLegalNumberInfo_input{
      /**  Legal Number to get Customer information from  */  
   legalNumber:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetHdrLegalNumberInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param invoiceNum
   */  
export interface GetInvcMiscWithoutTakeDiscount_input{
      /**  Group ID  */  
   invoiceNum:number,
}

export interface GetInvcMiscWithoutTakeDiscount_output{
   returnObj:number,
}

   /** Required : 
      @param invoiceNum
      @param ttARInvcAllocTablesetDS
   */  
export interface GetInvoiceBalance_input{
   invoiceNum:number,
   ttARInvcAllocTablesetDS:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface GetInvoiceBalance_output{
parameters : {
      /**  output parameters  */  
   ttARInvcAllocTablesetDS:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListForAdjustment_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListForAdjustment_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
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
   returnObj:Erp_Tablesets_CashHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param sCheckRef
      @param ds
   */  
export interface GetMXOriginalCheckRef_input{
      /**  Proposed CheckRef  */  
   sCheckRef:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetMXOriginalCheckRef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

export interface GetMXTaxRcptType_output{
parameters : {
      /**  output parameters  */  
   mxTaxRcptType:string,
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
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetNewBankTranByHeadNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param tranNum
      @param voided
   */  
export interface GetNewBankTranTGLC_input{
   ds:Erp_Tablesets_CashRecTableset[],
   bankAcctID:string,
   tranNum:number,
   voided:boolean,
}

export interface GetNewBankTranTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
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
   ds:Erp_Tablesets_CashRecTableset[],
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
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param tranNum
   */  
export interface GetNewBankTran_input{
   ds:Erp_Tablesets_CashRecTableset[],
   bankAcctID:string,
   tranNum:number,
}

export interface GetNewBankTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
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
export interface GetNewCDTaxDtl_input{
   ds:Erp_Tablesets_CashRecTableset[],
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

export interface GetNewCDTaxDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCashDtlTGLC_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetNewCashDtlTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
      @param invoiceNum
   */  
export interface GetNewCashDtl_input{
   ds:Erp_Tablesets_CashRecTableset[],
   groupID:string,
   headNum:number,
   invoiceNum:number,
}

export interface GetNewCashDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
   */  
export interface GetNewCashHeadAttch_input{
   ds:Erp_Tablesets_CashRecTableset[],
   groupID:string,
   headNum:number,
}

export interface GetNewCashHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCashHeadTGLC_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetNewCashHeadTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param tranType
   */  
export interface GetNewCashHeadType_input{
   ds:Erp_Tablesets_CashRecTableset[],
      /**  Cash Group ID  */  
   groupID:string,
      /**  Transaction type  */  
   tranType:string,
}

export interface GetNewCashHeadType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewCashHead_input{
   ds:Erp_Tablesets_CashRecTableset[],
   groupID:string,
}

export interface GetNewCashHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
      @param debitNoteID
   */  
export interface GetNewDebNoteAttch_input{
   ds:Erp_Tablesets_CashRecTableset[],
   debitNoteID:number,
}

export interface GetNewDebNoteAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewDebNote_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetNewDebNote_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
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
   ds:Erp_Tablesets_CashRecTableset[],
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
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param orderNum
      @param dskCurrCode
      @param ds
   */  
export interface GetOrderInfo4DskCurr_input{
      /**  Proposed Order Number  */  
   orderNum:number,
      /**  Petty Cash Desc Currency Code  */  
   dskCurrCode:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetOrderInfo4DskCurr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param orderNum
      @param ds
   */  
export interface GetOrderInfo_input{
      /**  Proposed Order Number  */  
   orderNum:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetOrderInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param invoiceNum
   */  
export interface GetPendingToPostAdjustments_input{
   invoiceNum:number,
}

export interface GetPendingToPostAdjustments_output{
parameters : {
      /**  output parameters  */  
   messageList:string,
   docUnPostedBal:number,
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
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetRateCodeInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param whereClauseCashHead
      @param whereClauseCashHeadAttch
      @param whereClauseBankTran
      @param whereClauseBankTranTaxDtl
      @param whereClauseBankTranTGLC
      @param whereClauseDebNote
      @param whereClauseDebNoteAttch
      @param whereClauseCashDtl
      @param whereClauseCashDtlTGLC
      @param whereClauseCDTaxDtl
      @param whereClauseCashHeadTGLC
      @param whereClauseTaxDtl
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCashHead:string,
   whereClauseCashHeadAttch:string,
   whereClauseBankTran:string,
   whereClauseBankTranTaxDtl:string,
   whereClauseBankTranTGLC:string,
   whereClauseDebNote:string,
   whereClauseDebNoteAttch:string,
   whereClauseCashDtl:string,
   whereClauseCashDtlTGLC:string,
   whereClauseCDTaxDtl:string,
   whereClauseCashHeadTGLC:string,
   whereClauseTaxDtl:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
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
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetSalesTaxInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
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
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetTaxableInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param baseEntered
      @param ds
   */  
export interface GetTranAmt_input{
      /**  If the TranAmt field was updated then value should be yes, otherwise no  */  
   baseEntered:boolean,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface GetTranAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ipTranAmt
   */  
export interface GetTransTypeComboList_input{
   ipTranAmt:number,
}

export interface GetTransTypeComboList_output{
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
      @param ipCustNum
      @param ipDueDate
   */  
export interface IsDueDateHighLighted_input{
      /**  Customer  */  
   ipCustNum:number,
      /**  Due Date  */  
   ipDueDate:string,
}

export interface IsDueDateHighLighted_output{
parameters : {
      /**  output parameters  */  
   bDueDateHighLighted:boolean,
}
}

   /** Required : 
      @param groupID
      @param cashHeadNum
   */  
export interface IsUnAppliedDNExists_input{
      /**  Group ID  */  
   groupID:string,
      /**  CashHead Number  */  
   cashHeadNum:number,
}

export interface IsUnAppliedDNExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param docTranAmt
      @param ds
   */  
export interface IsWriteOffOverpayment_input{
      /**  Proposed Customer applied amount  */  
   docTranAmt:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface IsWriteOffOverpayment_output{
parameters : {
      /**  output parameters  */  
   result:boolean,
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param groupID
      @param headNum
      @param onAccount
      @param ds
   */  
export interface LeaveCashHead_input{
      /**  Cash Receipt Group ID  */  
   groupID:string,
      /**  Cash Receipt number  */  
   headNum:number,
      /**  Indicates if excess cash should go on account  */  
   onAccount:boolean,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface LeaveCashHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param custNum
      @param ds
   */  
export interface MassApplyDebitNotes_input{
      /**  Customer Number  */  
   custNum:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface MassApplyDebitNotes_output{
parameters : {
      /**  output parameters  */  
   dnApplyErrorMsg:string,
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param pcGroupID
   */  
export interface MassDelete_input{
      /**  Cash Receipt Group ID  */  
   pcGroupID:string,
}

export interface MassDelete_output{
}

   /** Required : 
      @param silent
      @param groupID
      @param headNum
      @param DocUnAppliedAmt
      @param ds
   */  
export interface MassGenerateCashDtlExt_input{
   silent:boolean,
   groupID:string,
   headNum:number,
   DocUnAppliedAmt:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface MassGenerateCashDtlExt_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
parameters : {
      /**  output parameters  */  
   massGenErrorMsg:string,
   opTotalCashReceived:number,
   opTotalApplied:number,
   opUnappliedBalance:number,
   opTotalMisc:number,
   opTotalDiscount:number,
   opTotalDeposit:number,
   opTotalARAmount:number,
   opTotalWithhold:number,
   opTotalWriteOff:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param pcGroupID
      @param ipHeadNum
      @param useDisc
      @param ds
   */  
export interface MassGenerateCashDtl_input{
      /**  Cash Receipt Group ID  */  
   pcGroupID:string,
      /**  Cash Receipt Header HeadNum  */  
   ipHeadNum:number,
      /**  Yes or no  */  
   useDisc:boolean,
   ds:Erp_Tablesets_ARInvSelTableset[],
}

export interface MassGenerateCashDtl_output{
   returnObj:Erp_Tablesets_CashRecTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvSelTableset[],
   massGenErrorMsg:string,
   opTotalCashReceived:number,
   opTotalApplied:number,
   opUnappliedBalance:number,
   opTotalMisc:number,
   opTotalDiscount:number,
   opTotalDeposit:number,
   opTotalARAmount:number,
   opTotalWithhold:number,
   opTotalWriteOff:number,
}
}

   /** Required : 
      @param pcBankFeeID
      @param ds
   */  
export interface OnChangeBankFeeID_input{
   pcBankFeeID:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface OnChangeBankFeeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param creditCard
      @param ds
   */  
export interface OnChangeCreditCard_input{
   creditCard:boolean,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface OnChangeCreditCard_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param taxableWriteOff
      @param invoiceNum
   */  
export interface OnChangeTaxableWriteOff_input{
      /**  New value of TaxableWriteOff flag  */  
   taxableWriteOff:boolean,
      /**  InvoiceNum  */  
   invoiceNum:number,
}

export interface OnChangeTaxableWriteOff_output{
}

   /** Required : 
      @param ipTranDocTypeID
      @param ds
   */  
export interface OnChangeTranDocTypeID_input{
   ipTranDocTypeID:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface OnChangeTranDocTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param cashHeadNum
      @param invoiceNum
      @param newWriteOffAmount
      @param appliedBalance
      @param ttARInvAllocTablesetDS
   */  
export interface OnChangeWriteOffAmount_input{
   cashHeadNum:number,
   invoiceNum:number,
   newWriteOffAmount:number,
   appliedBalance:number,
   ttARInvAllocTablesetDS:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface OnChangeWriteOffAmount_output{
parameters : {
      /**  output parameters  */  
   ttARInvAllocTablesetDS:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param headNum
      @param updDisc
      @param ds
   */  
export interface OnChangedAllocAmount_input{
   headNum:number,
   updDisc:boolean,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface OnChangedAllocAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param headNum
      @param UpdDisc
      @param ds
   */  
export interface OnChangedCashApplied_input{
   headNum:number,
   UpdDisc:boolean,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface OnChangedCashApplied_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param headNum
      @param ds
   */  
export interface OnChangedDiscount_input{
   headNum:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface OnChangedDiscount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param headNum
      @param unAppliedAmt
      @param forceDiscount
      @param proposedValue
      @param ds
   */  
export interface OnChangedInvcSelected_input{
   headNum:number,
   unAppliedAmt:number,
   forceDiscount:boolean,
   proposedValue:boolean,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface OnChangedInvcSelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param headNum
      @param proposedValue
      @param answer
      @param ds
   */  
export interface OnChangingAllocAmount_input{
   headNum:number,
   proposedValue:number,
   answer:string,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface OnChangingAllocAmount_output{
parameters : {
      /**  output parameters  */  
   question:string,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param proposedValue
      @param ds
   */  
export interface OnChangingCashApplied_input{
   proposedValue:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface OnChangingCashApplied_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param proposedValue
      @param validDic
      @param ds
   */  
export interface OnChangingDiscount_input{
   proposedValue:number,
   validDic:boolean,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface OnChangingDiscount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param proposedValue
      @param headNum
      @param ds
   */  
export interface OnChangingWriteOffAmount_input{
   proposedValue:number,
   headNum:number,
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface OnChangingWriteOffAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param filename
      @param ds
   */  
export interface ParseCEPXml2_input{
      /**  path to CEP XML  */  
   filename:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ParseCEPXml2_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param filename
      @param ds
   */  
export interface ParseCEPXml_input{
      /**  path to CEP XML  */  
   filename:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ParseCEPXml_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface ProcessPayGateMessage_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ProcessPayGateMessage_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface RecalcBankTax_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface RecalcBankTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface RecalcCDTax_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface RecalcCDTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface RecalcTax_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface RecalcTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param headNum
      @param reverseDate
   */  
export interface ReverseCashReceipt_input{
      /**  Head number  */  
   headNum:number,
      /**  Reverse Date  */  
   reverseDate:string,
}

export interface ReverseCashReceipt_output{
parameters : {
      /**  output parameters  */  
   postErrorLog:string,
}
}

   /** Required : 
      @param pcGroupID
      @param pdtDueDate
      @param pdtTranDate
      @param plApplyDiscount
      @param pcCustomerList
      @param pcPaymentMethod
   */  
export interface SelectInvoices_input{
      /**  AR Check Group ID  */  
   pcGroupID:string,
      /**  Select invoices due by this date.  */  
   pdtDueDate:string,
      /**  The date of the transaction.  */  
   pdtTranDate:string,
      /**  Yes or no  */  
   plApplyDiscount:boolean,
      /**  Select invoices for the customer list.  */  
   pcCustomerList:string,
      /**  Select payment methods for the specific.  */  
   pcPaymentMethod:string,
}

export interface SelectInvoices_output{
   returnObj:Erp_Tablesets_ARInvSelTableset[],
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface SetEInvoiceStatusToSent_input{
      /**  Cash Receipt GroupID  */  
   groupID:string,
      /**  Cash Receipt HeadNum  */  
   headNum:number,
}

export interface SetEInvoiceStatusToSent_output{
}

   /** Required : 
      @param chkWriteOff
      @param ds
   */  
export interface SetWriteOff_input{
   chkWriteOff:boolean,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface SetWriteOff_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface TakeDiscount_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface TakeDiscount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateAutoGen_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface UpdateAutoGen_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCashRecTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCashRecTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param mxSubstHeadNum
      @param mxSubstGroupID
      @param headNum
      @param groupID
   */  
export interface UpdateMXSubstitutionCashReceipt_input{
      /**  Substitution Cash Receipt HeadNum  */  
   mxSubstHeadNum:number,
      /**  Substitution Cash Receipt GroupID  */  
   mxSubstGroupID:string,
      /**  Current HeadNum  */  
   headNum:number,
   groupID:string,
}

export interface UpdateMXSubstitutionCashReceipt_output{
}

   /** Required : 
      @param ds
      @param ipGroupID
      @param ipTableName
      @param updGroupTotals
      @param ipIgnoreValidation
   */  
export interface UpdateMaster_input{
   ds:Erp_Tablesets_CashRecTableset[],
      /**  current GroupID Cash Receipts  */  
   ipGroupID:string,
      /**  Indicates the tableName that triggered the update  */  
   ipTableName:string,
      /**  Indicates if the group totals should be calculated  */  
   updGroupTotals:boolean,
      /**  Indicates if some validations should be ignored (Bank Reconciliation)  */  
   ipIgnoreValidation:number,
}

export interface UpdateMaster_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
   opTotalCashReceived:number,
   opTotalApplied:number,
   opUnappliedBalance:number,
   opTotalMisc:number,
   opTotalDiscount:number,
   opTotalDeposit:number,
   opTotalARAmount:number,
   opTotalWithhold:number,
   opTotalWriteOff:number,
   opUpdateRan:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param ipBankID
      @param ipCustNum
      @param ds
   */  
export interface ValidateCustomerBankID_input{
   ipBankID:string,
   ipCustNum:number,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface ValidateCustomerBankID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

   /** Required : 
      @param invoiceNum
      @param tranDate
      @param ttARInvcAllocTablesetDS
   */  
export interface ValidateInvoiceWriteOffAccount_input{
      /**  Invoice Num  */  
   invoiceNum:number,
      /**  Tran Date  */  
   tranDate:string,
   ttARInvcAllocTablesetDS:Erp_Tablesets_ARInvcAllocTableset[],
}

export interface ValidateInvoiceWriteOffAccount_output{
parameters : {
      /**  output parameters  */  
   ttARInvcAllocTablesetDS:Erp_Tablesets_ARInvcAllocTableset[],
}
}

   /** Required : 
      @param ipGroupID
   */  
export interface ValidatePaymentsWithUnappliedAmntInGroup_input{
   ipGroupID:string,
}

export interface ValidatePaymentsWithUnappliedAmntInGroup_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   opWarningMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
   */  
export interface ValidatePrintEditList_input{
   ipGroupID:string,
   ipHeadNum:number,
}

export interface ValidatePrintEditList_output{
parameters : {
      /**  output parameters  */  
   opWarningReceipt:string,
   opWarningWithhold:string,
}
}

   /** Required : 
      @param ipGroupID
   */  
export interface ValidateTotalCash_input{
   ipGroupID:string,
}

export interface ValidateTotalCash_output{
   returnObj:boolean,
}

   /** Required : 
      @param HeadNum
      @param VoidedReason
      @param ds
   */  
export interface VoidLegalNumber_input{
      /**  Cash Head number  */  
   HeadNum:number,
      /**  Reason for the void  */  
   VoidedReason:string,
   ds:Erp_Tablesets_CashRecTableset[],
}

export interface VoidLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashRecTableset[],
}
}

