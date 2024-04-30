import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PurTermsSvc
// Description: Purchasing PurTerms master. Used by Purchase Order management and Accounts Payable modules.
DELETE: Not allowed if referenced in the Vendor, POHeader or APInvHed file.
Since the delete of a PurTerms code should be a very rare occurence, these files will not
be indexed by the code. This is done so not to put undue overhead on the system for
maintaining indexes. A Message will be displayed "Please Wait...Validating delete Request".
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get PurTerms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurTerms
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsRow
   */  
export function get_PurTerms(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurTerms
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurTermsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PurTermsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PurTerms(requestBody:Erp_Tablesets_PurTermsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PurTerm item
   Description: Calls GetByID to retrieve the PurTerm item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTerm
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PurTermsRow
   */  
export function get_PurTerms_Company_TermsCode(Company:string, TermsCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PurTermsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PurTermsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PurTerm for the service
   Description: Calls UpdateExt to update PurTerm. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurTerm
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurTermsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PurTerms_Company_TermsCode(Company:string, TermsCode:string, requestBody:Erp_Tablesets_PurTermsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")", {
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
   Summary: Call UpdateExt to delete PurTerm item
   Description: Call UpdateExt to delete PurTerm item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurTerm
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PurTerms_Company_TermsCode(Company:string, TermsCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")", {
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
   Description: Get PurTermsDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PurTermsDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsDtlRow
   */  
export function get_PurTerms_Company_TermsCode_PurTermsDtls(Company:string, TermsCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")/PurTermsDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PurTermsDtl item
   Description: Calls GetByID to retrieve the PurTermsDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTermsDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param TermsSeq Desc: TermsSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PurTermsDtlRow
   */  
export function get_PurTerms_Company_TermsCode_PurTermsDtls_Company_TermsCode_TermsSeq(Company:string, TermsCode:string, TermsSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PurTermsDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")/PurTermsDtls(" + Company + "," + TermsCode + "," + TermsSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PurTermsDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PurTermsScheds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PurTermsScheds1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsSchedRow
   */  
export function get_PurTerms_Company_TermsCode_PurTermsScheds(Company:string, TermsCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")/PurTermsScheds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PurTermsSched item
   Description: Calls GetByID to retrieve the PurTermsSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTermsSched1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param PaySeq Desc: PaySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PurTermsSchedRow
   */  
export function get_PurTerms_Company_TermsCode_PurTermsScheds_Company_TermsCode_PaySeq(Company:string, TermsCode:string, PaySeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PurTermsSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")/PurTermsScheds(" + Company + "," + TermsCode + "," + PaySeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PurTermsSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PurTermsAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PurTermsAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsAttchRow
   */  
export function get_PurTerms_Company_TermsCode_PurTermsAttches(Company:string, TermsCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")/PurTermsAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PurTermsAttch item
   Description: Calls GetByID to retrieve the PurTermsAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTermsAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PurTermsAttchRow
   */  
export function get_PurTerms_Company_TermsCode_PurTermsAttches_Company_TermsCode_DrawingSeq(Company:string, TermsCode:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PurTermsAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")/PurTermsAttches(" + Company + "," + TermsCode + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PurTermsAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PurTermsDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurTermsDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsDtlRow
   */  
export function get_PurTermsDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurTermsDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurTermsDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PurTermsDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PurTermsDtls(requestBody:Erp_Tablesets_PurTermsDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PurTermsDtl item
   Description: Calls GetByID to retrieve the PurTermsDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTermsDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param TermsSeq Desc: TermsSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PurTermsDtlRow
   */  
export function get_PurTermsDtls_Company_TermsCode_TermsSeq(Company:string, TermsCode:string, TermsSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PurTermsDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsDtls(" + Company + "," + TermsCode + "," + TermsSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PurTermsDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PurTermsDtl for the service
   Description: Calls UpdateExt to update PurTermsDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurTermsDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param TermsSeq Desc: TermsSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurTermsDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PurTermsDtls_Company_TermsCode_TermsSeq(Company:string, TermsCode:string, TermsSeq:string, requestBody:Erp_Tablesets_PurTermsDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsDtls(" + Company + "," + TermsCode + "," + TermsSeq + ")", {
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
   Summary: Call UpdateExt to delete PurTermsDtl item
   Description: Call UpdateExt to delete PurTermsDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurTermsDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param TermsSeq Desc: TermsSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PurTermsDtls_Company_TermsCode_TermsSeq(Company:string, TermsCode:string, TermsSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsDtls(" + Company + "," + TermsCode + "," + TermsSeq + ")", {
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
   Description: Get PurTermsScheds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurTermsScheds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsSchedRow
   */  
export function get_PurTermsScheds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsScheds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurTermsScheds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurTermsSchedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PurTermsSchedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PurTermsScheds(requestBody:Erp_Tablesets_PurTermsSchedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsScheds", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PurTermsSched item
   Description: Calls GetByID to retrieve the PurTermsSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTermsSched
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param PaySeq Desc: PaySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PurTermsSchedRow
   */  
export function get_PurTermsScheds_Company_TermsCode_PaySeq(Company:string, TermsCode:string, PaySeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PurTermsSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsScheds(" + Company + "," + TermsCode + "," + PaySeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PurTermsSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PurTermsSched for the service
   Description: Calls UpdateExt to update PurTermsSched. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurTermsSched
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param PaySeq Desc: PaySeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurTermsSchedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PurTermsScheds_Company_TermsCode_PaySeq(Company:string, TermsCode:string, PaySeq:string, requestBody:Erp_Tablesets_PurTermsSchedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsScheds(" + Company + "," + TermsCode + "," + PaySeq + ")", {
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
   Summary: Call UpdateExt to delete PurTermsSched item
   Description: Call UpdateExt to delete PurTermsSched item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurTermsSched
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param PaySeq Desc: PaySeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PurTermsScheds_Company_TermsCode_PaySeq(Company:string, TermsCode:string, PaySeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsScheds(" + Company + "," + TermsCode + "," + PaySeq + ")", {
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
   Description: Get PurTermsAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurTermsAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsAttchRow
   */  
export function get_PurTermsAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurTermsAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurTermsAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PurTermsAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PurTermsAttches(requestBody:Erp_Tablesets_PurTermsAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PurTermsAttch item
   Description: Calls GetByID to retrieve the PurTermsAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTermsAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PurTermsAttchRow
   */  
export function get_PurTermsAttches_Company_TermsCode_DrawingSeq(Company:string, TermsCode:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PurTermsAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsAttches(" + Company + "," + TermsCode + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PurTermsAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PurTermsAttch for the service
   Description: Calls UpdateExt to update PurTermsAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurTermsAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurTermsAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PurTermsAttches_Company_TermsCode_DrawingSeq(Company:string, TermsCode:string, DrawingSeq:string, requestBody:Erp_Tablesets_PurTermsAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsAttches(" + Company + "," + TermsCode + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PurTermsAttch item
   Description: Call UpdateExt to delete PurTermsAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurTermsAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TermsCode Desc: TermsCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PurTermsAttches_Company_TermsCode_DrawingSeq(Company:string, TermsCode:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsAttches(" + Company + "," + TermsCode + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePurTerms:string, whereClausePurTermsAttch:string, whereClausePurTermsDtl:string, whereClausePurTermsSched:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePurTerms!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePurTerms=" + whereClausePurTerms
   }
   if(typeof whereClausePurTermsAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePurTermsAttch=" + whereClausePurTermsAttch
   }
   if(typeof whereClausePurTermsDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePurTermsDtl=" + whereClausePurTermsDtl
   }
   if(typeof whereClausePurTermsSched!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePurTermsSched=" + whereClausePurTermsSched
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(termsCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof termsCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "termsCode=" + termsCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method OnChangingDisDays
   Description: Purpose:
Parameters:  none
Notes:
<param name="vDueOnDay">Propose Discount Days</param><param name="ds">Temporary tables for PurTerms details</param>
   OperationID: OnChangingDisDays
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingDisDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDisDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingDisDays(requestBody:OnChangingDisDays_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingDisDays_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/OnChangingDisDays", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingDisDays_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingDisPercent
   Description: Purpose:
Parameters:  none
Notes:
<param name="vDiscountPercent">Propose Discount Days</param><param name="ds">Temporary tables for PurTerms details</param>
   OperationID: OnChangingDisPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingDisPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDisPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingDisPercent(requestBody:OnChangingDisPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingDisPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/OnChangingDisPercent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingDisPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumOfDays
   Description: Purpose:
Parameters:  none
Notes:
<param name="vNumOfDay">Propose Discount Days</param><param name="ds">Temporary tables for PurTerms details</param>
   OperationID: OnChangingNumOfDays
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingNumOfDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumOfDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumOfDays(requestBody:OnChangingNumOfDays_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingNumOfDays_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/OnChangingNumOfDays", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingNumOfDays_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumOfMonths
   Description: Purpose:
Parameters:  none
Notes:
<param name="vNumOfMonths">Propose Discount Days</param><param name="ds">Temporary tables for PurTerms details</param>
   OperationID: OnChangingNumOfMonths
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingNumOfMonths_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumOfMonths_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumOfMonths(requestBody:OnChangingNumOfMonths_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingNumOfMonths_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/OnChangingNumOfMonths", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingNumOfMonths_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingTermDueOnDay
   Description: Purpose:
Parameters:  none
Notes:
<param name="pDueOnDay">Propose Discount Days</param>
   OperationID: OnChangingTermDueOnDay
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingTermDueOnDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTermDueOnDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingTermDueOnDay(requestBody:OnChangingTermDueOnDay_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingTermDueOnDay_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/OnChangingTermDueOnDay", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingTermDueOnDay_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPurTermsSched
   OperationID: GetPurTermsSched
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPurTermsSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPurTermsSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPurTermsSched(requestBody:GetPurTermsSched_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPurTermsSched_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/GetPurTermsSched", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPurTermsSched_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTermsTypeCodeDescList
   Description: Purpose: Gets list of codes/descriptions for TermsType combo-box
Parameters: none
   OperationID: GetTermsTypeCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTermsTypeCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTermsTypeCodeDescList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTermsTypeCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/GetTermsTypeCodeDescList", {
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
         resolve(data as GetTermsTypeCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnPurTermsSchedPercentageUpdate
   Description: Called on PurTermsSched.PayPercentage update
   OperationID: OnPurTermsSchedPercentageUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnPurTermsSchedPercentageUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPurTermsSchedPercentageUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnPurTermsSchedPercentageUpdate(requestBody:OnPurTermsSchedPercentageUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnPurTermsSchedPercentageUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/OnPurTermsSchedPercentageUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnPurTermsSchedPercentageUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateDiscountPercent
   Description: This method will check if current discount percent is less or greater than previous or next discounts and send a warning message.
   OperationID: ValidateDiscountPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateDiscountPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDiscountPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateDiscountPercent(requestBody:ValidateDiscountPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateDiscountPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/ValidateDiscountPercent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateDiscountPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnPurTermsSchedPercentageUpdate2
   OperationID: OnPurTermsSchedPercentageUpdate2
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnPurTermsSchedPercentageUpdate2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPurTermsSchedPercentageUpdate2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnPurTermsSchedPercentageUpdate2(requestBody:OnPurTermsSchedPercentageUpdate2_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnPurTermsSchedPercentageUpdate2_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/OnPurTermsSchedPercentageUpdate2", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnPurTermsSchedPercentageUpdate2_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPurTerms
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurTerms
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPurTerms_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurTerms_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPurTerms(requestBody:GetNewPurTerms_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPurTerms_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/GetNewPurTerms", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPurTerms_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPurTermsAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurTermsAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPurTermsAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurTermsAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPurTermsAttch(requestBody:GetNewPurTermsAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPurTermsAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/GetNewPurTermsAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPurTermsAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPurTermsDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurTermsDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPurTermsDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurTermsDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPurTermsDtl(requestBody:GetNewPurTermsDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPurTermsDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/GetNewPurTermsDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPurTermsDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPurTermsSched
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurTermsSched
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPurTermsSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurTermsSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPurTermsSched(requestBody:GetNewPurTermsSched_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPurTermsSched_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/GetNewPurTermsSched", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPurTermsSched_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PurTermsAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PurTermsDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PurTermsListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PurTermsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsSchedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PurTermsSchedRow,
}

export interface Erp_Tablesets_PurTermsAttchRow{
   "Company":string,
   "TermsCode":string,
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

export interface Erp_Tablesets_PurTermsDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the terms assigned by the user.  */  
   "TermsCode":string,
      /**  Sequence Counter to allow multiple Discounts  */  
   "TermsSeq":number,
      /**  Used for Discount Type (Day of Months)  */  
   "DueOnDay":number,
      /**   The discount percentage given for prompt payment of an invoice.
Invoice printing uses this value to calculate a prompt payment discount amount.  */  
   "DiscountPercent":number,
      /**  Used for Terms Type (X Month Y Days)  */  
   "NumberOfMonths":number,
      /**  Used for Terms Type (X Months + Y Days)  */  
   "NumberOfDays":number,
      /**  Used for Disc Type (Days of Month)  */  
   "MinimumDays":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PurTermsListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Purchase Terms code master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TermsCode":string,
      /**  System Default Term  */  
   "SysDefault":boolean,
      /**  This field define the type of the term.  */  
   "TermsType":string,
      /**  Full description of terms....this is printed on purchase orders. Can't be blank.  */  
   "Description":string,
      /**  This field is used in invoice entry to calculate the due date of the invoice.  For "Monthly" terms this is the number of days from the end of the invoice's month that the invoice is due.  */  
   "DueDays":number,
      /**  Number of days in which payment discount can be earned.  Invoice entry uses this value to calculate a discount due date.  */  
   "DiscountDays":number,
      /**   OBSOLETE FIELD The discount percentage given for prompt payment of invoice.
Invoice entry uses this value to calculate a prompt payment discount amount.  */  
   "DiscountPercent":number,
      /**  An optional entry which if used defines the # of installment payments that will be made for invoices using the specific terms. Invoicing will generate due dates and disburse the invoice total into equal corresponding amounts based on this value.  */  
   "NumberOfPayments":number,
      /**  Indicates that the due date is calculated on a monthly basis instead of a strict number of days from the invoice date.  */  
   "Monthly":boolean,
      /**  Used for Terms Type (X Months + Y Days)  */  
   "NumberOfDays":number,
      /**  Used for Terms Type (Day of Month)  */  
   "MinimumDays":number,
      /**  Used for Tems Type (Day of Months)  */  
   "DueOnDay":number,
      /**  Used for Terms Type (X Months + Y Days)  */  
   "NumberOfMonths":number,
      /**  This field defines the type of the Discount  */  
   "DiscountType":string,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   "PartPayment":boolean,
      /**  Require Letter of Credit.  */  
   "ReqLOC":boolean,
      /**  Marks this PurTerms as global, available to be sent out to other companies.  */  
   "GlobalPurTerms":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Months In Future  */  
   "MonthsInFuture":number,
      /**  DueDayOfMonth  */  
   "DueDayOfMonth":number,
      /**  Indicate if the Purchase Term is default  */  
   "IsDefault":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PurTermsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Purchase Terms code master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TermsCode":string,
      /**  System Default Term  */  
   "SysDefault":boolean,
      /**  This field define the type of the term.  */  
   "TermsType":string,
      /**  Full description of terms....this is printed on purchase orders. Can't be blank.  */  
   "Description":string,
      /**  This field is used in invoice entry to calculate the due date of the invoice.  For "Monthly" terms this is the number of days from the end of the invoice's month that the invoice is due.  */  
   "DueDays":number,
      /**  Number of days in which payment discount can be earned.  Invoice entry uses this value to calculate a discount due date.  */  
   "DiscountDays":number,
      /**   OBSOLETE FIELD The discount percentage given for prompt payment of invoice.
Invoice entry uses this value to calculate a prompt payment discount amount.  */  
   "DiscountPercent":number,
      /**  An optional entry which if used defines the # of installment payments that will be made for invoices using the specific terms. Invoicing will generate due dates and disburse the invoice total into equal corresponding amounts based on this value.  */  
   "NumberOfPayments":number,
      /**  Indicates that the due date is calculated on a monthly basis instead of a strict number of days from the invoice date.  */  
   "Monthly":boolean,
      /**  Used for Terms Type (X Months + Y Days)  */  
   "NumberOfDays":number,
      /**  Used for Terms Type (Day of Month)  */  
   "MinimumDays":number,
      /**  Used for Tems Type (Day of Months)  */  
   "DueOnDay":number,
      /**  Used for Terms Type (X Months + Y Days)  */  
   "NumberOfMonths":number,
      /**  This field defines the type of the Discount  */  
   "DiscountType":string,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   "PartPayment":boolean,
      /**  Require Letter of Credit.  */  
   "ReqLOC":boolean,
      /**  Marks this PurTerms as global, available to be sent out to other companies.  */  
   "GlobalPurTerms":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  COIFRSCalculation  */  
   "COIFRSCalculation":boolean,
      /**  COIFRSNumberOfPeriods  */  
   "COIFRSNumberOfPeriods":number,
      /**  Months In Future  */  
   "MonthsInFuture":number,
      /**  DueDayOfMonth  */  
   "DueDayOfMonth":number,
      /**  Indicate if the Purchase Term is default  */  
   "IsDefault":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PurTermsSchedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the terms assigned by the user.  */  
   "TermsCode":string,
      /**  Specifies the number of payment of the Payment Schedule. This is an auto-generated sequence number.  */  
   "PaySeq":number,
      /**  Specifies the number of days for the payment to be paid. This is used to calculate Due Date in Invoice Payment Schedule.  */  
   "Days":number,
      /**  Specifies the percent of the payment to be paid. This is used to calculate amount to be paid per payment in Purchase Order and Invoice Payment Sechedule.  */  
   "PayPercent":number,
      /**  Userid of user who created this record.  */  
   "CreatedBy":string,
      /**  The date that the record was created.  */  
   "CreatedOn":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangedOn":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
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
      @param termsCode
   */  
export interface DeleteByID_input{
   termsCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PurTermsAttchRow{
   Company:string,
   TermsCode:string,
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

export interface Erp_Tablesets_PurTermsDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the terms assigned by the user.  */  
   TermsCode:string,
      /**  Sequence Counter to allow multiple Discounts  */  
   TermsSeq:number,
      /**  Used for Discount Type (Day of Months)  */  
   DueOnDay:number,
      /**   The discount percentage given for prompt payment of an invoice.
Invoice printing uses this value to calculate a prompt payment discount amount.  */  
   DiscountPercent:number,
      /**  Used for Terms Type (X Month Y Days)  */  
   NumberOfMonths:number,
      /**  Used for Terms Type (X Months + Y Days)  */  
   NumberOfDays:number,
      /**  Used for Disc Type (Days of Month)  */  
   MinimumDays:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PurTermsListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Purchase Terms code master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TermsCode:string,
      /**  System Default Term  */  
   SysDefault:boolean,
      /**  This field define the type of the term.  */  
   TermsType:string,
      /**  Full description of terms....this is printed on purchase orders. Can't be blank.  */  
   Description:string,
      /**  This field is used in invoice entry to calculate the due date of the invoice.  For "Monthly" terms this is the number of days from the end of the invoice's month that the invoice is due.  */  
   DueDays:number,
      /**  Number of days in which payment discount can be earned.  Invoice entry uses this value to calculate a discount due date.  */  
   DiscountDays:number,
      /**   OBSOLETE FIELD The discount percentage given for prompt payment of invoice.
Invoice entry uses this value to calculate a prompt payment discount amount.  */  
   DiscountPercent:number,
      /**  An optional entry which if used defines the # of installment payments that will be made for invoices using the specific terms. Invoicing will generate due dates and disburse the invoice total into equal corresponding amounts based on this value.  */  
   NumberOfPayments:number,
      /**  Indicates that the due date is calculated on a monthly basis instead of a strict number of days from the invoice date.  */  
   Monthly:boolean,
      /**  Used for Terms Type (X Months + Y Days)  */  
   NumberOfDays:number,
      /**  Used for Terms Type (Day of Month)  */  
   MinimumDays:number,
      /**  Used for Tems Type (Day of Months)  */  
   DueOnDay:number,
      /**  Used for Terms Type (X Months + Y Days)  */  
   NumberOfMonths:number,
      /**  This field defines the type of the Discount  */  
   DiscountType:string,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PartPayment:boolean,
      /**  Require Letter of Credit.  */  
   ReqLOC:boolean,
      /**  Marks this PurTerms as global, available to be sent out to other companies.  */  
   GlobalPurTerms:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Months In Future  */  
   MonthsInFuture:number,
      /**  DueDayOfMonth  */  
   DueDayOfMonth:number,
      /**  Indicate if the Purchase Term is default  */  
   IsDefault:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PurTermsListTableset{
   PurTermsList:Erp_Tablesets_PurTermsListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PurTermsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Purchase Terms code master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TermsCode:string,
      /**  System Default Term  */  
   SysDefault:boolean,
      /**  This field define the type of the term.  */  
   TermsType:string,
      /**  Full description of terms....this is printed on purchase orders. Can't be blank.  */  
   Description:string,
      /**  This field is used in invoice entry to calculate the due date of the invoice.  For "Monthly" terms this is the number of days from the end of the invoice's month that the invoice is due.  */  
   DueDays:number,
      /**  Number of days in which payment discount can be earned.  Invoice entry uses this value to calculate a discount due date.  */  
   DiscountDays:number,
      /**   OBSOLETE FIELD The discount percentage given for prompt payment of invoice.
Invoice entry uses this value to calculate a prompt payment discount amount.  */  
   DiscountPercent:number,
      /**  An optional entry which if used defines the # of installment payments that will be made for invoices using the specific terms. Invoicing will generate due dates and disburse the invoice total into equal corresponding amounts based on this value.  */  
   NumberOfPayments:number,
      /**  Indicates that the due date is calculated on a monthly basis instead of a strict number of days from the invoice date.  */  
   Monthly:boolean,
      /**  Used for Terms Type (X Months + Y Days)  */  
   NumberOfDays:number,
      /**  Used for Terms Type (Day of Month)  */  
   MinimumDays:number,
      /**  Used for Tems Type (Day of Months)  */  
   DueOnDay:number,
      /**  Used for Terms Type (X Months + Y Days)  */  
   NumberOfMonths:number,
      /**  This field defines the type of the Discount  */  
   DiscountType:string,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PartPayment:boolean,
      /**  Require Letter of Credit.  */  
   ReqLOC:boolean,
      /**  Marks this PurTerms as global, available to be sent out to other companies.  */  
   GlobalPurTerms:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  COIFRSCalculation  */  
   COIFRSCalculation:boolean,
      /**  COIFRSNumberOfPeriods  */  
   COIFRSNumberOfPeriods:number,
      /**  Months In Future  */  
   MonthsInFuture:number,
      /**  DueDayOfMonth  */  
   DueDayOfMonth:number,
      /**  Indicate if the Purchase Term is default  */  
   IsDefault:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PurTermsSchedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the terms assigned by the user.  */  
   TermsCode:string,
      /**  Specifies the number of payment of the Payment Schedule. This is an auto-generated sequence number.  */  
   PaySeq:number,
      /**  Specifies the number of days for the payment to be paid. This is used to calculate Due Date in Invoice Payment Schedule.  */  
   Days:number,
      /**  Specifies the percent of the payment to be paid. This is used to calculate amount to be paid per payment in Purchase Order and Invoice Payment Sechedule.  */  
   PayPercent:number,
      /**  Userid of user who created this record.  */  
   CreatedBy:string,
      /**  The date that the record was created.  */  
   CreatedOn:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangedOn:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PurTermsTableset{
   PurTerms:Erp_Tablesets_PurTermsRow[],
   PurTermsAttch:Erp_Tablesets_PurTermsAttchRow[],
   PurTermsDtl:Erp_Tablesets_PurTermsDtlRow[],
   PurTermsSched:Erp_Tablesets_PurTermsSchedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPurTermsTableset{
   PurTerms:Erp_Tablesets_PurTermsRow[],
   PurTermsAttch:Erp_Tablesets_PurTermsAttchRow[],
   PurTermsDtl:Erp_Tablesets_PurTermsDtlRow[],
   PurTermsSched:Erp_Tablesets_PurTermsSchedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param termsCode
   */  
export interface GetByID_input{
   termsCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PurTermsTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PurTermsTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PurTermsTableset[],
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
   returnObj:Erp_Tablesets_PurTermsListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param termsCode
   */  
export interface GetNewPurTermsAttch_input{
   ds:Erp_Tablesets_PurTermsTableset[],
   termsCode:string,
}

export interface GetNewPurTermsAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurTermsTableset,
}
}

   /** Required : 
      @param ds
      @param termsCode
   */  
export interface GetNewPurTermsDtl_input{
   ds:Erp_Tablesets_PurTermsTableset[],
   termsCode:string,
}

export interface GetNewPurTermsDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurTermsTableset,
}
}

   /** Required : 
      @param ds
      @param termsCode
   */  
export interface GetNewPurTermsSched_input{
   ds:Erp_Tablesets_PurTermsTableset[],
   termsCode:string,
}

export interface GetNewPurTermsSched_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurTermsTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPurTerms_input{
   ds:Erp_Tablesets_PurTermsTableset[],
}

export interface GetNewPurTerms_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurTermsTableset,
}
}

   /** Required : 
      @param termsCode
      @param purTermsSchedTable
   */  
export interface GetPurTermsSched_input{
   termsCode:string,
   purTermsSchedTable:object
}

export interface GetPurTermsSched_output{
parameters : {
      /**  output parameters  */  
   purTermsSchedTable:any[],
}
}

   /** Required : 
      @param whereClausePurTerms
      @param whereClausePurTermsAttch
      @param whereClausePurTermsDtl
      @param whereClausePurTermsSched
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePurTerms:string,
   whereClausePurTermsAttch:string,
   whereClausePurTermsDtl:string,
   whereClausePurTermsSched:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PurTermsTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetTermsTypeCodeDescList_output{
      /**  List of Terms Type codes/descriptions  */  
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
      @param vDueOnDay
      @param ds
   */  
export interface OnChangingDisDays_input{
   vDueOnDay:number,
   ds:Erp_Tablesets_PurTermsTableset[],
}

export interface OnChangingDisDays_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurTermsTableset,
}
}

   /** Required : 
      @param vDiscountPercent
      @param ds
   */  
export interface OnChangingDisPercent_input{
   vDiscountPercent:number,
   ds:Erp_Tablesets_PurTermsTableset[],
}

export interface OnChangingDisPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurTermsTableset,
}
}

   /** Required : 
      @param vNumOfDay
      @param ds
   */  
export interface OnChangingNumOfDays_input{
   vNumOfDay:number,
   ds:Erp_Tablesets_PurTermsTableset[],
}

export interface OnChangingNumOfDays_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurTermsTableset,
}
}

   /** Required : 
      @param vNumOfMonths
      @param ds
   */  
export interface OnChangingNumOfMonths_input{
   vNumOfMonths:number,
   ds:Erp_Tablesets_PurTermsTableset[],
}

export interface OnChangingNumOfMonths_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurTermsTableset,
}
}

   /** Required : 
      @param pDueOnDay
   */  
export interface OnChangingTermDueOnDay_input{
   pDueOnDay:number,
}

export interface OnChangingTermDueOnDay_output{
}

   /** Required : 
      @param ds
   */  
export interface OnPurTermsSchedPercentageUpdate2_input{
   ds:Erp_Tablesets_PurTermsTableset[],
}

export interface OnPurTermsSchedPercentageUpdate2_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurTermsTableset,
}
}

   /** Required : 
      @param ts
   */  
export interface OnPurTermsSchedPercentageUpdate_input{
   ts:Erp_Tablesets_PurTermsTableset[],
}

export interface OnPurTermsSchedPercentageUpdate_output{
parameters : {
      /**  output parameters  */  
   ts:Erp_Tablesets_PurTermsTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPurTermsTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPurTermsTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PurTermsTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurTermsTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateDiscountPercent_input{
   ds:Erp_Tablesets_PurTermsTableset[],
}

export interface ValidateDiscountPercent_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurTermsTableset,
   warningMessage:string,
}
}

