import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PartAllocRuleClassSvc
// Description: PartAllocRuleClassSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get PartAllocRuleClasses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartAllocRuleClasses
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocRuleClassRow
   */  
export function get_PartAllocRuleClasses(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartAllocRuleClasses
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartAllocRuleClassRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartAllocRuleClasses(requestBody:Erp_Tablesets_PartAllocRuleClassRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PartAllocRuleClass item
   Description: Calls GetByID to retrieve the PartAllocRuleClass item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAllocRuleClass
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RuleClassID Desc: RuleClassID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartAllocRuleClassRow
   */  
export function get_PartAllocRuleClasses_Company_RuleClassID(Company:string, RuleClassID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartAllocRuleClassRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses(" + Company + "," + RuleClassID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PartAllocRuleClassRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartAllocRuleClass for the service
   Description: Calls UpdateExt to update PartAllocRuleClass. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartAllocRuleClass
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RuleClassID Desc: RuleClassID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartAllocRuleClasses_Company_RuleClassID(Company:string, RuleClassID:string, requestBody:Erp_Tablesets_PartAllocRuleClassRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses(" + Company + "," + RuleClassID + ")", {
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
   Summary: Call UpdateExt to delete PartAllocRuleClass item
   Description: Call UpdateExt to delete PartAllocRuleClass item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartAllocRuleClass
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RuleClassID Desc: RuleClassID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartAllocRuleClasses_Company_RuleClassID(Company:string, RuleClassID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses(" + Company + "," + RuleClassID + ")", {
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
   Description: Get PartAllocRuleClassDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartAllocRuleClassDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RuleClassID Desc: RuleClassID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocRuleClassDtlRow
   */  
export function get_PartAllocRuleClasses_Company_RuleClassID_PartAllocRuleClassDtls(Company:string, RuleClassID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses(" + Company + "," + RuleClassID + ")/PartAllocRuleClassDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartAllocRuleClassDtl item
   Description: Calls GetByID to retrieve the PartAllocRuleClassDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAllocRuleClassDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RuleClassID Desc: RuleClassID   Required: True   Allow empty value : True
      @param RuleID Desc: RuleID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartAllocRuleClassDtlRow
   */  
export function get_PartAllocRuleClasses_Company_RuleClassID_PartAllocRuleClassDtls_Company_RuleClassID_RuleID(Company:string, RuleClassID:string, RuleID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartAllocRuleClassDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses(" + Company + "," + RuleClassID + ")/PartAllocRuleClassDtls(" + Company + "," + RuleClassID + "," + RuleID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PartAllocRuleClassDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PartAllocRuleClassDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartAllocRuleClassDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocRuleClassDtlRow
   */  
export function get_PartAllocRuleClassDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClassDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartAllocRuleClassDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartAllocRuleClassDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartAllocRuleClassDtls(requestBody:Erp_Tablesets_PartAllocRuleClassDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClassDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PartAllocRuleClassDtl item
   Description: Calls GetByID to retrieve the PartAllocRuleClassDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAllocRuleClassDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RuleClassID Desc: RuleClassID   Required: True   Allow empty value : True
      @param RuleID Desc: RuleID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartAllocRuleClassDtlRow
   */  
export function get_PartAllocRuleClassDtls_Company_RuleClassID_RuleID(Company:string, RuleClassID:string, RuleID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartAllocRuleClassDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClassDtls(" + Company + "," + RuleClassID + "," + RuleID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PartAllocRuleClassDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartAllocRuleClassDtl for the service
   Description: Calls UpdateExt to update PartAllocRuleClassDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartAllocRuleClassDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RuleClassID Desc: RuleClassID   Required: True   Allow empty value : True
      @param RuleID Desc: RuleID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartAllocRuleClassDtls_Company_RuleClassID_RuleID(Company:string, RuleClassID:string, RuleID:string, requestBody:Erp_Tablesets_PartAllocRuleClassDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClassDtls(" + Company + "," + RuleClassID + "," + RuleID + ")", {
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
   Summary: Call UpdateExt to delete PartAllocRuleClassDtl item
   Description: Call UpdateExt to delete PartAllocRuleClassDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartAllocRuleClassDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RuleClassID Desc: RuleClassID   Required: True   Allow empty value : True
      @param RuleID Desc: RuleID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartAllocRuleClassDtls_Company_RuleClassID_RuleID(Company:string, RuleClassID:string, RuleID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClassDtls(" + Company + "," + RuleClassID + "," + RuleID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocRuleClassListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassListRow)
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
export function get_GetRows(whereClausePartAllocRuleClass:string, whereClausePartAllocRuleClassDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartAllocRuleClass!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartAllocRuleClass=" + whereClausePartAllocRuleClass
   }
   if(typeof whereClausePartAllocRuleClassDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartAllocRuleClassDtl=" + whereClausePartAllocRuleClassDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(ruleClassID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ruleClassID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ruleClassID=" + ruleClassID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method CopyPartAllocRuleClass
   Description: Copies the current rule class and all rules to a new rule class of the specified name.
   OperationID: CopyPartAllocRuleClass
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyPartAllocRuleClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyPartAllocRuleClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyPartAllocRuleClass(requestBody:CopyPartAllocRuleClass_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyPartAllocRuleClass_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/CopyPartAllocRuleClass", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CopyPartAllocRuleClass_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartAllocRuleClassActive
   Description: Invoked when the PartAllocRuleClass Active flag is changed.  Returns a warning message string if there are potential issues with the rules
   OperationID: OnChangePartAllocRuleClassActive
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartAllocRuleClassActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartAllocRuleClassActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartAllocRuleClassActive(requestBody:OnChangePartAllocRuleClassActive_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartAllocRuleClassActive_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/OnChangePartAllocRuleClassActive", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePartAllocRuleClassActive_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartAllocRuleClassDtlAction
   Description: Invoked when PartAllocRuleClassDtl Action is changed.
   OperationID: OnChangePartAllocRuleClassDtlAction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartAllocRuleClassDtlAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartAllocRuleClassDtlAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartAllocRuleClassDtlAction(requestBody:OnChangePartAllocRuleClassDtlAction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartAllocRuleClassDtlAction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/OnChangePartAllocRuleClassDtlAction", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePartAllocRuleClassDtlAction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartAllocRuleClassDtlAllocTemplateID
   Description: Invoked when PartAllocRuleClassDtl AllocTemplateID is changed.
   OperationID: OnChangePartAllocRuleClassDtlAllocTemplateID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartAllocRuleClassDtlAllocTemplateID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartAllocRuleClassDtlAllocTemplateID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartAllocRuleClassDtlAllocTemplateID(requestBody:OnChangePartAllocRuleClassDtlAllocTemplateID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartAllocRuleClassDtlAllocTemplateID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/OnChangePartAllocRuleClassDtlAllocTemplateID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePartAllocRuleClassDtlAllocTemplateID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartAllocRuleClassDtlMasterRuleID
   Description: Invoked when MasterRuleID is changed.  Updates fields from PartAllocRuleMasterDtl
   OperationID: OnChangePartAllocRuleClassDtlMasterRuleID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartAllocRuleClassDtlMasterRuleID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartAllocRuleClassDtlMasterRuleID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartAllocRuleClassDtlMasterRuleID(requestBody:OnChangePartAllocRuleClassDtlMasterRuleID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartAllocRuleClassDtlMasterRuleID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/OnChangePartAllocRuleClassDtlMasterRuleID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePartAllocRuleClassDtlMasterRuleID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartAllocRuleClassDtlMasterDtlSync
   Description: Invoked when MasterDtlSync is set true. Updates fields from PartAllocRuleMasterDtl
   OperationID: OnChangePartAllocRuleClassDtlMasterDtlSync
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartAllocRuleClassDtlMasterDtlSync_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartAllocRuleClassDtlMasterDtlSync_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartAllocRuleClassDtlMasterDtlSync(requestBody:OnChangePartAllocRuleClassDtlMasterDtlSync_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartAllocRuleClassDtlMasterDtlSync_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/OnChangePartAllocRuleClassDtlMasterDtlSync", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePartAllocRuleClassDtlMasterDtlSync_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartAllocRuleClassDtlQueryID
   Description: Invoked when PartAllocRuleClassDtl QueryID is changed.  Query must have PartAllocQueueInfo as its first table.
   OperationID: OnChangePartAllocRuleClassDtlQueryID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartAllocRuleClassDtlQueryID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartAllocRuleClassDtlQueryID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartAllocRuleClassDtlQueryID(requestBody:OnChangePartAllocRuleClassDtlQueryID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartAllocRuleClassDtlQueryID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/OnChangePartAllocRuleClassDtlQueryID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePartAllocRuleClassDtlQueryID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildTree
   Description: Returns a DataSet with information required to build the Data and Functions trees in Expression Editor
   OperationID: BuildTree
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildTree(requestBody:BuildTree_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildTree_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/BuildTree", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildTree_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSyntax
   Description: Invoked from Expression Editor. Checks the syntax of the formula. If a query is defined the joins are extracted from the BAQ.
   OperationID: CheckSyntax
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckSyntax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSyntax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSyntax(requestBody:CheckSyntax_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckSyntax_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/CheckSyntax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckSyntax_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TestFulfillmentRuleClass
   Description: Called from Automated Fulfillment Rule Entry to test the execution of a Rule Class.
1) After each rule is executed, a snapshot of PartAllocQueueInfo is taken stamped with the RuleClassID and RuleID
2) Log entries that would be written to the Automated Fulfillment Process log during the execution of the Rule are written to a file called AutomatedFulfillmentRuleTester.log.
   OperationID: TestFulfillmentRuleClass
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/TestFulfillmentRuleClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestFulfillmentRuleClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestFulfillmentRuleClass(requestBody:TestFulfillmentRuleClass_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<TestFulfillmentRuleClass_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/TestFulfillmentRuleClass", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as TestFulfillmentRuleClass_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFulfillmentRuleTesterTableset
   Description: Called from Automated Fulfillment Rule Entry to display a snapshot of PartAllocQueueInfo taken after the execution of the Rule
   OperationID: GetFulfillmentRuleTesterTableset
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFulfillmentRuleTesterTableset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFulfillmentRuleTesterTableset_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFulfillmentRuleTesterTableset(requestBody:GetFulfillmentRuleTesterTableset_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFulfillmentRuleTesterTableset_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/GetFulfillmentRuleTesterTableset", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetFulfillmentRuleTesterTableset_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartAllocRuleClass
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartAllocRuleClass
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartAllocRuleClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartAllocRuleClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartAllocRuleClass(requestBody:GetNewPartAllocRuleClass_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartAllocRuleClass_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/GetNewPartAllocRuleClass", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPartAllocRuleClass_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartAllocRuleClassDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartAllocRuleClassDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartAllocRuleClassDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartAllocRuleClassDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartAllocRuleClassDtl(requestBody:GetNewPartAllocRuleClassDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartAllocRuleClassDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/GetNewPartAllocRuleClassDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPartAllocRuleClassDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartAllocRuleClassDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartAllocRuleClassListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartAllocRuleClassRow,
}

export interface Erp_Tablesets_PartAllocRuleClassDtlRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Rule Class ID  */  
   "RuleClassID":string,
      /**  Unique ID of Rule  */  
   "RuleID":string,
      /**  Description of the rule  */  
   "Description":string,
      /**  The sequence that the rules are processed in  */  
   "Sequence":number,
      /**  QueryID of a BAQ used to join other tables to the PartAllocQueueInfo  */  
   "QueryID":string,
      /**  The action that is executed for this rule  */  
   "Action":string,
      /**  Indicates if the Rule is Active  */  
   "Active":boolean,
      /**  Indicates the PartAllocTemplate to use when allocating  */  
   "AllocTemplateID":string,
      /**  The formula defined for this rule  */  
   "Formula":string,
      /**  Indicates if changes made to Reusable Rule are synchronized to this class rule  */  
   "MasterDtlSync":boolean,
      /**  Reusable master rule linked to this class rule.  */  
   "MasterRuleID":string,
      /**  Used to determine whether or not we (re)calculate fulfillment values following the return of the results of a search.  */  
   "RuleCalcFulfillOnSearch":boolean,
      /**  When TRUE the fulfillment calculations and actions will consider the Demand Warehouse only.  When false, all warehouses will be considered in fulfillment calculations, and the user will be able to choose on Reserve actions whether to consider only the Primary Warehouse or all warehouses.  */  
   "RuleUseDemandWhseOnly":boolean,
      /**  Following the execution of an action (Reserve, Allocate, Release for Picking, Unreserve, Unallocate), when true we will only refresh the rows that were actioned on, when false we will refresh all records.  */  
   "RuleLimitedRefresh":boolean,
      /**  DevCharacter01  */  
   "DevCharacter01":string,
      /**  DevDecimal01  */  
   "DevDecimal01":number,
      /**  DevBoolean01  */  
   "DevBoolean01":boolean,
      /**  DevDate01  */  
   "DevDate01":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  The type of allocation based on the Action.  Valid Values:  Order, Job, Transfer, or blank.  */  
   "AllocDemandType":string,
      /**  Indicates if the AllocationTemplate field should be enabled  */  
   "EnableAllocTemplateID":boolean,
      /**  Indicates if the user is able to enter a formula  */  
   "EnableFormula":boolean,
      /**  Indicates if the QueryID field should be enabled  */  
   "EnableQueryID":boolean,
      /**  Indicates if an Active SysTask exists for this rule class.  */  
   "ActiveSysTaskExists":boolean,
   "BitFlag":number,
   "PartAllocRuleMasterDtlFormula":string,
   "PartAllocRuleMasterDtlAction":string,
   "PartAllocRuleMasterDtlAllocTemplateID":string,
   "PartAllocRuleMasterDtlQueryID":string,
   "PartAllocRuleMasterDtlDescription":string,
   "PartAllocTemplateAllocTemplateDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartAllocRuleClassListRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Rule Class ID  */  
   "RuleClassID":string,
      /**  Description of the rule class  */  
   "Description":string,
      /**  Indicates if the Rule Class is Active  */  
   "Active":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartAllocRuleClassRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Rule Class ID  */  
   "RuleClassID":string,
      /**  Description of the rule class  */  
   "Description":string,
      /**  Indicates if the Rule Class is Active  */  
   "Active":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
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
      @param action
      @param queryID
   */  
export interface BuildTree_input{
   action:string,
   queryID:string,
}

export interface BuildTree_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param action
      @param queryID
      @param formula
      @param ruleClassID
   */  
export interface CheckSyntax_input{
   action:string,
   queryID:string,
   formula:string,
   ruleClassID:string,
}

export interface CheckSyntax_output{
}

   /** Required : 
      @param ruleClassID
      @param newRuleClassID
      @param newRuleClassDescription
   */  
export interface CopyPartAllocRuleClass_input{
   ruleClassID:string,
   newRuleClassID:string,
   newRuleClassDescription:string,
}

export interface CopyPartAllocRuleClass_output{
   returnObj:Erp_Tablesets_PartAllocRuleClassTableset[],
}

   /** Required : 
      @param ruleClassID
   */  
export interface DeleteByID_input{
   ruleClassID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_FulfillmentRuleTesterTableset{
   PartAllocQueueInfo:Erp_Tablesets_PartAllocQueueInfoRow[],
   PartAllocQueueInfoLog:Erp_Tablesets_PartAllocQueueInfoLogRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartAllocQueueInfoLogRow{
      /**  Company  */  
   Company:string,
      /**  UserID  */  
   UserID:string,
      /**  UserPlant  */  
   UserPlant:string,
      /**  SysTaskNum  */  
   SysTaskNum:number,
      /**  TestMode  */  
   TestMode:boolean,
      /**  RuleClassID  */  
   RuleClassID:string,
      /**  RuleID  */  
   RuleID:string,
      /**  Sequence  */  
   Sequence:number,
      /**  LogText  */  
   LogText:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAllocQueueInfoRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  UserID  */  
   UserID:string,
      /**  UserPlant  */  
   UserPlant:string,
      /**  SysTaskNum  */  
   SysTaskNum:number,
      /**  TestMode  */  
   TestMode:boolean,
      /**  RelatedToSchemaName  */  
   RelatedToSchemaName:string,
      /**  RelatedToTableName  */  
   RelatedToTableName:string,
      /**  RelatedToSysRowID  */  
   RelatedToSysRowID:string,
      /**  RuleClassID  */  
   RuleClassID:string,
      /**  RuleID  */  
   RuleID:string,
      /**  The action that is to be executed on this demand.  */  
   Action:string,
      /**  OrderNum  */  
   OrderNum:number,
      /**  OrderLine  */  
   OrderLine:number,
      /**  LineType  */  
   LineType:string,
      /**  ReqDate  */  
   ReqDate:string,
      /**  OurReqQty  */  
   OurReqQty:number,
      /**  ShipToNum  */  
   ShipToNum:string,
      /**  ShipViaCode  */  
   ShipViaCode:string,
      /**  OpenRelease  */  
   OpenRelease:boolean,
      /**  FirmRelease  */  
   FirmRelease:boolean,
      /**  Make  */  
   Make:boolean,
      /**  OurJobQty  */  
   OurJobQty:number,
      /**  OurJobShippedQty  */  
   OurJobShippedQty:number,
      /**  VoidRelease  */  
   VoidRelease:boolean,
      /**  OurStockQty  */  
   OurStockQty:number,
      /**  WarehouseCode  */  
   WarehouseCode:string,
      /**  OurStockShippedQty  */  
   OurStockShippedQty:number,
      /**  PartNum  */  
   PartNum:string,
      /**  RevisionNum  */  
   RevisionNum:string,
      /**  TaxExempt  */  
   TaxExempt:string,
      /**  ShpConNum  */  
   ShpConNum:number,
      /**  NeedByDate  */  
   NeedByDate:string,
      /**  Plant  */  
   Plant:string,
      /**  SelectForPicking  */  
   SelectForPicking:boolean,
      /**  PickError  */  
   PickError:string,
      /**  BuyToOrder  */  
   BuyToOrder:boolean,
      /**  PONum  */  
   PONum:number,
      /**  IUM  */  
   IUM:string,
      /**  SalesUM  */  
   SalesUM:string,
      /**  AttributeSetID  */  
   AttributeSetID:number,
      /**  DispOrderShippedQty  */  
   DispOrderShippedQty:number,
      /**  DispOrderRemainingQty  */  
   DispOrderRemainingQty:number,
      /**  DispOurStockShippedQty  */  
   DispOurStockShippedQty:number,
      /**  DispOurJobShippedQty  */  
   DispOurJobShippedQty:number,
      /**  DispOrderReserved  */  
   DispOrderReserved:number,
      /**  DispOrderMfgReserved  */  
   DispOrderMfgReserved:number,
      /**  DispOrderStockReserved  */  
   DispOrderStockReserved:number,
      /**  CustID  */  
   CustID:string,
      /**  CustName  */  
   CustName:string,
      /**  ShipToCity  */  
   ShipToCity:string,
      /**  ShipToState  */  
   ShipToState:string,
      /**  ShipToZip  */  
   ShipToZip:string,
      /**  ShipToCountryNum  */  
   ShipToCountryNum:number,
      /**  StagingWhseDescription  */  
   StagingWhseDescription:string,
      /**  ErrorStatusDisplay  */  
   ErrorStatusDisplay:string,
      /**  StageWhseCode  */  
   StageWhseCode:string,
      /**  StageBin  */  
   StageBin:string,
      /**  EnableSelectForPicking  */  
   EnableSelectForPicking:boolean,
      /**  OrderNumLineRel  */  
   OrderNumLineRel:string,
      /**  ShipViaCodeDescription  */  
   ShipViaCodeDescription:string,
      /**  WarehouseCodeDescription  */  
   WarehouseCodeDescription:string,
      /**  ShipToName  */  
   ShipToName:string,
      /**  ShipToAddress1  */  
   ShipToAddress1:string,
      /**  ShipToAddress2  */  
   ShipToAddress2:string,
      /**  ShipToAddress3  */  
   ShipToAddress3:string,
      /**  SupplyPartNum  */  
   SupplyPartNum:string,
      /**  ReservePriorityCode  */  
   ReservePriorityCode:string,
      /**  DoNotShipBeforeDate  */  
   DoNotShipBeforeDate:string,
      /**  CustGroupCode  */  
   CustGroupCode:string,
      /**  KitParentPartNum  */  
   KitParentPartNum:string,
      /**  KitParentLine  */  
   KitParentLine:number,
      /**  SelectedForAction  */  
   SelectedForAction:boolean,
      /**  ReservedQty  */  
   ReservedQty:number,
      /**  PickingQty  */  
   PickingQty:number,
      /**  PickedQty  */  
   PickedQty:number,
      /**  RemainingToReserve  */  
   RemainingToReserve:number,
      /**  UnitPrice  */  
   UnitPrice:number,
      /**  ExtPrice  */  
   ExtPrice:number,
      /**  UnreservedInventory  */  
   UnreservedInventory:number,
      /**  AvailablePercent  */  
   AvailablePercent:number,
      /**  OrderedLessShipped  */  
   OrderedLessShipped:number,
      /**  PartWhseOnHandQty  */  
   PartWhseOnHandQty:number,
      /**  KitFulfillmentValuePct  */  
   KitFulfillmentValuePct:number,
      /**  KitFulfilledValuePct  */  
   KitFulfilledValuePct:number,
      /**  PotentialReserveQty  */  
   PotentialReserveQty:number,
      /**  FulfilledQtyPct  */  
   FulfilledQtyPct:number,
      /**  FulfillmentQtyPct  */  
   FulfillmentQtyPct:number,
      /**  PartVolume  */  
   PartVolume:number,
      /**  PartWeight  */  
   PartWeight:number,
      /**  KitFlag  */  
   KitFlag:string,
      /**  DoNotShipAfterDate  */  
   DoNotShipAfterDate:string,
      /**  NeedsUpdate  */  
   NeedsUpdate:boolean,
      /**  KitShipComplete  */  
   KitShipComplete:boolean,
      /**  KitQtyPer  */  
   KitQtyPer:number,
      /**  AllocatedQty  */  
   AllocatedQty:number,
      /**  ReservedQtyPct  */  
   ReservedQtyPct:number,
      /**  AllocatedQtyPct  */  
   AllocatedQtyPct:number,
      /**  FulfilledQty  */  
   FulfilledQty:number,
      /**  WaveNum  */  
   WaveNum:number,
      /**  WaveDestBinNum  */  
   WaveDestBinNum:string,
      /**  WavePickTicketPrinted  */  
   WavePickTicketPrinted:boolean,
      /**  PartTrackLots  */  
   PartTrackLots:boolean,
      /**  PartTrackSerialNum  */  
   PartTrackSerialNum:boolean,
      /**  PartTrackMultipleUOM  */  
   PartTrackMultipleUOM:boolean,
      /**  BTCustNum  */  
   BTCustNum:number,
      /**  BTCustID  */  
   BTCustID:string,
      /**  ShipOrderComplete  */  
   ShipOrderComplete:boolean,
      /**  CreditHold  */  
   CreditHold:boolean,
      /**  BTCustName  */  
   BTCustName:string,
      /**  AllocatedUM  */  
   AllocatedUM:string,
      /**  ReservedUM  */  
   ReservedUM:string,
      /**  JobNum  */  
   JobNum:string,
      /**  AssemblySeq  */  
   AssemblySeq:number,
      /**  MtlSeq  */  
   MtlSeq:number,
      /**  TFOrdNum  */  
   TFOrdNum:string,
      /**  TFOrdLine  */  
   TFOrdLine:number,
      /**  TFOrdNumTFOrdLine  */  
   TFOrdNumTFOrdLine:string,
      /**  DemandType  */  
   DemandType:string,
      /**  DemandKey1  */  
   DemandKey1:string,
      /**  DemandKey2  */  
   DemandKey2:string,
      /**  DemandKey3  */  
   DemandKey3:string,
      /**  JobAssemblyMtl  */  
   JobAssemblyMtl:string,
      /**  DemandTypeDesc  */  
   DemandTypeDesc:string,
      /**  FulfillmentSeq  */  
   FulfillmentSeq:number,
      /**  CrossDockedQty  */  
   CrossDockedQty:number,
      /**  OrderFulfillmentPct  */  
   OrderFulfillmentPct:number,
      /**  ReservePriorityOverride  */  
   ReservePriorityOverride:number,
      /**  CustCategory  */  
   CustCategory:string,
      /**  CustTerritoryID  */  
   CustTerritoryID:string,
      /**  PartWeightUOM  */  
   PartWeightUOM:string,
      /**  NormalizedPartWeight  */  
   NormalizedPartWeight:number,
      /**  NormalizedPartWeightUOM  */  
   NormalizedPartWeightUOM:string,
      /**  NormalizedPartVolume  */  
   NormalizedPartVolume:number,
      /**  NormalizedPartVolumeUOM  */  
   NormalizedPartVolumeUOM:string,
      /**  PartVolumeUOM  */  
   PartVolumeUOM:string,
      /**  UnitPriceCurrencyCode  */  
   UnitPriceCurrencyCode:string,
      /**  TotalValue  */  
   TotalValue:number,
      /**  TotalVolume  */  
   TotalVolume:number,
      /**  TotalWeight  */  
   TotalWeight:number,
      /**  FulfillmentValue  */  
   FulfillmentValue:number,
      /**  FulfillmentValuePct  */  
   FulfillmentValuePct:number,
      /**  FulfilledValue  */  
   FulfilledValue:number,
      /**  FulfilledValuePct  */  
   FulfilledValuePct:number,
      /**  OrderProjectID  */  
   OrderProjectID:string,
      /**  UDShortChar01  */  
   UDShortChar01:string,
      /**  UDShortChar02  */  
   UDShortChar02:string,
      /**  UDNumber01  */  
   UDNumber01:number,
      /**  UDNumber02  */  
   UDNumber02:number,
      /**  UDCheckbox01  */  
   UDCheckbox01:boolean,
      /**  UDCheckbox02  */  
   UDCheckbox02:boolean,
      /**  UDDate01  */  
   UDDate01:string,
      /**  UDDate02  */  
   UDDate02:string,
      /**  OrderCounterSale  */  
   OrderCounterSale:boolean,
      /**  DistributionType  */  
   DistributionType:string,
      /**  WaveDesc  */  
   WaveDesc:string,
      /**  TFOrdToPlant  */  
   TFOrdToPlant:string,
      /**  TFOrdToPlantName  */  
   TFOrdToPlantName:string,
      /**  TFOrdToPlantCity  */  
   TFOrdToPlantCity:string,
      /**  TFOrdToPlantState  */  
   TFOrdToPlantState:string,
      /**  TFOrdToPlantZip  */  
   TFOrdToPlantZip:string,
      /**  TFOrdToPlantCountry  */  
   TFOrdToPlantCountry:string,
      /**  TFOrdFromPlant  */  
   TFOrdFromPlant:string,
      /**  TFOrdFromWarehouseCode  */  
   TFOrdFromWarehouseCode:string,
      /**  PartProdCode  */  
   PartProdCode:string,
      /**  LineCount  */  
   LineCount:number,
      /**  OrderStatus  */  
   OrderStatus:string,
      /**  JobStatus  */  
   JobStatus:string,
      /**  TFOrdStatus  */  
   TFOrdStatus:string,
      /**  CustRegionCode  */  
   CustRegionCode:string,
      /**  JobStartDate  */  
   JobStartDate:string,
      /**  JobSchedCode  */  
   JobSchedCode:string,
      /**  JobPartNum  */  
   JobPartNum:string,
      /**  ReleaseCount  */  
   ReleaseCount:number,
      /**  ReleaseForPickingSeq  */  
   ReleaseForPickingSeq:number,
      /**  OrderHeld  */  
   OrderHeld:boolean,
      /**  BackFlush  */  
   BackFlush:boolean,
      /**  DisplaySeq  */  
   DisplaySeq:number,
      /**  MtlQueueSeq  */  
   MtlQueueSeq:number,
      /**  OrderPONum  */  
   OrderPONum:string,
      /**  OrderAllocSupplyCounter  */  
   OrderAllocSupplyCounter:number,
      /**  KitOurReqQty  */  
   KitOurReqQty:number,
      /**  KitUnitPrice  */  
   KitUnitPrice:number,
      /**  KitExtPrice  */  
   KitExtPrice:number,
      /**  KitPricing  */  
   KitPricing:string,
      /**  PartDescription  */  
   PartDescription:string,
      /**  AttributeSetShortDescription  */  
   AttributeSetShortDescription:string,
      /**  AttributeSetDescription  */  
   AttributeSetDescription:string,
      /**  PartAttrClassID  */  
   PartAttrClassID:string,
      /**  FilterAttributeSetID  */  
   FilterAttributeSetID:number,
      /**  FilterAttributeSetShortDescription  */  
   FilterAttributeSetShortDescription:string,
      /**  TrackInventoryAttributes  */  
   TrackInventoryAttributes:boolean,
      /**  TrackInventoryByRevision  */  
   TrackInventoryByRevision:boolean,
      /**  OrderRelNum  */  
   OrderRelNum:number,
      /**  OrderRelShippedTotal  */  
   OrderRelShippedTotal:number,
      /**  MtoAvailQty  */  
   MtoAvailQty:number,
      /**  PartAllocQueueSysRowID  */  
   PartAllocQueueSysRowID:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAllocRuleClassDtlRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Rule Class ID  */  
   RuleClassID:string,
      /**  Unique ID of Rule  */  
   RuleID:string,
      /**  Description of the rule  */  
   Description:string,
      /**  The sequence that the rules are processed in  */  
   Sequence:number,
      /**  QueryID of a BAQ used to join other tables to the PartAllocQueueInfo  */  
   QueryID:string,
      /**  The action that is executed for this rule  */  
   Action:string,
      /**  Indicates if the Rule is Active  */  
   Active:boolean,
      /**  Indicates the PartAllocTemplate to use when allocating  */  
   AllocTemplateID:string,
      /**  The formula defined for this rule  */  
   Formula:string,
      /**  Indicates if changes made to Reusable Rule are synchronized to this class rule  */  
   MasterDtlSync:boolean,
      /**  Reusable master rule linked to this class rule.  */  
   MasterRuleID:string,
      /**  Used to determine whether or not we (re)calculate fulfillment values following the return of the results of a search.  */  
   RuleCalcFulfillOnSearch:boolean,
      /**  When TRUE the fulfillment calculations and actions will consider the Demand Warehouse only.  When false, all warehouses will be considered in fulfillment calculations, and the user will be able to choose on Reserve actions whether to consider only the Primary Warehouse or all warehouses.  */  
   RuleUseDemandWhseOnly:boolean,
      /**  Following the execution of an action (Reserve, Allocate, Release for Picking, Unreserve, Unallocate), when true we will only refresh the rows that were actioned on, when false we will refresh all records.  */  
   RuleLimitedRefresh:boolean,
      /**  DevCharacter01  */  
   DevCharacter01:string,
      /**  DevDecimal01  */  
   DevDecimal01:number,
      /**  DevBoolean01  */  
   DevBoolean01:boolean,
      /**  DevDate01  */  
   DevDate01:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  The type of allocation based on the Action.  Valid Values:  Order, Job, Transfer, or blank.  */  
   AllocDemandType:string,
      /**  Indicates if the AllocationTemplate field should be enabled  */  
   EnableAllocTemplateID:boolean,
      /**  Indicates if the user is able to enter a formula  */  
   EnableFormula:boolean,
      /**  Indicates if the QueryID field should be enabled  */  
   EnableQueryID:boolean,
      /**  Indicates if an Active SysTask exists for this rule class.  */  
   ActiveSysTaskExists:boolean,
   BitFlag:number,
   PartAllocRuleMasterDtlFormula:string,
   PartAllocRuleMasterDtlAction:string,
   PartAllocRuleMasterDtlAllocTemplateID:string,
   PartAllocRuleMasterDtlQueryID:string,
   PartAllocRuleMasterDtlDescription:string,
   PartAllocTemplateAllocTemplateDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAllocRuleClassListRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Rule Class ID  */  
   RuleClassID:string,
      /**  Description of the rule class  */  
   Description:string,
      /**  Indicates if the Rule Class is Active  */  
   Active:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAllocRuleClassListTableset{
   PartAllocRuleClassList:Erp_Tablesets_PartAllocRuleClassListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartAllocRuleClassRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Rule Class ID  */  
   RuleClassID:string,
      /**  Description of the rule class  */  
   Description:string,
      /**  Indicates if the Rule Class is Active  */  
   Active:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAllocRuleClassTableset{
   PartAllocRuleClass:Erp_Tablesets_PartAllocRuleClassRow[],
   PartAllocRuleClassDtl:Erp_Tablesets_PartAllocRuleClassDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPartAllocRuleClassTableset{
   PartAllocRuleClass:Erp_Tablesets_PartAllocRuleClassRow[],
   PartAllocRuleClassDtl:Erp_Tablesets_PartAllocRuleClassDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ruleClassID
   */  
export interface GetByID_input{
   ruleClassID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartAllocRuleClassTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PartAllocRuleClassTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PartAllocRuleClassTableset[],
}

   /** Required : 
      @param ruleClassID
      @param ruleID
   */  
export interface GetFulfillmentRuleTesterTableset_input{
   ruleClassID:string,
   ruleID:string,
}

export interface GetFulfillmentRuleTesterTableset_output{
   returnObj:Erp_Tablesets_FulfillmentRuleTesterTableset[],
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
   returnObj:Erp_Tablesets_PartAllocRuleClassListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param ruleClassID
   */  
export interface GetNewPartAllocRuleClassDtl_input{
   ds:Erp_Tablesets_PartAllocRuleClassTableset[],
   ruleClassID:string,
}

export interface GetNewPartAllocRuleClassDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocRuleClassTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPartAllocRuleClass_input{
   ds:Erp_Tablesets_PartAllocRuleClassTableset[],
}

export interface GetNewPartAllocRuleClass_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocRuleClassTableset,
}
}

   /** Required : 
      @param whereClausePartAllocRuleClass
      @param whereClausePartAllocRuleClassDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartAllocRuleClass:string,
   whereClausePartAllocRuleClassDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartAllocRuleClassTableset[],
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
      @param newActive
      @param ds
   */  
export interface OnChangePartAllocRuleClassActive_input{
   newActive:boolean,
   ds:Erp_Tablesets_PartAllocRuleClassTableset[],
}

export interface OnChangePartAllocRuleClassActive_output{
parameters : {
      /**  output parameters  */  
   warningMsg:string,
}
}

   /** Required : 
      @param newAction
      @param checkForWarnings
      @param ds
   */  
export interface OnChangePartAllocRuleClassDtlAction_input{
   newAction:string,
   checkForWarnings:boolean,
   ds:Erp_Tablesets_PartAllocRuleClassTableset[],
}

export interface OnChangePartAllocRuleClassDtlAction_output{
parameters : {
      /**  output parameters  */  
   warningMsg:string,
   ds:Erp_Tablesets_PartAllocRuleClassTableset,
}
}

   /** Required : 
      @param newAllocTemplateID
      @param ds
   */  
export interface OnChangePartAllocRuleClassDtlAllocTemplateID_input{
   newAllocTemplateID:string,
   ds:Erp_Tablesets_PartAllocRuleClassTableset[],
}

export interface OnChangePartAllocRuleClassDtlAllocTemplateID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocRuleClassTableset,
}
}

   /** Required : 
      @param newMasterDtlSync
      @param ds
   */  
export interface OnChangePartAllocRuleClassDtlMasterDtlSync_input{
   newMasterDtlSync:boolean,
   ds:Erp_Tablesets_PartAllocRuleClassTableset[],
}

export interface OnChangePartAllocRuleClassDtlMasterDtlSync_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocRuleClassTableset,
}
}

   /** Required : 
      @param newMasterRuleID
      @param checkOverride
      @param ds
   */  
export interface OnChangePartAllocRuleClassDtlMasterRuleID_input{
   newMasterRuleID:string,
   checkOverride:boolean,
   ds:Erp_Tablesets_PartAllocRuleClassTableset[],
}

export interface OnChangePartAllocRuleClassDtlMasterRuleID_output{
parameters : {
      /**  output parameters  */  
   overrideWarning:string,
   ds:Erp_Tablesets_PartAllocRuleClassTableset,
}
}

   /** Required : 
      @param newQueryID
      @param checkForWarnings
      @param ds
   */  
export interface OnChangePartAllocRuleClassDtlQueryID_input{
   newQueryID:string,
   checkForWarnings:boolean,
   ds:Erp_Tablesets_PartAllocRuleClassTableset[],
}

export interface OnChangePartAllocRuleClassDtlQueryID_output{
parameters : {
      /**  output parameters  */  
   warningMsg:string,
   ds:Erp_Tablesets_PartAllocRuleClassTableset,
}
}

   /** Required : 
      @param ruleClassID
   */  
export interface TestFulfillmentRuleClass_input{
   ruleClassID:string,
}

export interface TestFulfillmentRuleClass_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPartAllocRuleClassTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPartAllocRuleClassTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PartAllocRuleClassTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocRuleClassTableset,
}
}

