import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CNGoldenTaxInterfaceSvc
// Description: CN Golden Tax Interface Service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get CNGoldenTaxInterfaces items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CNGoldenTaxInterfaces
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GTIInvcHeadRow
   */  
export function get_CNGoldenTaxInterfaces(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CNGoldenTaxInterfaces
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GTIInvcHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GTIInvcHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CNGoldenTaxInterfaces(requestBody:Erp_Tablesets_GTIInvcHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CNGoldenTaxInterface item
   Description: Calls GetByID to retrieve the CNGoldenTaxInterface item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CNGoldenTaxInterface
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupNum Desc: GroupNum   Required: True
      @param GroupSuffix Desc: GroupSuffix   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GTIInvcHeadRow
   */  
export function get_CNGoldenTaxInterfaces_Company_GroupNum_GroupSuffix(Company:string, GroupNum:string, GroupSuffix:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GTIInvcHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces(" + Company + "," + GroupNum + "," + GroupSuffix + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_GTIInvcHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CNGoldenTaxInterface for the service
   Description: Calls UpdateExt to update CNGoldenTaxInterface. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CNGoldenTaxInterface
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupNum Desc: GroupNum   Required: True
      @param GroupSuffix Desc: GroupSuffix   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GTIInvcHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CNGoldenTaxInterfaces_Company_GroupNum_GroupSuffix(Company:string, GroupNum:string, GroupSuffix:string, requestBody:Erp_Tablesets_GTIInvcHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces(" + Company + "," + GroupNum + "," + GroupSuffix + ")", {
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
   Summary: Call UpdateExt to delete CNGoldenTaxInterface item
   Description: Call UpdateExt to delete CNGoldenTaxInterface item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CNGoldenTaxInterface
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupNum Desc: GroupNum   Required: True
      @param GroupSuffix Desc: GroupSuffix   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CNGoldenTaxInterfaces_Company_GroupNum_GroupSuffix(Company:string, GroupNum:string, GroupSuffix:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces(" + Company + "," + GroupNum + "," + GroupSuffix + ")", {
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
   Description: Get GTIInvcDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GTIInvcDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupNum Desc: GroupNum   Required: True
      @param GroupSuffix Desc: GroupSuffix   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GTIInvcDtlRow
   */  
export function get_CNGoldenTaxInterfaces_Company_GroupNum_GroupSuffix_GTIInvcDtls(Company:string, GroupNum:string, GroupSuffix:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces(" + Company + "," + GroupNum + "," + GroupSuffix + ")/GTIInvcDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GTIInvcDtl item
   Description: Calls GetByID to retrieve the GTIInvcDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GTIInvcDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupNum Desc: GroupNum   Required: True
      @param GroupSuffix Desc: GroupSuffix   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GTIInvcDtlRow
   */  
export function get_CNGoldenTaxInterfaces_Company_GroupNum_GroupSuffix_GTIInvcDtls_Company_GroupNum_GroupSuffix_InvoiceNum_InvoiceLine(Company:string, GroupNum:string, GroupSuffix:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GTIInvcDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces(" + Company + "," + GroupNum + "," + GroupSuffix + ")/GTIInvcDtls(" + Company + "," + GroupNum + "," + GroupSuffix + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_GTIInvcDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GTIInvcDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GTIInvcDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GTIInvcDtlRow
   */  
export function get_GTIInvcDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GTIInvcDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GTIInvcDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GTIInvcDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GTIInvcDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GTIInvcDtls(requestBody:Erp_Tablesets_GTIInvcDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GTIInvcDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the GTIInvcDtl item
   Description: Calls GetByID to retrieve the GTIInvcDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GTIInvcDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupNum Desc: GroupNum   Required: True
      @param GroupSuffix Desc: GroupSuffix   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GTIInvcDtlRow
   */  
export function get_GTIInvcDtls_Company_GroupNum_GroupSuffix_InvoiceNum_InvoiceLine(Company:string, GroupNum:string, GroupSuffix:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GTIInvcDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GTIInvcDtls(" + Company + "," + GroupNum + "," + GroupSuffix + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_GTIInvcDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GTIInvcDtl for the service
   Description: Calls UpdateExt to update GTIInvcDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GTIInvcDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupNum Desc: GroupNum   Required: True
      @param GroupSuffix Desc: GroupSuffix   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GTIInvcDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GTIInvcDtls_Company_GroupNum_GroupSuffix_InvoiceNum_InvoiceLine(Company:string, GroupNum:string, GroupSuffix:string, InvoiceNum:string, InvoiceLine:string, requestBody:Erp_Tablesets_GTIInvcDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GTIInvcDtls(" + Company + "," + GroupNum + "," + GroupSuffix + "," + InvoiceNum + "," + InvoiceLine + ")", {
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
   Summary: Call UpdateExt to delete GTIInvcDtl item
   Description: Call UpdateExt to delete GTIInvcDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GTIInvcDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupNum Desc: GroupNum   Required: True
      @param GroupSuffix Desc: GroupSuffix   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GTIInvcDtls_Company_GroupNum_GroupSuffix_InvoiceNum_InvoiceLine(Company:string, GroupNum:string, GroupSuffix:string, InvoiceNum:string, InvoiceLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GTIInvcDtls(" + Company + "," + GroupNum + "," + GroupSuffix + "," + InvoiceNum + "," + InvoiceLine + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GTIInvcHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcHeadListRow)
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
export function get_GetRows(whereClauseGTIInvcHead:string, whereClauseGTIInvcDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGTIInvcHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGTIInvcHead=" + whereClauseGTIInvcHead
   }
   if(typeof whereClauseGTIInvcDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGTIInvcDtl=" + whereClauseGTIInvcDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(groupNum:string, groupSuffix:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof groupNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupNum=" + groupNum
   }
   if(typeof groupSuffix!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupSuffix=" + groupSuffix
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method CreateNewGTIRecords
   Description: Creates records in GTIInvcHead and GTIInvcDtl for correspondent records selected by user.
   OperationID: CreateNewGTIRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateNewGTIRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewGTIRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateNewGTIRecords(requestBody:CreateNewGTIRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateNewGTIRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CreateNewGTIRecords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateNewGTIRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateNewGTIRecordsAndGetRows
   Description: Creates records in GTIInvcHead and GTIInvcDtl for correspondent records selected by user.
   OperationID: CreateNewGTIRecordsAndGetRows
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateNewGTIRecordsAndGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewGTIRecordsAndGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateNewGTIRecordsAndGetRows(requestBody:CreateNewGTIRecordsAndGetRows_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateNewGTIRecordsAndGetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CreateNewGTIRecordsAndGetRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateNewGTIRecordsAndGetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetStatus
   Description: This method return the list of possible statuses for search form.
   OperationID: GetStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetStatus(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GetStatus", {
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
         resolve(data as GetStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InvoiceMerge
   Description: Creates new record in GTIInvcHead during Invoice Merge on the base of existant ones if validation is passed.
   OperationID: InvoiceMerge
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InvoiceMerge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvoiceMerge_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InvoiceMerge(requestBody:InvoiceMerge_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InvoiceMerge_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/InvoiceMerge", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as InvoiceMerge_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InvoiceSplit
   Description: Creates new record in GTIInvcHead during Invoice Split on the base of existant ones if validation is passed.
   OperationID: InvoiceSplit
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InvoiceSplit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvoiceSplit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InvoiceSplit(requestBody:InvoiceSplit_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InvoiceSplit_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/InvoiceSplit", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as InvoiceSplit_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofShipToNum
   Description: This method should be called when the ship to number on the invoice detail
record is changed.
   OperationID: OnChangeofShipToNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofShipToNum(requestBody:OnChangeofShipToNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofShipToNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/OnChangeofShipToNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeofShipToNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteObsoleGTIRecs
   Description: This method deletes records from GTIInvcHead and GTIInvcDtl, for which correcpondent records in InvcHead and InvcDtl were deleted
   OperationID: DeleteObsoleGTIRecs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteObsoleGTIRecs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteObsoleGTIRecs(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteObsoleGTIRecs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/DeleteObsoleGTIRecs", {
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
         resolve(data as DeleteObsoleGTIRecs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDForGTIS
   Description: Returns GTIInvcHead record.
   OperationID: GetByIDForGTIS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByIDForGTIS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDForGTIS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDForGTIS(requestBody:GetByIDForGTIS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByIDForGTIS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GetByIDForGTIS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByIDForGTIS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForGTIS_Lite
   Description: Returns GTIInvcHead records.
   OperationID: GetRowsForGTIS_Lite
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForGTIS_Lite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForGTIS_Lite_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForGTIS_Lite(requestBody:GetRowsForGTIS_Lite_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForGTIS_Lite_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GetRowsForGTIS_Lite", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsForGTIS_Lite_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForGTIS
   Description: Returns GTIInvcHead records.
   OperationID: GetRowsForGTIS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForGTIS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForGTIS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForGTIS(requestBody:GetRowsForGTIS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForGTIS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GetRowsForGTIS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsForGTIS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfInvoiceLineQty
   Description: Invoice Line quantity change event handler
   OperationID: OnChangeOfInvoiceLineQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfInvoiceLineQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfInvoiceLineQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfInvoiceLineQty(requestBody:OnChangeOfInvoiceLineQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfInvoiceLineQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/OnChangeOfInvoiceLineQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfInvoiceLineQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveSplittedInvoiceLine
   Description: Save splitted lines to DB.
   OperationID: SaveSplittedInvoiceLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SaveSplittedInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveSplittedInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveSplittedInvoiceLine(requestBody:SaveSplittedInvoiceLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SaveSplittedInvoiceLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/SaveSplittedInvoiceLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SaveSplittedInvoiceLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SplitInvoiceLine
   Description: Creates empty record in tableset for GTIInvcDtl.
   OperationID: SplitInvoiceLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SplitInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SplitInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SplitInvoiceLine(requestBody:SplitInvoiceLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SplitInvoiceLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/SplitInvoiceLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SplitInvoiceLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGTIInvcHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGTIInvcHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGTIInvcHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGTIInvcHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGTIInvcHead(requestBody:GetNewGTIInvcHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGTIInvcHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GetNewGTIInvcHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewGTIInvcHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGTIInvcDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGTIInvcDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGTIInvcDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGTIInvcDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGTIInvcDtl(requestBody:GetNewGTIInvcDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGTIInvcDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GetNewGTIInvcDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewGTIInvcDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GTIInvcDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GTIInvcHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GTIInvcHeadRow,
}

export interface Erp_Tablesets_GTIInvcDtlRow{
      /**  Company  */  
   "Company":string,
      /**  GroupNum  */  
   "GroupNum":number,
      /**  GroupSuffix  */  
   "GroupSuffix":number,
      /**  InvoiceNum  */  
   "InvoiceNum":number,
      /**  InvoiceLine  */  
   "InvoiceLine":number,
      /**  PartNum  */  
   "PartNum":string,
      /**  Qty  */  
   "Qty":number,
      /**  UnitPrice  */  
   "UnitPrice":number,
      /**  DiscountAmt  */  
   "DiscountAmt":number,
      /**  DiscountTaxAmt  */  
   "DiscountTaxAmt":number,
      /**  TaxAmt  */  
   "TaxAmt":number,
      /**  TotalAmt  */  
   "TotalAmt":number,
      /**  TaxCode  */  
   "TaxCode":string,
      /**  TaxRate  */  
   "TaxRate":number,
      /**  PartDescription  */  
   "PartDescription":string,
      /**  IUM  */  
   "IUM":string,
      /**  Specification  */  
   "Specification":string,
      /**  Description  */  
   "Description":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  IUMDescription  */  
   "IUMDescription":string,
      /**  Code Version for China GTI purposes  */  
   "CodeVersion":string,
      /**  Tax Category Code for China GTI purposes  */  
   "TaxCategoryCode":string,
      /**  Has Preferential Treatment value  for China GTI purposes  */  
   "HasPreferentialTreatment":boolean,
      /**  Preferential Treatment Content for China GTI purposes  */  
   "PreferentialTreatmentContent":string,
      /**  Zero Tax Rate Mark  for China GTI purposes  */  
   "ZeroTaxRateMark":string,
      /**  Deduction Amount for China GTI purposes  */  
   "DeductionAmount":number,
   "IsSelected":boolean,
   "TotalNetAmt":number,
   "LimitExceeded":boolean,
   "SelectedForAction":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GTIInvcHeadListRow{
      /**  Company  */  
   "Company":string,
      /**  GroupNum  */  
   "GroupNum":number,
      /**  GroupSuffix  */  
   "GroupSuffix":number,
      /**  InvoiceNum  */  
   "InvoiceNum":number,
      /**  Action  */  
   "Action":string,
      /**  Status1  */  
   "Status1":string,
      /**  Status2  */  
   "Status2":boolean,
      /**  IsSplitMerge  */  
   "IsSplitMerge":boolean,
      /**  GTIInvoiceNum  */  
   "GTIInvoiceNum":string,
      /**  GTIInvoiceType  */  
   "GTIInvoiceType":number,
      /**  GTIInvoiceDate  */  
   "GTIInvoiceDate":string,
      /**  GTIInvoiceAmt  */  
   "GTIInvoiceAmt":number,
      /**  GTITaxAmnt  */  
   "GTITaxAmnt":number,
      /**  CustNum  */  
   "CustNum":number,
      /**  InvoiceDate  */  
   "InvoiceDate":string,
      /**  CurrencyCode  */  
   "CurrencyCode":string,
      /**  TaxPeriod  */  
   "TaxPeriod":string,
      /**  TaxRegionCode  */  
   "TaxRegionCode":string,
      /**  Comments  */  
   "Comments":string,
      /**  Notes  */  
   "Notes":string,
      /**  ShipToNum  */  
   "ShipToNum":string,
      /**  ExportDate  */  
   "ExportDate":string,
      /**  ImportDate  */  
   "ImportDate":string,
      /**  ExportedBy  */  
   "ExportedBy":string,
      /**  ImportedBy  */  
   "ImportedBy":string,
      /**  IsWaitForExport  */  
   "IsWaitForExport":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GTIInvcHeadRow{
      /**  Company  */  
   "Company":string,
      /**  GroupNum  */  
   "GroupNum":number,
      /**  GroupSuffix  */  
   "GroupSuffix":number,
      /**  InvoiceNum  */  
   "InvoiceNum":number,
      /**  Action  */  
   "Action":string,
      /**  Status1  */  
   "Status1":string,
      /**  Status2  */  
   "Status2":boolean,
      /**  IsSplitMerge  */  
   "IsSplitMerge":boolean,
      /**  GTIInvoiceNum  */  
   "GTIInvoiceNum":string,
      /**  GTIInvoiceType  */  
   "GTIInvoiceType":number,
      /**  GTIInvoiceDate  */  
   "GTIInvoiceDate":string,
      /**  GTIInvoiceAmt  */  
   "GTIInvoiceAmt":number,
      /**  GTITaxAmnt  */  
   "GTITaxAmnt":number,
      /**  CustNum  */  
   "CustNum":number,
      /**  InvoiceDate  */  
   "InvoiceDate":string,
      /**  CurrencyCode  */  
   "CurrencyCode":string,
      /**  TaxPeriod  */  
   "TaxPeriod":string,
      /**  TaxRegionCode  */  
   "TaxRegionCode":string,
      /**  Comments  */  
   "Comments":string,
      /**  Notes  */  
   "Notes":string,
      /**  ShipToNum  */  
   "ShipToNum":string,
      /**  ExportDate  */  
   "ExportDate":string,
      /**  ImportDate  */  
   "ImportDate":string,
      /**  ExportedBy  */  
   "ExportedBy":string,
      /**  ImportedBy  */  
   "ImportedBy":string,
      /**  IsWaitForExport  */  
   "IsWaitForExport":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "TaxCode":string,
   "BankAcctNumber":string,
   "ShipToName":string,
   "ShipToNameAndAddress":string,
   "ShipToAddess":string,
      /**  Invoice amount = InvcHead.InvoiceAmt - InvcHead.WithholdAmt  */  
   "InvoiceAmt":number,
   "GrossInvoiceAmt":number,
   "GroupNumSuffix":string,
   "GroupID":string,
   "IsSelected":boolean,
   "SellerAddress":string,
   "SellerBankName":string,
   "CustID":string,
      /**  Allowed Actions LIst separeted by ~  */  
   "AllowedActions":string,
   "LimitExceeded":boolean,
   "AllowedActionsWithDesc":string,
   "ActionDescription":string,
   "SelectedForAction":boolean,
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
      @param cGroupList
   */  
export interface CreateNewGTIRecordsAndGetRows_input{
      /**  List of Group, which data should be got for UI  */  
   cGroupList:string,
}

export interface CreateNewGTIRecordsAndGetRows_output{
   returnObj:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
}

   /** Required : 
      @param ds
   */  
export interface CreateNewGTIRecords_input{
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
}

export interface CreateNewGTIRecords_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset,
}
}

   /** Required : 
      @param groupNum
      @param groupSuffix
   */  
export interface DeleteByID_input{
   groupNum:number,
   groupSuffix:number,
}

export interface DeleteByID_output{
}

export interface DeleteObsoleGTIRecs_output{
}

export interface Erp_Tablesets_CNGoldenTaxInterfaceListTableset{
   GTIInvcHeadList:Erp_Tablesets_GTIInvcHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CNGoldenTaxInterfaceTableset{
   GTIInvcHead:Erp_Tablesets_GTIInvcHeadRow[],
   GTIInvcDtl:Erp_Tablesets_GTIInvcDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GTIInvcDtlRow{
      /**  Company  */  
   Company:string,
      /**  GroupNum  */  
   GroupNum:number,
      /**  GroupSuffix  */  
   GroupSuffix:number,
      /**  InvoiceNum  */  
   InvoiceNum:number,
      /**  InvoiceLine  */  
   InvoiceLine:number,
      /**  PartNum  */  
   PartNum:string,
      /**  Qty  */  
   Qty:number,
      /**  UnitPrice  */  
   UnitPrice:number,
      /**  DiscountAmt  */  
   DiscountAmt:number,
      /**  DiscountTaxAmt  */  
   DiscountTaxAmt:number,
      /**  TaxAmt  */  
   TaxAmt:number,
      /**  TotalAmt  */  
   TotalAmt:number,
      /**  TaxCode  */  
   TaxCode:string,
      /**  TaxRate  */  
   TaxRate:number,
      /**  PartDescription  */  
   PartDescription:string,
      /**  IUM  */  
   IUM:string,
      /**  Specification  */  
   Specification:string,
      /**  Description  */  
   Description:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  IUMDescription  */  
   IUMDescription:string,
      /**  Code Version for China GTI purposes  */  
   CodeVersion:string,
      /**  Tax Category Code for China GTI purposes  */  
   TaxCategoryCode:string,
      /**  Has Preferential Treatment value  for China GTI purposes  */  
   HasPreferentialTreatment:boolean,
      /**  Preferential Treatment Content for China GTI purposes  */  
   PreferentialTreatmentContent:string,
      /**  Zero Tax Rate Mark  for China GTI purposes  */  
   ZeroTaxRateMark:string,
      /**  Deduction Amount for China GTI purposes  */  
   DeductionAmount:number,
   IsSelected:boolean,
   TotalNetAmt:number,
   LimitExceeded:boolean,
   SelectedForAction:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GTIInvcHeadListRow{
      /**  Company  */  
   Company:string,
      /**  GroupNum  */  
   GroupNum:number,
      /**  GroupSuffix  */  
   GroupSuffix:number,
      /**  InvoiceNum  */  
   InvoiceNum:number,
      /**  Action  */  
   Action:string,
      /**  Status1  */  
   Status1:string,
      /**  Status2  */  
   Status2:boolean,
      /**  IsSplitMerge  */  
   IsSplitMerge:boolean,
      /**  GTIInvoiceNum  */  
   GTIInvoiceNum:string,
      /**  GTIInvoiceType  */  
   GTIInvoiceType:number,
      /**  GTIInvoiceDate  */  
   GTIInvoiceDate:string,
      /**  GTIInvoiceAmt  */  
   GTIInvoiceAmt:number,
      /**  GTITaxAmnt  */  
   GTITaxAmnt:number,
      /**  CustNum  */  
   CustNum:number,
      /**  InvoiceDate  */  
   InvoiceDate:string,
      /**  CurrencyCode  */  
   CurrencyCode:string,
      /**  TaxPeriod  */  
   TaxPeriod:string,
      /**  TaxRegionCode  */  
   TaxRegionCode:string,
      /**  Comments  */  
   Comments:string,
      /**  Notes  */  
   Notes:string,
      /**  ShipToNum  */  
   ShipToNum:string,
      /**  ExportDate  */  
   ExportDate:string,
      /**  ImportDate  */  
   ImportDate:string,
      /**  ExportedBy  */  
   ExportedBy:string,
      /**  ImportedBy  */  
   ImportedBy:string,
      /**  IsWaitForExport  */  
   IsWaitForExport:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GTIInvcHeadRow{
      /**  Company  */  
   Company:string,
      /**  GroupNum  */  
   GroupNum:number,
      /**  GroupSuffix  */  
   GroupSuffix:number,
      /**  InvoiceNum  */  
   InvoiceNum:number,
      /**  Action  */  
   Action:string,
      /**  Status1  */  
   Status1:string,
      /**  Status2  */  
   Status2:boolean,
      /**  IsSplitMerge  */  
   IsSplitMerge:boolean,
      /**  GTIInvoiceNum  */  
   GTIInvoiceNum:string,
      /**  GTIInvoiceType  */  
   GTIInvoiceType:number,
      /**  GTIInvoiceDate  */  
   GTIInvoiceDate:string,
      /**  GTIInvoiceAmt  */  
   GTIInvoiceAmt:number,
      /**  GTITaxAmnt  */  
   GTITaxAmnt:number,
      /**  CustNum  */  
   CustNum:number,
      /**  InvoiceDate  */  
   InvoiceDate:string,
      /**  CurrencyCode  */  
   CurrencyCode:string,
      /**  TaxPeriod  */  
   TaxPeriod:string,
      /**  TaxRegionCode  */  
   TaxRegionCode:string,
      /**  Comments  */  
   Comments:string,
      /**  Notes  */  
   Notes:string,
      /**  ShipToNum  */  
   ShipToNum:string,
      /**  ExportDate  */  
   ExportDate:string,
      /**  ImportDate  */  
   ImportDate:string,
      /**  ExportedBy  */  
   ExportedBy:string,
      /**  ImportedBy  */  
   ImportedBy:string,
      /**  IsWaitForExport  */  
   IsWaitForExport:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   TaxCode:string,
   BankAcctNumber:string,
   ShipToName:string,
   ShipToNameAndAddress:string,
   ShipToAddess:string,
      /**  Invoice amount = InvcHead.InvoiceAmt - InvcHead.WithholdAmt  */  
   InvoiceAmt:number,
   GrossInvoiceAmt:number,
   GroupNumSuffix:string,
   GroupID:string,
   IsSelected:boolean,
   SellerAddress:string,
   SellerBankName:string,
   CustID:string,
      /**  Allowed Actions LIst separeted by ~  */  
   AllowedActions:string,
   LimitExceeded:boolean,
   AllowedActionsWithDesc:string,
   ActionDescription:string,
   SelectedForAction:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtCNGoldenTaxInterfaceTableset{
   GTIInvcHead:Erp_Tablesets_GTIInvcHeadRow[],
   GTIInvcDtl:Erp_Tablesets_GTIInvcDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param cGroupNumSuffix
   */  
export interface GetByIDForGTIS_input{
      /**  Group number and suffix  */  
   cGroupNumSuffix:string,
}

export interface GetByIDForGTIS_output{
   returnObj:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
}

   /** Required : 
      @param groupNum
      @param groupSuffix
   */  
export interface GetByID_input{
   groupNum:number,
   groupSuffix:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
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
   returnObj:Erp_Tablesets_CNGoldenTaxInterfaceListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupNum
      @param groupSuffix
      @param invoiceNum
   */  
export interface GetNewGTIInvcDtl_input{
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
   groupNum:number,
   groupSuffix:number,
   invoiceNum:number,
}

export interface GetNewGTIInvcDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset,
}
}

   /** Required : 
      @param ds
      @param groupNum
   */  
export interface GetNewGTIInvcHead_input{
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
   groupNum:number,
}

export interface GetNewGTIInvcHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset,
}
}

   /** Required : 
      @param whereClauseGTIInvcHead
      @param whereClauseGTIInvcDtl
      @param bSelectFromInvcHead
      @param whereClauseDateFrom
      @param whereClauseDateTo
      @param whereClauseCustNum
      @param whereClauseStatus1
      @param includeCM
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForGTIS_Lite_input{
      /**  Base Whereclause for GTIInvcHead table.  */  
   whereClauseGTIInvcHead:string,
      /**  Base Whereclause for GTIInvcDtl table.  */  
   whereClauseGTIInvcDtl:string,
      /**  Flag: true - add records from InvcHead/InvcDtl to ds; false - select records from GTIInvcHead/GTIInvcDtl only.  */  
   bSelectFromInvcHead:boolean,
      /**  Whereclause for Date from  */  
   whereClauseDateFrom:string,
      /**  Whereclause for Date to  */  
   whereClauseDateTo:string,
      /**  Whereclause for CustNum  */  
   whereClauseCustNum:number,
      /**  Whereclause for Status1  */  
   whereClauseStatus1:string,
      /**  Flag: Include or not Credit Memos  */  
   includeCM:boolean,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsForGTIS_Lite_output{
   returnObj:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseGTIInvcHead
      @param whereClauseGTIInvcDtl
      @param bSelectFromInvcHead
      @param whereClauseDateFrom
      @param whereClauseDateTo
      @param whereClauseCustNum
      @param whereClauseStatus1
      @param includeCM
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForGTIS_input{
      /**  Base Whereclause for GTIInvcHead table.  */  
   whereClauseGTIInvcHead:string,
      /**  Base Whereclause for GTIInvcDtl table.  */  
   whereClauseGTIInvcDtl:string,
      /**  Flag: true - add records from InvcHead/InvcDtl to ds; false - select records from GTIInvcHead/GTIInvcDtl only.  */  
   bSelectFromInvcHead:boolean,
      /**  Whereclause for Date from  */  
   whereClauseDateFrom:string,
      /**  Whereclause for Date to  */  
   whereClauseDateTo:string,
      /**  Whereclause for CustNum  */  
   whereClauseCustNum:number,
      /**  Whereclause for Status1  */  
   whereClauseStatus1:string,
      /**  Flag: Include or not Credit Memos  */  
   includeCM:boolean,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsForGTIS_output{
   returnObj:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseGTIInvcHead
      @param whereClauseGTIInvcDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGTIInvcHead:string,
   whereClauseGTIInvcDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetStatus_output{
      /**  Default status  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   cDefaultStatus:string,
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
      @param ds
   */  
export interface InvoiceMerge_input{
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
}

export interface InvoiceMerge_output{
   returnObj:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface InvoiceSplit_input{
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
}

export interface InvoiceSplit_output{
   returnObj:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset,
}
}

   /** Required : 
      @param proposedQty
      @param ds
   */  
export interface OnChangeOfInvoiceLineQty_input{
   proposedQty:number,
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
}

export interface OnChangeOfInvoiceLineQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset,
}
}

   /** Required : 
      @param iGroupNum
      @param iGroupSuffix
      @param cNewShipToNum
      @param ds
   */  
export interface OnChangeofShipToNum_input{
      /**  Group Number  */  
   iGroupNum:number,
      /**  Group Suffix  */  
   iGroupSuffix:number,
      /**  Proposed ship to number  */  
   cNewShipToNum:string,
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
}

export interface OnChangeofShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface SaveSplittedInvoiceLine_input{
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
}

export interface SaveSplittedInvoiceLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset,
}
}

   /** Required : 
      @param sGroupNumSuffix
      @param sStatus1
      @param bStatus2
      @param ds
   */  
export interface SplitInvoiceLine_input{
      /**  Group Number and Suffix  */  
   sGroupNumSuffix:string,
      /**  Status1: New or Exported or Updated  */  
   sStatus1:string,
      /**  Status2: Regular or Voided  */  
   bStatus2:boolean,
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
}

export interface SplitInvoiceLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCNGoldenTaxInterfaceTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCNGoldenTaxInterfaceTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNGoldenTaxInterfaceTableset,
}
}

