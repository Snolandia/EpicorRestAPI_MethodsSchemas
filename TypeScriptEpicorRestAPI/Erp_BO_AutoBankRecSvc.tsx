import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.AutoBankRecSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/$metadata", {
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
   Description: Get AutoBankRecs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AutoBankRecs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBHedRow
   */  
export function get_AutoBankRecs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AutoBankRecs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashBHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CashBHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoBankRecs(requestBody:Erp_Tablesets_CashBHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the AutoBankRec item
   Description: Calls GetByID to retrieve the AutoBankRec item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AutoBankRec
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashBHedRow
   */  
export function get_AutoBankRecs_Company_CashBookNum(Company:string, CashBookNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashBHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")", {
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
         resolve(data as Erp_Tablesets_CashBHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AutoBankRec for the service
   Description: Calls UpdateExt to update AutoBankRec. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AutoBankRec
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashBHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AutoBankRecs_Company_CashBookNum(Company:string, CashBookNum:string, requestBody:Erp_Tablesets_CashBHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")", {
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
   Summary: Call UpdateExt to delete AutoBankRec item
   Description: Call UpdateExt to delete AutoBankRec item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AutoBankRec
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AutoBankRecs_Company_CashBookNum(Company:string, CashBookNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")", {
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
   Description: Get CashBFilterOptions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashBFilterOptions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBFilterOptionsRow
   */  
export function get_AutoBankRecs_Company_CashBookNum_CashBFilterOptions(Company:string, CashBookNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBFilterOptionsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/CashBFilterOptions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBFilterOptionsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashBFilterOption item
   Description: Calls GetByID to retrieve the CashBFilterOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBFilterOption1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param LineType Desc: LineType   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashBFilterOptionsRow
   */  
export function get_AutoBankRecs_Company_CashBookNum_CashBFilterOptions_Company_BankAcctID_CashBookNum_LineType(Company:string, CashBookNum:string, BankAcctID:string, LineType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashBFilterOptionsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/CashBFilterOptions(" + Company + "," + BankAcctID + "," + CashBookNum + "," + LineType + ")", {
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
         resolve(data as Erp_Tablesets_CashBFilterOptionsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get SubLedgerDocs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SubLedgerDocs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SubLedgerDocsRow
   */  
export function get_AutoBankRecs_Company_CashBookNum_SubLedgerDocs(Company:string, CashBookNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SubLedgerDocsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/SubLedgerDocs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SubLedgerDocsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SubLedgerDoc item
   Description: Calls GetByID to retrieve the SubLedgerDoc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SubLedgerDoc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param DocumentType Desc: DocumentType   Required: True
      @param Reference Desc: Reference   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SubLedgerDocsRow
   */  
export function get_AutoBankRecs_Company_CashBookNum_SubLedgerDocs_Company_BankAcctID_CashBookNum_DocumentType_Reference(Company:string, CashBookNum:string, BankAcctID:string, DocumentType:string, Reference:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SubLedgerDocsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/SubLedgerDocs(" + Company + "," + BankAcctID + "," + CashBookNum + "," + DocumentType + "," + Reference + ")", {
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
         resolve(data as Erp_Tablesets_SubLedgerDocsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CashBDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashBDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBDtlRow
   */  
export function get_AutoBankRecs_Company_CashBookNum_CashBDtls(Company:string, CashBookNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/CashBDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashBDtl item
   Description: Calls GetByID to retrieve the CashBDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashbookLine Desc: CashbookLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashBDtlRow
   */  
export function get_AutoBankRecs_Company_CashBookNum_CashBDtls_Company_CashBookNum_CashbookLine(Company:string, CashBookNum:string, CashbookLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashBDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")", {
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
         resolve(data as Erp_Tablesets_CashBDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CashBHedAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashBHedAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBHedAttchRow
   */  
export function get_AutoBankRecs_Company_CashBookNum_CashBHedAttches(Company:string, CashBookNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/CashBHedAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashBHedAttch item
   Description: Calls GetByID to retrieve the CashBHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBHedAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashBHedAttchRow
   */  
export function get_AutoBankRecs_Company_CashBookNum_CashBHedAttches_Company_CashBookNum_DrawingSeq(Company:string, CashBookNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashBHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/CashBHedAttches(" + Company + "," + CashBookNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_CashBHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CashBFilterOptions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashBFilterOptions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBFilterOptionsRow
   */  
export function get_CashBFilterOptions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBFilterOptionsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBFilterOptions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBFilterOptionsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashBFilterOptions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashBFilterOptionsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CashBFilterOptionsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashBFilterOptions(requestBody:Erp_Tablesets_CashBFilterOptionsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBFilterOptions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CashBFilterOption item
   Description: Calls GetByID to retrieve the CashBFilterOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBFilterOption
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param LineType Desc: LineType   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashBFilterOptionsRow
   */  
export function get_CashBFilterOptions_Company_BankAcctID_CashBookNum_LineType(Company:string, BankAcctID:string, CashBookNum:string, LineType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashBFilterOptionsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBFilterOptions(" + Company + "," + BankAcctID + "," + CashBookNum + "," + LineType + ")", {
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
         resolve(data as Erp_Tablesets_CashBFilterOptionsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashBFilterOption for the service
   Description: Calls UpdateExt to update CashBFilterOption. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashBFilterOption
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param LineType Desc: LineType   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashBFilterOptionsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashBFilterOptions_Company_BankAcctID_CashBookNum_LineType(Company:string, BankAcctID:string, CashBookNum:string, LineType:string, requestBody:Erp_Tablesets_CashBFilterOptionsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBFilterOptions(" + Company + "," + BankAcctID + "," + CashBookNum + "," + LineType + ")", {
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
   Summary: Call UpdateExt to delete CashBFilterOption item
   Description: Call UpdateExt to delete CashBFilterOption item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashBFilterOption
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param LineType Desc: LineType   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashBFilterOptions_Company_BankAcctID_CashBookNum_LineType(Company:string, BankAcctID:string, CashBookNum:string, LineType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBFilterOptions(" + Company + "," + BankAcctID + "," + CashBookNum + "," + LineType + ")", {
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
   Description: Get SubLedgerDocs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SubLedgerDocs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SubLedgerDocsRow
   */  
export function get_SubLedgerDocs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SubLedgerDocsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SubLedgerDocs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SubLedgerDocsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SubLedgerDocs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SubLedgerDocsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SubLedgerDocsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubLedgerDocs(requestBody:Erp_Tablesets_SubLedgerDocsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SubLedgerDocs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the SubLedgerDoc item
   Description: Calls GetByID to retrieve the SubLedgerDoc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SubLedgerDoc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param DocumentType Desc: DocumentType   Required: True
      @param Reference Desc: Reference   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SubLedgerDocsRow
   */  
export function get_SubLedgerDocs_Company_BankAcctID_CashBookNum_DocumentType_Reference(Company:string, BankAcctID:string, CashBookNum:string, DocumentType:string, Reference:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SubLedgerDocsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SubLedgerDocs(" + Company + "," + BankAcctID + "," + CashBookNum + "," + DocumentType + "," + Reference + ")", {
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
         resolve(data as Erp_Tablesets_SubLedgerDocsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SubLedgerDoc for the service
   Description: Calls UpdateExt to update SubLedgerDoc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SubLedgerDoc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param DocumentType Desc: DocumentType   Required: True
      @param Reference Desc: Reference   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SubLedgerDocsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SubLedgerDocs_Company_BankAcctID_CashBookNum_DocumentType_Reference(Company:string, BankAcctID:string, CashBookNum:string, DocumentType:string, Reference:string, requestBody:Erp_Tablesets_SubLedgerDocsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SubLedgerDocs(" + Company + "," + BankAcctID + "," + CashBookNum + "," + DocumentType + "," + Reference + ")", {
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
   Summary: Call UpdateExt to delete SubLedgerDoc item
   Description: Call UpdateExt to delete SubLedgerDoc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SubLedgerDoc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param DocumentType Desc: DocumentType   Required: True
      @param Reference Desc: Reference   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SubLedgerDocs_Company_BankAcctID_CashBookNum_DocumentType_Reference(Company:string, BankAcctID:string, CashBookNum:string, DocumentType:string, Reference:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SubLedgerDocs(" + Company + "," + BankAcctID + "," + CashBookNum + "," + DocumentType + "," + Reference + ")", {
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
   Description: Get CashBDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashBDtls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBDtlRow
   */  
export function get_CashBDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashBDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashBDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CashBDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashBDtls(requestBody:Erp_Tablesets_CashBDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CashBDtl item
   Description: Calls GetByID to retrieve the CashBDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashbookLine Desc: CashbookLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashBDtlRow
   */  
export function get_CashBDtls_Company_CashBookNum_CashbookLine(Company:string, CashBookNum:string, CashbookLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashBDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")", {
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
         resolve(data as Erp_Tablesets_CashBDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashBDtl for the service
   Description: Calls UpdateExt to update CashBDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashBDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashbookLine Desc: CashbookLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashBDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashBDtls_Company_CashBookNum_CashbookLine(Company:string, CashBookNum:string, CashbookLine:string, requestBody:Erp_Tablesets_CashBDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")", {
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
   Summary: Call UpdateExt to delete CashBDtl item
   Description: Call UpdateExt to delete CashBDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashBDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashbookLine Desc: CashbookLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashBDtls_Company_CashBookNum_CashbookLine(Company:string, CashBookNum:string, CashbookLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")", {
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
   Description: Get MatchedDocuments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MatchedDocuments1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashbookLine Desc: CashbookLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MatchedDocumentsRow
   */  
export function get_CashBDtls_Company_CashBookNum_CashbookLine_MatchedDocuments(Company:string, CashBookNum:string, CashbookLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MatchedDocumentsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")/MatchedDocuments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MatchedDocumentsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MatchedDocument item
   Description: Calls GetByID to retrieve the MatchedDocument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MatchedDocument1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashbookLine Desc: CashbookLine   Required: True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param CashBookLine Desc: CashBookLine   Required: True
      @param MatchLineNum Desc: MatchLineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MatchedDocumentsRow
   */  
export function get_CashBDtls_Company_CashBookNum_CashbookLine_MatchedDocuments_Company_BankAcctID_CashBookNum_CashBookLine_MatchLineNum(Company:string, CashBookNum:string, CashbookLine:string, BankAcctID:string, CashBookLine:string, MatchLineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MatchedDocumentsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")/MatchedDocuments(" + Company + "," + BankAcctID + "," + CashBookNum + "," + CashBookLine + "," + MatchLineNum + ")", {
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
         resolve(data as Erp_Tablesets_MatchedDocumentsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CashBDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashBDtlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashbookLine Desc: CashbookLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBDtlAttchRow
   */  
export function get_CashBDtls_Company_CashBookNum_CashbookLine_CashBDtlAttches(Company:string, CashBookNum:string, CashbookLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")/CashBDtlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashBDtlAttch item
   Description: Calls GetByID to retrieve the CashBDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBDtlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashbookLine Desc: CashbookLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashBDtlAttchRow
   */  
export function get_CashBDtls_Company_CashBookNum_CashbookLine_CashBDtlAttches_Company_CashBookNum_CashbookLine_DrawingSeq(Company:string, CashBookNum:string, CashbookLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashBDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")/CashBDtlAttches(" + Company + "," + CashBookNum + "," + CashbookLine + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_CashBDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get MatchedDocuments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MatchedDocuments
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MatchedDocumentsRow
   */  
export function get_MatchedDocuments(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MatchedDocumentsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/MatchedDocuments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MatchedDocumentsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MatchedDocuments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MatchedDocumentsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MatchedDocumentsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MatchedDocuments(requestBody:Erp_Tablesets_MatchedDocumentsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/MatchedDocuments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the MatchedDocument item
   Description: Calls GetByID to retrieve the MatchedDocument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MatchedDocument
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashBookLine Desc: CashBookLine   Required: True
      @param MatchLineNum Desc: MatchLineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MatchedDocumentsRow
   */  
export function get_MatchedDocuments_Company_BankAcctID_CashBookNum_CashBookLine_MatchLineNum(Company:string, BankAcctID:string, CashBookNum:string, CashBookLine:string, MatchLineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MatchedDocumentsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/MatchedDocuments(" + Company + "," + BankAcctID + "," + CashBookNum + "," + CashBookLine + "," + MatchLineNum + ")", {
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
         resolve(data as Erp_Tablesets_MatchedDocumentsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MatchedDocument for the service
   Description: Calls UpdateExt to update MatchedDocument. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MatchedDocument
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashBookLine Desc: CashBookLine   Required: True
      @param MatchLineNum Desc: MatchLineNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MatchedDocumentsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MatchedDocuments_Company_BankAcctID_CashBookNum_CashBookLine_MatchLineNum(Company:string, BankAcctID:string, CashBookNum:string, CashBookLine:string, MatchLineNum:string, requestBody:Erp_Tablesets_MatchedDocumentsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/MatchedDocuments(" + Company + "," + BankAcctID + "," + CashBookNum + "," + CashBookLine + "," + MatchLineNum + ")", {
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
   Summary: Call UpdateExt to delete MatchedDocument item
   Description: Call UpdateExt to delete MatchedDocument item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MatchedDocument
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashBookLine Desc: CashBookLine   Required: True
      @param MatchLineNum Desc: MatchLineNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MatchedDocuments_Company_BankAcctID_CashBookNum_CashBookLine_MatchLineNum(Company:string, BankAcctID:string, CashBookNum:string, CashBookLine:string, MatchLineNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/MatchedDocuments(" + Company + "," + BankAcctID + "," + CashBookNum + "," + CashBookLine + "," + MatchLineNum + ")", {
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
   Description: Get CashBDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashBDtlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBDtlAttchRow
   */  
export function get_CashBDtlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashBDtlAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashBDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CashBDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashBDtlAttches(requestBody:Erp_Tablesets_CashBDtlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtlAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CashBDtlAttch item
   Description: Calls GetByID to retrieve the CashBDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashbookLine Desc: CashbookLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashBDtlAttchRow
   */  
export function get_CashBDtlAttches_Company_CashBookNum_CashbookLine_DrawingSeq(Company:string, CashBookNum:string, CashbookLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashBDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtlAttches(" + Company + "," + CashBookNum + "," + CashbookLine + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_CashBDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashBDtlAttch for the service
   Description: Calls UpdateExt to update CashBDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashBDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashbookLine Desc: CashbookLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashBDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashBDtlAttches_Company_CashBookNum_CashbookLine_DrawingSeq(Company:string, CashBookNum:string, CashbookLine:string, DrawingSeq:string, requestBody:Erp_Tablesets_CashBDtlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtlAttches(" + Company + "," + CashBookNum + "," + CashbookLine + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete CashBDtlAttch item
   Description: Call UpdateExt to delete CashBDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashBDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param CashbookLine Desc: CashbookLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashBDtlAttches_Company_CashBookNum_CashbookLine_DrawingSeq(Company:string, CashBookNum:string, CashbookLine:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtlAttches(" + Company + "," + CashBookNum + "," + CashbookLine + "," + DrawingSeq + ")", {
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
   Description: Get CashBHedAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashBHedAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBHedAttchRow
   */  
export function get_CashBHedAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBHedAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashBHedAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashBHedAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CashBHedAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashBHedAttches(requestBody:Erp_Tablesets_CashBHedAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBHedAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CashBHedAttch item
   Description: Calls GetByID to retrieve the CashBHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashBHedAttchRow
   */  
export function get_CashBHedAttches_Company_CashBookNum_DrawingSeq(Company:string, CashBookNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashBHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBHedAttches(" + Company + "," + CashBookNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_CashBHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashBHedAttch for the service
   Description: Calls UpdateExt to update CashBHedAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashBHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashBHedAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashBHedAttches_Company_CashBookNum_DrawingSeq(Company:string, CashBookNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_CashBHedAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBHedAttches(" + Company + "," + CashBookNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete CashBHedAttch item
   Description: Call UpdateExt to delete CashBHedAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashBHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashBookNum Desc: CashBookNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashBHedAttches_Company_CashBookNum_DrawingSeq(Company:string, CashBookNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBHedAttches(" + Company + "," + CashBookNum + "," + DrawingSeq + ")", {
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
   Description: Get BankRecExchangeRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankRecExchangeRates
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankRecExchangeRatesRow
   */  
export function get_BankRecExchangeRates(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankRecExchangeRatesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecExchangeRates", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankRecExchangeRatesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankRecExchangeRates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankRecExchangeRatesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BankRecExchangeRatesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankRecExchangeRates(requestBody:Erp_Tablesets_BankRecExchangeRatesRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecExchangeRates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the BankRecExchangeRate item
   Description: Calls GetByID to retrieve the BankRecExchangeRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankRecExchangeRate
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BankRecExchangeRatesRow
   */  
export function get_BankRecExchangeRates_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankRecExchangeRatesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecExchangeRates(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_BankRecExchangeRatesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BankRecExchangeRate for the service
   Description: Calls UpdateExt to update BankRecExchangeRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankRecExchangeRate
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankRecExchangeRatesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankRecExchangeRates_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_BankRecExchangeRatesRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecExchangeRates(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete BankRecExchangeRate item
   Description: Call UpdateExt to delete BankRecExchangeRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankRecExchangeRate
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BankRecExchangeRates_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecExchangeRates(" + SysRowID + ")", {
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
   Description: Get BankRecMessages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankRecMessages
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankRecMessagesRow
   */  
export function get_BankRecMessages(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankRecMessagesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecMessages", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankRecMessagesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankRecMessages
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankRecMessagesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BankRecMessagesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankRecMessages(requestBody:Erp_Tablesets_BankRecMessagesRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecMessages", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the BankRecMessage item
   Description: Calls GetByID to retrieve the BankRecMessage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankRecMessage
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BankRecMessagesRow
   */  
export function get_BankRecMessages_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankRecMessagesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecMessages(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_BankRecMessagesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BankRecMessage for the service
   Description: Calls UpdateExt to update BankRecMessage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankRecMessage
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankRecMessagesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankRecMessages_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_BankRecMessagesRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecMessages(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete BankRecMessage item
   Description: Call UpdateExt to delete BankRecMessage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankRecMessage
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BankRecMessages_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecMessages(" + SysRowID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedListRow)
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
export function get_GetRows(whereClauseCashBHed:string, whereClauseCashBHedAttch:string, whereClauseCashBFilterOptions:string, whereClauseSubLedgerDocs:string, whereClauseCashBDtl:string, whereClauseCashBDtlAttch:string, whereClauseMatchedDocuments:string, whereClauseBankRecExchangeRates:string, whereClauseBankRecMessages:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCashBHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashBHed=" + whereClauseCashBHed
   }
   if(typeof whereClauseCashBHedAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashBHedAttch=" + whereClauseCashBHedAttch
   }
   if(typeof whereClauseCashBFilterOptions!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashBFilterOptions=" + whereClauseCashBFilterOptions
   }
   if(typeof whereClauseSubLedgerDocs!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSubLedgerDocs=" + whereClauseSubLedgerDocs
   }
   if(typeof whereClauseCashBDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashBDtl=" + whereClauseCashBDtl
   }
   if(typeof whereClauseCashBDtlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashBDtlAttch=" + whereClauseCashBDtlAttch
   }
   if(typeof whereClauseMatchedDocuments!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMatchedDocuments=" + whereClauseMatchedDocuments
   }
   if(typeof whereClauseBankRecExchangeRates!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBankRecExchangeRates=" + whereClauseBankRecExchangeRates
   }
   if(typeof whereClauseBankRecMessages!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBankRecMessages=" + whereClauseBankRecMessages
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetRows" + params, {
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
export function get_GetByID(cashBookNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof cashBookNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "cashBookNum=" + cashBookNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetList" + params, {
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
   Summary: Invoke method AddStatement
   Description: Add Statement.  It is similar to GetNewCashBHed in functionality.
It should be used to create CashBHed with BankAcctID as input.
   OperationID: AddStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddStatement(requestBody:AddStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AddStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AddStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AutoMatchStatement
   Description: Used for Automated Bank Reconciliation
Auto match statement Lines
   OperationID: AutoMatchStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AutoMatchStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoMatchStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoMatchStatement(requestBody:AutoMatchStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AutoMatchStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoMatchStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AutoMatchStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BankStGetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: BankStGetLegalNumGenOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BankStGetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BankStGetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankStGetLegalNumGenOpts(requestBody:BankStGetLegalNumGenOpts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BankStGetLegalNumGenOpts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankStGetLegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BankStGetLegalNumGenOpts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsUnconvertedStatement
   Description: Check for unconverted statement
   OperationID: IsUnconvertedStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsUnconvertedStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsUnconvertedStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsUnconvertedStatement(requestBody:IsUnconvertedStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsUnconvertedStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/IsUnconvertedStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as IsUnconvertedStatement_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CheckDocumentIsLocked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method CreateLine
   Description: Call this method before calling other business objects like
Cash Receipts, PaymentEntry, Bank Adjustment etc.
This method creates the CashBDtl record and any other records
required to call the business object.
   OperationID: CreateLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateLine(requestBody:CreateLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CreateLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateManualLine
   Description: This method creates the CashBDtl record and any other records
required to call the business object.
   OperationID: CreateManualLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateManualLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateManualLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateManualLine(requestBody:CreateManualLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateManualLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CreateManualLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateManualLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateMatchedLink
   Description: Used for conversion from old Bank Statement
   OperationID: UpdateMatchedLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateMatchedLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMatchedLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateMatchedLink(requestBody:UpdateMatchedLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateMatchedLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/UpdateMatchedLink", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateMatchedLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OpenDocument
   Description: Use this method to open Payments/Cash receipts for non-matched
Bank Statement lines
   OperationID: OpenDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OpenDocument_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenDocument_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpenDocument(requestBody:OpenDocument_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OpenDocument_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/OpenDocument", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OpenDocument_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method NewDocumentWithUpdateStatement
   Description: Create Payments/Cash receipts for non-matched Bank Statement lines
   OperationID: NewDocumentWithUpdateStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/NewDocumentWithUpdateStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NewDocumentWithUpdateStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NewDocumentWithUpdateStatement(requestBody:NewDocumentWithUpdateStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<NewDocumentWithUpdateStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/NewDocumentWithUpdateStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as NewDocumentWithUpdateStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateNewDocuments
   Description: Used for Automated Bank Reconciliation
Use this method to create Payments/Cash receipts for non-matched
Bank Statement lines
   OperationID: CreateNewDocuments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateNewDocuments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewDocuments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateNewDocuments(requestBody:CreateNewDocuments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateNewDocuments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CreateNewDocuments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateNewDocuments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateNewCashMove
   Description: Used for Automated Bank Reconciliation
   OperationID: GenerateNewCashMove
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateNewCashMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateNewCashMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateNewCashMove(requestBody:GenerateNewCashMove_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateNewCashMove_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GenerateNewCashMove", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GenerateNewCashMove_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportStatement
   Description: Used for Automated Bank Reconciliation
Import Bank Statement file
   OperationID: ImportStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportStatement(requestBody:ImportStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ImportStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImporMultiStatement
   Description: Import Multi-Bank Statement file
   OperationID: ImporMultiStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImporMultiStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImporMultiStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImporMultiStatement(requestBody:ImporMultiStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImporMultiStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ImporMultiStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImporMultiStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportStatementContinue
   Description: Used for Automated Bank Reconciliation
Import Bank Statement file. Continue processing.
Importing of Bank Statement file could be interrupted by question message throwed to UI.
   OperationID: ImportStatementContinue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportStatementContinue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportStatementContinue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportStatementContinue(requestBody:ImportStatementContinue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportStatementContinue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ImportStatementContinue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportStatementContinue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportStatementDelete
   Description: Delete Bank Statement file.
   OperationID: ImportStatementDelete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportStatementDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportStatementDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportStatementDelete(requestBody:ImportStatementDelete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportStatementDelete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ImportStatementDelete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportStatementDelete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base CurrencyCode
   OperationID: GetCurrencyBase
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyBase(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCurrencyBase_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetCurrencyBase", {
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
         resolve(data as GetCurrencyBase_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFiscalPer
   OperationID: GetNewFiscalPer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFiscalPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFiscalPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFiscalPer(requestBody:GetNewFiscalPer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFiscalPer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetNewFiscalPer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewFiscalPer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetStatement
   Description: Get Statement.  Call this method when the user enters the Statement#.
It is similar to GetByID in functionality.
   OperationID: GetStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetStatement(requestBody:GetStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MatchDocument2Line
   Description: Used for Automated Bank Reconciliation
Match Transaction 2 statement Line.
   OperationID: MatchDocument2Line
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MatchDocument2Line_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchDocument2Line_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MatchDocument2Line(requestBody:MatchDocument2Line_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MatchDocument2Line_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/MatchDocument2Line", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MatchDocument2Line_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDocDiscount
   Description: Used for Automated Bank Reconciliation
   OperationID: OnChangeDocDiscount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDocDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDocDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDocDiscount(requestBody:OnChangeDocDiscount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDocDiscount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/OnChangeDocDiscount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDocDiscount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofApplyDate
   Description: This method should be called before the apply date has been updated.
   OperationID: OnChangeofApplyDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofApplyDate(requestBody:OnChangeofApplyDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofApplyDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/OnChangeofApplyDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeofApplyDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTranDocTypeId
   Description: Sets default values when the TranDocTypeID changes
   OperationID: OnChangeTranDocTypeId
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTranDocTypeId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranDocTypeId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTranDocTypeId(requestBody:OnChangeTranDocTypeId_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTranDocTypeId_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/OnChangeTranDocTypeId", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeTranDocTypeId_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingMXRecDate
   Description: Used to validate new Reconciled Date.
   OperationID: OnChangingMXRecDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingMXRecDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingMXRecDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingMXRecDate(requestBody:OnChangingMXRecDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingMXRecDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/OnChangingMXRecDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingMXRecDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingDocClosingBalance
   Description: Sets default values when Document Closing Balance is changes
   OperationID: OnChangingDocClosingBalance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingDocClosingBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDocClosingBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingDocClosingBalance(requestBody:OnChangingDocClosingBalance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingDocClosingBalance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/OnChangingDocClosingBalance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingDocClosingBalance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshCashBDtlAuto
   Description: This method similar to RefreshCashBDtl but uses for auto bank reconciliation
   OperationID: RefreshCashBDtlAuto
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshCashBDtlAuto_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshCashBDtlAuto_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshCashBDtlAuto(requestBody:RefreshCashBDtlAuto_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshCashBDtlAuto_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/RefreshCashBDtlAuto", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RefreshCashBDtlAuto_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshCashBDtl
   Description: Call this method after calling other business objects like
Cash Receipts, PaymentEntry, Bank Adjustment etc.
This method updates the CashBDtl record with the
data from other business objects.
   OperationID: RefreshCashBDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshCashBDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshCashBDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshCashBDtl(requestBody:RefreshCashBDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshCashBDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/RefreshCashBDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RefreshCashBDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshRatesList
   Description: Refresh Rates.
   OperationID: RefreshRatesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshRatesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshRatesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshRatesList(requestBody:RefreshRatesList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshRatesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/RefreshRatesList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RefreshRatesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRemittanceInfo
   Description: (Auto bank reconciliation) load remittance info dataset
   OperationID: GetRemittanceInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRemittanceInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRemittanceInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRemittanceInfo(requestBody:GetRemittanceInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRemittanceInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetRemittanceInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRemittanceInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetProcessStatus
   Description: Returns Statement status
   OperationID: GetProcessStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetProcessStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProcessStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetProcessStatus(requestBody:GetProcessStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetProcessStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetProcessStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetProcessStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RetrieveDocuments
   Description: Used for Automated Bank Reconciliation
   OperationID: RetrieveDocuments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RetrieveDocuments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveDocuments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RetrieveDocuments(requestBody:RetrieveDocuments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RetrieveDocuments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/RetrieveDocuments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RetrieveDocuments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectBank
   Description: Select a Bank.
   OperationID: SelectBank
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectBank(requestBody:SelectBank_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectBank_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SelectBank", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SelectBank_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LockGroup
   Description: Lock Group by Bank Account ID
   OperationID: LockGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockGroup(requestBody:LockGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LockGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/LockGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LockGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnmatchDocument
   Description: Used for Automated Bank Reconciliation
Unmatch single document.
   OperationID: UnmatchDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnmatchDocument_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnmatchDocument_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnmatchDocument(requestBody:UnmatchDocument_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnmatchDocument_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/UnmatchDocument", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnmatchDocument_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnmatchDocuments
   Description: Used for Automated Bank Reconciliation
   OperationID: UnmatchDocuments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnmatchDocuments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnmatchDocuments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnmatchDocuments(requestBody:UnmatchDocuments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnmatchDocuments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/UnmatchDocuments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnmatchDocuments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnSelectBank
   Description: Unlocks the group record locked by group name pcBankAcctID and by the user DCD-USERID.
   OperationID: UnSelectBank
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnSelectBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnSelectBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnSelectBank(requestBody:UnSelectBank_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnSelectBank_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/UnSelectBank", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnSelectBank_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnlockStatement
   Description: Unlocks the bank statement
   OperationID: UnlockStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnlockStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlockStatement(requestBody:UnlockStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnlockStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/UnlockStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnlockStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateAPPay
   Description: Delete obsolete Check
   OperationID: UpdateAPPay
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateAPPay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAPPay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAPPay(requestBody:UpdateAPPay_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateAPPay_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/UpdateAPPay", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateAPPay_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AllowPostStatement
   OperationID: AllowPostStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowPostStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AllowPostStatement(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AllowPostStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AllowPostStatement", {
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
         resolve(data as AllowPostStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNextCashBookNum
   Description: Get next CashBookNum.
   OperationID: GetNextCashBookNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextCashBookNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNextCashBookNum(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNextCashBookNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetNextCashBookNum", {
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
         resolve(data as GetNextCashBookNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReCalcAmount
   Description: Used for Automated Bank Reconciliation
   OperationID: ReCalcAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReCalcAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReCalcAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReCalcAmount(requestBody:ReCalcAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReCalcAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ReCalcAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ReCalcAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetBalances
   Description: Used for Automated Bank Reconciliation
Set balances amounts.
   OperationID: SetBalances
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetBalances_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetBalances_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetBalances(requestBody:SetBalances_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetBalances_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SetBalances", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetBalances_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method enableAddNewStatement
   Description: Method to determine the existence of a non posted Statement within the current bank account id.
   OperationID: enableAddNewStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/enableAddNewStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/enableAddNewStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_enableAddNewStatement(requestBody:enableAddNewStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<enableAddNewStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/enableAddNewStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as enableAddNewStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExtractInvoices
   Description: Extracts Invoice numbers from text
   OperationID: ExtractInvoices
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExtractInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExtractInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtractInvoices(requestBody:ExtractInvoices_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExtractInvoices_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ExtractInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExtractInvoices_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ParseText
   Description: Parse text using Regular Expressions
   OperationID: ParseText
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ParseText_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseText_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ParseText(requestBody:ParseText_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ParseText_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ParseText", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ParseText_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SplitKeywords
   Description: Split keys string into string array
   OperationID: SplitKeywords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SplitKeywords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SplitKeywords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SplitKeywords(requestBody:SplitKeywords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SplitKeywords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SplitKeywords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SplitKeywords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConcatenateKeywords
   Description: Concatenate keys array into string
   OperationID: ConcatenateKeywords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ConcatenateKeywords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConcatenateKeywords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConcatenateKeywords(requestBody:ConcatenateKeywords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ConcatenateKeywords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ConcatenateKeywords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ConcatenateKeywords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistsUnverifiedTransfers
   Description: Checks if there are any unposted transfers to or from this bank created from automatic bank reconciliation,
or if there are any uncleared posted transfers which are not already loaded as posible transfers for that statement line.
   OperationID: ExistsUnverifiedTransfers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExistsUnverifiedTransfers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsUnverifiedTransfers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsUnverifiedTransfers(requestBody:ExistsUnverifiedTransfers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExistsUnverifiedTransfers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ExistsUnverifiedTransfers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExistsUnverifiedTransfers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnPartnerInfoChanged
   Description: Tries to recognize partner using transaction code, partner ID (XRef), partner bank code, partner bank account.
   OperationID: OnPartnerInfoChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnPartnerInfoChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPartnerInfoChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnPartnerInfoChanged(requestBody:OnPartnerInfoChanged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnPartnerInfoChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/OnPartnerInfoChanged", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnPartnerInfoChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnPartnerNameChanged
   Description: Tries to recognize partner using partner ID (XRef).
   OperationID: OnPartnerNameChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnPartnerNameChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPartnerNameChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnPartnerNameChanged(requestBody:OnPartnerNameChanged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnPartnerNameChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/OnPartnerNameChanged", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnPartnerNameChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshTranCodeList
   OperationID: RefreshTranCodeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshTranCodeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshTranCodeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshTranCodeList(requestBody:RefreshTranCodeList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshTranCodeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/RefreshTranCodeList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RefreshTranCodeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPeriodThresholdDate
   OperationID: GetPeriodThresholdDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPeriodThresholdDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPeriodThresholdDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPeriodThresholdDate(requestBody:GetPeriodThresholdDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPeriodThresholdDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetPeriodThresholdDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPeriodThresholdDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method StorePartner
   Description: Stores Partner
   OperationID: StorePartner
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/StorePartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StorePartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StorePartner(requestBody:StorePartner_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<StorePartner_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/StorePartner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as StorePartner_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PartnerExists
   Description: Search partner by Partner name
   OperationID: PartnerExists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PartnerExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartnerExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartnerExists(requestBody:PartnerExists_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PartnerExists_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/PartnerExists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PartnerExists_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearSuggestion
   Description: Clear suggestion from documents for specified line.
   OperationID: ClearSuggestion
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ClearSuggestion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearSuggestion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearSuggestion(requestBody:ClearSuggestion_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ClearSuggestion_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ClearSuggestion", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ClearSuggestion_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReLoadBatchSubLedgerDocs
   OperationID: ReLoadBatchSubLedgerDocs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReLoadBatchSubLedgerDocs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReLoadBatchSubLedgerDocs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReLoadBatchSubLedgerDocs(requestBody:ReLoadBatchSubLedgerDocs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReLoadBatchSubLedgerDocs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ReLoadBatchSubLedgerDocs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ReLoadBatchSubLedgerDocs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddMissingBankBatchSubLedgerDoc
   OperationID: AddMissingBankBatchSubLedgerDoc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddMissingBankBatchSubLedgerDoc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMissingBankBatchSubLedgerDoc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddMissingBankBatchSubLedgerDoc(requestBody:AddMissingBankBatchSubLedgerDoc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddMissingBankBatchSubLedgerDoc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AddMissingBankBatchSubLedgerDoc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AddMissingBankBatchSubLedgerDoc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddMissingBatchedSubLedgerDocs
   OperationID: AddMissingBatchedSubLedgerDocs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddMissingBatchedSubLedgerDocs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMissingBatchedSubLedgerDocs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddMissingBatchedSubLedgerDocs(requestBody:AddMissingBatchedSubLedgerDocs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddMissingBatchedSubLedgerDocs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AddMissingBatchedSubLedgerDocs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AddMissingBatchedSubLedgerDocs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSubLedgerDocs
   Description: Check if SubLedgerDocs was modified outside AutoBankRec.
   OperationID: CheckSubLedgerDocs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckSubLedgerDocs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSubLedgerDocs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSubLedgerDocs(requestBody:CheckSubLedgerDocs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckSubLedgerDocs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CheckSubLedgerDocs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckSubLedgerDocs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsExistingSearchIDForPartner
   OperationID: IsExistingSearchIDForPartner
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsExistingSearchIDForPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsExistingSearchIDForPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsExistingSearchIDForPartner(requestBody:IsExistingSearchIDForPartner_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsExistingSearchIDForPartner_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/IsExistingSearchIDForPartner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as IsExistingSearchIDForPartner_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTolerance
   OperationID: CheckTolerance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckTolerance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTolerance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTolerance(requestBody:CheckTolerance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckTolerance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CheckTolerance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckTolerance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTransactionCodes
   Description: Get Transaction Code list
   OperationID: GetTransactionCodes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTransactionCodes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransactionCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransactionCodes(requestBody:GetTransactionCodes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTransactionCodes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetTransactionCodes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTransactionCodes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDocumentList
   Description: Used for Automated Bank Reconciliation
Get documents with manual legal number entry.
   OperationID: GetDocumentList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDocumentList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDocumentList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDocumentList(requestBody:GetDocumentList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDocumentList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetDocumentList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDocumentList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HasLinkedReverseLines
   Description: Check whether exists matched reversed
   OperationID: HasLinkedReverseLines
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HasLinkedReverseLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasLinkedReverseLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HasLinkedReverseLines(requestBody:HasLinkedReverseLines_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HasLinkedReverseLines_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/HasLinkedReverseLines", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as HasLinkedReverseLines_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnmatchLinkedReverseLines
   OperationID: UnmatchLinkedReverseLines
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnmatchLinkedReverseLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnmatchLinkedReverseLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnmatchLinkedReverseLines(requestBody:UnmatchLinkedReverseLines_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnmatchLinkedReverseLines_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/UnmatchLinkedReverseLines", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnmatchLinkedReverseLines_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecognizePartners
   Description: Used for Automated Bank Reconciliation
Recognize partners in statement lines
   OperationID: RecognizePartners
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RecognizePartners_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecognizePartners_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecognizePartners(requestBody:RecognizePartners_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RecognizePartners_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/RecognizePartners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RecognizePartners_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindObsoleteReceiptsPayments
   Description: The method 1. finds and deletes obsolete payments (created in statement, but not matched)
2. finds obsolete receipts (with NO customer)
   OperationID: FindObsoleteReceiptsPayments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FindObsoleteReceiptsPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindObsoleteReceiptsPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindObsoleteReceiptsPayments(requestBody:FindObsoleteReceiptsPayments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FindObsoleteReceiptsPayments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/FindObsoleteReceiptsPayments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as FindObsoleteReceiptsPayments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExtendedProperties
   Description: Get Amounts Extended properties
   OperationID: GetExtendedProperties
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetExtendedProperties_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtendedProperties_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExtendedProperties(requestBody:GetExtendedProperties_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetExtendedProperties_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetExtendedProperties", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetExtendedProperties_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/PreUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetLegNumDefaults
   Description: This method will return a record in the LegalNumGenOpts data table if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: GetLegNumDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLegNumDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegNumDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLegNumDefaults(requestBody:GetLegNumDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLegNumDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetLegNumDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetLegNumDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsAutomaticVoiding
   Description: Determines whether legal number configuration for bank statement is automatic voiding for a the specified date.
   OperationID: IsAutomaticVoiding
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsAutomaticVoiding_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAutomaticVoiding_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsAutomaticVoiding(requestBody:IsAutomaticVoiding_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsAutomaticVoiding_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/IsAutomaticVoiding", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as IsAutomaticVoiding_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the Bank Statement.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AssignLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/VoidLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method SelectBankLockGroups
   Description: Select a Bank.
   OperationID: SelectBankLockGroups
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectBankLockGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectBankLockGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectBankLockGroups(requestBody:SelectBankLockGroups_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectBankLockGroups_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SelectBankLockGroups", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SelectBankLockGroups_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBankInfo
   Description: Gets Bank account info.
   OperationID: GetBankInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBankInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankInfo(requestBody:GetBankInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBankInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetBankInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBankInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddNewStatement
   Description: Add Statement.  It is similar to GetNewCashBHed in functionality.
It should be used to create CashBHed with BankAcctID as input.
   OperationID: AddNewStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddNewStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddNewStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddNewStatement(requestBody:AddNewStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddNewStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AddNewStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AddNewStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportStatementSlip
   Description: Used for Automated Bank Reconciliation
Import Bank Statement file
   OperationID: ImportStatementSlip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportStatementSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportStatementSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportStatementSlip(requestBody:ImportStatementSlip_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportStatementSlip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ImportStatementSlip", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportStatementSlip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportStatementSlipContinue
   Description: Used for Automated Bank Reconciliation
Import Bank Statement file
   OperationID: ImportStatementSlipContinue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportStatementSlipContinue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportStatementSlipContinue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportStatementSlipContinue(requestBody:ImportStatementSlipContinue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportStatementSlipContinue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/ImportStatementSlipContinue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportStatementSlipContinue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BankStmtGetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: BankStmtGetLegalNumGenOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BankStmtGetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BankStmtGetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankStmtGetLegalNumGenOpts(requestBody:BankStmtGetLegalNumGenOpts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BankStmtGetLegalNumGenOpts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankStmtGetLegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BankStmtGetLegalNumGenOpts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBankStatement
   OperationID: GetBankStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBankStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankStatement(requestBody:GetBankStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBankStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetBankStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBankStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBankSlip
   Description: Valid Bank slip check
   OperationID: CheckBankSlip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckBankSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBankSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBankSlip(requestBody:CheckBankSlip_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckBankSlip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CheckBankSlip", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckBankSlip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LockStatement
   Description: Locks the bank statement
   OperationID: LockStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LockStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockStatement(requestBody:LockStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LockStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/LockStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LockStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeClosingDate
   Description: This method should be called before the closing date has been updated.
   OperationID: OnChangeClosingDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeClosingDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClosingDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeClosingDate(requestBody:OnChangeClosingDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeClosingDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/OnChangeClosingDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeClosingDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOpeningDate
   Description: This method should be called before the opening date has been updated.
   OperationID: OnChangeOpeningDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOpeningDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOpeningDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOpeningDate(requestBody:OnChangeOpeningDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOpeningDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/OnChangeOpeningDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOpeningDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeClearDate
   Description: This method should be called before the clear date has been updated.
   OperationID: OnChangeClearDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeClearDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClearDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeClearDate(requestBody:OnChangeClearDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeClearDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/OnChangeClearDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeClearDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrePostStatement
   Description: Prepost statement
   OperationID: PrePostStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PrePostStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePostStatement(requestBody:PrePostStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PrePostStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/PrePostStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PrePostStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SearchPartner
   Description: Prepost statement
   OperationID: SearchPartner
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SearchPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SearchPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SearchPartner(requestBody:SearchPartner_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SearchPartner_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SearchPartner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SearchPartner_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshLineRatesList
   Description: Refresh Rates.
   OperationID: RefreshLineRatesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshLineRatesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshLineRatesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshLineRatesList(requestBody:RefreshLineRatesList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshLineRatesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/RefreshLineRatesList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RefreshLineRatesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashBHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashBHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCashBHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashBHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashBHed(requestBody:GetNewCashBHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCashBHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetNewCashBHed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCashBHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashBHedAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashBHedAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCashBHedAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashBHedAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashBHedAttch(requestBody:GetNewCashBHedAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCashBHedAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetNewCashBHedAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCashBHedAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashBFilterOptions
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashBFilterOptions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCashBFilterOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashBFilterOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashBFilterOptions(requestBody:GetNewCashBFilterOptions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCashBFilterOptions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetNewCashBFilterOptions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCashBFilterOptions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSubLedgerDocs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSubLedgerDocs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSubLedgerDocs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSubLedgerDocs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSubLedgerDocs(requestBody:GetNewSubLedgerDocs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSubLedgerDocs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetNewSubLedgerDocs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewSubLedgerDocs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashBDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashBDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCashBDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashBDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashBDtl(requestBody:GetNewCashBDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCashBDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetNewCashBDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCashBDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashBDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashBDtlAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCashBDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashBDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashBDtlAttch(requestBody:GetNewCashBDtlAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCashBDtlAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetNewCashBDtlAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCashBDtlAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMatchedDocuments
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMatchedDocuments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMatchedDocuments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMatchedDocuments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMatchedDocuments(requestBody:GetNewMatchedDocuments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMatchedDocuments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetNewMatchedDocuments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewMatchedDocuments_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankRecExchangeRatesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankRecExchangeRatesRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankRecMessagesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankRecMessagesRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBDtlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashBDtlAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashBDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBFilterOptionsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashBFilterOptionsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashBHedAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashBHedListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashBHedRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MatchedDocumentsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MatchedDocumentsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SubLedgerDocsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SubLedgerDocsRow,
}

export interface Erp_Tablesets_BankRecExchangeRatesRow{
   "CashBookLine":number,
   "CurrencyCode":string,
   "DecimalsGeneral":number,
   "ExchangeRate":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BankRecMessagesRow{
   "MessageType":number,
   "MessageText":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashBDtlAttchRow{
   "Company":string,
   "CashBookNum":number,
   "CashbookLine":number,
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

export interface Erp_Tablesets_CashBDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  BankAcctID  */  
   "BankAcctID":string,
      /**  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed and uses its CashBookNum + 1. Not directly entered by the user.  */  
   "CashBookNum":number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   "CashbookLine":number,
      /**  Indicates the line number.  */  
   "LineNum":number,
      /**  Description  */  
   "Description":string,
      /**  Identifies the type of transaction. Possible values are 'Banktran' for bank adjustments, 'manual' for manual A/P payments, 'appay' for A/P payments, 'prpay' for P/R payments, 'crpay' for cashreceipts which are entered in the Cash Receipt Entry program, 'payinv' for invoice cash receipts, 'deposit' for deposit cash receipts and 'mispay' for miscellaneous cash receipts.  */  
   "TranType":string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Fiscal Year. This is not entered by the user on each record.  */  
   "FiscalYear":number,
      /**  Fiscal period for the transaction. Not directly entered by the user.  */  
   "FiscalPeriod":number,
      /**  Indicates the transaction date in the statement line.  */  
   "TranDate":string,
      /**  Amount of transaction that is being applied.  */  
   "TranAmt":number,
      /**  Amount of transaction that is being applied.  */  
   "DocTranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**  Fiscal Year Suffix. This is not entered by the user on each record.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Used on Bank Fees created from Bank Reconciliation, Identifies the type of transaction from was created. Possible values are 'Manual' for Manual A/P payments and ?PayInv? for Invoice Cash Receipt.  */  
   "LinkedTranType":string,
      /**  Used on Bank Fees, this field will be used to link Checks or AR Payments created from Bank Reconciliation.  */  
   "LinkedHeadNum":number,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  Indicates the name of the partner in the statement line.  */  
   "Partner":string,
      /**  Indicates the ID of the partner. The bank uses this ID to specify the partner in the statement line.  */  
   "PartnerName":string,
      /**  Partner Number  */  
   "PartnerNum":number,
      /**  Partner Type  */  
   "PartnerType":number,
      /**  Debit Credit Mark  */  
   "DebitCreditMark":string,
      /**  Indicates the statement line amount in line currency.  */  
   "ImportTranAmount":number,
      /**  Indicates the part of statement line amount that is not matched with an existing document in transaction currency.  */  
   "ImportTranUnclearedAmount":number,
      /**  Indicates the part of statement line amount that is not matched with an existing document.  */  
   "ImportUnclearedAmount":number,
      /**  Import Report 1 Uncleared Amount  */  
   "ImportRpt1UnclearedAmount":number,
      /**  Import Report 2 Uncleared Amount  */  
   "ImportRpt2UnclearedAmount":number,
      /**  Import Report 3 Uncleared Amount  */  
   "ImportRpt3UnclearedAmount":number,
      /**  Indicates the currency code for the transaction amount.  */  
   "ImportTranCurrency":string,
      /**  Indicates the statement line amount in bank currency.  */  
   "ImportBankAmount":number,
      /**  Indicates the difference between the amount of the currently selected statement line and the total amount of transactions currently selected for  */  
   "ImportBankVariance":number,
      /**  Import Amount  */  
   "ImportAmount":number,
      /**  Indicates the exchange rate between the line currency and the bank currency.  */  
   "ExchangeRate":number,
      /**  Indicates the statement line's status.  */  
   "LineStatus":number,
      /**  Indicates the type of the statement line.  */  
   "LineType":number,
      /**  Indicates the statement line transaction text.  */  
   "LineDescription":string,
      /**  Document List  */  
   "DocumentList":string,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  The application displays here the information explaining why it did not perform correctly automatic line recognition, document creation or matching.  */  
   "ImportError":string,
      /**  Filter By Partner  */  
   "FilterByPartner":boolean,
      /**  Import Bank Gain Loss  */  
   "ImportBankGainLoss":number,
      /**  Gain/Loss  */  
   "ImportGainLoss":number,
      /**  Import Report 1 Gain Loss  */  
   "ImportRpt1GainLoss":number,
      /**  Import Report 2 Gain Loss  */  
   "ImportRpt2GainLoss":number,
      /**  Import Report 3 Gain Loss  */  
   "ImportRpt3GainLoss":number,
      /**  BankTranType  */  
   "BankTranType":string,
      /**  Indicates the difference between the total line amount in bank currency and the applied transactions amount  */  
   "ImportBankUnclearedAmount":number,
      /**  Indicates the type of the transaction.  */  
   "ImportTranType":string,
      /**  Indicates the code of the transaction.  */  
   "ImportTranCode":string,
      /**  Indicates the number of the business document related to the line which is known to the bank.  */  
   "TranRef":string,
      /**  Indicates the code of the partner bank.  */  
   "PartnerBank":string,
      /**  Indicates the account of the partner bank.  */  
   "PartnerBankAcct":string,
      /**  This check box is selected if the line is of the Reverse Cash Receipt or Voided AP Payment type.  */  
   "ReverseFlag":boolean,
      /**  Indicates the total charges amount.  */  
   "TotalChrgAmt":number,
      /**  Indicates the currency code for the total charges.  */  
   "ChrgCurrCode":string,
      /**  RawData  */  
   "RawData":string,
      /**  Indicates the reference details of the invoice.  */  
   "MatchingInfo":string,
      /**  RemitData  */  
   "RemitData":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Bank Fee ID  */  
   "BankFeeID":string,
      /**  Transfer Bank ID  */  
   "TransferBankID":string,
      /**  PartnerID  */  
   "PartnerID":string,
      /**  CreateMode  */  
   "CreateMode":number,
      /**  Add any comments in this field if required.  */  
   "UserComment":string,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  UserReference  */  
   "UserReference":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Disable MXRecDate  */  
   "DisableMXRecDate":boolean,
   "DocTotalCandAmt":number,
   "DocTotalRemAmt":number,
   "DocTotalSelAmt":number,
      /**  Contains description of imported line with potential Invoices numbers list.  */  
   "DocumentsRefData":string,
   "DspLineNum":string,
   "ExchangeRates":string,
      /**  Stores HeadNum or TranNum value.  Used to call BankAdjEntry, PaymentEntry or CashRec - GetByID method.  */  
   "HeadNum":number,
      /**  Indicates the difference between the amount of the currently selected statement line and the total amount of transactions currently selected for  */  
   "ImportBankVarianceDsp":number,
   "ImportCreditAmount":number,
   "ImportDebitAmount":number,
   "ImportDspBankAmount":number,
      /**  Transaction Code Description  */  
   "ImportTranCodeDesc":string,
   "isCleared":boolean,
   "NewDoc":boolean,
      /**  Reference field.  */  
   "Reference":string,
   "Rounding":number,
   "Rpt1TotalCandAmt":number,
   "Rpt1TotalRemAmt":number,
   "Rpt1TotalSelAmt":number,
   "Rpt2TotalCandAmt":number,
   "Rpt2TotalRemAmt":number,
   "Rpt2TotalSelAmt":number,
   "Rpt3TotalCandAmt":number,
   "Rpt3TotalRemAmt":number,
   "Rpt3TotalSelAmt":number,
      /**  AP Clearing Total Candidates  */  
   "TotalCandAmt":number,
      /**  AP Clearing Total Remaining  */  
   "TotalRemAmt":number,
      /**  AP Clearing Total Selected  */  
   "TotalSelAmt":number,
      /**  Transaction Reference 1  */  
   "TranRef1":string,
      /**  Transaction Reference 2  */  
   "TranRef2":string,
      /**  Transaction Reference 3  */  
   "TranRef3":string,
   "TranTemplateID":string,
      /**  Tran Type description  */  
   "TranTypeDescription":string,
   "DspUnallocatedAmount":number,
   "DspUnallocatedCurrency":string,
   "BitFlag":number,
   "BankAcctIDBankName":string,
   "BankAcctIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashBFilterOptionsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the bank account.  */  
   "BankAcctID":string,
      /**  Cash Book Number.  */  
   "CashBookNum":number,
      /**  Line Type  */  
   "LineType":number,
      /**  Filter AP Invoices  */  
   "FilterAPInvoices":boolean,
      /**  Filter AP Pay  */  
   "FilterAPPay":boolean,
      /**  Filter AP Payment Instruments  */  
   "FilterAPPI":boolean,
      /**  Filter AR Payment Instruments  */  
   "FilterARPI":boolean,
      /**  Filter AR Invoices  */  
   "FilterARInvoices":boolean,
      /**  Filter Bank Adjustments  */  
   "FilterBankAdj":boolean,
      /**  Filter Bank Transactions  */  
   "FilterBankTran":boolean,
      /**  Filter Cash Receipts Payments  */  
   "FilterCRPay":boolean,
      /**  Filter Reversed AP Payments  */  
   "FilterRevAPPay":boolean,
      /**  Filter Reversed Cash Receipts Payments  */  
   "FilterRevCRPay":boolean,
      /**  Filter All  */  
   "FilterAll":boolean,
      /**  Filter Payments  */  
   "FilterPayments":boolean,
      /**  Filter Receipts  */  
   "FilterReceipts":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Filter PR Pay  */  
   "FilterPRPay":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashBHedAttchRow{
   "Company":string,
   "CashBookNum":number,
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

export interface Erp_Tablesets_CashBHedListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Specifies the identifier for the bank account.  */  
   "BankAcctID":string,
      /**  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed and uses its CashBookNum + 1. Not directly entered by the user.  */  
   "CashBookNum":number,
      /**  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed of a Bank Account and a Fiscal Year and uses its Bankslip + 1. The user can override this number when no cashbook lines are available for this bankslip.  */  
   "Bankslip":number,
      /**  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  */  
   "GroupID":string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Indicates a description of the statement.  */  
   "Description":string,
      /**  Specifies opening balance for the statement.  */  
   "OpeningBalance":number,
      /**  The Opening Balance of the Bank Account.  When a Reconciliation is posted this field is set to the Closing Balance.  */  
   "DocOpeningBalance":number,
      /**  Specifies the opening date for transactions for the bank account.  */  
   "OpeningDate":string,
      /**  Specifies the closing amount for the statement.  */  
   "ClosingBalance":number,
      /**  The Closing Balance of the Bank Account.  */  
   "DocClosingBalance":number,
      /**  Specifies the closing date for transactions for the bank account.  */  
   "ClosingDate":string,
      /**  Displays the fiscal year of the transaction.  */  
   "FiscalYear":number,
      /**  Displays the fiscal period of the transaction.  */  
   "FiscalPeriod":number,
      /**  The currency of the Bank Account  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this Check.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClosingBalance":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClosingBalance":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClosingBalance":number,
      /**  Reporting currency value of this field  */  
   "Rpt1OpeningBalance":number,
      /**  Reporting currency value of this field  */  
   "Rpt2OpeningBalance":number,
      /**  Reporting currency value of this field  */  
   "Rpt3OpeningBalance":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Specifies the fiscal year suffix of the fiscal year during which the transactions occurred.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Specifies the date for which the statement applies.  */  
   "ApplyDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DocNetChange":number,
   "LineTotal":number,
   "Variance":number,
   "DocLineTotal":number,
   "DocVariance":number,
   "CurrencySwitch":boolean,
   "APInterfaced":boolean,
   "Rpt1LineTotal":number,
   "Rpt1Variance":number,
   "Rpt2LineTotal":number,
   "Rpt2Variance":number,
   "Rpt3LineTotal":number,
   "Rpt3Variance":number,
      /**  shows is this invoice is blocked in RvLock  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  Locked means can not be posted: an invoice is already in review journal or in posting process  */  
   "LockStatus":string,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Full description of the bank account.  */  
   "BankAcctIDDescription":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrSymbol":string,
      /**  Description of the currency  */  
   "BaseCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseDocumentDesc":string,
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
      /**  Description  */  
   "RateGrpDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashBHedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Specifies the identifier for the bank account.  */  
   "BankAcctID":string,
      /**  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed and uses its CashBookNum + 1. Not directly entered by the user.  */  
   "CashBookNum":number,
      /**  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed of a Bank Account and a Fiscal Year and uses its Bankslip + 1. The user can override this number when no cashbook lines are available for this bankslip.  */  
   "Bankslip":number,
      /**  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  */  
   "GroupID":string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Indicates a description of the statement.  */  
   "Description":string,
      /**  Specifies opening balance for the statement.  */  
   "OpeningBalance":number,
      /**  The Opening Balance of the Bank Account.  When a Reconciliation is posted this field is set to the Closing Balance.  */  
   "DocOpeningBalance":number,
      /**  Specifies the opening date for transactions for the bank account.  */  
   "OpeningDate":string,
      /**  Specifies the closing amount for the statement.  */  
   "ClosingBalance":number,
      /**  The Closing Balance of the Bank Account.  */  
   "DocClosingBalance":number,
      /**  Specifies the closing date for transactions for the bank account.  */  
   "ClosingDate":string,
      /**  Displays the fiscal year of the transaction.  */  
   "FiscalYear":number,
      /**  Displays the fiscal period of the transaction.  */  
   "FiscalPeriod":number,
      /**  The currency of the Bank Account  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this Check.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClosingBalance":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClosingBalance":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClosingBalance":number,
      /**  Reporting currency value of this field  */  
   "Rpt1OpeningBalance":number,
      /**  Reporting currency value of this field  */  
   "Rpt2OpeningBalance":number,
      /**  Reporting currency value of this field  */  
   "Rpt3OpeningBalance":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Specifies the fiscal year suffix of the fiscal year during which the transactions occurred.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Specifies the date for which the statement applies.  */  
   "ApplyDate":string,
      /**  Filter To Date  */  
   "FilterToDate":string,
      /**  Filter To Date Token  */  
   "FilterToDateToken":string,
      /**  Retrieve Status  */  
   "RetrieveStatus":number,
      /**  Include PI Past Close  */  
   "IncludePIPastClose":boolean,
      /**  Imported  */  
   "Imported":boolean,
      /**  CashReceipt Group  */  
   "GrpCashReceipt":string,
      /**  AP Payment Group  */  
   "GrpAPPay":string,
      /**  Bank Adjustment Group  */  
   "GrpBankAdj":string,
      /**  BankTransfer Group  */  
   "GrpBankTrans":string,
      /**  RefNum  */  
   "RefNum":string,
      /**  Info  */  
   "Info":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  FilterByLineType  */  
   "FilterByLineType":boolean,
      /**  StatementDate  */  
   "StatementDate":string,
      /**  UseClosingDateCutoff  */  
   "UseClosingDateCutoff":boolean,
      /**  Select the transaction document type for the bank statement, if necessary.  */  
   "TranDocTypeID":string,
      /**  When the application assigns a legal number to the statement, it is displayed in this field. Refer to the Actions - Legal Numbers commands.  */  
   "LegalNumber":string,
      /**  UnconvertedStatement  */  
   "UnconvertedStatement":boolean,
      /**  StatementVersion  */  
   "StatementVersion":number,
      /**  AR Payment Instrument Group  */  
   "GrpARPI":string,
      /**  ProcessStatus  */  
   "ProcessStatus":string,
      /**  ThresholdDate  */  
   "ThresholdDate":string,
      /**  ClearDate  */  
   "ClearDate":string,
      /**  Comments  */  
   "Comments":string,
   "APInterfaced":boolean,
   "BankTranCodeList":string,
   "BaseCurrDesc":string,
   "BaseCurrencyID":string,
   "BaseCurrName":string,
   "BaseCurrSymbol":string,
   "BaseDocumentDesc":string,
   "CurrencyList":string,
   "CurrencySwitch":boolean,
   "CurrentBalance":number,
   "DefaultLineType":number,
   "DocCurrentBalance":number,
   "DocLineTotal":number,
   "DocNetChange":number,
   "DocNonReconciled":number,
   "DocReconciledBalance":number,
   "DocVariance":number,
   "DspDocRunningBal":number,
   "DspDocVariance":number,
   "DspRunningBal":number,
   "DspVariance":number,
      /**  Legal Number Field  */  
   "EnableAssignLegNum":boolean,
   "EnableTranDocType":boolean,
      /**  Legal Number Field  */  
   "EnableVoidLegNum":boolean,
      /**  Legal Number Field  */  
   "HasLegNumCnfg":boolean,
      /**  shows is this invoice is blocked in RvLock  */  
   "IsLcked":boolean,
   "LegalNumStyle":string,
   "LineTotal":number,
      /**  Locked means can not be posted: an invoice is already in review journal or in posting process  */  
   "LockStatus":string,
   "NonReconciled":number,
   "ReconciledBalance":number,
   "Rpt1CurrentBalance":number,
   "Rpt1DspRunningBal":number,
   "Rpt1DspVariance":number,
   "Rpt1LineTotal":number,
   "Rpt1NonReconciled":number,
   "Rpt1ReconciledBalance":number,
   "Rpt1Variance":number,
   "Rpt2CurrentBalance":number,
   "Rpt2DspRunningBal":number,
   "Rpt2DspVariance":number,
   "Rpt2LineTotal":number,
   "Rpt2NonReconciled":number,
   "Rpt2ReconciledBalance":number,
   "Rpt2Variance":number,
   "Rpt3CurrentBalance":number,
   "Rpt3DspRunningBal":number,
   "Rpt3DspVariance":number,
   "Rpt3LineTotal":number,
   "Rpt3NonReconciled":number,
   "Rpt3ReconciledBalance":number,
   "Rpt3Variance":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  Legal Number Field  */  
   "SystemTranType":string,
   "TranDocTypeDesc":string,
   "UpdateDates":number,
   "Variance":number,
      /**  Legal Number Field  */  
   "AllowChgAfterPrint":boolean,
   "BalanceStatus":string,
      /**  Standar Legal Number message when a new legal number is created.  */  
   "LegalNumMessage":string,
   "ActiveUserID":string,
   "BitFlag":number,
   "BankAcctIDBankName":string,
   "BankAcctIDDescription":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrDesc":string,
   "RateGrpDescription":string,
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

export interface Erp_Tablesets_MatchedDocumentsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the bank account.  */  
   "BankAcctID":string,
      /**  Cash Book Number.  */  
   "CashBookNum":number,
      /**  Cash Book Line Number.  */  
   "CashBookLine":number,
      /**  Match Line Num  */  
   "MatchLineNum":number,
      /**  Indicates the type of the document matched to the line. The application uses  */  
   "DocumentType":number,
      /**  Document Type Mode  */  
   "DocumentTypeMode":number,
      /**  Reference  */  
   "Reference":string,
      /**  Partner  */  
   "Partner":string,
      /**  Indicates the name of the partner in the matched document.  */  
   "PartnerName":string,
      /**  Indicates the legal number of the matched document.  */  
   "LegalNumber":string,
      /**  Indicates the internal number of the matched document.  */  
   "InternalNumber":string,
      /**  Indicates the matched document amount in the document currency.  */  
   "DocAmount":number,
      /**  Indicates the matched document currency.  */  
   "DocCurrency":string,
      /**  Indicates the matched document date.  */  
   "DocDate":string,
      /**  Doc Discount Amount  */  
   "DocDiscountAmount":number,
      /**  Indicates the matched document amount in the bank currency.  */  
   "TranAmount":number,
      /**  Indicates the document currency  */  
   "TranCurrency":string,
      /**  Indicates the matched document amount in the bank currency.  */  
   "BankAmount":number,
      /**  Bank Currency  */  
   "BankCurrency":string,
      /**  Base Amount  */  
   "BaseAmount":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  If the line was matched to a batch or a batch payment, this field indicates the number of the batch reference.  */  
   "BankBatchRef":string,
      /**  If this document was created either manually or automatically, this field indicates the document type.  */  
   "NewDoc":number,
      /**  SysRowID of matched document  */  
   "ExternalSysRowID":string,
      /**  If the line was matched to a batch or a batch payment, this field indicates the SysRowID of the batch.  */  
   "BankBatchSysRowID":string,
      /**  UserReference  */  
   "UserReference":string,
      /**  Matched document reference key 1  */  
   "Key1":string,
      /**  Matched document reference key 2  */  
   "Key2":string,
      /**  Matched document reference key 3  */  
   "Key3":string,
   "MasterTypeMode":number,
   "Selected":boolean,
   "BankBatchID":string,
   "CreateMode":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SubLedgerDocsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the bank account.  */  
   "BankAcctID":string,
      /**  Cash Book Number.  */  
   "CashBookNum":number,
      /**  Document Type  */  
   "DocumentType":number,
      /**  Reference  */  
   "Reference":string,
      /**  Cash Book Line Number.  */  
   "CashBookLine":number,
      /**  Document Type Mode  */  
   "DocumentTypeMode":number,
      /**  Indicates the partner ID.  */  
   "Partner":string,
      /**  Indicates the partner name.  */  
   "PartnerName":string,
      /**  Partner Number  */  
   "PartnerNum":number,
      /**  Document Status  */  
   "DocumentStatus":boolean,
      /**  Indicates the legal number of the unmatched document.  */  
   "LegalNumber":string,
      /**  Internal Number  */  
   "InternalNumber":string,
      /**  Indicates the unmatched document amount in the document currency.  */  
   "DocAmount":number,
      /**  Indicates the unmatched document currency.  */  
   "DocCurrency":string,
      /**  Indicates the unmatched document date.  */  
   "DocDate":string,
      /**  Indicates the document amount in bank currency.  */  
   "BankAmount":number,
      /**  Indicates a bank currency code.  */  
   "BankCurrency":string,
      /**  Group ID  */  
   "GroupID":string,
      /**  Base Amount  */  
   "BaseAmount":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Suggested For Lines  */  
   "SuggestedForLines":string,
      /**  Indicates the refrence number of the batch.  */  
   "BankBatchRef":string,
      /**  SysRowID of the unmatched document  */  
   "ExternalSysRowID":string,
      /**  Indicates the SysRowID of the batch.  */  
   "BankBatchSysRowID":string,
      /**  UserReference  */  
   "UserReference":string,
      /**  SubLedger document reference key 2  */  
   "Key2":string,
      /**  SubLedger document reference key 3  */  
   "Key3":string,
   "QSInternalNumber":string,
   "Ranged":boolean,
   "Selected":boolean,
   "ShouldBeHidden":boolean,
   "Suggested":boolean,
   "BankBatchID":string,
      /**  SubLedger document reference key 1  */  
   "Key1":string,
   "BitFlag":number,
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
      @param cashBookNum
      @param bankAcctID
      @param bankBatchRef
   */  
export interface AddMissingBankBatchSubLedgerDoc_input{
   cashBookNum:number,
   bankAcctID:string,
   bankBatchRef:string,
}

export interface AddMissingBankBatchSubLedgerDoc_output{
}

   /** Required : 
      @param cashBookNum
      @param bankAcctID
      @param bankBatchRef
   */  
export interface AddMissingBatchedSubLedgerDocs_input{
   cashBookNum:number,
   bankAcctID:string,
   bankBatchRef:string,
}

export interface AddMissingBatchedSubLedgerDocs_output{
}

   /** Required : 
      @param ipBankAcctID
      @param ipFiscalYear
      @param ds
   */  
export interface AddNewStatement_input{
      /**  Bank Account ID of the statement.  */  
   ipBankAcctID:string,
      /**  Fiscal Year.  */  
   ipFiscalYear:any,      //schema had no properties on an object.
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface AddNewStatement_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param pcBankAcctID
      @param ds
      @param statementDate
   */  
export interface AddStatement_input{
      /**  Bank Account ID of the statement.  */  
   pcBankAcctID:string,
   ds:Erp_Tablesets_BankRecTableset[],
      /**  Opening date of statement (Default null).  */  
   statementDate:string,
}

export interface AddStatement_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

export interface AllowPostStatement_output{
   returnObj:boolean,
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
      @param ds
   */  
export interface AssignLegalNumber_input{
      /**  Bank account identifier.  */  
   ipBankAcct:string,
      /**  Cash Book number.  */  
   ipCashBookNum:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface AssignLegalNumber_output{
parameters : {
      /**  output parameters  */  
   opLegalNumMsg:string,
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
      @param ds
   */  
export interface AutoMatchStatement_input{
      /**  Bank Account  */  
   ipBankAcct:string,
      /**  Cashbook num  */  
   ipCashBookNum:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface AutoMatchStatement_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
   */  
export interface BankStGetLegalNumGenOpts_input{
      /**  Bank account  */  
   ipBankAcct:string,
      /**  Cash Book number  */  
   ipCashBookNum:number,
}

export interface BankStGetLegalNumGenOpts_output{
   returnObj:Erp_Tablesets_BankRecTableset[],
parameters : {
      /**  output parameters  */  
   opPromptForNum:boolean,
}
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
      @param ds
   */  
export interface BankStmtGetLegalNumGenOpts_input{
      /**  Bank account  */  
   ipBankAcct:string,
      /**  Cash Book number  */  
   ipCashBookNum:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface BankStmtGetLegalNumGenOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
   opPromptForNum:boolean,
}
}

   /** Required : 
      @param ipBankAcctID
      @param ipFiscalYear
      @param ipBankSlip
   */  
export interface CheckBankSlip_input{
      /**  Bank account ID  */  
   ipBankAcctID:string,
      /**  Fiscal Year  */  
   ipFiscalYear:number,
      /**  Bank slip  */  
   ipBankSlip:number,
}

export interface CheckBankSlip_output{
parameters : {
      /**  output parameters  */  
   opCashBookNum:number,
   opUnconverted:boolean,
   opLegalNumber:string,
}
}

   /** Required : 
      @param iBankAcctID
      @param iFiscalYear
      @param iFiscalYearSuffix
      @param iBankSlip
      @param iFiscalCalendarID
   */  
export interface CheckDocumentIsLocked_input{
      /**  BankAcctID  */  
   iBankAcctID:string,
      /**  FiscalYear  */  
   iFiscalYear:number,
      /**  FiscalYearSuffix  */  
   iFiscalYearSuffix:string,
      /**  BankSlip  */  
   iBankSlip:number,
      /**  FiscalCalendarID  */  
   iFiscalCalendarID:string,
}

export interface CheckDocumentIsLocked_output{
}

   /** Required : 
      @param ds
   */  
export interface CheckSubLedgerDocs_input{
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface CheckSubLedgerDocs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
      @param ipLineNum
      @param ipMode
      @param ds
   */  
export interface CheckTolerance_input{
      /**  Bank account  */  
   ipBankAcct:string,
      /**  Book  */  
   ipCashBookNum:number,
      /**  Line No  */  
   ipLineNum:number,
      /**  Mode  */  
   ipMode:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface CheckTolerance_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipBankAcctID
      @param ipCashBookNum
      @param ipCashBookLine
   */  
export interface ClearSuggestion_input{
   ipBankAcctID:string,
   ipCashBookNum:number,
   ipCashBookLine:number,
}

export interface ClearSuggestion_output{
   returnObj:boolean,
}

   /** Required : 
      @param keys
   */  
export interface ConcatenateKeywords_input{
      /**  Keys array  */  
   keys:string,
}

export interface ConcatenateKeywords_output{
      /**  Concatenated string  */  
   returnObj:string,
}

   /** Required : 
      @param pcLineType
      @param pdCashBookNum
      @param ds
   */  
export interface CreateLine_input{
      /**  Line Type.  For example, Manual, MisPay, PayInv, Deposit, APPay, PRPay, CRPay, BankTran, APPIPay and ARPIPay  */  
   pcLineType:string,
      /**  Cash book number  */  
   pdCashBookNum:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface CreateLine_output{
parameters : {
      /**  output parameters  */  
   piCashBookLine:number,
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipLineType
      @param ipBankAcct
      @param ipCashBookNum
      @param ds
   */  
export interface CreateManualLine_input{
      /**  Line Type  */  
   ipLineType:string,
      /**  Bank Account  */  
   ipBankAcct:string,
      /**  Cash book number  */  
   ipCashBookNum:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface CreateManualLine_output{
parameters : {
      /**  output parameters  */  
   opCashBookLine:number,
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipLineType
      @param ipCashBook
      @param ipLinesList
      @param ds
   */  
export interface CreateNewDocuments_input{
      /**  Line Type  */  
   ipLineType:number,
      /**  Cash book number  */  
   ipCashBook:number,
      /**  Lines for which documents should be created  */  
   ipLinesList:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface CreateNewDocuments_output{
parameters : {
      /**  output parameters  */  
   opLastNewDocNum:number,
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param cashBookNum
   */  
export interface DeleteByID_input{
   cashBookNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_BankRecBankAcctRow{
   Company:string,
   BankAcctID:string,
   Description:string,
   CheckingAccount:string,
   CurrencyCode:string,
   FiscalYear:number,
   FiscalPeriod:number,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeDocumentDesc:string,
   FiscalCalendarID:string,
   FiscalYearSuffix:string,
   AutoStatementImport:boolean,
   AutoRetrieve:boolean,
   FilterByLine:boolean,
   AutoMatch:boolean,
   BankClosed:boolean,
   IBANCode:string,
   Tolerance:number,
   TranTemplateID:string,
   PayrollCheckingAccount:boolean,
   EnableAddNewStatement:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BankRecBankAcctTableset{
   BankRecBankAcct:Erp_Tablesets_BankRecBankAcctRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BankRecExchangeRatesRow{
   CashBookLine:number,
   CurrencyCode:string,
   DecimalsGeneral:number,
   ExchangeRate:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BankRecMessagesRow{
   MessageType:number,
   MessageText:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BankRecRemittanceInfoTableset{
   RemittanceInfo:Erp_Tablesets_RemittanceInfoRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BankRecTableset{
   CashBHed:Erp_Tablesets_CashBHedRow[],
   CashBHedAttch:Erp_Tablesets_CashBHedAttchRow[],
   CashBFilterOptions:Erp_Tablesets_CashBFilterOptionsRow[],
   SubLedgerDocs:Erp_Tablesets_SubLedgerDocsRow[],
   CashBDtl:Erp_Tablesets_CashBDtlRow[],
   CashBDtlAttch:Erp_Tablesets_CashBDtlAttchRow[],
   MatchedDocuments:Erp_Tablesets_MatchedDocumentsRow[],
   BankRecExchangeRates:Erp_Tablesets_BankRecExchangeRatesRow[],
   BankRecMessages:Erp_Tablesets_BankRecMessagesRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashBDtlAttchRow{
   Company:string,
   CashBookNum:number,
   CashbookLine:number,
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

export interface Erp_Tablesets_CashBDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  BankAcctID  */  
   BankAcctID:string,
      /**  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed and uses its CashBookNum + 1. Not directly entered by the user.  */  
   CashBookNum:number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   CashbookLine:number,
      /**  Indicates the line number.  */  
   LineNum:number,
      /**  Description  */  
   Description:string,
      /**  Identifies the type of transaction. Possible values are 'Banktran' for bank adjustments, 'manual' for manual A/P payments, 'appay' for A/P payments, 'prpay' for P/R payments, 'crpay' for cashreceipts which are entered in the Cash Receipt Entry program, 'payinv' for invoice cash receipts, 'deposit' for deposit cash receipts and 'mispay' for miscellaneous cash receipts.  */  
   TranType:string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Fiscal Year. This is not entered by the user on each record.  */  
   FiscalYear:number,
      /**  Fiscal period for the transaction. Not directly entered by the user.  */  
   FiscalPeriod:number,
      /**  Indicates the transaction date in the statement line.  */  
   TranDate:string,
      /**  Amount of transaction that is being applied.  */  
   TranAmt:number,
      /**  Amount of transaction that is being applied.  */  
   DocTranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**  Fiscal Year Suffix. This is not entered by the user on each record.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Used on Bank Fees created from Bank Reconciliation, Identifies the type of transaction from was created. Possible values are 'Manual' for Manual A/P payments and ?PayInv? for Invoice Cash Receipt.  */  
   LinkedTranType:string,
      /**  Used on Bank Fees, this field will be used to link Checks or AR Payments created from Bank Reconciliation.  */  
   LinkedHeadNum:number,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  Indicates the name of the partner in the statement line.  */  
   Partner:string,
      /**  Indicates the ID of the partner. The bank uses this ID to specify the partner in the statement line.  */  
   PartnerName:string,
      /**  Partner Number  */  
   PartnerNum:number,
      /**  Partner Type  */  
   PartnerType:number,
      /**  Debit Credit Mark  */  
   DebitCreditMark:string,
      /**  Indicates the statement line amount in line currency.  */  
   ImportTranAmount:number,
      /**  Indicates the part of statement line amount that is not matched with an existing document in transaction currency.  */  
   ImportTranUnclearedAmount:number,
      /**  Indicates the part of statement line amount that is not matched with an existing document.  */  
   ImportUnclearedAmount:number,
      /**  Import Report 1 Uncleared Amount  */  
   ImportRpt1UnclearedAmount:number,
      /**  Import Report 2 Uncleared Amount  */  
   ImportRpt2UnclearedAmount:number,
      /**  Import Report 3 Uncleared Amount  */  
   ImportRpt3UnclearedAmount:number,
      /**  Indicates the currency code for the transaction amount.  */  
   ImportTranCurrency:string,
      /**  Indicates the statement line amount in bank currency.  */  
   ImportBankAmount:number,
      /**  Indicates the difference between the amount of the currently selected statement line and the total amount of transactions currently selected for  */  
   ImportBankVariance:number,
      /**  Import Amount  */  
   ImportAmount:number,
      /**  Indicates the exchange rate between the line currency and the bank currency.  */  
   ExchangeRate:number,
      /**  Indicates the statement line's status.  */  
   LineStatus:number,
      /**  Indicates the type of the statement line.  */  
   LineType:number,
      /**  Indicates the statement line transaction text.  */  
   LineDescription:string,
      /**  Document List  */  
   DocumentList:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  The application displays here the information explaining why it did not perform correctly automatic line recognition, document creation or matching.  */  
   ImportError:string,
      /**  Filter By Partner  */  
   FilterByPartner:boolean,
      /**  Import Bank Gain Loss  */  
   ImportBankGainLoss:number,
      /**  Gain/Loss  */  
   ImportGainLoss:number,
      /**  Import Report 1 Gain Loss  */  
   ImportRpt1GainLoss:number,
      /**  Import Report 2 Gain Loss  */  
   ImportRpt2GainLoss:number,
      /**  Import Report 3 Gain Loss  */  
   ImportRpt3GainLoss:number,
      /**  BankTranType  */  
   BankTranType:string,
      /**  Indicates the difference between the total line amount in bank currency and the applied transactions amount  */  
   ImportBankUnclearedAmount:number,
      /**  Indicates the type of the transaction.  */  
   ImportTranType:string,
      /**  Indicates the code of the transaction.  */  
   ImportTranCode:string,
      /**  Indicates the number of the business document related to the line which is known to the bank.  */  
   TranRef:string,
      /**  Indicates the code of the partner bank.  */  
   PartnerBank:string,
      /**  Indicates the account of the partner bank.  */  
   PartnerBankAcct:string,
      /**  This check box is selected if the line is of the Reverse Cash Receipt or Voided AP Payment type.  */  
   ReverseFlag:boolean,
      /**  Indicates the total charges amount.  */  
   TotalChrgAmt:number,
      /**  Indicates the currency code for the total charges.  */  
   ChrgCurrCode:string,
      /**  RawData  */  
   RawData:string,
      /**  Indicates the reference details of the invoice.  */  
   MatchingInfo:string,
      /**  RemitData  */  
   RemitData:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Bank Fee ID  */  
   BankFeeID:string,
      /**  Transfer Bank ID  */  
   TransferBankID:string,
      /**  PartnerID  */  
   PartnerID:string,
      /**  CreateMode  */  
   CreateMode:number,
      /**  Add any comments in this field if required.  */  
   UserComment:string,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  UserReference  */  
   UserReference:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Disable MXRecDate  */  
   DisableMXRecDate:boolean,
   DocTotalCandAmt:number,
   DocTotalRemAmt:number,
   DocTotalSelAmt:number,
      /**  Contains description of imported line with potential Invoices numbers list.  */  
   DocumentsRefData:string,
   DspLineNum:string,
   ExchangeRates:string,
      /**  Stores HeadNum or TranNum value.  Used to call BankAdjEntry, PaymentEntry or CashRec - GetByID method.  */  
   HeadNum:number,
      /**  Indicates the difference between the amount of the currently selected statement line and the total amount of transactions currently selected for  */  
   ImportBankVarianceDsp:number,
   ImportCreditAmount:number,
   ImportDebitAmount:number,
   ImportDspBankAmount:number,
      /**  Transaction Code Description  */  
   ImportTranCodeDesc:string,
   isCleared:boolean,
   NewDoc:boolean,
      /**  Reference field.  */  
   Reference:string,
   Rounding:number,
   Rpt1TotalCandAmt:number,
   Rpt1TotalRemAmt:number,
   Rpt1TotalSelAmt:number,
   Rpt2TotalCandAmt:number,
   Rpt2TotalRemAmt:number,
   Rpt2TotalSelAmt:number,
   Rpt3TotalCandAmt:number,
   Rpt3TotalRemAmt:number,
   Rpt3TotalSelAmt:number,
      /**  AP Clearing Total Candidates  */  
   TotalCandAmt:number,
      /**  AP Clearing Total Remaining  */  
   TotalRemAmt:number,
      /**  AP Clearing Total Selected  */  
   TotalSelAmt:number,
      /**  Transaction Reference 1  */  
   TranRef1:string,
      /**  Transaction Reference 2  */  
   TranRef2:string,
      /**  Transaction Reference 3  */  
   TranRef3:string,
   TranTemplateID:string,
      /**  Tran Type description  */  
   TranTypeDescription:string,
   DspUnallocatedAmount:number,
   DspUnallocatedCurrency:string,
   BitFlag:number,
   BankAcctIDBankName:string,
   BankAcctIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashBFilterOptionsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the bank account.  */  
   BankAcctID:string,
      /**  Cash Book Number.  */  
   CashBookNum:number,
      /**  Line Type  */  
   LineType:number,
      /**  Filter AP Invoices  */  
   FilterAPInvoices:boolean,
      /**  Filter AP Pay  */  
   FilterAPPay:boolean,
      /**  Filter AP Payment Instruments  */  
   FilterAPPI:boolean,
      /**  Filter AR Payment Instruments  */  
   FilterARPI:boolean,
      /**  Filter AR Invoices  */  
   FilterARInvoices:boolean,
      /**  Filter Bank Adjustments  */  
   FilterBankAdj:boolean,
      /**  Filter Bank Transactions  */  
   FilterBankTran:boolean,
      /**  Filter Cash Receipts Payments  */  
   FilterCRPay:boolean,
      /**  Filter Reversed AP Payments  */  
   FilterRevAPPay:boolean,
      /**  Filter Reversed Cash Receipts Payments  */  
   FilterRevCRPay:boolean,
      /**  Filter All  */  
   FilterAll:boolean,
      /**  Filter Payments  */  
   FilterPayments:boolean,
      /**  Filter Receipts  */  
   FilterReceipts:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Filter PR Pay  */  
   FilterPRPay:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashBHedAttchRow{
   Company:string,
   CashBookNum:number,
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

export interface Erp_Tablesets_CashBHedListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Specifies the identifier for the bank account.  */  
   BankAcctID:string,
      /**  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed and uses its CashBookNum + 1. Not directly entered by the user.  */  
   CashBookNum:number,
      /**  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed of a Bank Account and a Fiscal Year and uses its Bankslip + 1. The user can override this number when no cashbook lines are available for this bankslip.  */  
   Bankslip:number,
      /**  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  */  
   GroupID:string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Indicates a description of the statement.  */  
   Description:string,
      /**  Specifies opening balance for the statement.  */  
   OpeningBalance:number,
      /**  The Opening Balance of the Bank Account.  When a Reconciliation is posted this field is set to the Closing Balance.  */  
   DocOpeningBalance:number,
      /**  Specifies the opening date for transactions for the bank account.  */  
   OpeningDate:string,
      /**  Specifies the closing amount for the statement.  */  
   ClosingBalance:number,
      /**  The Closing Balance of the Bank Account.  */  
   DocClosingBalance:number,
      /**  Specifies the closing date for transactions for the bank account.  */  
   ClosingDate:string,
      /**  Displays the fiscal year of the transaction.  */  
   FiscalYear:number,
      /**  Displays the fiscal period of the transaction.  */  
   FiscalPeriod:number,
      /**  The currency of the Bank Account  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this Check.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClosingBalance:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClosingBalance:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClosingBalance:number,
      /**  Reporting currency value of this field  */  
   Rpt1OpeningBalance:number,
      /**  Reporting currency value of this field  */  
   Rpt2OpeningBalance:number,
      /**  Reporting currency value of this field  */  
   Rpt3OpeningBalance:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Specifies the fiscal year suffix of the fiscal year during which the transactions occurred.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Specifies the date for which the statement applies.  */  
   ApplyDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DocNetChange:number,
   LineTotal:number,
   Variance:number,
   DocLineTotal:number,
   DocVariance:number,
   CurrencySwitch:boolean,
   APInterfaced:boolean,
   Rpt1LineTotal:number,
   Rpt1Variance:number,
   Rpt2LineTotal:number,
   Rpt2Variance:number,
   Rpt3LineTotal:number,
   Rpt3Variance:number,
      /**  shows is this invoice is blocked in RvLock  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  Locked means can not be posted: an invoice is already in review journal or in posting process  */  
   LockStatus:string,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Full description of the bank account.  */  
   BankAcctIDDescription:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrSymbol:string,
      /**  Description of the currency  */  
   BaseCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseDocumentDesc:string,
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
      /**  Description  */  
   RateGrpDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashBHedListTableset{
   CashBHedList:Erp_Tablesets_CashBHedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashBHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Specifies the identifier for the bank account.  */  
   BankAcctID:string,
      /**  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed and uses its CashBookNum + 1. Not directly entered by the user.  */  
   CashBookNum:number,
      /**  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed of a Bank Account and a Fiscal Year and uses its Bankslip + 1. The user can override this number when no cashbook lines are available for this bankslip.  */  
   Bankslip:number,
      /**  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  */  
   GroupID:string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Indicates a description of the statement.  */  
   Description:string,
      /**  Specifies opening balance for the statement.  */  
   OpeningBalance:number,
      /**  The Opening Balance of the Bank Account.  When a Reconciliation is posted this field is set to the Closing Balance.  */  
   DocOpeningBalance:number,
      /**  Specifies the opening date for transactions for the bank account.  */  
   OpeningDate:string,
      /**  Specifies the closing amount for the statement.  */  
   ClosingBalance:number,
      /**  The Closing Balance of the Bank Account.  */  
   DocClosingBalance:number,
      /**  Specifies the closing date for transactions for the bank account.  */  
   ClosingDate:string,
      /**  Displays the fiscal year of the transaction.  */  
   FiscalYear:number,
      /**  Displays the fiscal period of the transaction.  */  
   FiscalPeriod:number,
      /**  The currency of the Bank Account  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this Check.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClosingBalance:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClosingBalance:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClosingBalance:number,
      /**  Reporting currency value of this field  */  
   Rpt1OpeningBalance:number,
      /**  Reporting currency value of this field  */  
   Rpt2OpeningBalance:number,
      /**  Reporting currency value of this field  */  
   Rpt3OpeningBalance:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Specifies the fiscal year suffix of the fiscal year during which the transactions occurred.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Specifies the date for which the statement applies.  */  
   ApplyDate:string,
      /**  Filter To Date  */  
   FilterToDate:string,
      /**  Filter To Date Token  */  
   FilterToDateToken:string,
      /**  Retrieve Status  */  
   RetrieveStatus:number,
      /**  Include PI Past Close  */  
   IncludePIPastClose:boolean,
      /**  Imported  */  
   Imported:boolean,
      /**  CashReceipt Group  */  
   GrpCashReceipt:string,
      /**  AP Payment Group  */  
   GrpAPPay:string,
      /**  Bank Adjustment Group  */  
   GrpBankAdj:string,
      /**  BankTransfer Group  */  
   GrpBankTrans:string,
      /**  RefNum  */  
   RefNum:string,
      /**  Info  */  
   Info:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  FilterByLineType  */  
   FilterByLineType:boolean,
      /**  StatementDate  */  
   StatementDate:string,
      /**  UseClosingDateCutoff  */  
   UseClosingDateCutoff:boolean,
      /**  Select the transaction document type for the bank statement, if necessary.  */  
   TranDocTypeID:string,
      /**  When the application assigns a legal number to the statement, it is displayed in this field. Refer to the Actions - Legal Numbers commands.  */  
   LegalNumber:string,
      /**  UnconvertedStatement  */  
   UnconvertedStatement:boolean,
      /**  StatementVersion  */  
   StatementVersion:number,
      /**  AR Payment Instrument Group  */  
   GrpARPI:string,
      /**  ProcessStatus  */  
   ProcessStatus:string,
      /**  ThresholdDate  */  
   ThresholdDate:string,
      /**  ClearDate  */  
   ClearDate:string,
      /**  Comments  */  
   Comments:string,
   APInterfaced:boolean,
   BankTranCodeList:string,
   BaseCurrDesc:string,
   BaseCurrencyID:string,
   BaseCurrName:string,
   BaseCurrSymbol:string,
   BaseDocumentDesc:string,
   CurrencyList:string,
   CurrencySwitch:boolean,
   CurrentBalance:number,
   DefaultLineType:number,
   DocCurrentBalance:number,
   DocLineTotal:number,
   DocNetChange:number,
   DocNonReconciled:number,
   DocReconciledBalance:number,
   DocVariance:number,
   DspDocRunningBal:number,
   DspDocVariance:number,
   DspRunningBal:number,
   DspVariance:number,
      /**  Legal Number Field  */  
   EnableAssignLegNum:boolean,
   EnableTranDocType:boolean,
      /**  Legal Number Field  */  
   EnableVoidLegNum:boolean,
      /**  Legal Number Field  */  
   HasLegNumCnfg:boolean,
      /**  shows is this invoice is blocked in RvLock  */  
   IsLcked:boolean,
   LegalNumStyle:string,
   LineTotal:number,
      /**  Locked means can not be posted: an invoice is already in review journal or in posting process  */  
   LockStatus:string,
   NonReconciled:number,
   ReconciledBalance:number,
   Rpt1CurrentBalance:number,
   Rpt1DspRunningBal:number,
   Rpt1DspVariance:number,
   Rpt1LineTotal:number,
   Rpt1NonReconciled:number,
   Rpt1ReconciledBalance:number,
   Rpt1Variance:number,
   Rpt2CurrentBalance:number,
   Rpt2DspRunningBal:number,
   Rpt2DspVariance:number,
   Rpt2LineTotal:number,
   Rpt2NonReconciled:number,
   Rpt2ReconciledBalance:number,
   Rpt2Variance:number,
   Rpt3CurrentBalance:number,
   Rpt3DspRunningBal:number,
   Rpt3DspVariance:number,
   Rpt3LineTotal:number,
   Rpt3NonReconciled:number,
   Rpt3ReconciledBalance:number,
   Rpt3Variance:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  Legal Number Field  */  
   SystemTranType:string,
   TranDocTypeDesc:string,
   UpdateDates:number,
   Variance:number,
      /**  Legal Number Field  */  
   AllowChgAfterPrint:boolean,
   BalanceStatus:string,
      /**  Standar Legal Number message when a new legal number is created.  */  
   LegalNumMessage:string,
   ActiveUserID:string,
   BitFlag:number,
   BankAcctIDBankName:string,
   BankAcctIDDescription:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrDesc:string,
   RateGrpDescription:string,
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

export interface Erp_Tablesets_MatchedDocumentsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the bank account.  */  
   BankAcctID:string,
      /**  Cash Book Number.  */  
   CashBookNum:number,
      /**  Cash Book Line Number.  */  
   CashBookLine:number,
      /**  Match Line Num  */  
   MatchLineNum:number,
      /**  Indicates the type of the document matched to the line. The application uses  */  
   DocumentType:number,
      /**  Document Type Mode  */  
   DocumentTypeMode:number,
      /**  Reference  */  
   Reference:string,
      /**  Partner  */  
   Partner:string,
      /**  Indicates the name of the partner in the matched document.  */  
   PartnerName:string,
      /**  Indicates the legal number of the matched document.  */  
   LegalNumber:string,
      /**  Indicates the internal number of the matched document.  */  
   InternalNumber:string,
      /**  Indicates the matched document amount in the document currency.  */  
   DocAmount:number,
      /**  Indicates the matched document currency.  */  
   DocCurrency:string,
      /**  Indicates the matched document date.  */  
   DocDate:string,
      /**  Doc Discount Amount  */  
   DocDiscountAmount:number,
      /**  Indicates the matched document amount in the bank currency.  */  
   TranAmount:number,
      /**  Indicates the document currency  */  
   TranCurrency:string,
      /**  Indicates the matched document amount in the bank currency.  */  
   BankAmount:number,
      /**  Bank Currency  */  
   BankCurrency:string,
      /**  Base Amount  */  
   BaseAmount:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  If the line was matched to a batch or a batch payment, this field indicates the number of the batch reference.  */  
   BankBatchRef:string,
      /**  If this document was created either manually or automatically, this field indicates the document type.  */  
   NewDoc:number,
      /**  SysRowID of matched document  */  
   ExternalSysRowID:string,
      /**  If the line was matched to a batch or a batch payment, this field indicates the SysRowID of the batch.  */  
   BankBatchSysRowID:string,
      /**  UserReference  */  
   UserReference:string,
      /**  Matched document reference key 1  */  
   Key1:string,
      /**  Matched document reference key 2  */  
   Key2:string,
      /**  Matched document reference key 3  */  
   Key3:string,
   MasterTypeMode:number,
   Selected:boolean,
   BankBatchID:string,
   CreateMode:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RemittanceInfoRow{
   TagCode:string,
   Description:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SubLedgerDocsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the bank account.  */  
   BankAcctID:string,
      /**  Cash Book Number.  */  
   CashBookNum:number,
      /**  Document Type  */  
   DocumentType:number,
      /**  Reference  */  
   Reference:string,
      /**  Cash Book Line Number.  */  
   CashBookLine:number,
      /**  Document Type Mode  */  
   DocumentTypeMode:number,
      /**  Indicates the partner ID.  */  
   Partner:string,
      /**  Indicates the partner name.  */  
   PartnerName:string,
      /**  Partner Number  */  
   PartnerNum:number,
      /**  Document Status  */  
   DocumentStatus:boolean,
      /**  Indicates the legal number of the unmatched document.  */  
   LegalNumber:string,
      /**  Internal Number  */  
   InternalNumber:string,
      /**  Indicates the unmatched document amount in the document currency.  */  
   DocAmount:number,
      /**  Indicates the unmatched document currency.  */  
   DocCurrency:string,
      /**  Indicates the unmatched document date.  */  
   DocDate:string,
      /**  Indicates the document amount in bank currency.  */  
   BankAmount:number,
      /**  Indicates a bank currency code.  */  
   BankCurrency:string,
      /**  Group ID  */  
   GroupID:string,
      /**  Base Amount  */  
   BaseAmount:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Suggested For Lines  */  
   SuggestedForLines:string,
      /**  Indicates the refrence number of the batch.  */  
   BankBatchRef:string,
      /**  SysRowID of the unmatched document  */  
   ExternalSysRowID:string,
      /**  Indicates the SysRowID of the batch.  */  
   BankBatchSysRowID:string,
      /**  UserReference  */  
   UserReference:string,
      /**  SubLedger document reference key 2  */  
   Key2:string,
      /**  SubLedger document reference key 3  */  
   Key3:string,
   QSInternalNumber:string,
   Ranged:boolean,
   Selected:boolean,
   ShouldBeHidden:boolean,
   Suggested:boolean,
   BankBatchID:string,
      /**  SubLedger document reference key 1  */  
   Key1:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtBankRecTableset{
   CashBHed:Erp_Tablesets_CashBHedRow[],
   CashBHedAttch:Erp_Tablesets_CashBHedAttchRow[],
   CashBFilterOptions:Erp_Tablesets_CashBFilterOptionsRow[],
   SubLedgerDocs:Erp_Tablesets_SubLedgerDocsRow[],
   CashBDtl:Erp_Tablesets_CashBDtlRow[],
   CashBDtlAttch:Erp_Tablesets_CashBDtlAttchRow[],
   MatchedDocuments:Erp_Tablesets_MatchedDocumentsRow[],
   BankRecExchangeRates:Erp_Tablesets_BankRecExchangeRatesRow[],
   BankRecMessages:Erp_Tablesets_BankRecMessagesRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param bankAcctID
      @param transferBankAcctID
      @param toDate
   */  
export interface ExistsUnverifiedTransfers_input{
      /**  BankAcctID of bank to check to.  */  
   bankAcctID:string,
      /**  BankAcctID of second bank. Could be empty.  */  
   transferBankAcctID:string,
      /**  Maximum transaction date value  */  
   toDate:string,
}

export interface ExistsUnverifiedTransfers_output{
      /**  True if any transfers found, otherwise false.  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   message:string,
}
}

   /** Required : 
      @param textData
      @param paramCode
   */  
export interface ExtractInvoices_input{
      /**  Source text data  */  
   textData:string,
      /**  Code of parameters set  */  
   paramCode:string,
}

export interface ExtractInvoices_output{
      /**  List of found Invoices with a comma as separator  */  
   returnObj:string,
}

   /** Required : 
      @param ipBankAcctID
      @param ipCashBookNum
   */  
export interface FindObsoleteReceiptsPayments_input{
      /**  Bank account  */  
   ipBankAcctID:string,
      /**  Current not posted cashbook  */  
   ipCashBookNum:number,
}

export interface FindObsoleteReceiptsPayments_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
      @param ds
   */  
export interface GenerateNewCashMove_input{
      /**  Bank Account  */  
   ipBankAcct:string,
      /**  Cashbook num  */  
   ipCashBookNum:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface GenerateNewCashMove_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipBankAcctID
   */  
export interface GetBankInfo_input{
      /**  Bank account ID  */  
   ipBankAcctID:string,
}

export interface GetBankInfo_output{
   returnObj:Erp_Tablesets_BankRecBankAcctTableset[],
}

   /** Required : 
      @param ipBankAcctID
      @param ipFiscalYear
      @param ipBankSlip
   */  
export interface GetBankStatement_input{
      /**  Bank account  */  
   ipBankAcctID:string,
      /**  Fiscal Year  */  
   ipFiscalYear:number,
      /**  Bank slip  */  
   ipBankSlip:number,
}

export interface GetBankStatement_output{
   returnObj:Erp_Tablesets_BankRecTableset[],
}

   /** Required : 
      @param cashBookNum
   */  
export interface GetByID_input{
   cashBookNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_BankRecTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_BankRecTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_BankRecTableset[],
}

export interface GetCurrencyBase_output{
parameters : {
      /**  output parameters  */  
   opCurrencyBase:string,
}
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
      @param ipLineNum
      @param ipTrandate
      @param ipLineType
      @param ds
   */  
export interface GetDocumentList_input{
      /**  Bank Account  */  
   ipBankAcct:string,
      /**  Cashbook num  */  
   ipCashBookNum:number,
      /**  Line #  */  
   ipLineNum:number,
      /**  Line Date  */  
   ipTrandate:string,
      /**  Line Date  */  
   ipLineType:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface GetDocumentList_output{
parameters : {
      /**  output parameters  */  
   opDocumentList:string,
   opTranDocTypeiD:string,
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipTableList
   */  
export interface GetExtendedProperties_input{
      /**  Tables list  */  
   ipTableList:string,
}

export interface GetExtendedProperties_output{
parameters : {
      /**  output parameters  */  
   opExtProperties:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetLegNumDefaults_input{
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface GetLegNumDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
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
   returnObj:Erp_Tablesets_CashBHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param cashBookNum
      @param cashbookLine
   */  
export interface GetNewCashBDtlAttch_input{
   ds:Erp_Tablesets_BankRecTableset[],
   cashBookNum:number,
   cashbookLine:number,
}

export interface GetNewCashBDtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ds
      @param cashBookNum
   */  
export interface GetNewCashBDtl_input{
   ds:Erp_Tablesets_BankRecTableset[],
   cashBookNum:number,
}

export interface GetNewCashBDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param cashBookNum
   */  
export interface GetNewCashBFilterOptions_input{
   ds:Erp_Tablesets_BankRecTableset[],
   bankAcctID:string,
   cashBookNum:number,
}

export interface GetNewCashBFilterOptions_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ds
      @param cashBookNum
   */  
export interface GetNewCashBHedAttch_input{
   ds:Erp_Tablesets_BankRecTableset[],
   cashBookNum:number,
}

export interface GetNewCashBHedAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCashBHed_input{
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface GetNewCashBHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param p_newdate
   */  
export interface GetNewFiscalPer_input{
   p_newdate:string,
}

export interface GetNewFiscalPer_output{
parameters : {
      /**  output parameters  */  
   n_FiscalCalendarID:string,
   n_FiscalYear:number,
   n_FiscalYearSuffix:string,
   n_FiscalPeriod:number,
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param cashBookNum
      @param cashBookLine
   */  
export interface GetNewMatchedDocuments_input{
   ds:Erp_Tablesets_BankRecTableset[],
   bankAcctID:string,
   cashBookNum:number,
   cashBookLine:number,
}

export interface GetNewMatchedDocuments_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param cashBookNum
      @param documentType
   */  
export interface GetNewSubLedgerDocs_input{
   ds:Erp_Tablesets_BankRecTableset[],
   bankAcctID:string,
   cashBookNum:number,
   documentType:number,
}

export interface GetNewSubLedgerDocs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

export interface GetNextCashBookNum_output{
      /**  decimal  */  
   returnObj:number,
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
   */  
export interface GetPeriodThresholdDate_input{
   ipBankAcct:string,
   ipCashBookNum:number,
}

export interface GetPeriodThresholdDate_output{
parameters : {
      /**  output parameters  */  
   opThresholdDate:string,
}
}

   /** Required : 
      @param ipBankAcct
   */  
export interface GetProcessStatus_input{
      /**  Bank Account  */  
   ipBankAcct:string,
}

export interface GetProcessStatus_output{
   returnObj:string,
}

   /** Required : 
      @param pdCashBookNum
      @param ipCashBookLine
   */  
export interface GetRemittanceInfo_input{
      /**  Cash book number  */  
   pdCashBookNum:number,
      /**  CashBookLine from CashbDtl datatable  */  
   ipCashBookLine:number,
}

export interface GetRemittanceInfo_output{
   returnObj:Erp_Tablesets_BankRecRemittanceInfoTableset[],
}

   /** Required : 
      @param whereClauseCashBHed
      @param whereClauseCashBHedAttch
      @param whereClauseCashBFilterOptions
      @param whereClauseSubLedgerDocs
      @param whereClauseCashBDtl
      @param whereClauseCashBDtlAttch
      @param whereClauseMatchedDocuments
      @param whereClauseBankRecExchangeRates
      @param whereClauseBankRecMessages
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCashBHed:string,
   whereClauseCashBHedAttch:string,
   whereClauseCashBFilterOptions:string,
   whereClauseSubLedgerDocs:string,
   whereClauseCashBDtl:string,
   whereClauseCashBDtlAttch:string,
   whereClauseMatchedDocuments:string,
   whereClauseBankRecExchangeRates:string,
   whereClauseBankRecMessages:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_BankRecTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param pcBankAcctID
      @param piFiscalYear
      @param piBankSlip
   */  
export interface GetStatement_input{
      /**  Bank Account ID of the statement.  */  
   pcBankAcctID:string,
      /**  Fiscal Year of the statement  */  
   piFiscalYear:number,
      /**  Bank slip#  */  
   piBankSlip:number,
}

export interface GetStatement_output{
   returnObj:Erp_Tablesets_BankRecTableset[],
}

   /** Required : 
      @param tranTemplateID
   */  
export interface GetTransactionCodes_input{
      /**  Template ID  */  
   tranTemplateID:string,
}

export interface GetTransactionCodes_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param bankAcctID
      @param cashBookNum
      @param cashBookLine
   */  
export interface HasLinkedReverseLines_input{
      /**  BankAcctID  */  
   bankAcctID:string,
      /**  CashBookNum  */  
   cashBookNum:number,
      /**  CashBookLine  */  
   cashBookLine:number,
}

export interface HasLinkedReverseLines_output{
      /**  0 - no revese lines, 1 - exists reverse lines, 2 - new document with reverse lines  */  
   returnObj:number,
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
      @param EFTHeadUID
      @param importFile
      @param instanceTaskNum
      @param logFile
   */  
export interface ImporMultiStatement_input{
      /**  Electronic Interface ID  */  
   EFTHeadUID:number,
      /**  Import file name (Server path)  */  
   importFile:string,
      /**  Task Number  */  
   instanceTaskNum:number,
      /**  Log file path  */  
   logFile:string,
}

export interface ImporMultiStatement_output{
   returnObj:boolean,
}

   /** Required : 
      @param bankAcct
      @param importFile
      @param ds
   */  
export interface ImportStatementContinue_input{
      /**  Bank Account  */  
   bankAcct:string,
      /**  Import file name  */  
   importFile:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface ImportStatementContinue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
   msgList:string,
   opCashBookNum:number,
}
}

   /** Required : 
      @param importFile
   */  
export interface ImportStatementDelete_input{
      /**  Server Import file path  */  
   importFile:string,
}

export interface ImportStatementDelete_output{
}

   /** Required : 
      @param bankAcct
      @param importFile
      @param ds
   */  
export interface ImportStatementSlipContinue_input{
      /**  Bank Account  */  
   bankAcct:string,
      /**  Import file name  */  
   importFile:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface ImportStatementSlipContinue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
   msgList:string,
   opFiscalYear:number,
   opBankslip:number,
}
}

   /** Required : 
      @param bankAcct
      @param importFile
      @param ds
   */  
export interface ImportStatementSlip_input{
      /**  Bank Account  */  
   bankAcct:string,
      /**  Import file name  */  
   importFile:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface ImportStatementSlip_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
   msgList:string,
   opFiscalYear:number,
   opBankslip:number,
}
}

   /** Required : 
      @param bankAcct
      @param importFile
      @param ds
   */  
export interface ImportStatement_input{
      /**  Bank Account  */  
   bankAcct:string,
      /**  Import file name  */  
   importFile:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface ImportStatement_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
   msgList:string,
   opCashBookNum:number,
}
}

   /** Required : 
      @param tranDocTypeID
      @param date
   */  
export interface IsAutomaticVoiding_input{
      /**  Transaction document type identifier.  */  
   tranDocTypeID:string,
      /**  Date to get legal number configuration.  */  
   date:string,
}

export interface IsAutomaticVoiding_output{
      /**  `true` if legal number configuration exists and s automatic voiding for the specified date; otherwise, `false`.  */  
   returnObj:boolean,
}

   /** Required : 
      @param searchID
      @param partnerNum
      @param partnerID
      @param partnerType
   */  
export interface IsExistingSearchIDForPartner_input{
   searchID:string,
   partnerNum:number,
   partnerID:string,
   partnerType:number,
}

export interface IsExistingSearchIDForPartner_output{
   returnObj:boolean,
}

   /** Required : 
      @param bankAcctID
      @param fiscalYear
      @param bankslip
   */  
export interface IsUnconvertedStatement_input{
   bankAcctID:string,
      /**  FiscalYear  */  
   fiscalYear:number,
      /**  Bankslip  */  
   bankslip:number,
}

export interface IsUnconvertedStatement_output{
   returnObj:boolean,
}

   /** Required : 
      @param bankAcctID
      @param fiscalYear
      @param bankSlip
   */  
export interface LockGroup_input{
   bankAcctID:string,
   fiscalYear:number,
   bankSlip:number,
}

export interface LockGroup_output{
      /**  bool  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   errorMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface LockStatement_input{
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface LockStatement_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
      @param ipLineNum
      @param ipMatchMode
      @param ipDocument
      @param ds
   */  
export interface MatchDocument2Line_input{
      /**  Bank Account  */  
   ipBankAcct:string,
      /**  Cashbook num  */  
   ipCashBookNum:number,
      /**  Line #  */  
   ipLineNum:number,
      /**  Manual match  */  
   ipMatchMode:number,
      /**  TranDocTypeID  */  
   ipDocument:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface MatchDocument2Line_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param lineType
      @param cashBookNum
      @param cashBookLine
      @param ds
   */  
export interface NewDocumentWithUpdateStatement_input{
      /**  Line Type  */  
   lineType:number,
      /**  Cash book number  */  
   cashBookNum:number,
      /**  Line for which document should be created  */  
   cashBookLine:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface NewDocumentWithUpdateStatement_output{
parameters : {
      /**  output parameters  */  
   opLastNewDocNum:number,
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipCashBookNum
      @param ipClearDate
      @param ds
   */  
export interface OnChangeClearDate_input{
      /**  CashBookNum from CashBHed datatable  */  
   ipCashBookNum:number,
      /**  Clear Date  */  
   ipClearDate:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface OnChangeClearDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipCashBookNum
      @param ipClosingDate
      @param ds
   */  
export interface OnChangeClosingDate_input{
      /**  CashBookNum from CashBHed datatable  */  
   ipCashBookNum:number,
      /**  Closing Date  */  
   ipClosingDate:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface OnChangeClosingDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipDiscAmount
      @param ipTranCurrency
      @param ipTranRateGroup
      @param ipTranDate
      @param ipDocCurrency
      @param ipBankCurrency
   */  
export interface OnChangeDocDiscount_input{
      /**  Doc Currency amount  */  
   ipDiscAmount:number,
      /**  Operation Currency  */  
   ipTranCurrency:string,
      /**  Operation Rate group  */  
   ipTranRateGroup:string,
      /**  Operation Date  */  
   ipTranDate:string,
      /**  Doc Currency  */  
   ipDocCurrency:string,
      /**  Doc Currency  */  
   ipBankCurrency:string,
}

export interface OnChangeDocDiscount_output{
parameters : {
      /**  output parameters  */  
   opTranAmount:number,
   opBankAmount:number,
}
}

   /** Required : 
      @param ipCashBookNum
      @param ipOpeningDate
      @param ds
   */  
export interface OnChangeOpeningDate_input{
      /**  CashBookNum from CashBHed datatable  */  
   ipCashBookNum:number,
      /**  Opening Date  */  
   ipOpeningDate:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface OnChangeOpeningDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipTranDocTypeID
      @param ds
   */  
export interface OnChangeTranDocTypeId_input{
      /**  TranDocTypeID supplied  */  
   ipTranDocTypeID:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface OnChangeTranDocTypeId_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param pdCashBookNum
      @param newApplyDate
      @param ds
   */  
export interface OnChangeofApplyDate_input{
      /**  CashBookNum from CashBHed datatable  */  
   pdCashBookNum:number,
      /**  Proposed Apply Date.  */  
   newApplyDate:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface OnChangeofApplyDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param proposedDocClosingBalance
      @param ds
   */  
export interface OnChangingDocClosingBalance_input{
      /**  Proposed Closing Balance  */  
   proposedDocClosingBalance:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface OnChangingDocClosingBalance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param plMXRecDate
      @param pdCashBookNum
      @param piCashBookLine
   */  
export interface OnChangingMXRecDate_input{
      /**  New Reconciled Date  */  
   plMXRecDate:string,
      /**  CashBookNum from CashbDtl datatable  */  
   pdCashBookNum:number,
      /**  CashBookLine from CashbDtl datatable  */  
   piCashBookLine:number,
}

export interface OnChangingMXRecDate_output{
}

   /** Required : 
      @param bankAcctID
      @param cashBookNum
      @param cashBookLine
      @param ds
   */  
export interface OnPartnerInfoChanged_input{
   bankAcctID:string,
   cashBookNum:number,
   cashBookLine:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface OnPartnerInfoChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param bankAcctID
      @param cashBookNum
      @param cashBookLine
      @param ds
   */  
export interface OnPartnerNameChanged_input{
   bankAcctID:string,
   cashBookNum:number,
   cashBookLine:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface OnPartnerNameChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipLineType
      @param ipCashBook
      @param ipLineNum
   */  
export interface OpenDocument_input{
      /**  Line Type  */  
   ipLineType:number,
      /**  Cash book number  */  
   ipCashBook:number,
      /**  Line for which document should be opened  */  
   ipLineNum:number,
}

export interface OpenDocument_output{
parameters : {
      /**  output parameters  */  
   opGroupID:string,
   opDocNum:number,
}
}

   /** Required : 
      @param pattern
      @param textData
   */  
export interface ParseText_input{
      /**  Pattern  */  
   pattern:string,
      /**  Text data  */  
   textData:string,
}

export interface ParseText_output{
      /**  List of found blocks with a comma as separator  */  
   returnObj:string,
}

   /** Required : 
      @param partnerType
      @param partnerName
   */  
export interface PartnerExists_input{
   partnerType:number,
   partnerName:string,
}

export interface PartnerExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param ipBankAcctID
      @param ipCashBookNum
      @param ipDocVariance
   */  
export interface PrePostStatement_input{
      /**  Bank account ID  */  
   ipBankAcctID:string,
      /**  Cash book  */  
   ipCashBookNum:number,
      /**  Variance  */  
   ipDocVariance:number,
}

export interface PrePostStatement_output{
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ipAmount
      @param ipRateGroup
      @param ipFromCurrency
      @param ipToCurrency
      @param ipExchangeDate
      @param ipFromDoc
   */  
export interface ReCalcAmount_input{
      /**  Amount to convert  */  
   ipAmount:number,
      /**  Rate Group  */  
   ipRateGroup:string,
      /**  From Currency  */  
   ipFromCurrency:string,
      /**  To Currency  */  
   ipToCurrency:string,
      /**  Exchange Date  */  
   ipExchangeDate:string,
      /**  Document Currency  */  
   ipFromDoc:boolean,
}

export interface ReCalcAmount_output{
parameters : {
      /**  output parameters  */  
   opAmount:number,
}
}

   /** Required : 
      @param BankAcctID
      @param CashBookNum
      @param ds
   */  
export interface ReLoadBatchSubLedgerDocs_input{
   BankAcctID:string,
   CashBookNum:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface ReLoadBatchSubLedgerDocs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
      @param ds
   */  
export interface RecognizePartners_input{
      /**  Bank Account  */  
   ipBankAcct:string,
      /**  Cashbook num  */  
   ipCashBookNum:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface RecognizePartners_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param pdCashBookNum
      @param piCashBookLine
      @param piDocNum
   */  
export interface RefreshCashBDtlAuto_input{
      /**  Cash book number  */  
   pdCashBookNum:number,
      /**  CashBookLine from CashbDtl datatable  */  
   piCashBookLine:number,
      /**  Document number  */  
   piDocNum:number,
}

export interface RefreshCashBDtlAuto_output{
   returnObj:Erp_Tablesets_BankRecTableset[],
}

   /** Required : 
      @param pdCashBookNum
      @param piCashBookLine
   */  
export interface RefreshCashBDtl_input{
      /**  Cash book number  */  
   pdCashBookNum:number,
      /**  CashBookLine from CashbDtl datatable  */  
   piCashBookLine:number,
}

export interface RefreshCashBDtl_output{
   returnObj:Erp_Tablesets_BankRecTableset[],
}

   /** Required : 
      @param ipCashBookLine
      @param ipDate
      @param ipRateGrpCode
      @param ipTranCurrency
      @param ds
   */  
export interface RefreshLineRatesList_input{
      /**  Line  */  
   ipCashBookLine:number,
      /**  Date  */  
   ipDate:string,
      /**  Group Code  */  
   ipRateGrpCode:string,
      /**  Currency  */  
   ipTranCurrency:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface RefreshLineRatesList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipDate
      @param ipRateGrpCode
      @param ipTranCurrency
   */  
export interface RefreshRatesList_input{
      /**  Date  */  
   ipDate:string,
      /**  Group Code  */  
   ipRateGrpCode:string,
      /**  Currency  */  
   ipTranCurrency:string,
}

export interface RefreshRatesList_output{
parameters : {
      /**  output parameters  */  
   opRatesList:string,
}
}

   /** Required : 
      @param ipBankAcctId
      @param ipCashBookNum
      @param ds
   */  
export interface RefreshTranCodeList_input{
   ipBankAcctId:string,
   ipCashBookNum:number,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface RefreshTranCodeList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
      @param ipCashBookLine
      @param ipDocType
      @param ipToDate
   */  
export interface RetrieveDocuments_input{
      /**  Bank Account  */  
   ipBankAcct:string,
      /**  Cashbook num  */  
   ipCashBookNum:number,
      /**  Line  */  
   ipCashBookLine:number,
      /**  Document Type  */  
   ipDocType:number,
      /**  To Date  */  
   ipToDate:string,
}

export interface RetrieveDocuments_output{
}

   /** Required : 
      @param ipLineType
      @param ipPartner
      @param ipPartnerName
   */  
export interface SearchPartner_input{
      /**  Statement Line Type  */  
   ipLineType:number,
      /**  Partner  */  
   ipPartner:string,
      /**  Partner Name  */  
   ipPartnerName:string,
}

export interface SearchPartner_output{
parameters : {
      /**  output parameters  */  
   opPartnerType:number,
   opPartnerNum:number,
   opPartnerID:string,
   opPartnerBank:string,
   opPartnerBankAcct:string,
   opStorePartner:boolean,
   opImportError:string,
}
}

   /** Required : 
      @param ipBankAcctID
   */  
export interface SelectBankLockGroups_input{
      /**  Bank account ID  */  
   ipBankAcctID:string,
}

export interface SelectBankLockGroups_output{
parameters : {
      /**  output parameters  */  
   opFiscalYear:number,
   opBankslip:number,
   errorMsg:string,
   opAutoStatementImport:boolean,
   opEnableAddNewStatement:boolean,
}
}

   /** Required : 
      @param pcBankAcctID
   */  
export interface SelectBank_input{
      /**  Bank account ID  */  
   pcBankAcctID:string,
}

export interface SelectBank_output{
   returnObj:Erp_Tablesets_BankRecBankAcctTableset[],
parameters : {
      /**  output parameters  */  
   pdCashBookNum:number,
   errorMsg:string,
}
}

   /** Required : 
      @param ipDocClosingBalance
      @param ipClosingDate
      @param cashBHedRow
   */  
export interface SetBalances_input{
      /**  DocClosingBalance  */  
   ipDocClosingBalance:number,
      /**  Closing Date  */  
   ipClosingDate:string,
   cashBHedRow:Erp_Tablesets_CashBHedRow[],
}

export interface SetBalances_output{
parameters : {
      /**  output parameters  */  
   cashBHedRow:Erp_Tablesets_CashBHedRow,
}
}

   /** Required : 
      @param keys
   */  
export interface SplitKeywords_input{
      /**  String contained keys with separators  */  
   keys:string,
}

export interface SplitKeywords_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   listKeys:string,
}
}

   /** Required : 
      @param ipPartnerNum
      @param ipPartnerID
      @param partnerType
      @param ipSearchID
   */  
export interface StorePartner_input{
   ipPartnerNum:number,
   ipPartnerID:string,
   partnerType:number,
   ipSearchID:string,
}

export interface StorePartner_output{
   returnObj:boolean,
}

   /** Required : 
      @param pcBankAcctID
   */  
export interface UnSelectBank_input{
      /**  Unlock the groups for Bank account ID  */  
   pcBankAcctID:string,
}

export interface UnSelectBank_output{
parameters : {
      /**  output parameters  */  
   plSuccess:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UnlockStatement_input{
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface UnlockStatement_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
      @param ipLineNum
      @param ipDocRef
      @param ds
   */  
export interface UnmatchDocument_input{
      /**  Bank Account  */  
   ipBankAcct:string,
      /**  Cashbook num  */  
   ipCashBookNum:number,
      /**  Line #  */  
   ipLineNum:number,
      /**  Line #  */  
   ipDocRef:string,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface UnmatchDocument_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
      @param ipLineNum
      @param unmatchLinkedReverseLines
      @param ds
   */  
export interface UnmatchDocuments_input{
   ipBankAcct:string,
   ipCashBookNum:number,
   ipLineNum:number,
   unmatchLinkedReverseLines:boolean,
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface UnmatchDocuments_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param bankAcctID
      @param cashBookNum
      @param cashBookLine
   */  
export interface UnmatchLinkedReverseLines_input{
   bankAcctID:string,
   cashBookNum:number,
   cashBookLine:number,
}

export interface UnmatchLinkedReverseLines_output{
}

   /** Required : 
      @param ipCashBookNum
      @param ipCashBookLine
      @param ipHeadNum
   */  
export interface UpdateAPPay_input{
      /**  Cash book number  */  
   ipCashBookNum:number,
      /**  CashBookLine from CashbDtl datatable  */  
   ipCashBookLine:number,
      /**  Document number  */  
   ipHeadNum:number,
}

export interface UpdateAPPay_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtBankRecTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtBankRecTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param company
      @param cashBookNum
      @param cashbookLine
   */  
export interface UpdateMatchedLink_input{
      /**  CompanyID  */  
   company:string,
      /**  CashBookNum  */  
   cashBookNum:number,
      /**  CashbookLine  */  
   cashbookLine:number,
}

export interface UpdateMatchedLink_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_BankRecTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankRecTableset,
}
}

   /** Required : 
      @param ipBankAcct
      @param ipCashBookNum
      @param ipVoidedReason
   */  
export interface VoidLegalNumber_input{
      /**  Bank account  */  
   ipBankAcct:string,
      /**  Cash Book number  */  
   ipCashBookNum:number,
      /**  Reason for the void  */  
   ipVoidedReason:string,
}

export interface VoidLegalNumber_output{
   returnObj:Erp_Tablesets_BankRecTableset[],
}

   /** Required : 
      @param keyBankAcctID
   */  
export interface enableAddNewStatement_input{
   keyBankAcctID:string,
}

export interface enableAddNewStatement_output{
   returnObj:boolean,
}

