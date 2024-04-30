import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ApplyDebitMemoSvc
// Description: Apply Debit Memo entry
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/$metadata", {
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
   Description: Get ApplyDebitMemoes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ApplyDebitMemoes
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
export function get_ApplyDebitMemoes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes", {
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
   OperationID: NewUpdateExt_ApplyDebitMemoes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CheckHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CheckHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApplyDebitMemoes(requestBody:Erp_Tablesets_CheckHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ApplyDebitMemo item
   Description: Calls GetByID to retrieve the ApplyDebitMemo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ApplyDebitMemo
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
export function get_ApplyDebitMemoes_Company_HeadNum(Company:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CheckHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes(" + Company + "," + HeadNum + ")", {
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
   Summary: Calls UpdateExt to update ApplyDebitMemo for the service
   Description: Calls UpdateExt to update ApplyDebitMemo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ApplyDebitMemo
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
export function patch_ApplyDebitMemoes_Company_HeadNum(Company:string, HeadNum:string, requestBody:Erp_Tablesets_CheckHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes(" + Company + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete ApplyDebitMemo item
   Description: Call UpdateExt to delete ApplyDebitMemo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ApplyDebitMemo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ApplyDebitMemoes_Company_HeadNum(Company:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes(" + Company + "," + HeadNum + ")", {
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
export function get_ApplyDebitMemoes_Company_HeadNum_APTrans(Company:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes(" + Company + "," + HeadNum + ")/APTrans", {
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
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APTranRow
   */  
export function get_ApplyDebitMemoes_Company_HeadNum_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes(" + Company + "," + HeadNum + ")/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get APTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APTrans
      @param select Desc: Odata select comma delimited list of fields
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
export function get_APTrans(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/APTrans", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/APTrans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APTranRow
   */  
export function get_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", {
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCheckHed:string, whereClauseAPTran:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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
   if(typeof whereClauseAPTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPTran=" + whereClauseAPTran
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/GetRows" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/GetList" + params, {
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
   Summary: Invoke method _ApplyDebitMemo
   Description: This method needs to be run as the last method as the user leaves the CheckHed record.
It validates that the entire memo has been applied and creates the required GL records
If the entire memo has not been applied, then an exception will be raised and the user
cannot leave the record until it all has been applied.
   OperationID: _ApplyDebitMemo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/_ApplyDebitMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/_ApplyDebitMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApplyDebitMemo(requestBody:_ApplyDebitMemo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<_ApplyDebitMemo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/_ApplyDebitMemo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as _ApplyDebitMemo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BeforeApplyDebitMemo
   Description: Method performs actions needed before sending the CheckHed to the posting engine
Checks Withholding Taxes
Creates additional APTran records
Performs Tax Calculation and Allocation
This method does not call the posting engine
   OperationID: BeforeApplyDebitMemo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BeforeApplyDebitMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BeforeApplyDebitMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BeforeApplyDebitMemo(requestBody:BeforeApplyDebitMemo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BeforeApplyDebitMemo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/BeforeApplyDebitMemo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BeforeApplyDebitMemo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeAmtToApply
   Description: This method is used to validate/update the dataset when the DocPaymentTotal is udpated
   OperationID: ChangeAmtToApply
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeAmtToApply_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAmtToApply_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAmtToApply(requestBody:ChangeAmtToApply_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeAmtToApply_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ChangeAmtToApply", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeAmtToApply_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDtlInvoice
   Description: This method is called when the APTran InvoiceNum field is modified
   OperationID: ChangeDtlInvoice
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDtlInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlInvoice(requestBody:ChangeDtlInvoice_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDtlInvoice_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ChangeDtlInvoice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDtlInvoice_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckExchangeRate
   Description: This method is called when the APTran InvoiceNum field is modified
   OperationID: CheckExchangeRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckExchangeRate(requestBody:CheckExchangeRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckExchangeRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/CheckExchangeRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckExchangeRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDtlTranAmt
   Description: This method is run when the DocTranAmt field is modified
   OperationID: ChangeDtlTranAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDtlTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlTranAmt(requestBody:ChangeDtlTranAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDtlTranAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ChangeDtlTranAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDtlTranAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeHedInvoice
   Description: This method is used when no Invoice Number is specified in the GetNewCheckHedInv function
This will validate the invoice number provided and if valid, will default CheckHed fields
to the values in the Invoice
   OperationID: ChangeHedInvoice
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeHedInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHedInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHedInvoice(requestBody:ChangeHedInvoice_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeHedInvoice_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ChangeHedInvoice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeHedInvoice_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTranDate
   Description: This method is run when the Transaction date is changed to update the fiscal period fields
   OperationID: ChangeTranDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTranDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTranDate(requestBody:ChangeTranDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTranDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ChangeTranDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTranDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendor
   Description: Call this method when the user enters the ttCheckHed.VendorID
   OperationID: ChangeVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendor(requestBody:ChangeVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ChangeVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendor_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/CheckDocumentIsLocked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method CheckOnScreenLoad
   Description: This method is called first thing when opening the screen.  It checks to see if
the G/L is interfaced and if the Fiscal Period is valid.  If the G/L is not interfaced,
a question asking if the user wants to continue will be returned.  If the user answers no,
then they are returned to the main menu.  If the Fiscal Period is invalid, an exception
will be raised and the user should be returned to the main menu.
   OperationID: CheckOnScreenLoad
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOnScreenLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOnScreenLoad(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckOnScreenLoad_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/CheckOnScreenLoad", {
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
         resolve(data as CheckOnScreenLoad_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPrevApplication
   Description: This method is used when no Invoice Number is specified in the GetNewCheckHedInv function
This will validate the invoice number provided and if valid, will default CheckHed fields
to the values in the Invoice
   OperationID: CheckPrevApplication
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPrevApplication_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrevApplication_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPrevApplication(requestBody:CheckPrevApplication_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPrevApplication_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/CheckPrevApplication", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckPrevApplication_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteCheckDetails
   Description: This method needs to be run as the last method if the user chooses not to
Apply Debit Memo but wants to leave the CheckHed record to create a new one
or closes/exits the ApplyDebitMemo UI screen.
This will delete the appropriate CheckHed and APTran records and update the
related APInvHed to reflect the appropriate invoice balance.
   OperationID: DeleteCheckDetails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteCheckDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCheckDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteCheckDetails(requestBody:DeleteCheckDetails_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteCheckDetails_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/DeleteCheckDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteCheckDetails_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCheckHedInv
   Description: This method replaces the standard GetNewCheckHed method.  Requires a Debit Memo Invoice
   OperationID: GetNewCheckHedInv
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCheckHedInv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCheckHedInv_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCheckHedInv(requestBody:GetNewCheckHedInv_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCheckHedInv_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/GetNewCheckHedInv", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCheckHedInv_output)
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
<param name="ipHeadNum">ipHeadNum </param><param name="ipAPTranNo">ipAPTranNo </param><param name="ipCalcAll">ipCalcAll</param><param name="ds">ApplyDebitMemo dataset</param>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/SetReadyToCalc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/GetNewCheckHed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/GetNewAPTran", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APTranRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CheckHedListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CheckHedRow,
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
      @param inHeadNum
   */  
export interface BeforeApplyDebitMemo_input{
      /**  CheckHead.HeadNum  */  
   inHeadNum:number,
}

export interface BeforeApplyDebitMemo_output{
}

   /** Required : 
      @param paymentAmt
      @param ds
   */  
export interface ChangeAmtToApply_input{
      /**  Proposed value change to the DocPaymentTotal field  */  
   paymentAmt:number,
   ds:Erp_Tablesets_ApplyDebitMemoTableset[],
}

export interface ChangeAmtToApply_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyDebitMemoTableset,
}
}

   /** Required : 
      @param invoiceNum
      @param ds
   */  
export interface ChangeDtlInvoice_input{
      /**  Proposed Invoice Number  */  
   invoiceNum:string,
   ds:Erp_Tablesets_ApplyDebitMemoTableset[],
}

export interface ChangeDtlInvoice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyDebitMemoTableset,
}
}

   /** Required : 
      @param docTranAmt
      @param ds
   */  
export interface ChangeDtlTranAmt_input{
      /**  Proposed amount  */  
   docTranAmt:number,
   ds:Erp_Tablesets_ApplyDebitMemoTableset[],
}

export interface ChangeDtlTranAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyDebitMemoTableset,
}
}

   /** Required : 
      @param invoiceNum
      @param ds
   */  
export interface ChangeHedInvoice_input{
      /**  proposed Invoice Number  */  
   invoiceNum:string,
   ds:Erp_Tablesets_ApplyDebitMemoTableset[],
}

export interface ChangeHedInvoice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyDebitMemoTableset,
}
}

   /** Required : 
      @param tranDate
      @param ds
   */  
export interface ChangeTranDate_input{
      /**  Proposed Transaction Date  */  
   tranDate:string,
   ds:Erp_Tablesets_ApplyDebitMemoTableset[],
}

export interface ChangeTranDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyDebitMemoTableset,
}
}

   /** Required : 
      @param pcVendorID
      @param ds
   */  
export interface ChangeVendor_input{
      /**  Vendor ID - character code for Vendor  */  
   pcVendorID:string,
   ds:Erp_Tablesets_ApplyDebitMemoTableset[],
}

export interface ChangeVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyDebitMemoTableset,
}
}

   /** Required : 
      @param keyValue1
      @param keyValue2
   */  
export interface CheckDocumentIsLocked_input{
      /**  VendorNum  */  
   keyValue1:string,
      /**  InvoiceNum  */  
   keyValue2:string,
}

export interface CheckDocumentIsLocked_output{
}

   /** Required : 
      @param headNum
      @param vendorNum
      @param invoiceNum
      @param currSymbol
   */  
export interface CheckExchangeRate_input{
      /**  CheckHed HeadNum  */  
   headNum:number,
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Proposed Invoice Number  */  
   invoiceNum:string,
      /**  Currency Symbol  */  
   currSymbol:string,
}

export interface CheckExchangeRate_output{
parameters : {
      /**  output parameters  */  
   pcQuestion:string,
}
}

export interface CheckOnScreenLoad_output{
parameters : {
      /**  output parameters  */  
   vQuestion:string,
}
}

   /** Required : 
      @param invoiceNum
      @param ipVendorNum
   */  
export interface CheckPrevApplication_input{
      /**  proposed Invoice Number  */  
   invoiceNum:string,
      /**  proposed Vendor Number  */  
   ipVendorNum:number,
}

export interface CheckPrevApplication_output{
   returnObj:Erp_Tablesets_ApplyDebitMemoTableset[],
parameters : {
      /**  output parameters  */  
   prevFound:boolean,
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
      @param ipHeadNum
   */  
export interface DeleteCheckDetails_input{
      /**  CheckHed.HeadNum  */  
   ipHeadNum:number,
}

export interface DeleteCheckDetails_output{
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

export interface Erp_Tablesets_ApplyDebitMemoTableset{
   CheckHed:Erp_Tablesets_CheckHedRow[],
   APTran:Erp_Tablesets_APTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

export interface Erp_Tablesets_UpdExtApplyDebitMemoTableset{
   CheckHed:Erp_Tablesets_CheckHedRow[],
   APTran:Erp_Tablesets_APTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param headNum
   */  
export interface GetByID_input{
   headNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ApplyDebitMemoTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ApplyDebitMemoTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ApplyDebitMemoTableset[],
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
      @param headNum
      @param apTranNo
      @param invoiceNum
   */  
export interface GetNewAPTran_input{
   ds:Erp_Tablesets_ApplyDebitMemoTableset[],
   headNum:number,
   apTranNo:number,
   invoiceNum:string,
}

export interface GetNewAPTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyDebitMemoTableset,
}
}

   /** Required : 
      @param vendorNum
      @param invoiceNum
      @param ds
   */  
export interface GetNewCheckHedInv_input{
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Invoice Number  */  
   invoiceNum:string,
   ds:Erp_Tablesets_ApplyDebitMemoTableset[],
}

export interface GetNewCheckHedInv_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyDebitMemoTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCheckHed_input{
   ds:Erp_Tablesets_ApplyDebitMemoTableset[],
}

export interface GetNewCheckHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyDebitMemoTableset,
}
}

   /** Required : 
      @param whereClauseCheckHed
      @param whereClauseAPTran
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCheckHed:string,
   whereClauseAPTran:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ApplyDebitMemoTableset[],
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
      @param ipHeadNum
      @param ipAPTranNo
      @param ipCalcAll
      @param ds
   */  
export interface SetReadyToCalc_input{
   ipHeadNum:number,
   ipAPTranNo:number,
   ipCalcAll:boolean,
   ds:Erp_Tablesets_ApplyDebitMemoTableset[],
}

export interface SetReadyToCalc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyDebitMemoTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtApplyDebitMemoTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtApplyDebitMemoTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ApplyDebitMemoTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyDebitMemoTableset,
}
}

   /** Required : 
      @param inHeadNum
   */  
export interface _ApplyDebitMemo_input{
      /**  CheckHead.HeadNum  */  
   inHeadNum:number,
}

export interface _ApplyDebitMemo_output{
parameters : {
      /**  output parameters  */  
   outRevJrnUID:number,
   peMessage:string,
}
}

