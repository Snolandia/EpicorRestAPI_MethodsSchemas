import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PCashEntrySvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/$metadata", {
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
   Description: Get PCashEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashEntries
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocRow
   */  
export function get_PCashEntries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashEntries
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDocRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PCashDocRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PCashEntries(requestBody:Erp_Tablesets_PCashDocRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PCashEntry item
   Description: Calls GetByID to retrieve the PCashEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PCashDocRow
   */  
export function get_PCashEntries_Company_CashDeskID_ReferenceNum(Company:string, CashDeskID:string, ReferenceNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDocRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")", {
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
         resolve(data as Erp_Tablesets_PCashDocRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PCashEntry for the service
   Description: Calls UpdateExt to update PCashEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDocRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PCashEntries_Company_CashDeskID_ReferenceNum(Company:string, CashDeskID:string, ReferenceNum:string, requestBody:Erp_Tablesets_PCashDocRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")", {
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
   Summary: Call UpdateExt to delete PCashEntry item
   Description: Call UpdateExt to delete PCashEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PCashEntries_Company_CashDeskID_ReferenceNum(Company:string, CashDeskID:string, ReferenceNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")", {
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
   Description: Get PCashDocTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCashDocTGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocTGLCRow
   */  
export function get_PCashEntries_Company_CashDeskID_ReferenceNum_PCashDocTGLCs(Company:string, CashDeskID:string, ReferenceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/PCashDocTGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PCashDocTGLC item
   Description: Calls GetByID to retrieve the PCashDocTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDocTGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PCashDocTGLCRow
   */  
export function get_PCashEntries_Company_CashDeskID_ReferenceNum_PCashDocTGLCs_Company_CashDeskID_ReferenceNum_SysRowID(Company:string, CashDeskID:string, ReferenceNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDocTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/PCashDocTGLCs(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_PCashDocTGLCRow)
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
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
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
export function get_PCashEntries_Company_CashDeskID_ReferenceNum_BankTrans(Company:string, CashDeskID:string, ReferenceNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/BankTrans", {
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
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
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
export function get_PCashEntries_Company_CashDeskID_ReferenceNum_BankTrans_Company_BankAcctID_TranNum_Voided(Company:string, CashDeskID:string, ReferenceNum:string, BankAcctID:string, TranNum:string, Voided:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
   Description: Get PCashDocLinkeds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCashDocLinkeds1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocLinkedRow
   */  
export function get_PCashEntries_Company_CashDeskID_ReferenceNum_PCashDocLinkeds(Company:string, CashDeskID:string, ReferenceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocLinkedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/PCashDocLinkeds", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocLinkedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PCashDocLinked item
   Description: Calls GetByID to retrieve the PCashDocLinked item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDocLinked1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param LinkedSeq Desc: LinkedSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PCashDocLinkedRow
   */  
export function get_PCashEntries_Company_CashDeskID_ReferenceNum_PCashDocLinkeds_Company_CashDeskID_ReferenceNum_LinkedSeq(Company:string, CashDeskID:string, ReferenceNum:string, LinkedSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDocLinkedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/PCashDocLinkeds(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + LinkedSeq + ")", {
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
         resolve(data as Erp_Tablesets_PCashDocLinkedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PCashDocAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCashDocAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocAttchRow
   */  
export function get_PCashEntries_Company_CashDeskID_ReferenceNum_PCashDocAttches(Company:string, CashDeskID:string, ReferenceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/PCashDocAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PCashDocAttch item
   Description: Calls GetByID to retrieve the PCashDocAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDocAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PCashDocAttchRow
   */  
export function get_PCashEntries_Company_CashDeskID_ReferenceNum_PCashDocAttches_Company_CashDeskID_ReferenceNum_DrawingSeq(Company:string, CashDeskID:string, ReferenceNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDocAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/PCashDocAttches(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_PCashDocAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PCashDocTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDocTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocTGLCRow
   */  
export function get_PCashDocTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocTGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDocTGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDocTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PCashDocTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PCashDocTGLCs(requestBody:Erp_Tablesets_PCashDocTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocTGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PCashDocTGLC item
   Description: Calls GetByID to retrieve the PCashDocTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDocTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PCashDocTGLCRow
   */  
export function get_PCashDocTGLCs_Company_CashDeskID_ReferenceNum_SysRowID(Company:string, CashDeskID:string, ReferenceNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDocTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocTGLCs(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_PCashDocTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PCashDocTGLC for the service
   Description: Calls UpdateExt to update PCashDocTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDocTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDocTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PCashDocTGLCs_Company_CashDeskID_ReferenceNum_SysRowID(Company:string, CashDeskID:string, ReferenceNum:string, SysRowID:string, requestBody:Erp_Tablesets_PCashDocTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocTGLCs(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete PCashDocTGLC item
   Description: Call UpdateExt to delete PCashDocTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDocTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PCashDocTGLCs_Company_CashDeskID_ReferenceNum_SysRowID(Company:string, CashDeskID:string, ReferenceNum:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocTGLCs(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + SysRowID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTaxDtls", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTaxDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTGLCs", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", {
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
   Description: Get PCashDocLinkeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDocLinkeds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocLinkedRow
   */  
export function get_PCashDocLinkeds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocLinkedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocLinkeds", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocLinkedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDocLinkeds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDocLinkedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PCashDocLinkedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PCashDocLinkeds(requestBody:Erp_Tablesets_PCashDocLinkedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocLinkeds", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PCashDocLinked item
   Description: Calls GetByID to retrieve the PCashDocLinked item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDocLinked
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param LinkedSeq Desc: LinkedSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PCashDocLinkedRow
   */  
export function get_PCashDocLinkeds_Company_CashDeskID_ReferenceNum_LinkedSeq(Company:string, CashDeskID:string, ReferenceNum:string, LinkedSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDocLinkedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocLinkeds(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + LinkedSeq + ")", {
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
         resolve(data as Erp_Tablesets_PCashDocLinkedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PCashDocLinked for the service
   Description: Calls UpdateExt to update PCashDocLinked. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDocLinked
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param LinkedSeq Desc: LinkedSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDocLinkedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PCashDocLinkeds_Company_CashDeskID_ReferenceNum_LinkedSeq(Company:string, CashDeskID:string, ReferenceNum:string, LinkedSeq:string, requestBody:Erp_Tablesets_PCashDocLinkedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocLinkeds(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + LinkedSeq + ")", {
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
   Summary: Call UpdateExt to delete PCashDocLinked item
   Description: Call UpdateExt to delete PCashDocLinked item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDocLinked
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param LinkedSeq Desc: LinkedSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PCashDocLinkeds_Company_CashDeskID_ReferenceNum_LinkedSeq(Company:string, CashDeskID:string, ReferenceNum:string, LinkedSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocLinkeds(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + LinkedSeq + ")", {
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
   Description: Get PCashDocAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDocAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocAttchRow
   */  
export function get_PCashDocAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDocAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDocAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PCashDocAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PCashDocAttches(requestBody:Erp_Tablesets_PCashDocAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PCashDocAttch item
   Description: Calls GetByID to retrieve the PCashDocAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDocAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PCashDocAttchRow
   */  
export function get_PCashDocAttches_Company_CashDeskID_ReferenceNum_DrawingSeq(Company:string, CashDeskID:string, ReferenceNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDocAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocAttches(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_PCashDocAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PCashDocAttch for the service
   Description: Calls UpdateExt to update PCashDocAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDocAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDocAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PCashDocAttches_Company_CashDeskID_ReferenceNum_DrawingSeq(Company:string, CashDeskID:string, ReferenceNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_PCashDocAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocAttches(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PCashDocAttch item
   Description: Call UpdateExt to delete PCashDocAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDocAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param ReferenceNum Desc: ReferenceNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PCashDocAttches_Company_CashDeskID_ReferenceNum_DrawingSeq(Company:string, CashDeskID:string, ReferenceNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocAttches(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + DrawingSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePCashDoc:string, whereClausePCashDocAttch:string, whereClauseBankTran:string, whereClauseBankTranTaxDtl:string, whereClauseBankTranTGLC:string, whereClausePCashDocLinked:string, whereClausePCashDocTGLC:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePCashDoc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePCashDoc=" + whereClausePCashDoc
   }
   if(typeof whereClausePCashDocAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePCashDocAttch=" + whereClausePCashDocAttch
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
   if(typeof whereClausePCashDocLinked!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePCashDocLinked=" + whereClausePCashDocLinked
   }
   if(typeof whereClausePCashDocTGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePCashDocTGLC=" + whereClausePCashDocTGLC
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetRows" + params, {
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
export function get_GetByID(cashDeskID:string, referenceNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof cashDeskID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "cashDeskID=" + cashDeskID
   }
   if(typeof referenceNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "referenceNum=" + referenceNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/CreateLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetBankFeeDefaultAccount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewBankTranForPCashDoc
   Description: Get New BankTran record for Petty Cash Document
   OperationID: GetNewBankTranForPCashDoc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBankTranForPCashDoc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranForPCashDoc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankTranForPCashDoc(requestBody:GetNewBankTranForPCashDoc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBankTranForPCashDoc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetNewBankTranForPCashDoc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewBankTranForPCashDoc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPCashDocByType
   OperationID: GetNewPCashDocByType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPCashDocByType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDocByType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCashDocByType(requestBody:GetNewPCashDocByType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPCashDocByType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetNewPCashDocByType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPCashDocByType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPCashDocDefaultAccount
   Description: This method is used to get the default account(s) for a Petty Cash Document
   OperationID: GetPCashDocDefaultAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPCashDocDefaultAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCashDocDefaultAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPCashDocDefaultAccount(requestBody:GetPCashDocDefaultAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPCashDocDefaultAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetPCashDocDefaultAccount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPCashDocDefaultAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankTranBankFeeID
   OperationID: OnChangeBankTranBankFeeID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranBankFeeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranBankFeeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankTranBankFeeID(requestBody:OnChangeBankTranBankFeeID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBankTranBankFeeID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangeBankTranBankFeeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeBankTranBankFeeID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankTranTaxAmt
   Description: Call method when the user changes the Tax Amt in Tax screen.
   OperationID: OnChangeBankTranTaxAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankTranTaxAmt(requestBody:OnChangeBankTranTaxAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBankTranTaxAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangeBankTranTaxAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeBankTranTaxAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankTranTaxCode
   Description: Call method when the user changes the Tax ID in Tax maintainence.
   OperationID: OnChangeBankTranTaxCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankTranTaxCode(requestBody:OnChangeBankTranTaxCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBankTranTaxCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangeBankTranTaxCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeBankTranTaxCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankTranTaxPercent
   Description: Call method when the user changes the Tax Percent.
   OperationID: OnChangeBankTranTaxPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankTranTaxPercent(requestBody:OnChangeBankTranTaxPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBankTranTaxPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangeBankTranTaxPercent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeBankTranTaxPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankTranTaxRateCode
   Description: This method updates the dataset when the RateCode field changes
   OperationID: OnChangeBankTranTaxRateCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankTranTaxRateCode(requestBody:OnChangeBankTranTaxRateCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBankTranTaxRateCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangeBankTranTaxRateCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeBankTranTaxRateCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankTranTaxTaxableAmt
   Description: Call method when the user changes the Taxable Amt in Tax screen.
   OperationID: OnChangeBankTranTaxTaxableAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankTranTaxTaxableAmt(requestBody:OnChangeBankTranTaxTaxableAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBankTranTaxTaxableAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangeBankTranTaxTaxableAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeBankTranTaxTaxableAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankTranTranAmt
   Description: This method updates the BankTran amounts when the adjustment amount changes or
the currency switch toggles.
   OperationID: OnChangeBankTranTranAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankTranTranAmt(requestBody:OnChangeBankTranTranAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBankTranTranAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangeBankTranTranAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeBankTranTranAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCashDocApplyDate
   Description: Occurs when Apply Date is changed
   OperationID: OnChangePCashDocApplyDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCashDocApplyDate(requestBody:OnChangePCashDocApplyDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCashDocApplyDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangePCashDocApplyDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCashDocApplyDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCashDocBankAcctID
   Description: Occurs when Bank Account is changed
   OperationID: OnChangePCashDocBankAcctID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCashDocBankAcctID(requestBody:OnChangePCashDocBankAcctID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCashDocBankAcctID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangePCashDocBankAcctID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCashDocBankAcctID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCashDocCashAmt
   Description: This method updates the bank amounts when the cash amount changes
   OperationID: OnChangePCashDocCashAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocCashAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocCashAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCashDocCashAmt(requestBody:OnChangePCashDocCashAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCashDocCashAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangePCashDocCashAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCashDocCashAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCashDocCashDeskIDTransfer
   Description: Occurs when Cash Desk ID Transfer is changed
   OperationID: OnChangePCashDocCashDeskIDTransfer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocCashDeskIDTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocCashDeskIDTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCashDocCashDeskIDTransfer(requestBody:OnChangePCashDocCashDeskIDTransfer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCashDocCashDeskIDTransfer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangePCashDocCashDeskIDTransfer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCashDocCashDeskIDTransfer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCashDocCustID
   Description: Occurs when Customer is changed
   OperationID: OnChangePCashDocCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCashDocCustID(requestBody:OnChangePCashDocCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCashDocCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangePCashDocCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCashDocCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCashDocDraft
   Description: Occurs when Apply Date is changed
   OperationID: OnChangePCashDocDraft
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocDraft_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocDraft_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCashDocDraft(requestBody:OnChangePCashDocDraft_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCashDocDraft_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangePCashDocDraft", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCashDocDraft_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCashDocEmployeeNum
   Description: Occurs when Employee is changed
   OperationID: OnChangePCashDocEmployeeNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocEmployeeNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocEmployeeNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCashDocEmployeeNum(requestBody:OnChangePCashDocEmployeeNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCashDocEmployeeNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangePCashDocEmployeeNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCashDocEmployeeNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCashDocExchRateDate
   Description: Occurs when Apply Date is changed
   OperationID: OnChangePCashDocExchRateDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocExchRateDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocExchRateDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCashDocExchRateDate(requestBody:OnChangePCashDocExchRateDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCashDocExchRateDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangePCashDocExchRateDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCashDocExchRateDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCashDocOprType
   Description: Occurs when Operation type was changed
   OperationID: OnChangePCashDocOprType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocOprType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocOprType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCashDocOprType(requestBody:OnChangePCashDocOprType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCashDocOprType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangePCashDocOprType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCashDocOprType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCashDocVendorID
   Description: Occurs when Vendor is changed
   OperationID: OnChangePCashDocVendorID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCashDocVendorID(requestBody:OnChangePCashDocVendorID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCashDocVendorID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/OnChangePCashDocVendorID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCashDocVendorID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Recalculate
   Description: Recalculate amounts according to Exchange Rate Date
   OperationID: Recalculate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Recalculate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Recalculate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Recalculate(requestBody:Recalculate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Recalculate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/Recalculate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Recalculate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdatePCashDoc
   Description: Call this method after calling other business objects like
Cash Receipts, PaymentEntry, Bank Adjustment etc.
This method updates the PCashDoc record with the
data from other business objects.
   OperationID: UpdatePCashDoc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdatePCashDoc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePCashDoc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePCashDoc(requestBody:UpdatePCashDoc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdatePCashDoc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/UpdatePCashDoc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdatePCashDoc_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetLegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the Document.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/AssignLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/VoidLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PreUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method PrePost
   Description: PrePost method to check accounts before posting.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PrePost", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewPCashDoc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDoc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPCashDoc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDoc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCashDoc(requestBody:GetNewPCashDoc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPCashDoc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetNewPCashDoc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPCashDoc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPCashDocAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDocAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPCashDocAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDocAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCashDocAttch(requestBody:GetNewPCashDocAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPCashDocAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetNewPCashDocAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPCashDocAttch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetNewBankTran", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetNewBankTranTaxDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetNewBankTranTGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewPCashDocTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDocTGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPCashDocTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDocTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCashDocTGLC(requestBody:GetNewPCashDocTGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPCashDocTGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetNewPCashDocTGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPCashDocTGLC_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCashDocAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocLinkedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCashDocLinkedRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCashDocListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCashDocRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCashDocTGLCRow,
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

export interface Erp_Tablesets_PCashDocAttchRow{
   "Company":string,
   "CashDeskID":string,
   "ReferenceNum":number,
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

export interface Erp_Tablesets_PCashDocLinkedRow{
   "Company":string,
   "CashDeskID":string,
   "ReferenceNum":number,
   "ApplyDate":string,
      /**  Description of the linked document  */  
   "Description":string,
   "TranAmt":number,
      /**  Description of the operation class  */  
   "OprClassDesc":string,
   "DocTranAmt":number,
   "Rpt1TranAmt":number,
   "Rpt2TranAmt":number,
   "Rpt3TranAmt":number,
      /**  The reference number of the linked document (i.e. ap/ar invoice number)  */  
   "DocReference":string,
   "CurrencyCode":string,
      /**  Internal sequence for uniqueness  */  
   "LinkedSeq":number,
      /**  GroupID of the linked document  */  
   "GroupID":string,
      /**  Tran num of the linked document  */  
   "TranNum":number,
   "InternalDate":string,
      /**  The module of the linked document, i.e. A/R, A/P.  */  
   "Module":string,
      /**  The type of transaction  */  
   "TranType":string,
      /**  Invoice date when applicable  */  
   "InvoiceDate":string,
      /**  Invoice due date when applicable  */  
   "DueDate":string,
   "DocDiscAmt":number,
   "DiscAmt":number,
   "WithholdAmt":number,
   "DocWithholdAmt":number,
      /**  Gain/Loss  */  
   "GainLoss":number,
      /**  Gain/Loss  */  
   "DocGainLoss":number,
   "Rpt1DiscAmt":number,
   "Rpt2DiscAmt":number,
   "Rpt3DiscAmt":number,
   "Rpt1WithholdAmt":number,
   "Rpt2WithholdAmt":number,
   "Rpt3WithholdAmt":number,
      /**  Gain/Loss  */  
   "Rpt1GainLoss":number,
      /**  Gain/Loss  */  
   "Rpt2GainLoss":number,
      /**  Gain/Loss  */  
   "Rpt3GainLoss":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PCashDocListRow{
      /**  Unique identifier of Cash Desk  */  
   "CashDeskID":string,
      /**  Reference Number, unique identifier of Petty Cash Document, sequentially assigned for each Petty Cash Desk internal number (never reused)  */  
   "ReferenceNum":number,
      /**  Apply Date of Operation  */  
   "ApplyDate":string,
      /**  Sequential number of Cash Receipt or Cash Issue for Petty Cask Desk within Apply Cash Day. Used for Authorized documents only.  */  
   "DaySeqNum":number,
      /**   CI ? Cash Issue
CR ? Cash Receipt  */  
   "Direction":string,
      /**  Available only when configuration of operation type allows using of draft documents.  */  
   "Draft":boolean,
      /**  Legal Number of the record. Available only for Authorized Documents.  */  
   "ExternalNum":string,
      /**  Legal Number of the record. Available only for Authorized Documents.  */  
   "LegalNumber":string,
      /**  Unique identifier of Petty Cash Operation Type  */  
   "OprTypeCode":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DirectionDesc":string,
      /**  description of operation type  */  
   "OperationTypeIDDescription":string,
      /**  PCashDesk Name  */  
   "PCashDeskName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PCashDocRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of Cash Desk  */  
   "CashDeskID":string,
      /**  Reference Number, unique identifier of Petty Cash Document, sequentially assigned for each Petty Cash Desk internal number (never reused)  */  
   "ReferenceNum":number,
      /**  Apply Date of Operation  */  
   "ApplyDate":string,
      /**  User Id of the user who authorize the record.  */  
   "AuthorizedBy":string,
      /**  Cashier Name  */  
   "Cashier":string,
      /**  Comment  */  
   "Comment":string,
      /**  User ID of the user who created the record.  */  
   "CreatedBy":string,
      /**  Date when the record was created.  */  
   "CreateDate":string,
      /**  The time the record was created (in seconds since midnight)  */  
   "CreateTime":number,
      /**  A unique code that identifies the currency  */  
   "CurrencyCode":string,
      /**  Sequential number of Cash Receipt or Cash Issue for Petty Cask Desk within Apply Cash Day. Used for Authorized documents only.  */  
   "DaySeqNum":number,
      /**   CI ? Cash Issue
CR ? Cash Receipt  */  
   "Direction":string,
      /**  Available only when configuration of operation type allows using of draft documents.  */  
   "Draft":boolean,
      /**  Legal Number of the record. Available only for Authorized Documents.  */  
   "ExternalNum":string,
      /**  Fiscal Calendar is Company Calendar  */  
   "FiscalCalendarID":string,
      /**  Defined by Apply Date for Company Calendar  */  
   "FiscalPeriod":number,
      /**  Defined by Apply Date for Company Calendar  */  
   "FiscalYear":number,
      /**  Defined by Apply Date for Company Calendar  */  
   "FiscalYearSuffix":string,
      /**  Legal Number of the record. Available only for Authorized Documents.  */  
   "LegalNumber":string,
      /**  Unique identifier of Petty Cash Operation Type  */  
   "OprTypeCode":string,
      /**  According to Operation Type  */  
   "PayrollBalOpr":boolean,
      /**  Posted  */  
   "Posted":boolean,
      /**  Printed  */  
   "Printed":boolean,
      /**  Reason  */  
   "ReasonCode":string,
      /**  Review Journal.  */  
   "RvJrnUID":number,
      /**   According to Operation type definition:
E - Employee; S - Supplier; C - Customer; B - Bank; CD - Cash Desk; O - Other  */  
   "RecipientType":string,
      /**  Customer  */  
   "CustNum":number,
      /**  Ship To Customer (CustCon.ShipToNum)  */  
   "CustShipTo":string,
      /**  Customer Contact Number (CustCon.ConNum)  */  
   "CustConNum":number,
      /**  Supplier  */  
   "VendorNum":number,
      /**  Purchase point from Vendor.(VendCon.PurPoint)  */  
   "VendPurPoint":string,
      /**  Supplier Contact number (VendCon.ConNum)  */  
   "VendConNum":number,
   "EmployeeNum":string,
      /**  Bank Account  */  
   "BankAcctID":string,
      /**  Depending on Recipient Type: Supplier ID; Customer ID; Bank Account ID; Cash Desk ID. Not available for Employee and Other.  */  
   "OrganizationID":string,
      /**   Depending on Recipient Type: Supplier Name; Customer Name;
Bank Account Name; Cash Desk Name; Company Name (default for Employee and Other Recipient types).  */  
   "OrganizationName":string,
      /**   Depending on Recipient type: Employee Display Name (composed from First Name, Middle Initial and Last Name); Supplier Contact Display Name; Customer Contact Display Name; Cash Desk Cashier Name, or Entrusted Cashier Name (recipient of cash transfer); Own Cash Desk Cashier name.
Person Name can be modified. There is no default for Bank and Other recipient.  */  
   "PersonName":string,
      /**  Default of Personal Data can be composed using BPM, and can be adjusted by user.  */  
   "PersonalData":string,
      /**  Amount to be paid/received in cash  */  
   "DocCashAmt":number,
      /**  Amount to be paid/received in cash  */  
   "CashAmt":number,
      /**  Amount to be paid/received in cash in reporting Currency  */  
   "Rpt1CashAmt":number,
      /**  Amount to be paid/received in cash in reporting Currency  */  
   "Rpt2CashAmt":number,
      /**  Amount to be paid/received in cash in reporting Currency  */  
   "Rpt3CashAmt":number,
      /**  Gross Amount to update AP or AR  */  
   "DocGrossAmt":number,
      /**  Gross Amount to update AP or AR  */  
   "GrossAmt":number,
      /**  Gross Amount in reporting Currency  */  
   "Rpt1GrossAmt":number,
      /**  Gross Amount in reporting Currency  */  
   "Rpt2GrossAmt":number,
      /**  Gross Amount in reporting Currency  */  
   "Rpt3GrossAmt":number,
      /**  Amount of Applied Cash Discount (AP or AR)  */  
   "DocDiscount":number,
      /**  Amount of Applied Cash Discount (AP or AR)  */  
   "Discount":number,
      /**  Amount of Applied Cash Discount  in reporting Currency  */  
   "Rpt1Discount":number,
      /**  Amount of Applied Cash Discount  in reporting Currency  */  
   "Rpt2Discount":number,
      /**  Amount of Applied Cash Discount  in reporting Currency  */  
   "Rpt3Discount":number,
      /**  Amount of calculated withhold taxes (AR or AP)  */  
   "DocWithholdAmt":number,
      /**  Amount of calculated withhold taxes (AR or AP)  */  
   "WithholdAmt":number,
      /**  Amount of calculated withhold taxes  in reporting currency  */  
   "Rpt1WithholdAmt":number,
      /**  Amount of calculated withhold taxes  in reporting currency  */  
   "Rpt2WithholdAmt":number,
      /**  Amount of calculated withhold taxes  in reporting currency  */  
   "Rpt3WithholdAmt":number,
      /**  Bank Amount(Bank To Cash / Cash To Bank)  */  
   "DocBankAmt":number,
      /**  Bank Amount(Bank To Cash / Cash To Bank)  */  
   "BankAmt":number,
      /**  Bank Amount in reporting currency  */  
   "Rpt1BankAmt":number,
      /**  Bank Amount in reporting currency  */  
   "Rpt2BankAmt":number,
      /**  Bank Amount in reporting currency  */  
   "Rpt3BankAmt":number,
      /**  Bank Fee Amount(Bank To Cash / Cash To Bank)  */  
   "DocBankFeeAmt":number,
      /**  Bank Fee Amount(Bank To Cash / Cash To Bank)  */  
   "BankFeeAmt":number,
      /**  Bank Fee Amount in reporting currency  */  
   "Rpt1BankFeeAmt":number,
      /**  Bank Fee Amount in reporting currency  */  
   "Rpt2BankFeeAmt":number,
      /**  Bank Fee Amount in reporting currency  */  
   "Rpt3BankFeeAmt":number,
      /**  Rate Type  */  
   "RateGrpType":string,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  OnAcctBankAcctID  */  
   "OnAcctBankAcctID":string,
      /**  ReceiptAmt  */  
   "ReceiptAmt":number,
      /**  Reference  */  
   "Reference":string,
      /**  Payee  */  
   "Payee":string,
      /**  AccountNumber  */  
   "AccountNumber":string,
      /**  OtherDetails  */  
   "OtherDetails":string,
      /**  PayMethodPMUID  */  
   "PayMethodPMUID":number,
      /**  PayMethodName  */  
   "PayMethodName":string,
      /**  PayMethodReference  */  
   "PayMethodReference":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CashDeskIDTransfer  */  
   "CashDeskIDTransfer":string,
      /**  ExchangeRateDate  */  
   "ExchangeRateDate":string,
      /**  ExchRateDateUserDefined  */  
   "ExchRateDateUserDefined":boolean,
      /**  PrintPage  */  
   "PrintPage":number,
      /**  PrintPageLegalNum  */  
   "PrintPageLegalNum":string,
      /**  Reason  */  
   "Reason":string,
   "AllowChangeAfterPrint":boolean,
   "BankPersonalData":string,
      /**  Cash Desk Transfer from/to Name for CashDesk to CashDesk documents  */  
   "CashDeskTransferName":string,
   "CDPersonalData":string,
   "CustomerPersonalData":string,
   "CustomerPersonName":string,
   "DirectionDesc":string,
   "EmpPersonalData":string,
   "EnableAssignLegalNum":boolean,
   "EnableDraft":boolean,
      /**  Enable the exchange rate date  */  
   "EnableExchangeRateDate":boolean,
   "EnableVoidLegNum":boolean,
      /**  Internal date used to set the parent view to PCashDocDates, which is defined in the UI.  */  
   "InternalDate":string,
   "IsLcked":boolean,
      /**  Locked means can not be posted: an invoice is already in review journal or in posting process  */  
   "LockStatus":string,
   "OprClassDesc":string,
   "OtherPersonalData":string,
   "SupplierPersonalData":string,
      /**  Text for the tree node  */  
   "TreeNodeText":string,
      /**  Indicates if the user can print the document  */  
   "UserCanPrint":boolean,
      /**  Indicates if the apply date is enabled  */  
   "EnableApplyDate":boolean,
      /**  Reversed Petty Cash Trans.  */  
   "CashReversed":boolean,
   "HasLegNumCnfg":boolean,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
   "BitFlag":number,
   "BankAcctDescription":string,
   "BankAcctBankName":string,
   "BaseCurrDocumentDesc":string,
   "BaseCurrCurrencyID":string,
   "BaseCurrCurrName":string,
   "BaseCurrCurrDesc":string,
   "BaseCurrCurrencyCode":string,
   "BaseCurrCurrSymbol":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CustCntLastName":string,
   "CustCntCorpName":string,
   "CustCntFirstName":string,
   "CustCntFaxNum":string,
   "CustCntPhoneNum":string,
   "CustCntMiddleName":string,
   "CustCntName":string,
   "CustomerCustID":string,
   "CustomerBTName":string,
   "CustomerName":string,
   "EmployeeName":string,
   "OperationTypeIDDescription":string,
   "OperationTypeIDPayrollBal":boolean,
   "OperationTypeIDOprClass":string,
   "PCashDeskCurrencyCode":string,
   "PCashDeskName":string,
   "PCashDeskOprAllowDraftDoc":boolean,
   "PCashDeskOprAllowUseExtnNum":boolean,
   "PCashDeskOprTranDocTypeID":string,
   "VendCntEmailAddress":string,
   "VendCntPhoneNum":string,
   "VendCntFaxNum":string,
   "VendCntName":string,
   "VendorCountry":string,
   "VendorTermsCode":string,
   "VendorVendorID":string,
   "VendorZIP":string,
   "VendorCurrencyCode":string,
   "VendorDefaultFOB":string,
   "VendorAddress1":string,
   "VendorName":string,
   "VendorAddress2":string,
   "VendorState":string,
   "VendorCity":string,
   "VendorAddress3":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PCashDocTGLCRow{
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
   "CashDeskID":string,
   "ReferenceNum":number,
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
      @param ipCashDeskID
      @param ipReferenceNum
      @param ds
   */  
export interface AssignLegalNumber_input{
      /**  Cash Desk ID  */  
   ipCashDeskID:string,
      /**  Cash Doc Reference Num  */  
   ipReferenceNum:number,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface AssignLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
   opLegalNumMsg:string,
}
}

   /** Required : 
      @param ipCashDeskID
      @param ipReferenceNum
      @param ipLineType
   */  
export interface CreateLine_input{
      /**  Identifier of Cash Desk  */  
   ipCashDeskID:string,
      /**  Petty Cash document number  */  
   ipReferenceNum:number,
      /**  Line type  */  
   ipLineType:string,
}

export interface CreateLine_output{
parameters : {
      /**  output parameters  */  
   opGroupID:string,
   opLineNum:number,
}
}

   /** Required : 
      @param cashDeskID
      @param referenceNum
   */  
export interface DeleteByID_input{
   cashDeskID:string,
   referenceNum:number,
}

export interface DeleteByID_output{
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

export interface Erp_Tablesets_PCashDocAttchRow{
   Company:string,
   CashDeskID:string,
   ReferenceNum:number,
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

export interface Erp_Tablesets_PCashDocLinkedRow{
   Company:string,
   CashDeskID:string,
   ReferenceNum:number,
   ApplyDate:string,
      /**  Description of the linked document  */  
   Description:string,
   TranAmt:number,
      /**  Description of the operation class  */  
   OprClassDesc:string,
   DocTranAmt:number,
   Rpt1TranAmt:number,
   Rpt2TranAmt:number,
   Rpt3TranAmt:number,
      /**  The reference number of the linked document (i.e. ap/ar invoice number)  */  
   DocReference:string,
   CurrencyCode:string,
      /**  Internal sequence for uniqueness  */  
   LinkedSeq:number,
      /**  GroupID of the linked document  */  
   GroupID:string,
      /**  Tran num of the linked document  */  
   TranNum:number,
   InternalDate:string,
      /**  The module of the linked document, i.e. A/R, A/P.  */  
   Module:string,
      /**  The type of transaction  */  
   TranType:string,
      /**  Invoice date when applicable  */  
   InvoiceDate:string,
      /**  Invoice due date when applicable  */  
   DueDate:string,
   DocDiscAmt:number,
   DiscAmt:number,
   WithholdAmt:number,
   DocWithholdAmt:number,
      /**  Gain/Loss  */  
   GainLoss:number,
      /**  Gain/Loss  */  
   DocGainLoss:number,
   Rpt1DiscAmt:number,
   Rpt2DiscAmt:number,
   Rpt3DiscAmt:number,
   Rpt1WithholdAmt:number,
   Rpt2WithholdAmt:number,
   Rpt3WithholdAmt:number,
      /**  Gain/Loss  */  
   Rpt1GainLoss:number,
      /**  Gain/Loss  */  
   Rpt2GainLoss:number,
      /**  Gain/Loss  */  
   Rpt3GainLoss:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashDocListRow{
      /**  Unique identifier of Cash Desk  */  
   CashDeskID:string,
      /**  Reference Number, unique identifier of Petty Cash Document, sequentially assigned for each Petty Cash Desk internal number (never reused)  */  
   ReferenceNum:number,
      /**  Apply Date of Operation  */  
   ApplyDate:string,
      /**  Sequential number of Cash Receipt or Cash Issue for Petty Cask Desk within Apply Cash Day. Used for Authorized documents only.  */  
   DaySeqNum:number,
      /**   CI ? Cash Issue
CR ? Cash Receipt  */  
   Direction:string,
      /**  Available only when configuration of operation type allows using of draft documents.  */  
   Draft:boolean,
      /**  Legal Number of the record. Available only for Authorized Documents.  */  
   ExternalNum:string,
      /**  Legal Number of the record. Available only for Authorized Documents.  */  
   LegalNumber:string,
      /**  Unique identifier of Petty Cash Operation Type  */  
   OprTypeCode:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DirectionDesc:string,
      /**  description of operation type  */  
   OperationTypeIDDescription:string,
      /**  PCashDesk Name  */  
   PCashDeskName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashDocRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of Cash Desk  */  
   CashDeskID:string,
      /**  Reference Number, unique identifier of Petty Cash Document, sequentially assigned for each Petty Cash Desk internal number (never reused)  */  
   ReferenceNum:number,
      /**  Apply Date of Operation  */  
   ApplyDate:string,
      /**  User Id of the user who authorize the record.  */  
   AuthorizedBy:string,
      /**  Cashier Name  */  
   Cashier:string,
      /**  Comment  */  
   Comment:string,
      /**  User ID of the user who created the record.  */  
   CreatedBy:string,
      /**  Date when the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  A unique code that identifies the currency  */  
   CurrencyCode:string,
      /**  Sequential number of Cash Receipt or Cash Issue for Petty Cask Desk within Apply Cash Day. Used for Authorized documents only.  */  
   DaySeqNum:number,
      /**   CI ? Cash Issue
CR ? Cash Receipt  */  
   Direction:string,
      /**  Available only when configuration of operation type allows using of draft documents.  */  
   Draft:boolean,
      /**  Legal Number of the record. Available only for Authorized Documents.  */  
   ExternalNum:string,
      /**  Fiscal Calendar is Company Calendar  */  
   FiscalCalendarID:string,
      /**  Defined by Apply Date for Company Calendar  */  
   FiscalPeriod:number,
      /**  Defined by Apply Date for Company Calendar  */  
   FiscalYear:number,
      /**  Defined by Apply Date for Company Calendar  */  
   FiscalYearSuffix:string,
      /**  Legal Number of the record. Available only for Authorized Documents.  */  
   LegalNumber:string,
      /**  Unique identifier of Petty Cash Operation Type  */  
   OprTypeCode:string,
      /**  According to Operation Type  */  
   PayrollBalOpr:boolean,
      /**  Posted  */  
   Posted:boolean,
      /**  Printed  */  
   Printed:boolean,
      /**  Reason  */  
   ReasonCode:string,
      /**  Review Journal.  */  
   RvJrnUID:number,
      /**   According to Operation type definition:
E - Employee; S - Supplier; C - Customer; B - Bank; CD - Cash Desk; O - Other  */  
   RecipientType:string,
      /**  Customer  */  
   CustNum:number,
      /**  Ship To Customer (CustCon.ShipToNum)  */  
   CustShipTo:string,
      /**  Customer Contact Number (CustCon.ConNum)  */  
   CustConNum:number,
      /**  Supplier  */  
   VendorNum:number,
      /**  Purchase point from Vendor.(VendCon.PurPoint)  */  
   VendPurPoint:string,
      /**  Supplier Contact number (VendCon.ConNum)  */  
   VendConNum:number,
   EmployeeNum:string,
      /**  Bank Account  */  
   BankAcctID:string,
      /**  Depending on Recipient Type: Supplier ID; Customer ID; Bank Account ID; Cash Desk ID. Not available for Employee and Other.  */  
   OrganizationID:string,
      /**   Depending on Recipient Type: Supplier Name; Customer Name;
Bank Account Name; Cash Desk Name; Company Name (default for Employee and Other Recipient types).  */  
   OrganizationName:string,
      /**   Depending on Recipient type: Employee Display Name (composed from First Name, Middle Initial and Last Name); Supplier Contact Display Name; Customer Contact Display Name; Cash Desk Cashier Name, or Entrusted Cashier Name (recipient of cash transfer); Own Cash Desk Cashier name.
Person Name can be modified. There is no default for Bank and Other recipient.  */  
   PersonName:string,
      /**  Default of Personal Data can be composed using BPM, and can be adjusted by user.  */  
   PersonalData:string,
      /**  Amount to be paid/received in cash  */  
   DocCashAmt:number,
      /**  Amount to be paid/received in cash  */  
   CashAmt:number,
      /**  Amount to be paid/received in cash in reporting Currency  */  
   Rpt1CashAmt:number,
      /**  Amount to be paid/received in cash in reporting Currency  */  
   Rpt2CashAmt:number,
      /**  Amount to be paid/received in cash in reporting Currency  */  
   Rpt3CashAmt:number,
      /**  Gross Amount to update AP or AR  */  
   DocGrossAmt:number,
      /**  Gross Amount to update AP or AR  */  
   GrossAmt:number,
      /**  Gross Amount in reporting Currency  */  
   Rpt1GrossAmt:number,
      /**  Gross Amount in reporting Currency  */  
   Rpt2GrossAmt:number,
      /**  Gross Amount in reporting Currency  */  
   Rpt3GrossAmt:number,
      /**  Amount of Applied Cash Discount (AP or AR)  */  
   DocDiscount:number,
      /**  Amount of Applied Cash Discount (AP or AR)  */  
   Discount:number,
      /**  Amount of Applied Cash Discount  in reporting Currency  */  
   Rpt1Discount:number,
      /**  Amount of Applied Cash Discount  in reporting Currency  */  
   Rpt2Discount:number,
      /**  Amount of Applied Cash Discount  in reporting Currency  */  
   Rpt3Discount:number,
      /**  Amount of calculated withhold taxes (AR or AP)  */  
   DocWithholdAmt:number,
      /**  Amount of calculated withhold taxes (AR or AP)  */  
   WithholdAmt:number,
      /**  Amount of calculated withhold taxes  in reporting currency  */  
   Rpt1WithholdAmt:number,
      /**  Amount of calculated withhold taxes  in reporting currency  */  
   Rpt2WithholdAmt:number,
      /**  Amount of calculated withhold taxes  in reporting currency  */  
   Rpt3WithholdAmt:number,
      /**  Bank Amount(Bank To Cash / Cash To Bank)  */  
   DocBankAmt:number,
      /**  Bank Amount(Bank To Cash / Cash To Bank)  */  
   BankAmt:number,
      /**  Bank Amount in reporting currency  */  
   Rpt1BankAmt:number,
      /**  Bank Amount in reporting currency  */  
   Rpt2BankAmt:number,
      /**  Bank Amount in reporting currency  */  
   Rpt3BankAmt:number,
      /**  Bank Fee Amount(Bank To Cash / Cash To Bank)  */  
   DocBankFeeAmt:number,
      /**  Bank Fee Amount(Bank To Cash / Cash To Bank)  */  
   BankFeeAmt:number,
      /**  Bank Fee Amount in reporting currency  */  
   Rpt1BankFeeAmt:number,
      /**  Bank Fee Amount in reporting currency  */  
   Rpt2BankFeeAmt:number,
      /**  Bank Fee Amount in reporting currency  */  
   Rpt3BankFeeAmt:number,
      /**  Rate Type  */  
   RateGrpType:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  OnAcctBankAcctID  */  
   OnAcctBankAcctID:string,
      /**  ReceiptAmt  */  
   ReceiptAmt:number,
      /**  Reference  */  
   Reference:string,
      /**  Payee  */  
   Payee:string,
      /**  AccountNumber  */  
   AccountNumber:string,
      /**  OtherDetails  */  
   OtherDetails:string,
      /**  PayMethodPMUID  */  
   PayMethodPMUID:number,
      /**  PayMethodName  */  
   PayMethodName:string,
      /**  PayMethodReference  */  
   PayMethodReference:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CashDeskIDTransfer  */  
   CashDeskIDTransfer:string,
      /**  ExchangeRateDate  */  
   ExchangeRateDate:string,
      /**  ExchRateDateUserDefined  */  
   ExchRateDateUserDefined:boolean,
      /**  PrintPage  */  
   PrintPage:number,
      /**  PrintPageLegalNum  */  
   PrintPageLegalNum:string,
      /**  Reason  */  
   Reason:string,
   AllowChangeAfterPrint:boolean,
   BankPersonalData:string,
      /**  Cash Desk Transfer from/to Name for CashDesk to CashDesk documents  */  
   CashDeskTransferName:string,
   CDPersonalData:string,
   CustomerPersonalData:string,
   CustomerPersonName:string,
   DirectionDesc:string,
   EmpPersonalData:string,
   EnableAssignLegalNum:boolean,
   EnableDraft:boolean,
      /**  Enable the exchange rate date  */  
   EnableExchangeRateDate:boolean,
   EnableVoidLegNum:boolean,
      /**  Internal date used to set the parent view to PCashDocDates, which is defined in the UI.  */  
   InternalDate:string,
   IsLcked:boolean,
      /**  Locked means can not be posted: an invoice is already in review journal or in posting process  */  
   LockStatus:string,
   OprClassDesc:string,
   OtherPersonalData:string,
   SupplierPersonalData:string,
      /**  Text for the tree node  */  
   TreeNodeText:string,
      /**  Indicates if the user can print the document  */  
   UserCanPrint:boolean,
      /**  Indicates if the apply date is enabled  */  
   EnableApplyDate:boolean,
      /**  Reversed Petty Cash Trans.  */  
   CashReversed:boolean,
   HasLegNumCnfg:boolean,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
   BitFlag:number,
   BankAcctDescription:string,
   BankAcctBankName:string,
   BaseCurrDocumentDesc:string,
   BaseCurrCurrencyID:string,
   BaseCurrCurrName:string,
   BaseCurrCurrDesc:string,
   BaseCurrCurrencyCode:string,
   BaseCurrCurrSymbol:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrencyID:string,
   CustCntLastName:string,
   CustCntCorpName:string,
   CustCntFirstName:string,
   CustCntFaxNum:string,
   CustCntPhoneNum:string,
   CustCntMiddleName:string,
   CustCntName:string,
   CustomerCustID:string,
   CustomerBTName:string,
   CustomerName:string,
   EmployeeName:string,
   OperationTypeIDDescription:string,
   OperationTypeIDPayrollBal:boolean,
   OperationTypeIDOprClass:string,
   PCashDeskCurrencyCode:string,
   PCashDeskName:string,
   PCashDeskOprAllowDraftDoc:boolean,
   PCashDeskOprAllowUseExtnNum:boolean,
   PCashDeskOprTranDocTypeID:string,
   VendCntEmailAddress:string,
   VendCntPhoneNum:string,
   VendCntFaxNum:string,
   VendCntName:string,
   VendorCountry:string,
   VendorTermsCode:string,
   VendorVendorID:string,
   VendorZIP:string,
   VendorCurrencyCode:string,
   VendorDefaultFOB:string,
   VendorAddress1:string,
   VendorName:string,
   VendorAddress2:string,
   VendorState:string,
   VendorCity:string,
   VendorAddress3:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashDocTGLCRow{
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
   CashDeskID:string,
   ReferenceNum:number,
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

export interface Erp_Tablesets_PCashEntryListTableset{
   PCashDocList:Erp_Tablesets_PCashDocListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PCashEntryTableset{
   PCashDoc:Erp_Tablesets_PCashDocRow[],
   PCashDocAttch:Erp_Tablesets_PCashDocAttchRow[],
   BankTran:Erp_Tablesets_BankTranRow[],
   BankTranTaxDtl:Erp_Tablesets_BankTranTaxDtlRow[],
   BankTranTGLC:Erp_Tablesets_BankTranTGLCRow[],
   PCashDocLinked:Erp_Tablesets_PCashDocLinkedRow[],
   PCashDocTGLC:Erp_Tablesets_PCashDocTGLCRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPCashEntryTableset{
   PCashDoc:Erp_Tablesets_PCashDocRow[],
   PCashDocAttch:Erp_Tablesets_PCashDocAttchRow[],
   BankTran:Erp_Tablesets_BankTranRow[],
   BankTranTaxDtl:Erp_Tablesets_BankTranTaxDtlRow[],
   BankTranTGLC:Erp_Tablesets_BankTranTGLCRow[],
   PCashDocLinked:Erp_Tablesets_PCashDocLinkedRow[],
   PCashDocTGLC:Erp_Tablesets_PCashDocTGLCRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface GetBankFeeDefaultAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param cashDeskID
      @param referenceNum
   */  
export interface GetByID_input{
   cashDeskID:string,
   referenceNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PCashEntryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PCashEntryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PCashEntryTableset[],
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
      @param ipCashDeskID
      @param ipReferenceNum
      @param ds
   */  
export interface GetLegalNumGenOpts_input{
      /**  Cash Desk ID  */  
   ipCashDeskID:string,
      /**  Cash Doc Reference Num  */  
   ipReferenceNum:number,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface GetLegalNumGenOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
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
   returnObj:Erp_Tablesets_PCashEntryListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param inCashDeskID
      @param inReferenceNum
      @param ds
   */  
export interface GetNewBankTranForPCashDoc_input{
   inCashDeskID:string,
   inReferenceNum:number,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface GetNewBankTranForPCashDoc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param tranNum
      @param voided
   */  
export interface GetNewBankTranTGLC_input{
   ds:Erp_Tablesets_PCashEntryTableset[],
   bankAcctID:string,
   tranNum:number,
   voided:boolean,
}

export interface GetNewBankTranTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
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
   ds:Erp_Tablesets_PCashEntryTableset[],
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
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ds
      @param bankAcctID
      @param tranNum
   */  
export interface GetNewBankTran_input{
   ds:Erp_Tablesets_PCashEntryTableset[],
   bankAcctID:string,
   tranNum:number,
}

export interface GetNewBankTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ds
      @param cashDeskID
      @param referenceNum
   */  
export interface GetNewPCashDocAttch_input{
   ds:Erp_Tablesets_PCashEntryTableset[],
   cashDeskID:string,
   referenceNum:number,
}

export interface GetNewPCashDocAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param inCashDeskID
      @param inNewType
      @param ds
   */  
export interface GetNewPCashDocByType_input{
   inCashDeskID:string,
   inNewType:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface GetNewPCashDocByType_output{
parameters : {
      /**  output parameters  */  
   outDocDate:string,
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ds
      @param cashDeskID
      @param referenceNum
   */  
export interface GetNewPCashDocTGLC_input{
   ds:Erp_Tablesets_PCashEntryTableset[],
   cashDeskID:string,
   referenceNum:number,
}

export interface GetNewPCashDocTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ds
      @param cashDeskID
   */  
export interface GetNewPCashDoc_input{
   ds:Erp_Tablesets_PCashEntryTableset[],
   cashDeskID:string,
}

export interface GetNewPCashDoc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param cashDeskID
      @param referenceNum
      @param ds
   */  
export interface GetPCashDocDefaultAccount_input{
      /**  The Petty Cash ID  */  
   cashDeskID:string,
      /**  The Petty Cash Reference Num  */  
   referenceNum:number,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface GetPCashDocDefaultAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param whereClausePCashDoc
      @param whereClausePCashDocAttch
      @param whereClauseBankTran
      @param whereClauseBankTranTaxDtl
      @param whereClauseBankTranTGLC
      @param whereClausePCashDocLinked
      @param whereClausePCashDocTGLC
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePCashDoc:string,
   whereClausePCashDocAttch:string,
   whereClauseBankTran:string,
   whereClauseBankTranTaxDtl:string,
   whereClauseBankTranTGLC:string,
   whereClausePCashDocLinked:string,
   whereClausePCashDocTGLC:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PCashEntryTableset[],
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
      @param inBankFeeID
      @param ds
   */  
export interface OnChangeBankTranBankFeeID_input{
   inBankFeeID:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangeBankTranBankFeeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param inAmtType
      @param inTaxAmt
      @param ds
   */  
export interface OnChangeBankTranTaxAmt_input{
      /**  Indicate which of the amount is changed.
            Valid values are: 'B' for Base Amount and 'D' for Doc Amount  */  
   inAmtType:string,
      /**  Proposed taxable amount value  */  
   inTaxAmt:number,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangeBankTranTaxAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param inTaxCode
      @param ds
   */  
export interface OnChangeBankTranTaxCode_input{
      /**  Proposed Tax ID  */  
   inTaxCode:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangeBankTranTaxCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param inPercent
      @param ds
   */  
export interface OnChangeBankTranTaxPercent_input{
      /**  Proposed taxable amount value  */  
   inPercent:number,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangeBankTranTaxPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param inRateCode
      @param ds
   */  
export interface OnChangeBankTranTaxRateCode_input{
      /**  Proposed RateCode value  */  
   inRateCode:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangeBankTranTaxRateCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param inAmtType
      @param inTaxableAmt
      @param ds
   */  
export interface OnChangeBankTranTaxTaxableAmt_input{
      /**  Indicate which of the amount is changed.
            Valid values are: 'B' for Base Amount and 'D' for Doc Amount  */  
   inAmtType:string,
      /**  Proposed taxable amount value  */  
   inTaxableAmt:number,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangeBankTranTaxTaxableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ipTranAmtType
      @param proposedTranAmt
      @param ds
   */  
export interface OnChangeBankTranTranAmt_input{
      /**  Indicate which of the transaction amount is changed.
            Valid values are: 'B' for Base Tran Amount and 'D' for Doc Tran Amount  */  
   ipTranAmtType:string,
      /**  The proposed Transaction Amount  */  
   proposedTranAmt:number,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangeBankTranTranAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ipApplyDate
      @param ds
   */  
export interface OnChangePCashDocApplyDate_input{
      /**  New Apply Date  */  
   ipApplyDate:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangePCashDocApplyDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ipBankAcctID
      @param ds
   */  
export interface OnChangePCashDocBankAcctID_input{
      /**  New Bank Acct ID  */  
   ipBankAcctID:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangePCashDocBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param inAmtType
      @param proposedCashAmt
      @param ds
   */  
export interface OnChangePCashDocCashAmt_input{
      /**  Indicate which of the cash amount is changed.
            Valid values are: 'B' for Base Cash Amount and 'D' for Doc Cash Amount  */  
   inAmtType:string,
      /**  The proposed Transaction Amount  */  
   proposedCashAmt:number,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangePCashDocCashAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ipCashDeskIDTransfer
      @param ds
   */  
export interface OnChangePCashDocCashDeskIDTransfer_input{
      /**  New Cash Desk ID Num  */  
   ipCashDeskIDTransfer:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangePCashDocCashDeskIDTransfer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ipCustomerID
      @param ds
   */  
export interface OnChangePCashDocCustID_input{
      /**  New Customer ID  */  
   ipCustomerID:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangePCashDocCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ipDraft
      @param ds
   */  
export interface OnChangePCashDocDraft_input{
      /**  New Draft  */  
   ipDraft:boolean,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangePCashDocDraft_output{
parameters : {
      /**  output parameters  */  
   opDateChangedMsg:string,
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ipEmployeeNum
      @param ds
   */  
export interface OnChangePCashDocEmployeeNum_input{
      /**  New Employee Num  */  
   ipEmployeeNum:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangePCashDocEmployeeNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ipExchRateDate
      @param ds
   */  
export interface OnChangePCashDocExchRateDate_input{
      /**  New Exchange Rate Date  */  
   ipExchRateDate:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangePCashDocExchRateDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ipOprTypeCode
      @param ds
   */  
export interface OnChangePCashDocOprType_input{
      /**  New Operation type code  */  
   ipOprTypeCode:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangePCashDocOprType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ipVendorID
      @param ds
   */  
export interface OnChangePCashDocVendorID_input{
      /**  New Vendor ID  */  
   ipVendorID:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface OnChangePCashDocVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param CashDeskID
      @param ReferenceNum
   */  
export interface PrePost_input{
      /**  Petty Cash Desk  */  
   CashDeskID:string,
      /**  Reference number  */  
   ReferenceNum:number,
}

export interface PrePost_output{
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Recalculate_input{
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface Recalculate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPCashEntryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPCashEntryTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param pCashDeskID
      @param pReferenceNum
   */  
export interface UpdatePCashDoc_input{
      /**  Cash Desk ID  */  
   pCashDeskID:string,
      /**  Cash Desk reference number  */  
   pReferenceNum:number,
}

export interface UpdatePCashDoc_output{
   returnObj:Erp_Tablesets_PCashEntryTableset[],
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

   /** Required : 
      @param pCashDeskId
      @param referenceNum
      @param VoidedReason
      @param ds
   */  
export interface VoidLegalNumber_input{
      /**  The cash desk ID.  */  
   pCashDeskId:string,
      /**  The reference number.  */  
   referenceNum:number,
      /**  Reason for the void  */  
   VoidedReason:string,
   ds:Erp_Tablesets_PCashEntryTableset[],
}

export interface VoidLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashEntryTableset,
}
}

