import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.APPromissoryNotesSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/$metadata", {
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
   Description: Get APPromissoryNotes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPromissoryNotes
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadRow
   */  
export function get_APPromissoryNotes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPromissoryNotes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APPNHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APPromissoryNotes(requestBody:Erp_Tablesets_APPNHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the APPromissoryNote item
   Description: Calls GetByID to retrieve the APPromissoryNote item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPromissoryNote
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNHeadRow
   */  
export function get_APPromissoryNotes_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
         resolve(data as Erp_Tablesets_APPNHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APPromissoryNote for the service
   Description: Calls UpdateExt to update APPromissoryNote. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPromissoryNote
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APPromissoryNotes_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, requestBody:Erp_Tablesets_APPNHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete APPromissoryNote item
   Description: Call UpdateExt to delete APPromissoryNote item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPromissoryNote
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APPromissoryNotes_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Description: Get APPNDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APPNDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNDtlRow
   */  
export function get_APPromissoryNotes_Company_GroupID_HeadNum_APPNDtls(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/APPNDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APPNDtl item
   Description: Calls GetByID to retrieve the APPNDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param AdjustmentSeq Desc: AdjustmentSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNDtlRow
   */  
export function get_APPromissoryNotes_Company_GroupID_HeadNum_APPNDtls_Company_GroupID_HeadNum_InvoiceNum_AdjustmentSeq(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, AdjustmentSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/APPNDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + AdjustmentSeq + ")", {
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
         resolve(data as Erp_Tablesets_APPNDtlRow)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranRow
   */  
export function get_APPromissoryNotes_Company_GroupID_HeadNum_BankTrans(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/BankTrans", {
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
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
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
export function get_APPromissoryNotes_Company_GroupID_HeadNum_BankTrans_Company_BankAcctID_TranNum_Voided(Company:string, GroupID:string, HeadNum:string, BankAcctID:string, TranNum:string, Voided:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
   Description: Get APPNHeadTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APPNHeadTGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadTGLCRow
   */  
export function get_APPromissoryNotes_Company_GroupID_HeadNum_APPNHeadTGLCs(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/APPNHeadTGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APPNHeadTGLC item
   Description: Calls GetByID to retrieve the APPNHeadTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNHeadTGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNHeadTGLCRow
   */  
export function get_APPromissoryNotes_Company_GroupID_HeadNum_APPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company:string, GroupID:string, HeadNum:string, TGLCTranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNHeadTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/APPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")", {
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
         resolve(data as Erp_Tablesets_APPNHeadTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_APPromissoryNotes_Company_GroupID_HeadNum_EntityGLCs(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/EntityGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_APPromissoryNotes_Company_GroupID_HeadNum_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, GroupID:string, HeadNum:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get APPNHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APPNHeadAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadAttchRow
   */  
export function get_APPromissoryNotes_Company_GroupID_HeadNum_APPNHeadAttches(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/APPNHeadAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APPNHeadAttch item
   Description: Calls GetByID to retrieve the APPNHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNHeadAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNHeadAttchRow
   */  
export function get_APPromissoryNotes_Company_GroupID_HeadNum_APPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company:string, GroupID:string, HeadNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/APPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_APPNHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get APPNDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPNDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNDtlRow
   */  
export function get_APPNDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPNDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APPNDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APPNDtls(requestBody:Erp_Tablesets_APPNDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the APPNDtl item
   Description: Calls GetByID to retrieve the APPNDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param AdjustmentSeq Desc: AdjustmentSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNDtlRow
   */  
export function get_APPNDtls_Company_GroupID_HeadNum_InvoiceNum_AdjustmentSeq(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, AdjustmentSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + AdjustmentSeq + ")", {
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
         resolve(data as Erp_Tablesets_APPNDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APPNDtl for the service
   Description: Calls UpdateExt to update APPNDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPNDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param AdjustmentSeq Desc: AdjustmentSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APPNDtls_Company_GroupID_HeadNum_InvoiceNum_AdjustmentSeq(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, AdjustmentSeq:string, requestBody:Erp_Tablesets_APPNDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + AdjustmentSeq + ")", {
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
   Summary: Call UpdateExt to delete APPNDtl item
   Description: Call UpdateExt to delete APPNDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPNDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param AdjustmentSeq Desc: AdjustmentSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APPNDtls_Company_GroupID_HeadNum_InvoiceNum_AdjustmentSeq(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, AdjustmentSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + AdjustmentSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
   Description: Get BankTranGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTranGLCs1
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranGLCRow
   */  
export function get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranGLCs(Company:string, BankAcctID:string, TranNum:string, Voided:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BankTranGLC item
   Description: Calls GetByID to retrieve the BankTranGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranGLC1
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
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BankTranGLCRow
   */  
export function get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company:string, BankAcctID:string, TranNum:string, Voided:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_BankTranGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BankTranGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTranGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranGLCRow
   */  
export function get_BankTranGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTranGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankTranGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BankTranGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankTranGLCs(requestBody:Erp_Tablesets_BankTranGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTranGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the BankTranGLC item
   Description: Calls GetByID to retrieve the BankTranGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranGLC
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
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BankTranGLCRow
   */  
export function get_BankTranGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company:string, BankAcctID:string, TranNum:string, Voided:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTranGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_BankTranGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BankTranGLC for the service
   Description: Calls UpdateExt to update BankTranGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankTranGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param Voided Desc: Voided   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankTranGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company:string, BankAcctID:string, TranNum:string, Voided:string, SysRowID:string, requestBody:Erp_Tablesets_BankTranGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTranGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete BankTranGLC item
   Description: Call UpdateExt to delete BankTranGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTranGLC
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
export function delete_BankTranGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company:string, BankAcctID:string, TranNum:string, Voided:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTranGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
   Description: Get APPNHeadTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPNHeadTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadTGLCRow
   */  
export function get_APPNHeadTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadTGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPNHeadTGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNHeadTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APPNHeadTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APPNHeadTGLCs(requestBody:Erp_Tablesets_APPNHeadTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadTGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the APPNHeadTGLC item
   Description: Calls GetByID to retrieve the APPNHeadTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNHeadTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNHeadTGLCRow
   */  
export function get_APPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company:string, GroupID:string, HeadNum:string, TGLCTranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNHeadTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")", {
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
         resolve(data as Erp_Tablesets_APPNHeadTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APPNHeadTGLC for the service
   Description: Calls UpdateExt to update APPNHeadTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPNHeadTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNHeadTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company:string, GroupID:string, HeadNum:string, TGLCTranNum:string, requestBody:Erp_Tablesets_APPNHeadTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")", {
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
   Summary: Call UpdateExt to delete APPNHeadTGLC item
   Description: Call UpdateExt to delete APPNHeadTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPNHeadTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company:string, GroupID:string, HeadNum:string, TGLCTranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")", {
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
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/EntityGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EntityGLCs(requestBody:Erp_Tablesets_EntityGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/EntityGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:Erp_Tablesets_EntityGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get APPNHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPNHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadAttchRow
   */  
export function get_APPNHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPNHeadAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APPNHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APPNHeadAttches(requestBody:Erp_Tablesets_APPNHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the APPNHeadAttch item
   Description: Calls GetByID to retrieve the APPNHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNHeadAttchRow
   */  
export function get_APPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company:string, GroupID:string, HeadNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_APPNHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APPNHeadAttch for the service
   Description: Calls UpdateExt to update APPNHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPNHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company:string, GroupID:string, HeadNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_APPNHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete APPNHeadAttch item
   Description: Call UpdateExt to delete APPNHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPNHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company:string, GroupID:string, HeadNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
   Description: Get PITotals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PITotals
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PITotalsRow
   */  
export function get_PITotals(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PITotalsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/PITotals", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PITotalsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PITotals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PITotalsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PITotalsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PITotals(requestBody:Erp_Tablesets_PITotalsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/PITotals", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PITotal item
   Description: Calls GetByID to retrieve the PITotal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PITotal
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PITotalsRow
   */  
export function get_PITotals_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PITotalsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/PITotals(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_PITotalsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PITotal for the service
   Description: Calls UpdateExt to update PITotal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PITotal
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PITotalsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PITotals_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_PITotalsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/PITotals(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete PITotal item
   Description: Call UpdateExt to delete PITotal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PITotal
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PITotals_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/PITotals(" + SysRowID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadListRow)
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
export function get_GetRows(whereClauseAPPNHead:string, whereClauseAPPNHeadAttch:string, whereClauseAPPNDtl:string, whereClauseBankTran:string, whereClauseBankTranGLC:string, whereClauseAPPNHeadTGLC:string, whereClauseEntityGLC:string, whereClauseLegalNumGenOpts:string, whereClausePITotals:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAPPNHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPPNHead=" + whereClauseAPPNHead
   }
   if(typeof whereClauseAPPNHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPPNHeadAttch=" + whereClauseAPPNHeadAttch
   }
   if(typeof whereClauseAPPNDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPPNDtl=" + whereClauseAPPNDtl
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
   if(typeof whereClauseBankTranGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBankTranGLC=" + whereClauseBankTranGLC
   }
   if(typeof whereClauseAPPNHeadTGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPPNHeadTGLC=" + whereClauseAPPNHeadTGLC
   }
   if(typeof whereClauseEntityGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEntityGLC=" + whereClauseEntityGLC
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
   if(typeof whereClausePITotals!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePITotals=" + whereClausePITotals
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetList" + params, {
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
   Summary: Invoke method ApplyInvoiceToGroup
   Description: Create Vendor Checks for selected invoice.
   OperationID: ApplyInvoiceToGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ApplyInvoiceToGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApplyInvoiceToGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApplyInvoiceToGroup(requestBody:ApplyInvoiceToGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ApplyInvoiceToGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/ApplyInvoiceToGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ApplyInvoiceToGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the miscellaneous shipment.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/AssignLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetEndorsedARPILegalNumGenOpts
   Description: Returns the legal number generation options for AR Promissory Note movement.
   OperationID: GetEndorsedARPILegalNumGenOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetEndorsedARPILegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEndorsedARPILegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEndorsedARPILegalNumGenOpts(requestBody:GetEndorsedARPILegalNumGenOpts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEndorsedARPILegalNumGenOpts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetEndorsedARPILegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetEndorsedARPILegalNumGenOpts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignEndorsedARPILegalNumber
   Description: Assigns a legal number to AR Promissory Note movement.
   OperationID: AssignEndorsedARPILegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AssignEndorsedARPILegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignEndorsedARPILegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignEndorsedARPILegalNumber(requestBody:AssignEndorsedARPILegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AssignEndorsedARPILegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/AssignEndorsedARPILegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AssignEndorsedARPILegalNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePIType
   Description: Call method when the user changes APPNHead.TransDate.
   OperationID: ChangePIType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePIType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePIType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePIType(requestBody:ChangePIType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePIType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/ChangePIType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangePIType_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/ChangeTranAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/CheckDocumentIsLocked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method CreateAPPNHead
   Description: Create Vendor Checks for selected invoices.
   OperationID: CreateAPPNHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateAPPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateAPPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateAPPNHead(requestBody:CreateAPPNHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateAPPNHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/CreateAPPNHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateAPPNHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidAPPNMoveLegalNumber
   Description: Voids legal number generated on a status change
   OperationID: VoidAPPNMoveLegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VoidAPPNMoveLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidAPPNMoveLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidAPPNMoveLegalNumber(requestBody:VoidAPPNMoveLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VoidAPPNMoveLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/VoidAPPNMoveLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as VoidAPPNMoveLegalNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteAPPNMove
   Description: Deletes a status change movement
   OperationID: DeleteAPPNMove
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteAPPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAPPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteAPPNMove(requestBody:DeleteAPPNMove_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteAPPNMove_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/DeleteAPPNMove", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteAPPNMove_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateStatusAndType
   Description: Validates that status was changed
   OperationID: ValidateStatusAndType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateStatusAndType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateStatusAndType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateStatusAndType(requestBody:ValidateStatusAndType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateStatusAndType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/ValidateStatusAndType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateStatusAndType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateUnpostedMovement
   Description: Validates if PI has an unposted movement and throws an error or returns a question to the user along with the unposted movement information.
   OperationID: ValidateUnpostedMovement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateUnpostedMovement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUnpostedMovement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateUnpostedMovement(requestBody:ValidateUnpostedMovement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateUnpostedMovement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/ValidateUnpostedMovement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateUnpostedMovement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CancelStatusChange
   Description: Validates Lock Status, Voids Legal Number and Deletes APPNMove when cancelling Status Change.
   OperationID: CancelStatusChange
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CancelStatusChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelStatusChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CancelStatusChange(requestBody:CancelStatusChange_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CancelStatusChange_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/CancelStatusChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CancelStatusChange_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateNewAPPNHead
   Description: Create New CheckHed record.  To be used instead of GetNewCheckHed record.
   OperationID: CreateNewAPPNHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateNewAPPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewAPPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateNewAPPNHead(requestBody:CreateNewAPPNHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateNewAPPNHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/CreateNewAPPNHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateNewAPPNHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateNewAPPNHeadEndorsement
   Description: Create New APPNHead record based on endorsed AR Promissory Note.
   OperationID: CreateNewAPPNHeadEndorsement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateNewAPPNHeadEndorsement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewAPPNHeadEndorsement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateNewAPPNHeadEndorsement(requestBody:CreateNewAPPNHeadEndorsement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateNewAPPNHeadEndorsement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/CreateNewAPPNHeadEndorsement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateNewAPPNHeadEndorsement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteNegPayment
   Description: DeleteNegPayments.  Deletes all checks in the group that have negative check.
amounts. Works the same as MassDelete but only deletes negative balance checks.
   OperationID: DeleteNegPayment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteNegPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteNegPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteNegPayment(requestBody:DeleteNegPayment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteNegPayment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/DeleteNegPayment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteNegPayment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateAPPNDtl
   Description: This method combines the GetNewAPPNDtl and Update() method into one routine
so that the user can run an "Auto Apply" Payment function
   OperationID: GenerateAPPNDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateAPPNDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateAPPNDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateAPPNDtl(requestBody:GenerateAPPNDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateAPPNDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GenerateAPPNDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GenerateAPPNDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAPPNMove
   Description: Get the APPNMove records for an APPromissoryNotes.
   OperationID: GetAPPNMove
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAPPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAPPNMove(requestBody:GetAPPNMove_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAPPNMove_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetAPPNMove", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetAPPNMove_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBankAcctInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankAcctInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankAcctInfo(requestBody:GetBankAcctInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBankAcctInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetBankAcctInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBankAcctInfo_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetBankFeeDefaultAccount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetData4ARPITracker
   Description: Get AP payment instrument data for AR Payment Instrument Tracker
   OperationID: GetData4ARPITracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetData4ARPITracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetData4ARPITracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetData4ARPITracker(requestBody:GetData4ARPITracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetData4ARPITracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetData4ARPITracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetData4ARPITracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGLJrnDtl
   Description: Get the GLJrnDtl records for an APPromissoryNote.
   OperationID: GetGLJrnDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGLJrnDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLJrnDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLJrnDtl(requestBody:GetGLJrnDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGLJrnDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetGLJrnDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetGLJrnDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGroupIDForPI
   Description: This method will retrieve the GroupID for an APPNHead record that's for the
APPromNoteID supplied.
   OperationID: GetGroupIDForPI
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGroupIDForPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupIDForPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGroupIDForPI(requestBody:GetGroupIDForPI_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGroupIDForPI_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetGroupIDForPI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetGroupIDForPI_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGroupIDForPNI
   OperationID: GetGroupIDForPNI
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGroupIDForPNI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupIDForPNI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGroupIDForPNI(requestBody:GetGroupIDForPNI_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGroupIDForPNI_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetGroupIDForPNI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetGroupIDForPNI_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultMoveTranDocType
   Description: Restores Default Document Type when user leaves it blank
   OperationID: GetDefaultMoveTranDocType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultMoveTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultMoveTranDocType(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultMoveTranDocType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetDefaultMoveTranDocType", {
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
         resolve(data as GetDefaultMoveTranDocType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method NeedsLegalNumber
   Description: Validates if a Legal Number can be created for the selected document type
   OperationID: NeedsLegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/NeedsLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NeedsLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NeedsLegalNumber(requestBody:NeedsLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<NeedsLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/NeedsLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as NeedsLegalNumber_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetLegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewAPPNHeadByGroupID
   OperationID: GetNewAPPNHeadByGroupID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPPNHeadByGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNHeadByGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPPNHeadByGroupID(requestBody:GetNewAPPNHeadByGroupID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPPNHeadByGroupID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetNewAPPNHeadByGroupID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAPPNHeadByGroupID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPPNMoveByAPPNHead
   OperationID: GetNewAPPNMoveByAPPNHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPPNMoveByAPPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNMoveByAPPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPPNMoveByAPPNHead(requestBody:GetNewAPPNMoveByAPPNHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPPNMoveByAPPNHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetNewAPPNMoveByAPPNHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAPPNMoveByAPPNHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBankTranByHeadNum
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetNewBankTranByHeadNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetPostCodeByPIStatus
   Description: GetPostCodeByPIStatus
   OperationID: GetPostCodeByPIStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPostCodeByPIStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostCodeByPIStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPostCodeByPIStatus(requestBody:GetPostCodeByPIStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPostCodeByPIStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetPostCodeByPIStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPostCodeByPIStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRestartAPPNPrinting
   Description: Gets restart AP Promissory Note printing
   OperationID: GetRestartAPPNPrinting
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRestartAPPNPrinting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRestartAPPNPrinting_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRestartAPPNPrinting(requestBody:GetRestartAPPNPrinting_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRestartAPPNPrinting_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetRestartAPPNPrinting", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRestartAPPNPrinting_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsTracker
   Description: Wrapper on GetRows for Trackers so Adjustment records are not deleted
   OperationID: GetRowsTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsTracker(requestBody:GetRowsTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetRowsTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsTracker_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/MassDelete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/OnChangeBankFeeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method OnChangeDocTranAmt
   Description: Call method when the user changes the Doc Tran Amount.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/OnChangeDocTranAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/OnChangeInvoiceNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
Use this method with Payment maintenance screen for ApInvSelDataSet.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/OnChangeInvSelPayment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method OnChangeTransDate
   Description: Call method when the user changes APPNHead.TransDate.
   OperationID: OnChangeTransDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTransDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTransDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTransDate(requestBody:OnChangeTransDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTransDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/OnChangeTransDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeTransDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeVendBankAcctID
   Description: Call this method when the user enters the ttAPNHead.VendBankAcctID
   OperationID: OnChangeVendBankAcctID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeVendBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendBankAcctID(requestBody:OnChangeVendBankAcctID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeVendBankAcctID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/OnChangeVendBankAcctID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeVendBankAcctID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeVendor
   Description: Call this method when the user enters the ttAPNHead.VendorNum
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/OnChangeVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method OnChangeType
   Description: OnChangeType
   OperationID: OnChangeType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeType(requestBody:OnChangeType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/OnChangeType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrePost
   Description: Check APPNHead before posting
   OperationID: PrePost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PrePost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePost(requestBody:PrePost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PrePost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/PrePost", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PrePost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectInvoices
   Description: Read ApInvHed records and create ApinvSel records if they meet the selection criteria.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/SelectInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method SelectInvoiceToApplyToGroup
   Description: Read ApInvHed records and create ApinvSel records if they meet the selection criteria.
   OperationID: SelectInvoiceToApplyToGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectInvoiceToApplyToGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectInvoiceToApplyToGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectInvoiceToApplyToGroup(requestBody:SelectInvoiceToApplyToGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectInvoiceToApplyToGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/SelectInvoiceToApplyToGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SelectInvoiceToApplyToGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateAPPNMove4WriteOff
   OperationID: UpdateAPPNMove4WriteOff
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateAPPNMove4WriteOff_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAPPNMove4WriteOff_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAPPNMove4WriteOff(requestBody:UpdateAPPNMove4WriteOff_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateAPPNMove4WriteOff_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/UpdateAPPNMove4WriteOff", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateAPPNMove4WriteOff_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateDueDateDescription
   Description: Purpose: Update DueDate and Description for APPNHead only.
Parameters:
inGroupID
inHeadNum
inDueDateNew new value of DueDate
inDescriptionNew new value of Description
define_output_parameter_dataset_for_APPromissoryNotesDataSet
Notes:
   OperationID: UpdateDueDateDescription
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateDueDateDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDueDateDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateDueDateDescription(requestBody:UpdateDueDateDescription_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateDueDateDescription_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/UpdateDueDateDescription", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateDueDateDescription_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/VoidLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetAvailTranDocTypes
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetAvailTranDocTypes", {
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
   Summary: Invoke method selectFilterPIPayMethod
   Description: Return the id’s for payment methods from AP
   OperationID: selectFilterPIPayMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/selectFilterPIPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_selectFilterPIPayMethod(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<selectFilterPIPayMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/selectFilterPIPayMethod", {
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
         resolve(data as selectFilterPIPayMethod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateRequiredFields
   Description: ValidateRequiredFields
   OperationID: ValidateRequiredFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateRequiredFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRequiredFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRequiredFields(requestBody:ValidateRequiredFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateRequiredFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/ValidateRequiredFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateRequiredFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateWithholdingExists
   Description: Method to validate if there is a withholding tax in either invoice or details.
   OperationID: ValidateWithholdingExists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateWithholdingExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWithholdingExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateWithholdingExists(requestBody:ValidateWithholdingExists_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateWithholdingExists_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/ValidateWithholdingExists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateWithholdingExists_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/PreUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method ValidatePaymentInstruments
   Description: Validate the PI Type Generation Options and Supplier Bank Required Flag
   OperationID: ValidatePaymentInstruments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePaymentInstruments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePaymentInstruments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePaymentInstruments(requestBody:ValidatePaymentInstruments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePaymentInstruments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/ValidatePaymentInstruments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidatePaymentInstruments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePIBeforePrint
   Description: Validate Payment Instruments are applied before printing, returns a warning if they are not.
   OperationID: ValidatePIBeforePrint
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePIBeforePrint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePIBeforePrint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePIBeforePrint(requestBody:ValidatePIBeforePrint_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePIBeforePrint_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/ValidatePIBeforePrint", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidatePIBeforePrint_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPPNHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPPNHead(requestBody:GetNewAPPNHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPPNHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetNewAPPNHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAPPNHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPPNHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNHeadAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPPNHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPPNHeadAttch(requestBody:GetNewAPPNHeadAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPPNHeadAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetNewAPPNHeadAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAPPNHeadAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPPNDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPPNDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPPNDtl(requestBody:GetNewAPPNDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPPNDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetNewAPPNDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAPPNDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetNewBankTran", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewBankTranGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankTranGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBankTranGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankTranGLC(requestBody:GetNewBankTranGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBankTranGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetNewBankTranGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewBankTranGLC_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPPNHeadTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNHeadTGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPPNHeadTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNHeadTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPPNHeadTGLC(requestBody:GetNewAPPNHeadTGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPPNHeadTGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetNewAPPNHeadTGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAPPNHeadTGLC_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEntityGLC(requestBody:GetNewEntityGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewEntityGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetNewEntityGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewEntityGLC_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APPNDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APPNHeadAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APPNHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APPNHeadRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APPNHeadTGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankTranGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankTranRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PITotalsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PITotalsRow,
}

export interface Erp_Tablesets_APPNDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Line  */  
   "APPNDtlLine":number,
      /**  Bank Account ID of the promissoiry note.  */  
   "BankAcctID":string,
      /**  Discount Amount in base currency.  */  
   "DiscAmt":number,
      /**  Discount Amount in invoice currency.  */  
   "DocDiscAmt":number,
      /**  Tax amount in invoice currency.  */  
   "DocTaxAmt":number,
      /**  Transaction amount in invoice currency.  */  
   "DocTranAmt":number,
      /**  Entry Person  */  
   "EntryPerson":string,
      /**  Indicates that the promissory note is posted to the GL.  */  
   "GLPosted":boolean,
      /**  AP Invoice Number linked to the promissory note.  */  
   "InvoiceNum":string,
      /**  Rounding Differences  */  
   "RoundDiff":number,
      /**  Discount Amount in report currency 1.  */  
   "Rpt1DiscAmt":number,
      /**  Tax amount  in report currency 1.  */  
   "Rpt1TaxAmt":number,
      /**  Transaction amount  in report currency 1.  */  
   "Rpt1TranAmt":number,
      /**  Discount Amount in report currency 2.  */  
   "Rpt2DiscAmt":number,
      /**  Tax amount  in report currency 2.  */  
   "Rpt2TaxAmt":number,
      /**  Transaction amount  in report currency 2.  */  
   "Rpt2TranAmt":number,
      /**  Discount Amount in report currency 3.  */  
   "Rpt3DiscAmt":number,
      /**  Tax amount  in report currency 3.  */  
   "Rpt3TaxAmt":number,
      /**  Transaction amount  in report currency 3.  */  
   "Rpt3TranAmt":number,
      /**  Tax amount in base currency.  */  
   "TaxAmt":number,
      /**  Tax Liability  */  
   "TaxRegionCode":string,
      /**  Transaction Amount in base currency.  */  
   "TranAmt":number,
      /**  Transaction date.  */  
   "TranDate":string,
      /**  Supplier  */  
   "VendorNum":number,
      /**  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  */  
   "HeadNum":number,
      /**  Indicates if the promissory node is voided.  */  
   "Voided":boolean,
      /**  Group ID  */  
   "GroupID":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  */  
   "FiscalPeriod":number,
      /**   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  */  
   "FiscalYear":number,
      /**   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  */  
   "FiscalYearSuffix":string,
      /**  The Legal Number for the record.  */  
   "LegalNumber":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  */  
   "Posted":boolean,
      /**  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  */  
   "Description":string,
      /**  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  */  
   "TranType":string,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Link To first checkhed record  */  
   "FirstHeadNum":number,
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
      /**  AdjustmentSeq  */  
   "AdjustmentSeq":number,
   "AmtToAP":number,
   "ApplyDate":string,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
   "BaseCurrSymbolCurrDesc":string,
   "BaseCurrSymbolCurrName":string,
   "BaseCurrSymbolCurrSymbol":string,
   "BaseCurrSymbolDocumentDesc":string,
   "BaseSelfAssessedTax":number,
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
      /**  The display gl account.  */  
   "DispGLAcct":string,
   "DispTranAmt":number,
   "DocBaseSelfAssessedTax":number,
   "DocDispTranAmt":number,
   "DocExpenseAmount":number,
   "DocInvoiceAmt":number,
   "DocInvoiceBal":number,
   "DocNetAmount":number,
   "DocNewBalance":number,
   "DocUnPostedBal":number,
   "DueDate":string,
   "ExchangeRate":number,
   "ExpenseAmount":number,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   "FullyPaid":boolean,
      /**  This is the source Company of the Central Payment linked invoice  */  
   "GlbCompany":string,
   "InvoiceAmt":number,
   "InvoiceBal":number,
   "InvoiceDate":string,
   "LockRate":boolean,
   "NetAmount":number,
   "NewBalance":number,
      /**  Indicates if posting GL transactions.  */  
   "PostToGL":boolean,
   "TermsCode":string,
   "TermsCodeDescription":string,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign.  */  
   "UnPostedBal":number,
   "WithHoldTax":number,
   "DiscountDate":string,
      /**  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  */  
   "ChangeExchangeRateResponse":string,
   "DocSelfAssessedTax":number,
   "DocWithHoldTax":number,
   "SelfAssessedTax":number,
   "IsFiltered":boolean,
   "APPromNoteID":string,
   "PIStatus":string,
   "PIStatusStatusDesc":string,
   "BitFlag":number,
   "BankAcctIDBankName":string,
   "BankAcctIDDescription":string,
   "InvoiceNumDescription":string,
   "TaxRegionCodeDescription":string,
   "VendorNumZIP":string,
   "VendorNumCity":string,
   "VendorNumCurrencyCode":string,
   "VendorNumVendorID":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress2":string,
   "VendorNumTermsCode":string,
   "VendorNumState":string,
   "VendorNumAddress1":string,
   "VendorNumName":string,
   "VendorNumAddress3":string,
   "VendorNumCountry":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APPNHeadAttchRow{
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

export interface Erp_Tablesets_APPNHeadListRow{
      /**  Applied Amount. Base Currency.  */  
   "AppliedAmount":number,
      /**  Bank Account of the promissory note.  */  
   "BankAcctID":string,
      /**  Bank Amount  */  
   "BankAmount":number,
      /**  Bank Slip Number of the promissory note.  */  
   "BankSlip":string,
      /**  Bank Total Amount.  */  
   "BankTotalAmt":number,
      /**  Cash book Number.  */  
   "CashBookNum":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Bank Account ID of the company.  */  
   "CompBankAcctID":string,
      /**  Currency code of the promissory note.  */  
   "CurrencyCode":string,
      /**  Description  */  
   "Description":string,
      /**  Discount amount in base currency.  */  
   "DiscountAmt":number,
      /**  Promissory Note amount in document currency.  */  
   "DocPNAmt":number,
      /**  Due date of the promissory note.  */  
   "DueDate":string,
      /**  Entry Person.  */  
   "EntryPerson":string,
      /**  Exchange Rate of the promissory note.  */  
   "ExchangeRate":number,
      /**  Indicates if the promissory node is fully paid.  */  
   "Paid":boolean,
      /**  Promissory note amount in base currency.  */  
   "PNAmt":number,
      /**  Indicates that the promissory note is posted.  */  
   "Posted":boolean,
      /**  Rate Group Code.  */  
   "RateGrpCode":string,
      /**  Promissory Note Amount in Report Currency 1.  */  
   "Rpt1PNAmt":number,
      /**  Promissory Note Discount Amount in Report Currency 1.  */  
   "Rpt1Discountamt":number,
      /**  Promissory Note Bank Total Amount in Report Currency 1.  */  
   "Rpt1BankTotalAmt":number,
      /**  Promissory Note Amount in Report Currency 2.  */  
   "Rpt2PNAmt":number,
      /**  Promissory Note Discount Amount in Report Currency 2.  */  
   "Rpt2DiscountAmt":number,
      /**  Promissory Note Bank Total Amount in Report Currency 2.  */  
   "Rpt2BankTotalAmt":number,
      /**  Promissory Note Amount in Report Currency 3.  */  
   "Rpt3PNAmt":number,
      /**  Promissory Note Discount Amount in Report Currency 3.  */  
   "Rpt3DiscountAmt":number,
      /**  Promissory Note Bank Total Amount in Report Currency 3.  */  
   "Rpt3BankTotalAmt":number,
      /**  Indicates that the promissory note is signed.  */  
   "Signed":boolean,
      /**  Total AP Amount  */  
   "TotalAPAmt":number,
      /**  Transaction date.  */  
   "TransDate":string,
      /**  Supplier Bank Account ID  */  
   "VendBankAcctID":string,
      /**  Supplier ID  */  
   "VendorID":string,
      /**  Supplier number  */  
   "VendorNum":number,
      /**  Voided Flag  */  
   "Voided":boolean,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   "GroupID":string,
      /**  AP Payment Instrument ID  */  
   "APPromNoteID":string,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  First company address line.  */  
   "CompanyAddr1":string,
      /**  Second company address line.  */  
   "CompanyAddr2":string,
      /**  Third company address line.  */  
   "CompanyAddr3":string,
      /**  Company City portion of the address.  */  
   "CompanyCity":string,
      /**  Company Country portion of the address.  */  
   "CompanyCountry":string,
      /**  Company Name  */  
   "CompanyName":string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   "CompanyPostalCode":string,
      /**  Company State portion of the address.  */  
   "CompanyState":string,
      /**  First supplier address line.  */  
   "SupplierAddr1":string,
      /**  Second supplier address line.  */  
   "SupplierAddr2":string,
      /**  Third supplier address line.  */  
   "SupplierAddr3":string,
      /**  Company City portion of the address.  */  
   "SupplierCity":string,
      /**  Supplier State portion of the address.  */  
   "SupplierState":string,
      /**  Supplier Postal Code or Zip Code portion of the address.  */  
   "SupplierPostalCode":string,
      /**  Supplier Name  */  
   "SupplierName":string,
      /**  Supplier Country portion of the address.  */  
   "SupplierCountry":string,
      /**   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  */  
   "PIStatus":string,
      /**  Promissory Note Type  */  
   "Type":string,
      /**  Issue Date  */  
   "IssueDate":string,
      /**  IBAN Code for company's bank.  */  
   "CompIBANCode":string,
      /**  Bank/Branch Code for company's bank.  */  
   "CompBankBranchCode":string,
      /**  Bank/Branch Code for customer's bank.  */  
   "CustBankBranchCode":string,
      /**  IBAN Code for customer's bank.  */  
   "CustIBANCode":string,
      /**  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  */  
   "ForceDiscount":boolean,
      /**  Total paid amount in Base  */  
   "PaymentTotal":number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   "Variance":number,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Enter Totals flag  */  
   "IsEnterTotal":boolean,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt1Variance":number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt2Variance":number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt3Variance":number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   "DocVariance":number,
      /**  Total paid amount in payment currency  */  
   "DocPaymentTotal":number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   "PaymentBankRate":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  Total paid amount in Rpt1 currency  */  
   "Rpt1PaymentTotal":number,
      /**  Total paid amount in Rpt2 currency  */  
   "Rpt2PaymentTotal":number,
      /**  Total paid amount in Rpt3 currency  */  
   "Rpt3PaymentTotal":number,
      /**  Amount that the bank cleared the payment instrument for.  */  
   "ClearedAmt":number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   "ClearedPerson":string,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPI":boolean,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   "CashbookLine":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Reference to the first checkhed  */  
   "FirstHeadNum":number,
      /**  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  */  
   "Manual":boolean,
      /**  Reason to change the Customer or Company information  */  
   "ChgComment":string,
      /**  Indicates APPRomNoteID was generated using AP CheckHed numbering  */  
   "PymtCntr":boolean,
      /**  Payment Instrument Stage  */  
   "PIStage":string,
      /**  Lock Exchange Rate  */  
   "LockRate":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  SupplierCountryNum  */  
   "SupplierCountryNum":number,
      /**  Enable the Bank Account Search Button  */  
   "BankAccountEnabled":boolean,
      /**  Bank Currency Code  */  
   "BankCurrCode":string,
   "BankCurrSymbol":string,
   "BaseCurrSymbol":string,
   "PaymentAmount":number,
   "PaymentStatus":string,
   "CompanyBankAcct":string,
   "CompanyBankIdentifier":string,
   "CompanyBankName":string,
   "VendBankName":string,
   "VendBankAcct":string,
   "VendBankIdentifier":string,
   "XRateLabel":string,
   "EnterPaymentTotal":boolean,
   "FullyPaid":boolean,
   "TotalRoundDiff":number,
   "XRateLabelPaymentBank":string,
   "XRateLabelPaymentBase":string,
   "VoidDate":string,
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
      /**  Field to bring the Company Country Name  */  
   "CompanyCountryNum":number,
   "TypeDesc":string,
   "IsFiltered":boolean,
   "GainLossReal":number,
   "DocGainLossReal":number,
   "Rpt1GainLossReal":number,
   "Rpt2GainLossReal":number,
   "Rpt3GainLossReal":number,
   "DocGainLossUnreal":number,
   "GainLossUnreal":number,
   "Rpt1GainLossUnreal":number,
   "Rpt2GainLossUnreal":number,
   "Rpt3GainLossUnreal":number,
   "RevalDate":string,
   "DocDiscountAmt":number,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Full description of the bank account.  */  
   "BankAcctIDDescription":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseCurrSymbolDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrSymbolCurrName":string,
      /**  Description of the currency  */  
   "BaseCurrSymbolCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrSymbolCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrSymbolCurrencyID":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  Status Description  */  
   "PIStatusStatusDesc":string,
      /**  Description  */  
   "TranDocTypeDescription":string,
      /**  Supplier Bank Name  */  
   "VendBankAcctIDBankName":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
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
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APPNHeadRow{
      /**  Applied Amount. Base Currency.  */  
   "AppliedAmount":number,
      /**  Bank Account of the promissory note.  */  
   "BankAcctID":string,
      /**  Bank Amount  */  
   "BankAmount":number,
      /**  Bank Slip Number of the promissory note.  */  
   "BankSlip":string,
      /**  Bank Total Amount.  */  
   "BankTotalAmt":number,
      /**  Cash book Number.  */  
   "CashBookNum":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Bank Account ID of the company.  */  
   "CompBankAcctID":string,
      /**  Currency code of the promissory note.  */  
   "CurrencyCode":string,
      /**  Description  */  
   "Description":string,
      /**  Discount amount in base currency.  */  
   "DiscountAmt":number,
      /**  Promissory Note amount in document currency.  */  
   "DocPNAmt":number,
      /**  Due date of the promissory note.  */  
   "DueDate":string,
      /**  Entry Person.  */  
   "EntryPerson":string,
      /**  Exchange Rate of the promissory note.  */  
   "ExchangeRate":number,
      /**  Indicates if the promissory node is fully paid.  */  
   "Paid":boolean,
      /**  Promissory note amount in base currency.  */  
   "PNAmt":number,
      /**  Indicates that the promissory note is posted.  */  
   "Posted":boolean,
      /**  Rate Group Code.  */  
   "RateGrpCode":string,
      /**  Promissory Note Amount in Report Currency 1.  */  
   "Rpt1PNAmt":number,
      /**  Promissory Note Discount Amount in Report Currency 1.  */  
   "Rpt1Discountamt":number,
      /**  Promissory Note Bank Total Amount in Report Currency 1.  */  
   "Rpt1BankTotalAmt":number,
      /**  Promissory Note Amount in Report Currency 2.  */  
   "Rpt2PNAmt":number,
      /**  Promissory Note Discount Amount in Report Currency 2.  */  
   "Rpt2DiscountAmt":number,
      /**  Promissory Note Bank Total Amount in Report Currency 2.  */  
   "Rpt2BankTotalAmt":number,
      /**  Promissory Note Amount in Report Currency 3.  */  
   "Rpt3PNAmt":number,
      /**  Promissory Note Discount Amount in Report Currency 3.  */  
   "Rpt3DiscountAmt":number,
      /**  Promissory Note Bank Total Amount in Report Currency 3.  */  
   "Rpt3BankTotalAmt":number,
      /**  Indicates that the promissory note is signed.  */  
   "Signed":boolean,
      /**  Total AP Amount  */  
   "TotalAPAmt":number,
      /**  Transaction date.  */  
   "TransDate":string,
      /**  Supplier Bank Account ID  */  
   "VendBankAcctID":string,
      /**  Supplier ID  */  
   "VendorID":string,
      /**  Supplier number  */  
   "VendorNum":number,
      /**  Voided Flag  */  
   "Voided":boolean,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   "GroupID":string,
      /**  AP Payment Instrument ID  */  
   "APPromNoteID":string,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  First company address line.  */  
   "CompanyAddr1":string,
      /**  Second company address line.  */  
   "CompanyAddr2":string,
      /**  Third company address line.  */  
   "CompanyAddr3":string,
      /**  Company City portion of the address.  */  
   "CompanyCity":string,
      /**  Company Country portion of the address.  */  
   "CompanyCountry":string,
      /**  Company Name  */  
   "CompanyName":string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   "CompanyPostalCode":string,
      /**  Company State portion of the address.  */  
   "CompanyState":string,
      /**  First supplier address line.  */  
   "SupplierAddr1":string,
      /**  Second supplier address line.  */  
   "SupplierAddr2":string,
      /**  Third supplier address line.  */  
   "SupplierAddr3":string,
      /**  Company City portion of the address.  */  
   "SupplierCity":string,
      /**  Supplier State portion of the address.  */  
   "SupplierState":string,
      /**  Supplier Postal Code or Zip Code portion of the address.  */  
   "SupplierPostalCode":string,
      /**  Supplier Name  */  
   "SupplierName":string,
      /**  Supplier Country portion of the address.  */  
   "SupplierCountry":string,
      /**   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  */  
   "PIStatus":string,
      /**  Promissory Note Type  */  
   "Type":string,
      /**  Issue Date  */  
   "IssueDate":string,
      /**  IBAN Code for company's bank.  */  
   "CompIBANCode":string,
      /**  Bank/Branch Code for company's bank.  */  
   "CompBankBranchCode":string,
      /**  Bank/Branch Code for customer's bank.  */  
   "CustBankBranchCode":string,
      /**  IBAN Code for customer's bank.  */  
   "CustIBANCode":string,
      /**  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  */  
   "ForceDiscount":boolean,
      /**  Total paid amount in Base  */  
   "PaymentTotal":number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   "Variance":number,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Enter Totals flag  */  
   "IsEnterTotal":boolean,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt1Variance":number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt2Variance":number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt3Variance":number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   "DocVariance":number,
      /**  Total paid amount in payment currency  */  
   "DocPaymentTotal":number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   "PaymentBankRate":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  Total paid amount in Rpt1 currency  */  
   "Rpt1PaymentTotal":number,
      /**  Total paid amount in Rpt2 currency  */  
   "Rpt2PaymentTotal":number,
      /**  Total paid amount in Rpt3 currency  */  
   "Rpt3PaymentTotal":number,
      /**  Amount that the bank cleared the payment instrument for.  */  
   "ClearedAmt":number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   "ClearedPerson":string,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPI":boolean,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   "CashbookLine":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Reference to the first checkhed  */  
   "FirstHeadNum":number,
      /**  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  */  
   "Manual":boolean,
      /**  Reason to change the Customer or Company information  */  
   "ChgComment":string,
      /**  Indicates APPRomNoteID was generated using AP CheckHed numbering  */  
   "PymtCntr":boolean,
      /**  Payment Instrument Stage  */  
   "PIStage":string,
      /**  Lock Exchange Rate  */  
   "LockRate":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankClearedAmt  */  
   "BankClearedAmt":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  SupplierCountryNum  */  
   "SupplierCountryNum":number,
      /**  Reference to Endorsed AR PI GroupID.  */  
   "EndorsedARPNGroupID":string,
      /**  Reference to Endorsed AR PI HeadNum.  */  
   "EndorsedARPNHeadNum":number,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Enable the Bank Account Search Button  */  
   "BankAccountEnabled":boolean,
      /**  Bank Currency Code  */  
   "BankCurrCode":string,
   "BankCurrSymbol":string,
   "BankFeeAmt":number,
   "BankRecGainLoss":number,
   "BaseCurrSymbol":string,
   "CompanyBankAcct":string,
   "CompanyBankIdentifier":string,
   "CompanyBankName":string,
      /**  Field to bring the Company Country Name  */  
   "CompanyCountryNum":number,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   "DisableBankAmt":boolean,
   "DocAllocAmt":number,
   "DocBankFeeAmt":number,
   "DocBankRecGainLoss":number,
   "DocDiscountAmt":number,
   "DocGainLossReal":number,
   "DocGainLossUnreal":number,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
   "EnterPaymentTotal":boolean,
   "FullyPaid":boolean,
   "GainLossReal":number,
   "GainLossUnreal":number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   "HasLegNumCnfg":boolean,
   "IsFiltered":boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "PaymentAmount":number,
   "PaymentStatus":string,
   "RevalDate":string,
   "Rpt1AllocAmt":number,
   "Rpt1BankFeeAmt":number,
   "Rpt1BankRecGainLoss":number,
   "Rpt1GainLossReal":number,
   "Rpt1GainLossUnreal":number,
   "Rpt2AllocAmt":number,
   "Rpt2BankFeeAmt":number,
   "Rpt2BankRecGainLoss":number,
   "Rpt2GainLossReal":number,
   "Rpt2GainLossUnreal":number,
   "Rpt3AllocAmt":number,
   "Rpt3BankFeeAmt":number,
   "Rpt3BankRecGainLoss":number,
   "Rpt3GainLossReal":number,
   "Rpt3GainLossUnreal":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "StatusChgLegalNum":string,
   "StatusChgTranDocType":string,
   "TotalRoundDiff":number,
   "TypeDesc":string,
   "VendBankAcct":string,
   "VendBankIdentifier":string,
   "VendBankName":string,
   "VoidDate":string,
   "XRateLabel":string,
   "XRateLabelPaymentBank":string,
   "XRateLabelPaymentBase":string,
   "AllocAmt":number,
      /**  Endorsed AR PI Status  */  
   "EndorsedARPNStatus":string,
      /**  Endorsed AR PI Status Change Transaction Document Type.  */  
   "EndorsedARPNStatusChgTranDocType":string,
      /**  Endorsed AR PI Status Change Legal Number.  */  
   "EndorsedARPNStatusChgLegalNum":string,
   "BitFlag":number,
   "BankAcctIDDescription":string,
   "BankAcctIDBankName":string,
   "BaseCurrSymbolCurrencyID":string,
   "BaseCurrSymbolCurrSymbol":string,
   "BaseCurrSymbolCurrDesc":string,
   "BaseCurrSymbolDocumentDesc":string,
   "BaseCurrSymbolCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrDesc":string,
   "PIStatusStatusDesc":string,
   "TranDocTypeDescription":string,
   "VendorNumAddress2":string,
   "VendorNumCity":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress3":string,
   "VendorNumVendorID":string,
   "VendorNumZIP":string,
   "VendorNumAddress1":string,
   "VendorNumCurrencyCode":string,
   "VendorNumName":string,
   "VendorNumCountry":string,
   "VendorNumTermsCode":string,
   "VendorNumState":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APPNHeadTGLCRow{
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
      /**  HeadNum of APNHead  */  
   "HeadNum":number,
   "IsFiltered":boolean,
      /**  GroupID for APPNHead  */  
   "GroupID":string,
   "BitFlag":number,
   "COADescription":string,
   "GLAccountGLShortAcct":string,
   "GLAccountAccountDesc":string,
   "GLAccountGLAcctDisp":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BankTranGLCRow{
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
   "GroupID":string,
   "HeadNum":number,
   "IsFiltered":boolean,
   "Voided":boolean,
      /**  Added to fix generation bug only. (for relation LRBankTranBankTranGLC)  */  
   "BankAcctID":string,
   "BitFlag":number,
   "COADescription":string,
   "GLAccountAccountDesc":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
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

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
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
      /**  Identifier of the GL Control Type.  */  
   "GLControlType":string,
      /**  GL Control Identifier.  */  
   "GLControlCode":string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   "BusinessEntity":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   "GlobalEntityGLC":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankAcctID of the related BankAcct record.  */  
   "BankAcctID":string,
   "BankFeeID":string,
      /**  CallCode of the related FSCallCd record.  */  
   "CallCode":string,
   "ChargeCode":string,
      /**  ClassCode of the related FAClass record.  */  
   "ClassCode":string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   "ClassID":string,
      /**  ContractCode of the related FSContCd record.  */  
   "ContractCode":string,
      /**  CurrencyCode of the related Currency record.  */  
   "CurrencyCode":string,
      /**  CustNum of the related Customer record  */  
   "CustNum":number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   "DeductionID":string,
      /**  EmpID of the related PREmpMas record.  */  
   "EmpID":string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   "ExpenseCode":string,
      /**  ExtSystemID of ExtCompany table  */  
   "ExtSystemID":string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   "FromPlant":string,
      /**  GroupCode of the related FAGroup record.  */  
   "GroupCode":string,
   "GroupID":string,
   "HeadNum":number,
   "InvoiceNum":string,
      /**  JCDept of the related JCDept record.  */  
   "JCDept":string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   "MiscCode":string,
      /**  PartNum of the related Part record.  */  
   "PartNum":string,
      /**  PayTypeID of PayType  */  
   "PayTypeID":string,
   "PerConName":string,
      /**  PI Status  */  
   "PIStatus":string,
      /**  Plant of the related PlantConfCtrl record.  */  
   "Plant":string,
      /**  ProdCode of the related ProdGrup record.  */  
   "ProdCode":string,
      /**  ProjectID of the related Project record.  */  
   "ProjectID":string,
      /**  PurchCode of the related GLPurch record.  */  
   "PurchCode":string,
      /**  RateCode of the related GLRate record.  */  
   "RateCode":string,
      /**  ReasonCode of the related Reason record.  */  
   "ReasonCode":string,
      /**  ReasonType of the related Reason record.  */  
   "ReasonType":string,
      /**  SalesCatID of the related SalesCat record.  */  
   "SalesCatID":string,
      /**  Shift value of the related JCShift record.  */  
   "Shift":number,
      /**  TaxCode of the related SalesTax record.  */  
   "TaxCode":string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   "TaxTblID":string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   "ToPlant":string,
      /**  TransferMethod of ExtCompany table  */  
   "TransferMethod":string,
      /**  Type ID  */  
   "TypeID":string,
      /**  VendorNum of the related Vendor record.  */  
   "VendorNum":number,
      /**  WarehouseCode of the related Warehse record.  */  
   "WarehouseCode":string,
   "ExpenseTypeCode":string,
   "IsFiltered":boolean,
   "OprTypeCode":string,
   "CashDeskID":string,
   "TIN":string,
   "ReclassCodeID":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
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

export interface Erp_Tablesets_PITotalsRow{
   "CashRcv":number,
   "DocCashRcv":number,
   "DocDscTaken":number,
   "DocGainReal":number,
   "DocGainUnreal":number,
   "DscTaken":number,
   "GainReal":number,
   "GainUnreal":number,
   "RevalDate":string,
   "Rpt1CashRcv":number,
   "Rpt1DscTaken":number,
   "Rpt1GainReal":number,
   "Rpt1GainUnreal":number,
   "Rpt2CashRcv":number,
   "Rpt2DscTaken":number,
   "Rpt2GainReal":number,
   "Rpt2GainUnreal":number,
   "Rpt3CashRcv":number,
   "Rpt3DscTaken":number,
   "Rpt3GainReal":number,
   "Rpt3GainUnreal":number,
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
      @param ipGroupID
      @param ds
   */  
export interface ApplyInvoiceToGroup_input{
      /**  AP Promissory Note  Group ID  */  
   ipGroupID:string,
   ds:Erp_Tablesets_APInvSelTableset[],
}

export interface ApplyInvoiceToGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvSelTableset,
}
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ipStatusChange
      @param ds
      @param dsAPPromNote
   */  
export interface AssignEndorsedARPILegalNumber_input{
      /**  AP Payment Instrument Group ID  */  
   ipGroupID:string,
      /**  AP Payment Instrument Head Number  */  
   ipHeadNum:number,
      /**  Call from AP Status Change  */  
   ipStatusChange:boolean,
   ds:Erp_Tablesets_LegalNumGenOptsTableset[],
   dsAPPromNote:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface AssignEndorsedARPILegalNumber_output{
   returnObj:Erp_Tablesets_APPromissoryNotesTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumGenOptsTableset,
   dsAPPromNote:Erp_Tablesets_APPromissoryNotesTableset,
   opLegalNumMsg:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ds
   */  
export interface AssignLegalNumber_input{
      /**  Group ID number  */  
   ipGroupID:string,
      /**  Header number  */  
   ipHeadNum:number,
   ds:Erp_Tablesets_LegalNumGenOptsTableset[],
}

export interface AssignLegalNumber_output{
   returnObj:Erp_Tablesets_APPromissoryNotesTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumGenOptsTableset,
   opLegalNumMsg:string,
}
}

   /** Required : 
      @param groupId
      @param headNum
      @param unpostedSeqNum
   */  
export interface CancelStatusChange_input{
      /**  Group ID  */  
   groupId:string,
      /**  HeadNum  */  
   headNum:number,
      /**  unpostedSeqNum  */  
   unpostedSeqNum:number,
}

export interface CancelStatusChange_output{
}

   /** Required : 
      @param ds
   */  
export interface ChangePIType_input{
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface ChangePIType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
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
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface ChangeTranAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
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
      @param pcGroupID
      @param ds
   */  
export interface CreateAPPNHead_input{
      /**  AP Promissory Note  Group ID  */  
   pcGroupID:string,
   ds:Erp_Tablesets_APInvSelTableset[],
}

export interface CreateAPPNHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvSelTableset,
}
}

   /** Required : 
      @param groupID
      @param endorsedARPNGroupID
      @param endorsedARPNHeadNum
      @param ds
   */  
export interface CreateNewAPPNHeadEndorsement_input{
      /**  AP Promissory Note Group ID  */  
   groupID:string,
      /**  Endorsed AR Promissory Note Group ID  */  
   endorsedARPNGroupID:string,
      /**  Endorsed AR Promissory Note HeadNum  */  
   endorsedARPNHeadNum:number,
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface CreateNewAPPNHeadEndorsement_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param pcGroupID
      @param ds
   */  
export interface CreateNewAPPNHead_input{
      /**  AP Promissory Note Group ID  */  
   pcGroupID:string,
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface CreateNewAPPNHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param groupId
      @param headNum
      @param seqNum
   */  
export interface DeleteAPPNMove_input{
      /**  Group ID  */  
   groupId:string,
      /**  HeadNum  */  
   headNum:number,
      /**  Seq  */  
   seqNum:number,
}

export interface DeleteAPPNMove_output{
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
      @param pcGroupID
   */  
export interface DeleteNegPayment_input{
      /**  AP Check Group ID  */  
   pcGroupID:string,
}

export interface DeleteNegPayment_output{
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

export interface Erp_Tablesets_APPNDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Line  */  
   APPNDtlLine:number,
      /**  Bank Account ID of the promissoiry note.  */  
   BankAcctID:string,
      /**  Discount Amount in base currency.  */  
   DiscAmt:number,
      /**  Discount Amount in invoice currency.  */  
   DocDiscAmt:number,
      /**  Tax amount in invoice currency.  */  
   DocTaxAmt:number,
      /**  Transaction amount in invoice currency.  */  
   DocTranAmt:number,
      /**  Entry Person  */  
   EntryPerson:string,
      /**  Indicates that the promissory note is posted to the GL.  */  
   GLPosted:boolean,
      /**  AP Invoice Number linked to the promissory note.  */  
   InvoiceNum:string,
      /**  Rounding Differences  */  
   RoundDiff:number,
      /**  Discount Amount in report currency 1.  */  
   Rpt1DiscAmt:number,
      /**  Tax amount  in report currency 1.  */  
   Rpt1TaxAmt:number,
      /**  Transaction amount  in report currency 1.  */  
   Rpt1TranAmt:number,
      /**  Discount Amount in report currency 2.  */  
   Rpt2DiscAmt:number,
      /**  Tax amount  in report currency 2.  */  
   Rpt2TaxAmt:number,
      /**  Transaction amount  in report currency 2.  */  
   Rpt2TranAmt:number,
      /**  Discount Amount in report currency 3.  */  
   Rpt3DiscAmt:number,
      /**  Tax amount  in report currency 3.  */  
   Rpt3TaxAmt:number,
      /**  Transaction amount  in report currency 3.  */  
   Rpt3TranAmt:number,
      /**  Tax amount in base currency.  */  
   TaxAmt:number,
      /**  Tax Liability  */  
   TaxRegionCode:string,
      /**  Transaction Amount in base currency.  */  
   TranAmt:number,
      /**  Transaction date.  */  
   TranDate:string,
      /**  Supplier  */  
   VendorNum:number,
      /**  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  */  
   HeadNum:number,
      /**  Indicates if the promissory node is voided.  */  
   Voided:boolean,
      /**  Group ID  */  
   GroupID:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  */  
   FiscalPeriod:number,
      /**   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  */  
   FiscalYear:number,
      /**   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  */  
   FiscalYearSuffix:string,
      /**  The Legal Number for the record.  */  
   LegalNumber:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  */  
   Posted:boolean,
      /**  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  */  
   Description:string,
      /**  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  */  
   TranType:string,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Link To first checkhed record  */  
   FirstHeadNum:number,
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
      /**  AdjustmentSeq  */  
   AdjustmentSeq:number,
   AmtToAP:number,
   ApplyDate:string,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
   BaseCurrSymbolCurrDesc:string,
   BaseCurrSymbolCurrName:string,
   BaseCurrSymbolCurrSymbol:string,
   BaseCurrSymbolDocumentDesc:string,
   BaseSelfAssessedTax:number,
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
      /**  The display gl account.  */  
   DispGLAcct:string,
   DispTranAmt:number,
   DocBaseSelfAssessedTax:number,
   DocDispTranAmt:number,
   DocExpenseAmount:number,
   DocInvoiceAmt:number,
   DocInvoiceBal:number,
   DocNetAmount:number,
   DocNewBalance:number,
   DocUnPostedBal:number,
   DueDate:string,
   ExchangeRate:number,
   ExpenseAmount:number,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   FullyPaid:boolean,
      /**  This is the source Company of the Central Payment linked invoice  */  
   GlbCompany:string,
   InvoiceAmt:number,
   InvoiceBal:number,
   InvoiceDate:string,
   LockRate:boolean,
   NetAmount:number,
   NewBalance:number,
      /**  Indicates if posting GL transactions.  */  
   PostToGL:boolean,
   TermsCode:string,
   TermsCodeDescription:string,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign.  */  
   UnPostedBal:number,
   WithHoldTax:number,
   DiscountDate:string,
      /**  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  */  
   ChangeExchangeRateResponse:string,
   DocSelfAssessedTax:number,
   DocWithHoldTax:number,
   SelfAssessedTax:number,
   IsFiltered:boolean,
   APPromNoteID:string,
   PIStatus:string,
   PIStatusStatusDesc:string,
   BitFlag:number,
   BankAcctIDBankName:string,
   BankAcctIDDescription:string,
   InvoiceNumDescription:string,
   TaxRegionCodeDescription:string,
   VendorNumZIP:string,
   VendorNumCity:string,
   VendorNumCurrencyCode:string,
   VendorNumVendorID:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress2:string,
   VendorNumTermsCode:string,
   VendorNumState:string,
   VendorNumAddress1:string,
   VendorNumName:string,
   VendorNumAddress3:string,
   VendorNumCountry:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APPNHeadAttchRow{
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

export interface Erp_Tablesets_APPNHeadListRow{
      /**  Applied Amount. Base Currency.  */  
   AppliedAmount:number,
      /**  Bank Account of the promissory note.  */  
   BankAcctID:string,
      /**  Bank Amount  */  
   BankAmount:number,
      /**  Bank Slip Number of the promissory note.  */  
   BankSlip:string,
      /**  Bank Total Amount.  */  
   BankTotalAmt:number,
      /**  Cash book Number.  */  
   CashBookNum:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Bank Account ID of the company.  */  
   CompBankAcctID:string,
      /**  Currency code of the promissory note.  */  
   CurrencyCode:string,
      /**  Description  */  
   Description:string,
      /**  Discount amount in base currency.  */  
   DiscountAmt:number,
      /**  Promissory Note amount in document currency.  */  
   DocPNAmt:number,
      /**  Due date of the promissory note.  */  
   DueDate:string,
      /**  Entry Person.  */  
   EntryPerson:string,
      /**  Exchange Rate of the promissory note.  */  
   ExchangeRate:number,
      /**  Indicates if the promissory node is fully paid.  */  
   Paid:boolean,
      /**  Promissory note amount in base currency.  */  
   PNAmt:number,
      /**  Indicates that the promissory note is posted.  */  
   Posted:boolean,
      /**  Rate Group Code.  */  
   RateGrpCode:string,
      /**  Promissory Note Amount in Report Currency 1.  */  
   Rpt1PNAmt:number,
      /**  Promissory Note Discount Amount in Report Currency 1.  */  
   Rpt1Discountamt:number,
      /**  Promissory Note Bank Total Amount in Report Currency 1.  */  
   Rpt1BankTotalAmt:number,
      /**  Promissory Note Amount in Report Currency 2.  */  
   Rpt2PNAmt:number,
      /**  Promissory Note Discount Amount in Report Currency 2.  */  
   Rpt2DiscountAmt:number,
      /**  Promissory Note Bank Total Amount in Report Currency 2.  */  
   Rpt2BankTotalAmt:number,
      /**  Promissory Note Amount in Report Currency 3.  */  
   Rpt3PNAmt:number,
      /**  Promissory Note Discount Amount in Report Currency 3.  */  
   Rpt3DiscountAmt:number,
      /**  Promissory Note Bank Total Amount in Report Currency 3.  */  
   Rpt3BankTotalAmt:number,
      /**  Indicates that the promissory note is signed.  */  
   Signed:boolean,
      /**  Total AP Amount  */  
   TotalAPAmt:number,
      /**  Transaction date.  */  
   TransDate:string,
      /**  Supplier Bank Account ID  */  
   VendBankAcctID:string,
      /**  Supplier ID  */  
   VendorID:string,
      /**  Supplier number  */  
   VendorNum:number,
      /**  Voided Flag  */  
   Voided:boolean,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  AP Payment Instrument ID  */  
   APPromNoteID:string,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   FiscalYear:number,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  First company address line.  */  
   CompanyAddr1:string,
      /**  Second company address line.  */  
   CompanyAddr2:string,
      /**  Third company address line.  */  
   CompanyAddr3:string,
      /**  Company City portion of the address.  */  
   CompanyCity:string,
      /**  Company Country portion of the address.  */  
   CompanyCountry:string,
      /**  Company Name  */  
   CompanyName:string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   CompanyPostalCode:string,
      /**  Company State portion of the address.  */  
   CompanyState:string,
      /**  First supplier address line.  */  
   SupplierAddr1:string,
      /**  Second supplier address line.  */  
   SupplierAddr2:string,
      /**  Third supplier address line.  */  
   SupplierAddr3:string,
      /**  Company City portion of the address.  */  
   SupplierCity:string,
      /**  Supplier State portion of the address.  */  
   SupplierState:string,
      /**  Supplier Postal Code or Zip Code portion of the address.  */  
   SupplierPostalCode:string,
      /**  Supplier Name  */  
   SupplierName:string,
      /**  Supplier Country portion of the address.  */  
   SupplierCountry:string,
      /**   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  */  
   PIStatus:string,
      /**  Promissory Note Type  */  
   Type:string,
      /**  Issue Date  */  
   IssueDate:string,
      /**  IBAN Code for company's bank.  */  
   CompIBANCode:string,
      /**  Bank/Branch Code for company's bank.  */  
   CompBankBranchCode:string,
      /**  Bank/Branch Code for customer's bank.  */  
   CustBankBranchCode:string,
      /**  IBAN Code for customer's bank.  */  
   CustIBANCode:string,
      /**  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  */  
   ForceDiscount:boolean,
      /**  Total paid amount in Base  */  
   PaymentTotal:number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   Variance:number,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Enter Totals flag  */  
   IsEnterTotal:boolean,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt1Variance:number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt2Variance:number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt3Variance:number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   DocVariance:number,
      /**  Total paid amount in payment currency  */  
   DocPaymentTotal:number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   PaymentBankRate:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  Total paid amount in Rpt1 currency  */  
   Rpt1PaymentTotal:number,
      /**  Total paid amount in Rpt2 currency  */  
   Rpt2PaymentTotal:number,
      /**  Total paid amount in Rpt3 currency  */  
   Rpt3PaymentTotal:number,
      /**  Amount that the bank cleared the payment instrument for.  */  
   ClearedAmt:number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   ClearedPerson:string,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPI:boolean,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   CashbookLine:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Reference to the first checkhed  */  
   FirstHeadNum:number,
      /**  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  */  
   Manual:boolean,
      /**  Reason to change the Customer or Company information  */  
   ChgComment:string,
      /**  Indicates APPRomNoteID was generated using AP CheckHed numbering  */  
   PymtCntr:boolean,
      /**  Payment Instrument Stage  */  
   PIStage:string,
      /**  Lock Exchange Rate  */  
   LockRate:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  SupplierCountryNum  */  
   SupplierCountryNum:number,
      /**  Enable the Bank Account Search Button  */  
   BankAccountEnabled:boolean,
      /**  Bank Currency Code  */  
   BankCurrCode:string,
   BankCurrSymbol:string,
   BaseCurrSymbol:string,
   PaymentAmount:number,
   PaymentStatus:string,
   CompanyBankAcct:string,
   CompanyBankIdentifier:string,
   CompanyBankName:string,
   VendBankName:string,
   VendBankAcct:string,
   VendBankIdentifier:string,
   XRateLabel:string,
   EnterPaymentTotal:boolean,
   FullyPaid:boolean,
   TotalRoundDiff:number,
   XRateLabelPaymentBank:string,
   XRateLabelPaymentBase:string,
   VoidDate:string,
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
      /**  Field to bring the Company Country Name  */  
   CompanyCountryNum:number,
   TypeDesc:string,
   IsFiltered:boolean,
   GainLossReal:number,
   DocGainLossReal:number,
   Rpt1GainLossReal:number,
   Rpt2GainLossReal:number,
   Rpt3GainLossReal:number,
   DocGainLossUnreal:number,
   GainLossUnreal:number,
   Rpt1GainLossUnreal:number,
   Rpt2GainLossUnreal:number,
   Rpt3GainLossUnreal:number,
   RevalDate:string,
   DocDiscountAmt:number,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Full description of the bank account.  */  
   BankAcctIDDescription:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseCurrSymbolDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrSymbolCurrName:string,
      /**  Description of the currency  */  
   BaseCurrSymbolCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrSymbolCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrSymbolCurrencyID:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  Status Description  */  
   PIStatusStatusDesc:string,
      /**  Description  */  
   TranDocTypeDescription:string,
      /**  Supplier Bank Name  */  
   VendBankAcctIDBankName:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
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
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APPNHeadListTableset{
   APPNHeadList:Erp_Tablesets_APPNHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APPNHeadRow{
      /**  Applied Amount. Base Currency.  */  
   AppliedAmount:number,
      /**  Bank Account of the promissory note.  */  
   BankAcctID:string,
      /**  Bank Amount  */  
   BankAmount:number,
      /**  Bank Slip Number of the promissory note.  */  
   BankSlip:string,
      /**  Bank Total Amount.  */  
   BankTotalAmt:number,
      /**  Cash book Number.  */  
   CashBookNum:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Bank Account ID of the company.  */  
   CompBankAcctID:string,
      /**  Currency code of the promissory note.  */  
   CurrencyCode:string,
      /**  Description  */  
   Description:string,
      /**  Discount amount in base currency.  */  
   DiscountAmt:number,
      /**  Promissory Note amount in document currency.  */  
   DocPNAmt:number,
      /**  Due date of the promissory note.  */  
   DueDate:string,
      /**  Entry Person.  */  
   EntryPerson:string,
      /**  Exchange Rate of the promissory note.  */  
   ExchangeRate:number,
      /**  Indicates if the promissory node is fully paid.  */  
   Paid:boolean,
      /**  Promissory note amount in base currency.  */  
   PNAmt:number,
      /**  Indicates that the promissory note is posted.  */  
   Posted:boolean,
      /**  Rate Group Code.  */  
   RateGrpCode:string,
      /**  Promissory Note Amount in Report Currency 1.  */  
   Rpt1PNAmt:number,
      /**  Promissory Note Discount Amount in Report Currency 1.  */  
   Rpt1Discountamt:number,
      /**  Promissory Note Bank Total Amount in Report Currency 1.  */  
   Rpt1BankTotalAmt:number,
      /**  Promissory Note Amount in Report Currency 2.  */  
   Rpt2PNAmt:number,
      /**  Promissory Note Discount Amount in Report Currency 2.  */  
   Rpt2DiscountAmt:number,
      /**  Promissory Note Bank Total Amount in Report Currency 2.  */  
   Rpt2BankTotalAmt:number,
      /**  Promissory Note Amount in Report Currency 3.  */  
   Rpt3PNAmt:number,
      /**  Promissory Note Discount Amount in Report Currency 3.  */  
   Rpt3DiscountAmt:number,
      /**  Promissory Note Bank Total Amount in Report Currency 3.  */  
   Rpt3BankTotalAmt:number,
      /**  Indicates that the promissory note is signed.  */  
   Signed:boolean,
      /**  Total AP Amount  */  
   TotalAPAmt:number,
      /**  Transaction date.  */  
   TransDate:string,
      /**  Supplier Bank Account ID  */  
   VendBankAcctID:string,
      /**  Supplier ID  */  
   VendorID:string,
      /**  Supplier number  */  
   VendorNum:number,
      /**  Voided Flag  */  
   Voided:boolean,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  AP Payment Instrument ID  */  
   APPromNoteID:string,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   FiscalYear:number,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  First company address line.  */  
   CompanyAddr1:string,
      /**  Second company address line.  */  
   CompanyAddr2:string,
      /**  Third company address line.  */  
   CompanyAddr3:string,
      /**  Company City portion of the address.  */  
   CompanyCity:string,
      /**  Company Country portion of the address.  */  
   CompanyCountry:string,
      /**  Company Name  */  
   CompanyName:string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   CompanyPostalCode:string,
      /**  Company State portion of the address.  */  
   CompanyState:string,
      /**  First supplier address line.  */  
   SupplierAddr1:string,
      /**  Second supplier address line.  */  
   SupplierAddr2:string,
      /**  Third supplier address line.  */  
   SupplierAddr3:string,
      /**  Company City portion of the address.  */  
   SupplierCity:string,
      /**  Supplier State portion of the address.  */  
   SupplierState:string,
      /**  Supplier Postal Code or Zip Code portion of the address.  */  
   SupplierPostalCode:string,
      /**  Supplier Name  */  
   SupplierName:string,
      /**  Supplier Country portion of the address.  */  
   SupplierCountry:string,
      /**   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  */  
   PIStatus:string,
      /**  Promissory Note Type  */  
   Type:string,
      /**  Issue Date  */  
   IssueDate:string,
      /**  IBAN Code for company's bank.  */  
   CompIBANCode:string,
      /**  Bank/Branch Code for company's bank.  */  
   CompBankBranchCode:string,
      /**  Bank/Branch Code for customer's bank.  */  
   CustBankBranchCode:string,
      /**  IBAN Code for customer's bank.  */  
   CustIBANCode:string,
      /**  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  */  
   ForceDiscount:boolean,
      /**  Total paid amount in Base  */  
   PaymentTotal:number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   Variance:number,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Enter Totals flag  */  
   IsEnterTotal:boolean,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt1Variance:number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt2Variance:number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt3Variance:number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   DocVariance:number,
      /**  Total paid amount in payment currency  */  
   DocPaymentTotal:number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   PaymentBankRate:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  Total paid amount in Rpt1 currency  */  
   Rpt1PaymentTotal:number,
      /**  Total paid amount in Rpt2 currency  */  
   Rpt2PaymentTotal:number,
      /**  Total paid amount in Rpt3 currency  */  
   Rpt3PaymentTotal:number,
      /**  Amount that the bank cleared the payment instrument for.  */  
   ClearedAmt:number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   ClearedPerson:string,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPI:boolean,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   CashbookLine:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Reference to the first checkhed  */  
   FirstHeadNum:number,
      /**  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  */  
   Manual:boolean,
      /**  Reason to change the Customer or Company information  */  
   ChgComment:string,
      /**  Indicates APPRomNoteID was generated using AP CheckHed numbering  */  
   PymtCntr:boolean,
      /**  Payment Instrument Stage  */  
   PIStage:string,
      /**  Lock Exchange Rate  */  
   LockRate:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  SupplierCountryNum  */  
   SupplierCountryNum:number,
      /**  Reference to Endorsed AR PI GroupID.  */  
   EndorsedARPNGroupID:string,
      /**  Reference to Endorsed AR PI HeadNum.  */  
   EndorsedARPNHeadNum:number,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Enable the Bank Account Search Button  */  
   BankAccountEnabled:boolean,
      /**  Bank Currency Code  */  
   BankCurrCode:string,
   BankCurrSymbol:string,
   BankFeeAmt:number,
   BankRecGainLoss:number,
   BaseCurrSymbol:string,
   CompanyBankAcct:string,
   CompanyBankIdentifier:string,
   CompanyBankName:string,
      /**  Field to bring the Company Country Name  */  
   CompanyCountryNum:number,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   DisableBankAmt:boolean,
   DocAllocAmt:number,
   DocBankFeeAmt:number,
   DocBankRecGainLoss:number,
   DocDiscountAmt:number,
   DocGainLossReal:number,
   DocGainLossUnreal:number,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
   EnterPaymentTotal:boolean,
   FullyPaid:boolean,
   GainLossReal:number,
   GainLossUnreal:number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   HasLegNumCnfg:boolean,
   IsFiltered:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   PaymentAmount:number,
   PaymentStatus:string,
   RevalDate:string,
   Rpt1AllocAmt:number,
   Rpt1BankFeeAmt:number,
   Rpt1BankRecGainLoss:number,
   Rpt1GainLossReal:number,
   Rpt1GainLossUnreal:number,
   Rpt2AllocAmt:number,
   Rpt2BankFeeAmt:number,
   Rpt2BankRecGainLoss:number,
   Rpt2GainLossReal:number,
   Rpt2GainLossUnreal:number,
   Rpt3AllocAmt:number,
   Rpt3BankFeeAmt:number,
   Rpt3BankRecGainLoss:number,
   Rpt3GainLossReal:number,
   Rpt3GainLossUnreal:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   StatusChgLegalNum:string,
   StatusChgTranDocType:string,
   TotalRoundDiff:number,
   TypeDesc:string,
   VendBankAcct:string,
   VendBankIdentifier:string,
   VendBankName:string,
   VoidDate:string,
   XRateLabel:string,
   XRateLabelPaymentBank:string,
   XRateLabelPaymentBase:string,
   AllocAmt:number,
      /**  Endorsed AR PI Status  */  
   EndorsedARPNStatus:string,
      /**  Endorsed AR PI Status Change Transaction Document Type.  */  
   EndorsedARPNStatusChgTranDocType:string,
      /**  Endorsed AR PI Status Change Legal Number.  */  
   EndorsedARPNStatusChgLegalNum:string,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   BaseCurrSymbolCurrencyID:string,
   BaseCurrSymbolCurrSymbol:string,
   BaseCurrSymbolCurrDesc:string,
   BaseCurrSymbolDocumentDesc:string,
   BaseCurrSymbolCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrDesc:string,
   PIStatusStatusDesc:string,
   TranDocTypeDescription:string,
   VendorNumAddress2:string,
   VendorNumCity:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress3:string,
   VendorNumVendorID:string,
   VendorNumZIP:string,
   VendorNumAddress1:string,
   VendorNumCurrencyCode:string,
   VendorNumName:string,
   VendorNumCountry:string,
   VendorNumTermsCode:string,
   VendorNumState:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APPNHeadTGLCRow{
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
      /**  HeadNum of APNHead  */  
   HeadNum:number,
   IsFiltered:boolean,
      /**  GroupID for APPNHead  */  
   GroupID:string,
   BitFlag:number,
   COADescription:string,
   GLAccountGLShortAcct:string,
   GLAccountAccountDesc:string,
   GLAccountGLAcctDisp:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APPNMoveRow{
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
      /**  Transaction date.  */  
   TranDate:string,
      /**  Creation Time  */  
   CreateTime:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Description  */  
   Description:string,
   LegalNumMessage:string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   LegalNumStyle:string,
      /**  Posting Error Message  */  
   PostErrMess:string,
      /**  Indicates if posting GL transactions.  */  
   PostToGL:boolean,
   StatusDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APPNMoveTableset{
   APPNMove:Erp_Tablesets_APPNMoveRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APPromissoryNotesTableset{
   APPNHead:Erp_Tablesets_APPNHeadRow[],
   APPNHeadAttch:Erp_Tablesets_APPNHeadAttchRow[],
   APPNDtl:Erp_Tablesets_APPNDtlRow[],
   BankTran:Erp_Tablesets_BankTranRow[],
   BankTranGLC:Erp_Tablesets_BankTranGLCRow[],
   APPNHeadTGLC:Erp_Tablesets_APPNHeadTGLCRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   PITotals:Erp_Tablesets_PITotalsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BankTranGLCRow{
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
   GroupID:string,
   HeadNum:number,
   IsFiltered:boolean,
   Voided:boolean,
      /**  Added to fix generation bug only. (for relation LRBankTranBankTranGLC)  */  
   BankAcctID:string,
   BitFlag:number,
   COADescription:string,
   GLAccountAccountDesc:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
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

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
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
      /**  Identifier of the GL Control Type.  */  
   GLControlType:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   BusinessEntity:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   GlobalEntityGLC:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankAcctID of the related BankAcct record.  */  
   BankAcctID:string,
   BankFeeID:string,
      /**  CallCode of the related FSCallCd record.  */  
   CallCode:string,
   ChargeCode:string,
      /**  ClassCode of the related FAClass record.  */  
   ClassCode:string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   ClassID:string,
      /**  ContractCode of the related FSContCd record.  */  
   ContractCode:string,
      /**  CurrencyCode of the related Currency record.  */  
   CurrencyCode:string,
      /**  CustNum of the related Customer record  */  
   CustNum:number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   DeductionID:string,
      /**  EmpID of the related PREmpMas record.  */  
   EmpID:string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   ExpenseCode:string,
      /**  ExtSystemID of ExtCompany table  */  
   ExtSystemID:string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   FromPlant:string,
      /**  GroupCode of the related FAGroup record.  */  
   GroupCode:string,
   GroupID:string,
   HeadNum:number,
   InvoiceNum:string,
      /**  JCDept of the related JCDept record.  */  
   JCDept:string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   MiscCode:string,
      /**  PartNum of the related Part record.  */  
   PartNum:string,
      /**  PayTypeID of PayType  */  
   PayTypeID:string,
   PerConName:string,
      /**  PI Status  */  
   PIStatus:string,
      /**  Plant of the related PlantConfCtrl record.  */  
   Plant:string,
      /**  ProdCode of the related ProdGrup record.  */  
   ProdCode:string,
      /**  ProjectID of the related Project record.  */  
   ProjectID:string,
      /**  PurchCode of the related GLPurch record.  */  
   PurchCode:string,
      /**  RateCode of the related GLRate record.  */  
   RateCode:string,
      /**  ReasonCode of the related Reason record.  */  
   ReasonCode:string,
      /**  ReasonType of the related Reason record.  */  
   ReasonType:string,
      /**  SalesCatID of the related SalesCat record.  */  
   SalesCatID:string,
      /**  Shift value of the related JCShift record.  */  
   Shift:number,
      /**  TaxCode of the related SalesTax record.  */  
   TaxCode:string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   TaxTblID:string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   ToPlant:string,
      /**  TransferMethod of ExtCompany table  */  
   TransferMethod:string,
      /**  Type ID  */  
   TypeID:string,
      /**  VendorNum of the related Vendor record.  */  
   VendorNum:number,
      /**  WarehouseCode of the related Warehse record.  */  
   WarehouseCode:string,
   ExpenseTypeCode:string,
   IsFiltered:boolean,
   OprTypeCode:string,
   CashDeskID:string,
   TIN:string,
   ReclassCodeID:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnlDtlMovTableset{
   GLJrnlDtl:Erp_Tablesets_GLJrnlDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLJrnlDtlRow{
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
   StatAmount:number,
   BookCurrencyCode:string,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   ExtRefCodeRefCodeDesc:string,
   GLAccountGLAcctDisp:string,
   GLAccountGLShortAcct:string,
   GLAccountAccountDesc:string,
   GLRefCodeDescRefCodeDesc:string,
   JournalCodeJrnlDescription:string,
   SrcGLAccountGLShortAcct:string,
   SrcGLAccountGLAcctDisp:string,
   SrcGLAccountAccountDesc:string,
   StatUOMStatUOMDesc:string,
   VendorNumCountry:string,
   VendorNumCurrencyCode:string,
   VendorNumDefaultFOB:string,
   VendorNumState:string,
   VendorNumCity:string,
   VendorNumAddress3:string,
   VendorNumAddress1:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorNumVendorID:string,
   VendorNumName:string,
   VendorNumAddress2:string,
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

export interface Erp_Tablesets_LegalNumGenOptsTableset{
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

export interface Erp_Tablesets_UpdExtAPPromissoryNotesTableset{
   APPNHead:Erp_Tablesets_APPNHeadRow[],
   APPNHeadAttch:Erp_Tablesets_APPNHeadAttchRow[],
   APPNDtl:Erp_Tablesets_APPNDtlRow[],
   BankTran:Erp_Tablesets_BankTranRow[],
   BankTranGLC:Erp_Tablesets_BankTranGLCRow[],
   APPNHeadTGLC:Erp_Tablesets_APPNHeadTGLCRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   PITotals:Erp_Tablesets_PITotalsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface GenerateAPPNDtl_input{
      /**  Cash Group ID  */  
   groupID:string,
      /**  Promissory Note HeadNum  */  
   headNum:number,
}

export interface GenerateAPPNDtl_output{
   returnObj:Erp_Tablesets_APPromissoryNotesTableset[],
}

   /** Required : 
      @param iGroupID
      @param iHeadNum
   */  
export interface GetAPPNMove_input{
      /**  The Group Number  */  
   iGroupID:string,
      /**  The Header Number  */  
   iHeadNum:number,
}

export interface GetAPPNMove_output{
   returnObj:Erp_Tablesets_APPNMoveTableset[],
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   listAvailTranDocTypes:string,
}
}

   /** Required : 
      @param bankAcctID
      @param ds
   */  
export interface GetBankAcctInfo_input{
      /**  Proposed BankAcctID  */  
   bankAcctID:string,
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface GetBankAcctInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
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
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface GetBankFeeDefaultAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
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
   returnObj:Erp_Tablesets_APPromissoryNotesTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_APPromissoryNotesTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_APPromissoryNotesTableset[],
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
      @param ipHeadNum
      @param ds
   */  
export interface GetData4ARPITracker_input{
      /**  Group ID  */  
   ipGroupID:string,
      /**  Head Num  */  
   ipHeadNum:number,
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface GetData4ARPITracker_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

export interface GetDefaultMoveTranDocType_output{
      /**  Default TranDocType  */  
   returnObj:string,
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param tranDocTypeId
      @param ipGenOnSave
      @param ipStatusChange
   */  
export interface GetEndorsedARPILegalNumGenOpts_input{
      /**  AP Payment Instrument Group ID  */  
   ipGroupID:string,
      /**  AP Payment Instrument Head Number  */  
   ipHeadNum:number,
      /**  Transaction document type ID  */  
   tranDocTypeId:string,
      /**  Generate Legal Number on Save  */  
   ipGenOnSave:boolean,
      /**  Call from AP Status Change  */  
   ipStatusChange:boolean,
}

export interface GetEndorsedARPILegalNumGenOpts_output{
   returnObj:Erp_Tablesets_LegalNumGenOptsTableset[],
parameters : {
      /**  output parameters  */  
   opPromptForNum:boolean,
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
   returnObj:Erp_Tablesets_GLJrnlDtlMovTableset[],
}

   /** Required : 
      @param apPromNoteID
   */  
export interface GetGroupIDForPI_input{
      /**  AR Promissory Note ID  */  
   apPromNoteID:string,
}

export interface GetGroupIDForPI_output{
parameters : {
      /**  output parameters  */  
   groupID:string,
   headNum:number,
}
}

   /** Required : 
      @param apPromNoteID
   */  
export interface GetGroupIDForPNI_input{
   apPromNoteID:string,
}

export interface GetGroupIDForPNI_output{
   returnObj:Erp_Tablesets_APPromissoryNotesTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param tranDocTypeId
      @param ipStatusChange
   */  
export interface GetLegalNumGenOpts_input{
      /**  Group ID number  */  
   ipGroupID:string,
      /**  Header number  */  
   ipHeadNum:number,
      /**  Transaction document type Id  */  
   tranDocTypeId:string,
      /**  Status Change  */  
   ipStatusChange:boolean,
}

export interface GetLegalNumGenOpts_output{
   returnObj:Erp_Tablesets_LegalNumGenOptsTableset[],
parameters : {
      /**  output parameters  */  
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
   returnObj:Erp_Tablesets_APPNHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
      @param invoiceNum
   */  
export interface GetNewAPPNDtl_input{
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
   groupID:string,
   headNum:number,
   invoiceNum:string,
}

export interface GetNewAPPNDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
   */  
export interface GetNewAPPNHeadAttch_input{
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
   groupID:string,
   headNum:number,
}

export interface GetNewAPPNHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param pcGroupID
      @param APPromissoryNotesTableset
   */  
export interface GetNewAPPNHeadByGroupID_input{
   pcGroupID:string,
   APPromissoryNotesTableset:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface GetNewAPPNHeadByGroupID_output{
parameters : {
      /**  output parameters  */  
   APPromissoryNotesTableset:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
   */  
export interface GetNewAPPNHeadTGLC_input{
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
   groupID:string,
   headNum:number,
}

export interface GetNewAPPNHeadTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewAPPNHead_input{
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
   groupID:string,
}

export interface GetNewAPPNHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
   */  
export interface GetNewAPPNMoveByAPPNHead_input{
   ipGroupID:string,
   ipHeadNum:number,
}

export interface GetNewAPPNMoveByAPPNHead_output{
   returnObj:Erp_Tablesets_APPNMoveTableset[],
}

   /** Required : 
      @param lvHeadNum
      @param lvBankAcctID
      @param APPromissoryNotesTableset
   */  
export interface GetNewBankTranByHeadNum_input{
   lvHeadNum:number,
   lvBankAcctID:string,
   APPromissoryNotesTableset:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface GetNewBankTranByHeadNum_output{
parameters : {
      /**  output parameters  */  
   APPromissoryNotesTableset:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param tranNum
      @param voided
   */  
export interface GetNewBankTranGLC_input{
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
   bankAcctID:string,
   tranNum:number,
   voided:boolean,
}

export interface GetNewBankTranGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param tranNum
   */  
export interface GetNewBankTran_input{
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
   bankAcctID:string,
   tranNum:number,
}

export interface GetNewBankTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
   */  
export interface GetNewEntityGLC_input{
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewEntityGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param ipPIStatus
   */  
export interface GetPostCodeByPIStatus_input{
      /**  ipPIStatus  */  
   ipPIStatus:string,
}

export interface GetPostCodeByPIStatus_output{
parameters : {
      /**  output parameters  */  
   opPostCode:string,
}
}

   /** Required : 
      @param groupID
   */  
export interface GetRestartAPPNPrinting_input{
      /**  GroupID  */  
   groupID:string,
}

export interface GetRestartAPPNPrinting_output{
parameters : {
      /**  output parameters  */  
   restartAPPNPrinting:boolean,
}
}

   /** Required : 
      @param whereClauseAPPNHead
      @param whereClauseAPPNHeadAttch
      @param whereClauseAPPNDtl
      @param whereClauseBankTran
      @param whereClauseBankTranGLC
      @param whereClauseAPPNHeadTGLC
      @param whereClauseEntityGLC
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsTracker_input{
   whereClauseAPPNHead:string,
   whereClauseAPPNHeadAttch:string,
   whereClauseAPPNDtl:string,
   whereClauseBankTran:string,
   whereClauseBankTranGLC:string,
   whereClauseAPPNHeadTGLC:string,
   whereClauseEntityGLC:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsTracker_output{
   returnObj:Erp_Tablesets_APPromissoryNotesTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseAPPNHead
      @param whereClauseAPPNHeadAttch
      @param whereClauseAPPNDtl
      @param whereClauseBankTran
      @param whereClauseBankTranGLC
      @param whereClauseAPPNHeadTGLC
      @param whereClauseEntityGLC
      @param whereClauseLegalNumGenOpts
      @param whereClausePITotals
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAPPNHead:string,
   whereClauseAPPNHeadAttch:string,
   whereClauseAPPNDtl:string,
   whereClauseBankTran:string,
   whereClauseBankTranGLC:string,
   whereClauseAPPNHeadTGLC:string,
   whereClauseEntityGLC:string,
   whereClauseLegalNumGenOpts:string,
   whereClausePITotals:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_APPromissoryNotesTableset[],
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
      @param pcGroupID
   */  
export interface MassDelete_input{
      /**  AP Promissory Note Group ID  */  
   pcGroupID:string,
}

export interface MassDelete_output{
}

   /** Required : 
      @param tranDocType
   */  
export interface NeedsLegalNumber_input{
   tranDocType:string,
}

export interface NeedsLegalNumber_output{
   returnObj:boolean,
}

   /** Required : 
      @param pcBankFeeID
      @param ds
   */  
export interface OnChangeBankFeeID_input{
   pcBankFeeID:string,
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface OnChangeBankFeeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param pdDocTranAmt
      @param ds
   */  
export interface OnChangeDocTranAmt_input{
      /**  Proposed Document Amount value  */  
   pdDocTranAmt:number,
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface OnChangeDocTranAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param pdDocGrossPay
      @param pcRowIdent
      @param ds
   */  
export interface OnChangeInvSelPayment_input{
      /**  Proposeed Document Gross Payment value  */  
   pdDocGrossPay:number,
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
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface OnChangeInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
   pcQuestion:string,
}
}

   /** Required : 
      @param pdtTransDate
      @param ds
   */  
export interface OnChangeTransDate_input{
      /**  Propopsed TransDate  */  
   pdtTransDate:string,
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface OnChangeTransDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param pcType
      @param ds
   */  
export interface OnChangeType_input{
   pcType:string,
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface OnChangeType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param pcVendBankAcctID
      @param ds
   */  
export interface OnChangeVendBankAcctID_input{
      /**  Vendor Bank Acct ID - Bank Account ID for Vendor  */  
   pcVendBankAcctID:string,
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface OnChangeVendBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param pcVendorID
      @param ds
   */  
export interface OnChangeVendor_input{
      /**  Vendor ID - character code for Vendor  */  
   pcVendorID:string,
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface OnChangeVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param inGroupID
      @param inHeadNum
      @param inPIStatusNew
      @param inTypeNew
      @param statusChgTranDocType
      @param appnDs
      @param ds
   */  
export interface PrePost_input{
      /**  Group ID number  */  
   inGroupID:string,
      /**  Header number  */  
   inHeadNum:number,
      /**  new value of PIStatus  */  
   inPIStatusNew:string,
      /**  new value of Type  */  
   inTypeNew:string,
   statusChgTranDocType:string,
   appnDs:Erp_Tablesets_APPromissoryNotesTableset[],
   ds:Erp_Tablesets_LegalNumGenOptsTableset[],
}

export interface PrePost_output{
   returnObj:Erp_Tablesets_APPromissoryNotesTableset[],
parameters : {
      /**  output parameters  */  
   outPostToGL:string,
   appnDs:Erp_Tablesets_APPromissoryNotesTableset,
   ds:Erp_Tablesets_LegalNumGenOptsTableset,
   opLegalNumMsg:string,
   seqNum:number,
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPayableAccountsList
      @param ipSupplierNum
      @param ipDueDate
      @param ipInvoicePM
      @param ipPaymentMethod
      @param ipIncludePartialPosted
   */  
export interface SelectInvoiceToApplyToGroup_input{
      /**  AP Check Group ID  */  
   ipGroupID:string,
      /**  Delimited list of Payable Accounts  */  
   ipPayableAccountsList:string,
      /**  Select invoices for the supplier.  */  
   ipSupplierNum:number,
      /**  Select invoices due by this date.  */  
   ipDueDate:string,
      /**  Select invoices without Payment Method.  */  
   ipInvoicePM:boolean,
      /**  Select payment methods for the specific.  */  
   ipPaymentMethod:string,
      /**  Select invoices including partially posted.  */  
   ipIncludePartialPosted:boolean,
}

export interface SelectInvoiceToApplyToGroup_output{
   returnObj:Erp_Tablesets_APInvSelTableset[],
}

   /** Required : 
      @param pcGroupID
      @param pcPayableAccountsList
      @param pdtDueDate
      @param pdtInvoicePM
      @param pcSupplierList
      @param pcPaymentMethod
   */  
export interface SelectInvoices_input{
      /**  AP Check Group ID  */  
   pcGroupID:string,
      /**  Delimited list of Payable Accounts  */  
   pcPayableAccountsList:string,
      /**  Select invoices due by this date.  */  
   pdtDueDate:string,
      /**  Select invoices without Payment Method.  */  
   pdtInvoicePM:boolean,
      /**  Select invoices for the supplier list.  */  
   pcSupplierList:string,
      /**  Select payment methods for the specific.  */  
   pcPaymentMethod:string,
}

export interface SelectInvoices_output{
   returnObj:Erp_Tablesets_APInvSelTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ds
   */  
export interface UpdateAPPNMove4WriteOff_input{
   ipGroupID:string,
   ipHeadNum:number,
   ds:Erp_Tablesets_APPNMoveTableset[],
}

export interface UpdateAPPNMove4WriteOff_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPNMoveTableset,
}
}

   /** Required : 
      @param inGroupID
      @param inHeadNum
      @param inDueDateNew
      @param inDescriptionNew
   */  
export interface UpdateDueDateDescription_input{
   inGroupID:string,
   inHeadNum:number,
   inDueDateNew:string,
   inDescriptionNew:string,
}

export interface UpdateDueDateDescription_output{
   returnObj:Erp_Tablesets_APPromissoryNotesTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAPPromissoryNotesTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAPPromissoryNotesTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromissoryNotesTableset,
}
}

   /** Required : 
      @param group
   */  
export interface ValidatePIBeforePrint_input{
      /**  Group ID to validate  */  
   group:string,
}

export interface ValidatePIBeforePrint_output{
   returnObj:string,
}

   /** Required : 
      @param group
   */  
export interface ValidatePaymentInstruments_input{
      /**  Group ID to validate  */  
   group:string,
}

export interface ValidatePaymentInstruments_output{
}

   /** Required : 
      @param ds
   */  
export interface ValidateRequiredFields_input{
   ds:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface ValidateRequiredFields_output{
}

   /** Required : 
      @param groupId
      @param headNum
      @param newStatus
      @param newType
   */  
export interface ValidateStatusAndType_input{
      /**  Group ID  */  
   groupId:string,
      /**  HeadNum  */  
   headNum:number,
      /**  Status  */  
   newStatus:string,
      /**  Type  */  
   newType:string,
}

export interface ValidateStatusAndType_output{
}

   /** Required : 
      @param groupId
      @param headNum
   */  
export interface ValidateUnpostedMovement_input{
      /**  Group ID  */  
   groupId:string,
      /**  HeadNum  */  
   headNum:number,
}

export interface ValidateUnpostedMovement_output{
parameters : {
      /**  output parameters  */  
   unpostedSeqNum:number,
   unpostedStatus:string,
   unpostedType:string,
   userMessage:string,
   postToGL:string,
}
}

   /** Required : 
      @param company
      @param vendorNum
      @param invoiceNum
   */  
export interface ValidateWithholdingExists_input{
   company:string,
   vendorNum:number,
   invoiceNum:string,
}

export interface ValidateWithholdingExists_output{
parameters : {
      /**  output parameters  */  
   exists:boolean,
}
}

   /** Required : 
      @param groupId
      @param headNum
      @param seqNum
      @param reason
      @param endorsedReason
   */  
export interface VoidAPPNMoveLegalNumber_input{
      /**  Group ID  */  
   groupId:string,
      /**  HeadNum  */  
   headNum:number,
      /**  Seq  */  
   seqNum:number,
      /**  void reason  */  
   reason:string,
      /**  void reason for endorsed movement legal number  */  
   endorsedReason:string,
}

export interface VoidAPPNMoveLegalNumber_output{
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ipVoidedReason
   */  
export interface VoidLegalNumber_input{
      /**  Group ID number  */  
   ipGroupID:string,
      /**  Header number  */  
   ipHeadNum:number,
      /**  Reason for the void  */  
   ipVoidedReason:string,
}

export interface VoidLegalNumber_output{
   returnObj:Erp_Tablesets_APPromissoryNotesTableset[],
}

export interface selectFilterPIPayMethod_output{
   returnObj:string,
}

