import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.NLVATDeclarationSvc
// Description: Netherlands Electronic VAT Declaration BO
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/$metadata", {
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
   Description: Get NLVATDeclarations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NLVATDeclarations
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NLTaxReportDeclarationRow
   */  
export function get_NLVATDeclarations(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NLVATDeclarations
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.NLTaxReportDeclarationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NLVATDeclarations(requestBody:Erp_Tablesets_NLTaxReportDeclarationRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the NLVATDeclaration item
   Description: Calls GetByID to retrieve the NLVATDeclaration item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NLVATDeclaration
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationUID Desc: DeclarationUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.NLTaxReportDeclarationRow
   */  
export function get_NLVATDeclarations_Company_DeclarationUID(Company:string, DeclarationUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_NLTaxReportDeclarationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations(" + Company + "," + DeclarationUID + ")", {
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
         resolve(data as Erp_Tablesets_NLTaxReportDeclarationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update NLVATDeclaration for the service
   Description: Calls UpdateExt to update NLVATDeclaration. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NLVATDeclaration
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationUID Desc: DeclarationUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_NLVATDeclarations_Company_DeclarationUID(Company:string, DeclarationUID:string, requestBody:Erp_Tablesets_NLTaxReportDeclarationRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations(" + Company + "," + DeclarationUID + ")", {
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
   Summary: Call UpdateExt to delete NLVATDeclaration item
   Description: Call UpdateExt to delete NLVATDeclaration item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NLVATDeclaration
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationUID Desc: DeclarationUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_NLVATDeclarations_Company_DeclarationUID(Company:string, DeclarationUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations(" + Company + "," + DeclarationUID + ")", {
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
   Description: Get NLTaxReportDeclarationAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_NLTaxReportDeclarationAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationUID Desc: DeclarationUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NLTaxReportDeclarationAttchRow
   */  
export function get_NLVATDeclarations_Company_DeclarationUID_NLTaxReportDeclarationAttches(Company:string, DeclarationUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations(" + Company + "," + DeclarationUID + ")/NLTaxReportDeclarationAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the NLTaxReportDeclarationAttch item
   Description: Calls GetByID to retrieve the NLTaxReportDeclarationAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NLTaxReportDeclarationAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationUID Desc: DeclarationUID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.NLTaxReportDeclarationAttchRow
   */  
export function get_NLVATDeclarations_Company_DeclarationUID_NLTaxReportDeclarationAttches_Company_DeclarationUID_DrawingSeq(Company:string, DeclarationUID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_NLTaxReportDeclarationAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations(" + Company + "," + DeclarationUID + ")/NLTaxReportDeclarationAttches(" + Company + "," + DeclarationUID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_NLTaxReportDeclarationAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get NLTaxReportDeclarationAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NLTaxReportDeclarationAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NLTaxReportDeclarationAttchRow
   */  
export function get_NLTaxReportDeclarationAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLTaxReportDeclarationAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NLTaxReportDeclarationAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.NLTaxReportDeclarationAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NLTaxReportDeclarationAttches(requestBody:Erp_Tablesets_NLTaxReportDeclarationAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLTaxReportDeclarationAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the NLTaxReportDeclarationAttch item
   Description: Calls GetByID to retrieve the NLTaxReportDeclarationAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NLTaxReportDeclarationAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationUID Desc: DeclarationUID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.NLTaxReportDeclarationAttchRow
   */  
export function get_NLTaxReportDeclarationAttches_Company_DeclarationUID_DrawingSeq(Company:string, DeclarationUID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_NLTaxReportDeclarationAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLTaxReportDeclarationAttches(" + Company + "," + DeclarationUID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_NLTaxReportDeclarationAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update NLTaxReportDeclarationAttch for the service
   Description: Calls UpdateExt to update NLTaxReportDeclarationAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NLTaxReportDeclarationAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationUID Desc: DeclarationUID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_NLTaxReportDeclarationAttches_Company_DeclarationUID_DrawingSeq(Company:string, DeclarationUID:string, DrawingSeq:string, requestBody:Erp_Tablesets_NLTaxReportDeclarationAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLTaxReportDeclarationAttches(" + Company + "," + DeclarationUID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete NLTaxReportDeclarationAttch item
   Description: Call UpdateExt to delete NLTaxReportDeclarationAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NLTaxReportDeclarationAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationUID Desc: DeclarationUID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_NLTaxReportDeclarationAttches_Company_DeclarationUID_DrawingSeq(Company:string, DeclarationUID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLTaxReportDeclarationAttches(" + Company + "," + DeclarationUID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NLTaxReportDeclarationListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationListRow)
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
export function get_GetRows(whereClauseNLTaxReportDeclaration:string, whereClauseNLTaxReportDeclarationAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseNLTaxReportDeclaration!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseNLTaxReportDeclaration=" + whereClauseNLTaxReportDeclaration
   }
   if(typeof whereClauseNLTaxReportDeclarationAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseNLTaxReportDeclarationAttch=" + whereClauseNLTaxReportDeclarationAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/GetRows" + params, {
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
export function get_GetByID(declarationUID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof declarationUID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "declarationUID=" + declarationUID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/GetList" + params, {
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
   Summary: Invoke method GetNextNewNLTaxReportDeclaration
   Description: This method add new NLTaxReportDeclaration row to data set for specific VAT Report
   OperationID: GetNextNewNLTaxReportDeclaration
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNextNewNLTaxReportDeclaration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextNewNLTaxReportDeclaration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNextNewNLTaxReportDeclaration(requestBody:GetNextNewNLTaxReportDeclaration_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNextNewNLTaxReportDeclaration_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/GetNextNewNLTaxReportDeclaration", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNextNewNLTaxReportDeclaration_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaxBoxData
   Description: This method retrieve Tax Box Amounts
   OperationID: GetTaxBoxData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTaxBoxData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxBoxData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxBoxData(requestBody:GetTaxBoxData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTaxBoxData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/GetTaxBoxData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTaxBoxData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenExportFile
   Description: Export VAT Declaration to XBRL *.xml file.
   OperationID: GenExportFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenExportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenExportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenExportFile(requestBody:GenExportFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenExportFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/GenExportFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GenExportFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResetDeclarationStatus
   Description: This method Reset VAT Declaration status to NOT GENERATED.
   OperationID: ResetDeclarationStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ResetDeclarationStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetDeclarationStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetDeclarationStatus(requestBody:ResetDeclarationStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ResetDeclarationStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/ResetDeclarationStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ResetDeclarationStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetStatusToSubmitted
   Description: This method Manually Submitted VAT Declaration.
   OperationID: SetStatusToSubmitted
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetStatusToSubmitted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetStatusToSubmitted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetStatusToSubmitted(requestBody:SetStatusToSubmitted_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetStatusToSubmitted_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/SetStatusToSubmitted", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetStatusToSubmitted_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewNLTaxReportDeclaration
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNLTaxReportDeclaration
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewNLTaxReportDeclaration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNLTaxReportDeclaration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewNLTaxReportDeclaration(requestBody:GetNewNLTaxReportDeclaration_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewNLTaxReportDeclaration_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/GetNewNLTaxReportDeclaration", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewNLTaxReportDeclaration_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewNLTaxReportDeclarationAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNLTaxReportDeclarationAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewNLTaxReportDeclarationAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNLTaxReportDeclarationAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewNLTaxReportDeclarationAttch(requestBody:GetNewNLTaxReportDeclarationAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewNLTaxReportDeclarationAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/GetNewNLTaxReportDeclarationAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewNLTaxReportDeclarationAttch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_NLTaxReportDeclarationAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_NLTaxReportDeclarationListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationRow{
   "odatametadata":string,
   "value":Erp_Tablesets_NLTaxReportDeclarationRow,
}

export interface Erp_Tablesets_NLTaxReportDeclarationAttchRow{
   "Company":string,
   "DeclarationUID":number,
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

export interface Erp_Tablesets_NLTaxReportDeclarationListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Declaration Unique Identifier.  */  
   "DeclarationUID":number,
      /**  Declaration Date.  */  
   "DeclarationDate":string,
      /**  Document Flag (0 - Declaration, 1 - Correction).  */  
   "Correction":boolean,
      /**  Tax Report ID.  */  
   "ReportID":string,
      /**  Electronic Interface Unique Identifier.  */  
   "EFTHeadUID":number,
      /**  Last Exported Date.  */  
   "LastExportedDate":string,
      /**  Last Sent Date.  */  
   "LastSentDate":string,
      /**  Sent Status (0 – Not Generated; 1 – Ready; 2 – Error; 3 – Sent; 4 – Accepted; 5 – Manually Submitted)  */  
   "SentStatus":number,
      /**  Declaration/Correction Code  */  
   "DeclarationCode":string,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_NLTaxReportDeclarationRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Declaration Unique Identifier.  */  
   "DeclarationUID":number,
      /**  Declaration Date.  */  
   "DeclarationDate":string,
      /**  Document Flag (0 - Declaration, 1 - Correction).  */  
   "Correction":boolean,
      /**  Tax Report ID.  */  
   "ReportID":string,
      /**  Electronic Interface Unique Identifier.  */  
   "EFTHeadUID":number,
      /**  Output File.  */  
   "OutputFile":string,
      /**  Last Exported Date.  */  
   "LastExportedDate":string,
      /**  Last Exported By User.  */  
   "LastExportedBy":string,
      /**  Last Sent Date.  */  
   "LastSentDate":string,
      /**  Last Sent By User.  */  
   "LastSentBy":string,
      /**  Sent Status (0 – Not Generated; 1 – Ready; 2 – Error; 3 – Sent; 4 – Accepted; 5 – Manually Submitted)  */  
   "SentStatus":number,
      /**  Sent Error Message.  */  
   "SentErrorMessage":string,
      /**  Currency Code.  */  
   "CurrencyCode":string,
      /**  Comment text.  */  
   "RptComment":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Declaration/Correction Code  */  
   "DeclarationCode":string,
      /**  Tax Report Description  */  
   "ReportDescription":string,
      /**  Box 1a Taxable Amount in Doc Currency  */  
   "Box1aDocTaxableAmt":number,
      /**  Box 1a Tax Amount in Doc Currency  */  
   "Box1aDocTaxAmt":number,
      /**  Box 1a Taxable Amount  */  
   "Box1aTaxableAmt":number,
      /**  Box 1a Tax Amount  */  
   "Box1aTaxAmt":number,
      /**  Box 1b Taxable Amount in Doc Currency  */  
   "Box1bDocTaxableAmt":number,
      /**  Box 1b Tax Amount in Doc Currency  */  
   "Box1bDocTaxAmt":number,
      /**  Box 1b Taxable Amount  */  
   "Box1bTaxableAmt":number,
      /**  Box 1b Tax Amount  */  
   "Box1bTaxAmt":number,
      /**  Box 1c Taxable Amount in Doc Currency  */  
   "Box1cDocTaxableAmt":number,
      /**  Box 1c Tax Amount in Doc Currency  */  
   "Box1cDocTaxAmt":number,
      /**  Box 1c Taxable Amount  */  
   "Box1cTaxableAmt":number,
      /**  Box 1c Tax Amount  */  
   "Box1cTaxAmt":number,
      /**  Box 1d Taxable Amount in Doc Currency  */  
   "Box1dDocTaxableAmt":number,
      /**  Box 1d Tax Amount in Doc Currency  */  
   "Box1dDocTaxAmt":number,
      /**  Box 1d Taxable Amount  */  
   "Box1dTaxableAmt":number,
      /**  Box 1d Tax Amount  */  
   "Box1dTaxAmt":number,
      /**  Box 1e Taxable Amount in Doc Currency  */  
   "Box1eDocTaxableAmt":number,
      /**  Box 1e Taxable Amount  */  
   "Box1eTaxableAmt":number,
      /**  Box 2a Taxable Amount in Doc Currency  */  
   "Box2aDocTaxableAmt":number,
      /**  Box 2a Tax Amount in Doc Currency  */  
   "Box2aDocTaxAmt":number,
      /**  Box 2a Taxable Amount  */  
   "Box2aTaxableAmt":number,
      /**  Box 2a Tax Amount  */  
   "Box2aTaxAmt":number,
      /**  Box 3a Taxable Amount in Doc Currency  */  
   "Box3aDocTaxableAmt":number,
      /**  Box 3a Taxable Amount  */  
   "Box3aTaxableAmt":number,
      /**  Box 3b Taxable Amount in Doc Currency  */  
   "Box3bDocTaxableAmt":number,
      /**  Box 3b Taxable Amount  */  
   "Box3bTaxableAmt":number,
      /**  Box 3c Taxable Amount in Doc Currency  */  
   "Box3cDocTaxableAmt":number,
      /**  Box 3c Taxable Amount  */  
   "Box3cTaxableAmt":number,
      /**  Box 4a Taxable Amount in Doc Currency  */  
   "Box4aDocTaxableAmt":number,
      /**  Box 4a Tax Amount in Doc Currency  */  
   "Box4aDocTaxAmt":number,
      /**  Box 4a Taxable Amount  */  
   "Box4aTaxableAmt":number,
      /**  Box 4a Tax Amount  */  
   "Box4aTaxAmt":number,
      /**  Box 4b Taxable Amount in Doc Currency  */  
   "Box4bDocTaxableAmt":number,
      /**  Box 4b Tax Amount in Doc Currency  */  
   "Box4bDocTaxAmt":number,
      /**  Box 4b Taxable Amount  */  
   "Box4bTaxableAmt":number,
      /**  Box 4b Tax Amount  */  
   "Box4bTaxAmt":number,
      /**  Box 5a Tax Amount in Doc Currency  */  
   "Box5aDocTaxAmt":number,
      /**  Box 5a Tax Amount  */  
   "Box5aTaxAmt":number,
      /**  Box 5b Tax Amount in Doc Currency  */  
   "Box5bDocTaxAmt":number,
      /**  Box 5b Tax Amount  */  
   "Box5bTaxAmt":number,
      /**  Box 5c Tax Amount in Doc Currency  */  
   "Box5cDocTaxAmt":number,
      /**  Box 5c Tax Amount  */  
   "Box5cTaxAmt":number,
      /**  Box 5d Tax Amount in Doc Currency  */  
   "Box5dDocTaxAmt":number,
      /**  Box 5d Tax Amount  */  
   "Box5dTaxAmt":number,
      /**  Box 5e Tax Amount in Doc Currency  */  
   "Box5eDocTaxAmt":number,
      /**  Box 5e Tax Amount  */  
   "Box5eTaxAmt":number,
      /**  Box 5f Tax Amount in Doc Currency  */  
   "Box5fDocTaxAmt":number,
      /**  Box 5f Tax Amount  */  
   "Box5fTaxAmt":number,
      /**  Box 5g To Pay Tax Amount in Doc Currency  */  
   "Box5gToPayDocTaxAmt":number,
      /**  Box 5g To Pay Tax Amount  */  
   "Box5gToPayTaxAmt":number,
      /**  Box 5g To Reclaim Tax Amount in Doc Currency  */  
   "Box5gToReclaimDocTaxAmt":number,
      /**  Box 5g To Reclaim Tax Amount  */  
   "Box5gToReclaimTaxAmt":number,
      /**  Is To Pay  */  
   "Box5gIsToPay":boolean,
      /**  Is To Reclaim  */  
   "Box5gIsToReclaim":boolean,
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
      @param declarationUID
   */  
export interface DeleteByID_input{
   declarationUID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_NLTaxReportDeclarationAttchRow{
   Company:string,
   DeclarationUID:number,
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

export interface Erp_Tablesets_NLTaxReportDeclarationListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Declaration Unique Identifier.  */  
   DeclarationUID:number,
      /**  Declaration Date.  */  
   DeclarationDate:string,
      /**  Document Flag (0 - Declaration, 1 - Correction).  */  
   Correction:boolean,
      /**  Tax Report ID.  */  
   ReportID:string,
      /**  Electronic Interface Unique Identifier.  */  
   EFTHeadUID:number,
      /**  Last Exported Date.  */  
   LastExportedDate:string,
      /**  Last Sent Date.  */  
   LastSentDate:string,
      /**  Sent Status (0 – Not Generated; 1 – Ready; 2 – Error; 3 – Sent; 4 – Accepted; 5 – Manually Submitted)  */  
   SentStatus:number,
      /**  Declaration/Correction Code  */  
   DeclarationCode:string,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_NLTaxReportDeclarationRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Declaration Unique Identifier.  */  
   DeclarationUID:number,
      /**  Declaration Date.  */  
   DeclarationDate:string,
      /**  Document Flag (0 - Declaration, 1 - Correction).  */  
   Correction:boolean,
      /**  Tax Report ID.  */  
   ReportID:string,
      /**  Electronic Interface Unique Identifier.  */  
   EFTHeadUID:number,
      /**  Output File.  */  
   OutputFile:string,
      /**  Last Exported Date.  */  
   LastExportedDate:string,
      /**  Last Exported By User.  */  
   LastExportedBy:string,
      /**  Last Sent Date.  */  
   LastSentDate:string,
      /**  Last Sent By User.  */  
   LastSentBy:string,
      /**  Sent Status (0 – Not Generated; 1 – Ready; 2 – Error; 3 – Sent; 4 – Accepted; 5 – Manually Submitted)  */  
   SentStatus:number,
      /**  Sent Error Message.  */  
   SentErrorMessage:string,
      /**  Currency Code.  */  
   CurrencyCode:string,
      /**  Comment text.  */  
   RptComment:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Declaration/Correction Code  */  
   DeclarationCode:string,
      /**  Tax Report Description  */  
   ReportDescription:string,
      /**  Box 1a Taxable Amount in Doc Currency  */  
   Box1aDocTaxableAmt:number,
      /**  Box 1a Tax Amount in Doc Currency  */  
   Box1aDocTaxAmt:number,
      /**  Box 1a Taxable Amount  */  
   Box1aTaxableAmt:number,
      /**  Box 1a Tax Amount  */  
   Box1aTaxAmt:number,
      /**  Box 1b Taxable Amount in Doc Currency  */  
   Box1bDocTaxableAmt:number,
      /**  Box 1b Tax Amount in Doc Currency  */  
   Box1bDocTaxAmt:number,
      /**  Box 1b Taxable Amount  */  
   Box1bTaxableAmt:number,
      /**  Box 1b Tax Amount  */  
   Box1bTaxAmt:number,
      /**  Box 1c Taxable Amount in Doc Currency  */  
   Box1cDocTaxableAmt:number,
      /**  Box 1c Tax Amount in Doc Currency  */  
   Box1cDocTaxAmt:number,
      /**  Box 1c Taxable Amount  */  
   Box1cTaxableAmt:number,
      /**  Box 1c Tax Amount  */  
   Box1cTaxAmt:number,
      /**  Box 1d Taxable Amount in Doc Currency  */  
   Box1dDocTaxableAmt:number,
      /**  Box 1d Tax Amount in Doc Currency  */  
   Box1dDocTaxAmt:number,
      /**  Box 1d Taxable Amount  */  
   Box1dTaxableAmt:number,
      /**  Box 1d Tax Amount  */  
   Box1dTaxAmt:number,
      /**  Box 1e Taxable Amount in Doc Currency  */  
   Box1eDocTaxableAmt:number,
      /**  Box 1e Taxable Amount  */  
   Box1eTaxableAmt:number,
      /**  Box 2a Taxable Amount in Doc Currency  */  
   Box2aDocTaxableAmt:number,
      /**  Box 2a Tax Amount in Doc Currency  */  
   Box2aDocTaxAmt:number,
      /**  Box 2a Taxable Amount  */  
   Box2aTaxableAmt:number,
      /**  Box 2a Tax Amount  */  
   Box2aTaxAmt:number,
      /**  Box 3a Taxable Amount in Doc Currency  */  
   Box3aDocTaxableAmt:number,
      /**  Box 3a Taxable Amount  */  
   Box3aTaxableAmt:number,
      /**  Box 3b Taxable Amount in Doc Currency  */  
   Box3bDocTaxableAmt:number,
      /**  Box 3b Taxable Amount  */  
   Box3bTaxableAmt:number,
      /**  Box 3c Taxable Amount in Doc Currency  */  
   Box3cDocTaxableAmt:number,
      /**  Box 3c Taxable Amount  */  
   Box3cTaxableAmt:number,
      /**  Box 4a Taxable Amount in Doc Currency  */  
   Box4aDocTaxableAmt:number,
      /**  Box 4a Tax Amount in Doc Currency  */  
   Box4aDocTaxAmt:number,
      /**  Box 4a Taxable Amount  */  
   Box4aTaxableAmt:number,
      /**  Box 4a Tax Amount  */  
   Box4aTaxAmt:number,
      /**  Box 4b Taxable Amount in Doc Currency  */  
   Box4bDocTaxableAmt:number,
      /**  Box 4b Tax Amount in Doc Currency  */  
   Box4bDocTaxAmt:number,
      /**  Box 4b Taxable Amount  */  
   Box4bTaxableAmt:number,
      /**  Box 4b Tax Amount  */  
   Box4bTaxAmt:number,
      /**  Box 5a Tax Amount in Doc Currency  */  
   Box5aDocTaxAmt:number,
      /**  Box 5a Tax Amount  */  
   Box5aTaxAmt:number,
      /**  Box 5b Tax Amount in Doc Currency  */  
   Box5bDocTaxAmt:number,
      /**  Box 5b Tax Amount  */  
   Box5bTaxAmt:number,
      /**  Box 5c Tax Amount in Doc Currency  */  
   Box5cDocTaxAmt:number,
      /**  Box 5c Tax Amount  */  
   Box5cTaxAmt:number,
      /**  Box 5d Tax Amount in Doc Currency  */  
   Box5dDocTaxAmt:number,
      /**  Box 5d Tax Amount  */  
   Box5dTaxAmt:number,
      /**  Box 5e Tax Amount in Doc Currency  */  
   Box5eDocTaxAmt:number,
      /**  Box 5e Tax Amount  */  
   Box5eTaxAmt:number,
      /**  Box 5f Tax Amount in Doc Currency  */  
   Box5fDocTaxAmt:number,
      /**  Box 5f Tax Amount  */  
   Box5fTaxAmt:number,
      /**  Box 5g To Pay Tax Amount in Doc Currency  */  
   Box5gToPayDocTaxAmt:number,
      /**  Box 5g To Pay Tax Amount  */  
   Box5gToPayTaxAmt:number,
      /**  Box 5g To Reclaim Tax Amount in Doc Currency  */  
   Box5gToReclaimDocTaxAmt:number,
      /**  Box 5g To Reclaim Tax Amount  */  
   Box5gToReclaimTaxAmt:number,
      /**  Is To Pay  */  
   Box5gIsToPay:boolean,
      /**  Is To Reclaim  */  
   Box5gIsToReclaim:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_NLVATDeclarationListTableset{
   NLTaxReportDeclarationList:Erp_Tablesets_NLTaxReportDeclarationListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_NLVATDeclarationTableset{
   NLTaxReportDeclaration:Erp_Tablesets_NLTaxReportDeclarationRow[],
   NLTaxReportDeclarationAttch:Erp_Tablesets_NLTaxReportDeclarationAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtNLVATDeclarationTableset{
   NLTaxReportDeclaration:Erp_Tablesets_NLTaxReportDeclarationRow[],
   NLTaxReportDeclarationAttch:Erp_Tablesets_NLTaxReportDeclarationAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param declarationUID
      @param eftHeadUID
      @param exportFileName
   */  
export interface GenExportFile_input{
      /**  VAT Declaration ID  */  
   declarationUID:number,
      /**  Electronic Interface ID  */  
   eftHeadUID:number,
      /**  Export File Name  */  
   exportFileName:string,
}

export interface GenExportFile_output{
      /**  Generated File Name  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   attachErrMessage:string,
}
}

   /** Required : 
      @param declarationUID
   */  
export interface GetByID_input{
   declarationUID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_NLVATDeclarationTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_NLVATDeclarationTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_NLVATDeclarationTableset[],
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
   returnObj:Erp_Tablesets_NLVATDeclarationListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param declarationUID
   */  
export interface GetNewNLTaxReportDeclarationAttch_input{
   ds:Erp_Tablesets_NLVATDeclarationTableset[],
   declarationUID:number,
}

export interface GetNewNLTaxReportDeclarationAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NLVATDeclarationTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewNLTaxReportDeclaration_input{
   ds:Erp_Tablesets_NLVATDeclarationTableset[],
}

export interface GetNewNLTaxReportDeclaration_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NLVATDeclarationTableset,
}
}

   /** Required : 
      @param vatReportID
      @param ds
   */  
export interface GetNextNewNLTaxReportDeclaration_input{
      /**  VAT Report ID  */  
   vatReportID:string,
   ds:Erp_Tablesets_NLVATDeclarationTableset[],
}

export interface GetNextNewNLTaxReportDeclaration_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NLVATDeclarationTableset,
}
}

   /** Required : 
      @param whereClauseNLTaxReportDeclaration
      @param whereClauseNLTaxReportDeclarationAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseNLTaxReportDeclaration:string,
   whereClauseNLTaxReportDeclarationAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_NLVATDeclarationTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param vatReportID
      @param ds
   */  
export interface GetTaxBoxData_input{
      /**  VAT Report ID  */  
   vatReportID:string,
   ds:Erp_Tablesets_NLVATDeclarationTableset[],
}

export interface GetTaxBoxData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NLVATDeclarationTableset,
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
      @param declarationUID
   */  
export interface ResetDeclarationStatus_input{
      /**  VAT Declaration ID  */  
   declarationUID:number,
}

export interface ResetDeclarationStatus_output{
parameters : {
      /**  output parameters  */  
   attachErrMessage:string,
}
}

   /** Required : 
      @param declarationUID
   */  
export interface SetStatusToSubmitted_input{
      /**  VAT Declaration ID  */  
   declarationUID:number,
}

export interface SetStatusToSubmitted_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtNLVATDeclarationTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtNLVATDeclarationTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_NLVATDeclarationTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NLVATDeclarationTableset,
}
}

