import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PayrollTaxSvc
// Description: Payroll Tax Maintenance object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/$metadata", {
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
   Description: Get PayrollTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PayrollTaxes
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxMasRow
   */  
export function get_PayrollTaxes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxMasRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxMasRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PayrollTaxes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRTaxMasRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PRTaxMasRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PayrollTaxes(requestBody:Erp_Tablesets_PRTaxMasRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PayrollTax item
   Description: Calls GetByID to retrieve the PayrollTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PayrollTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PRTaxMasRow
   */  
export function get_PayrollTaxes_Company_TaxTblID(Company:string, TaxTblID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRTaxMasRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")", {
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
         resolve(data as Erp_Tablesets_PRTaxMasRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PayrollTax for the service
   Description: Calls UpdateExt to update PayrollTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PayrollTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRTaxMasRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PayrollTaxes_Company_TaxTblID(Company:string, TaxTblID:string, requestBody:Erp_Tablesets_PRTaxMasRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")", {
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
   Summary: Call UpdateExt to delete PayrollTax item
   Description: Call UpdateExt to delete PayrollTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PayrollTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PayrollTaxes_Company_TaxTblID(Company:string, TaxTblID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")", {
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
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
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
export function get_PayrollTaxes_Company_TaxTblID_EntityGLCs(Company:string, TaxTblID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")/EntityGLCs", {
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
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
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
export function get_PayrollTaxes_Company_TaxTblID_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, TaxTblID:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get PRTaxDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRTaxDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxDtlRow
   */  
export function get_PayrollTaxes_Company_TaxTblID_PRTaxDtls(Company:string, TaxTblID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")/PRTaxDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PRTaxDtl item
   Description: Calls GetByID to retrieve the PRTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PRTaxDtlRow
   */  
export function get_PayrollTaxes_Company_TaxTblID_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")", {
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
         resolve(data as Erp_Tablesets_PRTaxDtlRow)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/EntityGLCs", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/EntityGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get PRTaxDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRTaxDtls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxDtlRow
   */  
export function get_PRTaxDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRTaxDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PRTaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRTaxDtls(requestBody:Erp_Tablesets_PRTaxDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PRTaxDtl item
   Description: Calls GetByID to retrieve the PRTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PRTaxDtlRow
   */  
export function get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")", {
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
         resolve(data as Erp_Tablesets_PRTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRTaxDtl for the service
   Description: Calls UpdateExt to update PRTaxDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRTaxDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, requestBody:Erp_Tablesets_PRTaxDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")", {
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
   Summary: Call UpdateExt to delete PRTaxDtl item
   Description: Call UpdateExt to delete PRTaxDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRTaxDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")", {
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
   Description: Get PRTaxCrds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRTaxCrds1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxCrdRow
   */  
export function get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear_PRTaxCrds(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxCrdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")/PRTaxCrds", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxCrdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PRTaxCrd item
   Description: Calls GetByID to retrieve the PRTaxCrd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxCrd1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param TaxTblLine Desc: TaxTblLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PRTaxCrdRow
   */  
export function get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear_PRTaxCrds_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, TaxTblLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRTaxCrdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")/PRTaxCrds(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", {
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
         resolve(data as Erp_Tablesets_PRTaxCrdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PRTaxExps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRTaxExps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxExpRow
   */  
export function get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear_PRTaxExps(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxExpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")/PRTaxExps", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxExpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PRTaxExp item
   Description: Calls GetByID to retrieve the PRTaxExp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxExp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param TaxTblLine Desc: TaxTblLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PRTaxExpRow
   */  
export function get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear_PRTaxExps_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, TaxTblLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRTaxExpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")/PRTaxExps(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", {
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
         resolve(data as Erp_Tablesets_PRTaxExpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PRTaxTbls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRTaxTbls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxTblRow
   */  
export function get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear_PRTaxTbls(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxTblRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")/PRTaxTbls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxTblRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PRTaxTbl item
   Description: Calls GetByID to retrieve the PRTaxTbl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxTbl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param TaxTblLine Desc: TaxTblLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PRTaxTblRow
   */  
export function get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear_PRTaxTbls_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, TaxTblLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRTaxTblRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")/PRTaxTbls(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", {
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
         resolve(data as Erp_Tablesets_PRTaxTblRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PRTaxCrds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRTaxCrds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxCrdRow
   */  
export function get_PRTaxCrds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxCrdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxCrds", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxCrdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRTaxCrds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRTaxCrdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PRTaxCrdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRTaxCrds(requestBody:Erp_Tablesets_PRTaxCrdRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxCrds", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PRTaxCrd item
   Description: Calls GetByID to retrieve the PRTaxCrd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxCrd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxTblLine Desc: TaxTblLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PRTaxCrdRow
   */  
export function get_PRTaxCrds_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company:string, TaxTblID:string, TaxYear:string, FileStatus:string, TaxTblLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRTaxCrdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxCrds(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", {
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
         resolve(data as Erp_Tablesets_PRTaxCrdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRTaxCrd for the service
   Description: Calls UpdateExt to update PRTaxCrd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRTaxCrd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxTblLine Desc: TaxTblLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRTaxCrdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRTaxCrds_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company:string, TaxTblID:string, TaxYear:string, FileStatus:string, TaxTblLine:string, requestBody:Erp_Tablesets_PRTaxCrdRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxCrds(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", {
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
   Summary: Call UpdateExt to delete PRTaxCrd item
   Description: Call UpdateExt to delete PRTaxCrd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRTaxCrd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxTblLine Desc: TaxTblLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRTaxCrds_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company:string, TaxTblID:string, TaxYear:string, FileStatus:string, TaxTblLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxCrds(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", {
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
   Description: Get PRTaxExps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRTaxExps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxExpRow
   */  
export function get_PRTaxExps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxExpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxExps", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxExpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRTaxExps
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRTaxExpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PRTaxExpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRTaxExps(requestBody:Erp_Tablesets_PRTaxExpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxExps", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PRTaxExp item
   Description: Calls GetByID to retrieve the PRTaxExp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxExp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxTblLine Desc: TaxTblLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PRTaxExpRow
   */  
export function get_PRTaxExps_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company:string, TaxTblID:string, TaxYear:string, FileStatus:string, TaxTblLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRTaxExpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxExps(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", {
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
         resolve(data as Erp_Tablesets_PRTaxExpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRTaxExp for the service
   Description: Calls UpdateExt to update PRTaxExp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRTaxExp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxTblLine Desc: TaxTblLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRTaxExpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRTaxExps_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company:string, TaxTblID:string, TaxYear:string, FileStatus:string, TaxTblLine:string, requestBody:Erp_Tablesets_PRTaxExpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxExps(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", {
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
   Summary: Call UpdateExt to delete PRTaxExp item
   Description: Call UpdateExt to delete PRTaxExp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRTaxExp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxTblLine Desc: TaxTblLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRTaxExps_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company:string, TaxTblID:string, TaxYear:string, FileStatus:string, TaxTblLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxExps(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", {
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
   Description: Get PRTaxTbls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRTaxTbls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxTblRow
   */  
export function get_PRTaxTbls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxTblRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxTbls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxTblRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRTaxTbls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRTaxTblRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PRTaxTblRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRTaxTbls(requestBody:Erp_Tablesets_PRTaxTblRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxTbls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PRTaxTbl item
   Description: Calls GetByID to retrieve the PRTaxTbl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxTbl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxTblLine Desc: TaxTblLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PRTaxTblRow
   */  
export function get_PRTaxTbls_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company:string, TaxTblID:string, TaxYear:string, FileStatus:string, TaxTblLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRTaxTblRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxTbls(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", {
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
         resolve(data as Erp_Tablesets_PRTaxTblRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRTaxTbl for the service
   Description: Calls UpdateExt to update PRTaxTbl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRTaxTbl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxTblLine Desc: TaxTblLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRTaxTblRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRTaxTbls_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company:string, TaxTblID:string, TaxYear:string, FileStatus:string, TaxTblLine:string, requestBody:Erp_Tablesets_PRTaxTblRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxTbls(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", {
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
   Summary: Call UpdateExt to delete PRTaxTbl item
   Description: Call UpdateExt to delete PRTaxTbl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRTaxTbl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxTblLine Desc: TaxTblLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRTaxTbls_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company:string, TaxTblID:string, TaxYear:string, FileStatus:string, TaxTblLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxTbls(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxMasListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxMasListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxMasListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePRTaxMas:string, whereClauseEntityGLC:string, whereClausePRTaxDtl:string, whereClausePRTaxCrd:string, whereClausePRTaxExp:string, whereClausePRTaxTbl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePRTaxMas!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRTaxMas=" + whereClausePRTaxMas
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
   if(typeof whereClausePRTaxDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRTaxDtl=" + whereClausePRTaxDtl
   }
   if(typeof whereClausePRTaxCrd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRTaxCrd=" + whereClausePRTaxCrd
   }
   if(typeof whereClausePRTaxExp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRTaxExp=" + whereClausePRTaxExp
   }
   if(typeof whereClausePRTaxTbl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRTaxTbl=" + whereClausePRTaxTbl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetRows" + params, {
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
export function get_GetByID(taxTblID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof taxTblID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "taxTblID=" + taxTblID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetList" + params, {
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
   Summary: Invoke method CheckForDetails
   Description: This method is to be called when leaving the PRTaxMas record by any means
(changing rows, new search, leaving the screen, etc.).  A PRTaxMas record must
have at least one PRTaxDtl record to be considered a valid PRTaxMas record.  If no
details exist for the PRTaxDtl, the user must either delete the PRTaxMas record or
add a detail record before being allowed to leave.
   OperationID: CheckForDetails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckForDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckForDetails(requestBody:CheckForDetails_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckForDetails_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/CheckForDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckForDetails_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyDetails
   Description: This method copies a detail record for a specific TaxTblID, FileStatus and Year
to the specified new Year
   OperationID: CopyDetails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyDetails(requestBody:CopyDetails_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyDetails_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/CopyDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CopyDetails_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTaxMaster
   Description: This method creates a new PRTaxMas record after prompting for the TaxType.
Certain fields are initialized on create depending on which TaxType is being created.
This method replaces the standard GetNewPRTaxMas() method
   OperationID: GetNewTaxMaster
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTaxMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxMaster(requestBody:GetNewTaxMaster_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTaxMaster_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetNewTaxMaster", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewTaxMaster_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetFilingDescription
   Description: This method uses the PRTaxDtl.FileStatus field to determine the PRTaxDtl.FileStatusDesc
if there exists another PRTaxDtl with the same FileStatus for the same TaxTblID
   OperationID: SetFilingDescription
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetFilingDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFilingDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetFilingDescription(requestBody:SetFilingDescription_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetFilingDescription_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/SetFilingDescription", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetFilingDescription_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetW2State
   Description: This method sets the W2State to the first 2 digits of the TaxTblId when the
taxType = "SIT" if the W2State is blank
   OperationID: SetW2State
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetW2State_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetW2State_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetW2State(requestBody:SetW2State_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetW2State_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/SetW2State", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetW2State_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetNextOverAmount
   Description: This method sets the OverAmount of the next taxTblLine record when NotOverAmount changes on previous line
   OperationID: SetNextOverAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetNextOverAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetNextOverAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetNextOverAmount(requestBody:SetNextOverAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetNextOverAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/SetNextOverAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetNextOverAmount_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewPRTaxMas
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRTaxMas
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPRTaxMas_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRTaxMas_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRTaxMas(requestBody:GetNewPRTaxMas_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPRTaxMas_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetNewPRTaxMas", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPRTaxMas_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetNewEntityGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewPRTaxDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRTaxDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPRTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRTaxDtl(requestBody:GetNewPRTaxDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPRTaxDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetNewPRTaxDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPRTaxDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPRTaxCrd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRTaxCrd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPRTaxCrd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRTaxCrd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRTaxCrd(requestBody:GetNewPRTaxCrd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPRTaxCrd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetNewPRTaxCrd", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPRTaxCrd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPRTaxExp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRTaxExp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPRTaxExp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRTaxExp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRTaxExp(requestBody:GetNewPRTaxExp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPRTaxExp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetNewPRTaxExp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPRTaxExp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPRTaxTbl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRTaxTbl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPRTaxTbl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRTaxTbl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRTaxTbl(requestBody:GetNewPRTaxTbl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPRTaxTbl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetNewPRTaxTbl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPRTaxTbl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxCrdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRTaxCrdRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRTaxDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxExpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRTaxExpRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxMasListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRTaxMasListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxMasRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRTaxMasRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxTblRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRTaxTblRow,
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

export interface Erp_Tablesets_PRTaxCrdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Tax Table ID  */  
   "TaxTblID":string,
      /**   Mirror image of related PRTaxDtl.TaxYear.
(See PRTaxDtl.TaxYear)  */  
   "TaxYear":number,
      /**  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   "FileStatus":string,
      /**  An integer assigned by the system which is used to uniquely identify an individual table record within its related tax/filing status. This is assigned by reading last record and adding 1.  */  
   "TaxTblLine":number,
      /**   The lower amount range which the annualized range is compared to when selecting the proper table entry.
(See also NotOverAmount)  */  
   "OverAmount":number,
      /**   The higher amount range which the annualized range is compared to when selecting the proper table entry.  A  table entry is selected when the annualized wage amount is greater than the OverAmount and Less than or equal to the corresponding NotOverAmount.
(See also OverAmount)  */  
   "NotOverAmount":number,
      /**  Personal Tax Credit Percent.  */  
   "CreditPercent":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "TaxTblIDDescription":string,
   "TaxYearFileStatusDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRTaxDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Tax Table ID  */  
   "TaxTblID":string,
      /**  Tax year identifies the year in which this tax becomes effective. Note: The system uses the tax master which has a year equal or less than the check date when determining which tax master to use.  That means that the tax master does not have to be recreated every year if  there is no change from the previous year.  */  
   "TaxYear":number,
      /**  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   "FileStatus":string,
      /**  Description of this tax filing status master.  Ex: Married, Single.  */  
   "FileStatusDesc":string,
      /**   Indicates the amount upon which the tax is calculated.  Valid values are G - % of Gross,  F - % of FIT,  S - % of SIT, or H - % of Hours. Note: The state of Oregon has a tax based on % of hours.
Note: This does not apply to supplemental tax calculations, they are always a percent of taxable gross wages.  */  
   "TaxBasis":string,
      /**  The limit of annual wages after which taxes are no longer taken.  A wage limit is common in such taxes as Soc. Security, FUTA, SDI...  */  
   "TaxableWageLimit":number,
      /**  This percentage is used when the tax is not based on a graduated table.  That is, it's a fixed percentage regardless of wage amount.  */  
   "TaxPercent":number,
      /**  The annual  minimum deduction amount.  This is the minimum annual deduction amount which is used when the deduction is a percent of wages within minimum and maximum limits.  */  
   "StdDeductionMin":number,
      /**  The annual maximum deduction amount.  This is the maximum annual deduction amount which is used when the tax deduction is a percent of wages with minimum and maximum limits.  */  
   "StdDeductionMax":number,
      /**  Standard deduction percentage.  (See also StdDeductionMin, Max)  */  
   "StdDeductionPct":number,
      /**  An annual deduction amount which some states use when personal exemptions = 0.  */  
   "StdDeduction0":number,
      /**  An annual deduction amount which some states use when personal exemptions = 1.  */  
   "StdDeduction1":number,
      /**  An annual deduction amount which some states use when personal exemptions = 1.  */  
   "StdDeduction2":number,
      /**  The annual exemption amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  */  
   "PersonalExAmt":number,
      /**  The annual exemption amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.  */  
   "DependentExAmt":number,
      /**  The annual credit amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  */  
   "PersonalCrAmt":number,
      /**  The annual credit amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.
Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  */  
   "DependentCrAmt":number,
      /**  The percentage of Federal Income Tax that is exempt from taxes for this taxing locality.  (See also FITExMax)  */  
   "FITExPct":number,
      /**  Maximum amount of FIT exemption for this tax locality. (see FITExPct).  */  
   "FITExMax":number,
      /**  The percentage of FICA that is tax exempt for this tax locality. Note: FICA include both Medicare & Soc. Security (See also FITExMax)  */  
   "FICAExPct":number,
      /**   Maximum amount of FICA exemption for this locality. (see FICAExPct).
Note: FICA include both Medicare & Soc. Security.  */  
   "FICAExMax":number,
      /**  The weekly limit that is withheld.  Ex: SDI in New York is .05% of weekly wages with a max of .60 cents per week.  */  
   "WeeklyLimit":number,
      /**   The tax rate that is used for supplemental wages such as bonuses and commissions.
Note: Supplemental tax is always a percent of taxable gross.  */  
   "SupplementalPercent":number,
      /**  This percentage is used for Oklahoma.  It is the additional tax percentage on gross wages over PRTaxDtl.AddTaxAmount.  */  
   "AddTaxPercent":number,
      /**  This amount is used for Oklahoma.  It is the maximum wage amount before additional tax is calculated using field PRTaxDtl.AddTaxPercent.  */  
   "AddTaxAmount":number,
      /**  This percent is used for Oklahoma.  It is the percentage used in calculating the additional deductions.  */  
   "AddDeductionPercent":number,
      /**  This amount is used for Oklahoma.  It is the deduction amount per exemption used in calculating the additional deductions.  */  
   "AddDeductionAmt1":number,
      /**  This amount is used for Oklahoma.  It is the flat deduction amount used in calculating the additional deductions.  */  
   "AddDeductionAmt2":number,
      /**  Added for OK payroll.  Wages above this threshold will recieve the Above Threshold Tax Percent.  */  
   "TaxableThreshold":number,
      /**  Added for OK payroll.  Wages above the threshold amount will recieve this tax percent.  */  
   "AboveThresholdPercent":number,
      /**  Added for OK payroll.  Additional tax amount for wages above threshold.  */  
   "AboveThresholdAdditionalAmt":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "TaxTblIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRTaxExpRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Tax Table ID  */  
   "TaxTblID":string,
      /**   Mirror image of related PRTaxDtl.TaxYear.
(See PRTaxDtl.TaxYear)  */  
   "TaxYear":number,
      /**  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   "FileStatus":string,
      /**  An integer assigned by the system which is used to uniquely identify an individual table record within its related tax/filing status. This is assigned by reading last record and adding 1.  */  
   "TaxTblLine":number,
      /**   The lower amount range which the annualized range is compared to when selecting the proper table entry.
(See also NotOverAmount)  */  
   "OverAmount":number,
      /**   The higher amount range which the annualized range is compared to when selecting the proper table entry.  A  table entry is selected when the annualized wage amount is greater than the OverAmount and Less than or equal to the corresponding NotOverAmount.
(See also OverAmount)  */  
   "NotOverAmount":number,
      /**  Exemption amount.  */  
   "ExemptionAmount":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "TaxTblIDDescription":string,
   "TaxYearFileStatusDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRTaxMasListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A character set which is used as a component of the index to uniquely identify a tax master. Some tax types have system assigned values and some are assigned by the user. The system assigned values are as follows ( TaxType/TaxTblID); FIT/FED, FUTA/FUTA, SSEE/SSEE(Soc Sec Employee), SSER/SSER (Soc Sec Employer),  MDEE/MEDEE (Medicare Employee), MDER/MEDER (Medicare Employer).  */  
   "TaxTblID":string,
      /**   Identifies the type of tax table.  Valid values are "FIT" - Federal, "SIT" - State, "FUTA" - Federal Unemployment, "SUTA" - State Unemployment,  "SSEE" - Social Security employee paid, "SSER" - Social Security employer paid,  "MDEE" - Medicare employee paid, "MDER" - Medicare employer paid, "Locl" - Local.
Supplemental Percent is only allowed for FIT, SIT & Locl.  */  
   "TaxType":string,
      /**   An internally used field to control the order in which taxes are calculated.  This is need because some taxes are based on a % of  FIT, SIT and others may have an exemption percent on FIT, SIT...
Values are assigned based on TaxType as follows:
FIT = 10, SSEE/SSER = 20, MDEE/MDER = 30, SIT = 4), Locl = 50, , FUTA = 80 and SUTA = 90  */  
   "CalcOrder":number,
      /**  Description  */  
   "Description":string,
      /**  This State ID is used for printing on the W2 forms.  */  
   "W2State":string,
      /**  Indicates if this tax is an expense to the employer. This is automatically set = Yes and disabled for FUTA & SUTA. The user would set this to yes for the employer's side of FICA.  */  
   "EmployerExp":boolean,
      /**  This is the number by which your company is known to the taxing authority.  */  
   "TaxID":string,
      /**   Indicates whether or not this tax master represents unemployment insurance, such as FUTA or SUTA.  This is only used for reference purposes.
This is automatically set = Yes and disabled for FUTA & SUTA  */  
   "UnemploymentIns":boolean,
      /**  Some states require that withholding amounts per paycheck be rounded to the nearest dollar, this field will determine if withholding amounds will be rounded to the nearest dollar.  */  
   "RoundWithholdings":boolean,
      /**  Tax ID Reference  */  
   "TaxIDRef":string,
      /**  State Tax ID  */  
   "StateTaxID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRTaxMasRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A character set which is used as a component of the index to uniquely identify a tax master. Some tax types have system assigned values and some are assigned by the user. The system assigned values are as follows ( TaxType/TaxTblID); FIT/FED, FUTA/FUTA, SSEE/SSEE(Soc Sec Employee), SSER/SSER (Soc Sec Employer),  MDEE/MEDEE (Medicare Employee), MDER/MEDER (Medicare Employer).  */  
   "TaxTblID":string,
      /**   Identifies the type of tax table.  Valid values are "FIT" - Federal, "SIT" - State, "FUTA" - Federal Unemployment, "SUTA" - State Unemployment,  "SSEE" - Social Security employee paid, "SSER" - Social Security employer paid,  "MDEE" - Medicare employee paid, "MDER" - Medicare employer paid, "Locl" - Local.
Supplemental Percent is only allowed for FIT, SIT & Locl.  */  
   "TaxType":string,
      /**   An internally used field to control the order in which taxes are calculated.  This is need because some taxes are based on a % of  FIT, SIT and others may have an exemption percent on FIT, SIT...
Values are assigned based on TaxType as follows:
FIT = 10, SSEE/SSER = 20, MDEE/MDER = 30, SIT = 4), Locl = 50, , FUTA = 80 and SUTA = 90  */  
   "CalcOrder":number,
      /**  Description  */  
   "Description":string,
      /**  This State ID is used for printing on the W2 forms.  */  
   "W2State":string,
      /**  Indicates if this tax is an expense to the employer. This is automatically set = Yes and disabled for FUTA & SUTA. The user would set this to yes for the employer's side of FICA.  */  
   "EmployerExp":boolean,
      /**  This is the number by which your company is known to the taxing authority.  */  
   "TaxID":string,
      /**   Indicates whether or not this tax master represents unemployment insurance, such as FUTA or SUTA.  This is only used for reference purposes.
This is automatically set = Yes and disabled for FUTA & SUTA  */  
   "UnemploymentIns":boolean,
      /**  Some states require that withholding amounts per paycheck be rounded to the nearest dollar, this field will determine if withholding amounds will be rounded to the nearest dollar.  */  
   "RoundWithholdings":boolean,
      /**  Tax ID Reference  */  
   "TaxIDRef":string,
      /**  State Tax ID  */  
   "StateTaxID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRTaxTblRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Tax Table ID  */  
   "TaxTblID":string,
      /**   Mirror image of related PRTaxDtl.TaxYear.
(See PRTaxDtl.TaxYear)  */  
   "TaxYear":number,
      /**  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   "FileStatus":string,
      /**  An integer assigned by the system which is used to uniquely identify an individual tax table record within its related tax/filing status. This is assigned by reading last record and adding 1.  */  
   "TaxTblLine":number,
      /**   The lower amount range which the annualized range is compared to when selecting the proper tax table entry.
(See also NotOverAmount)  */  
   "OverAmount":number,
      /**   The higher amount range which the annualized range is compared to when selecting the proper tax table entry.  A  tax table entry is selected when the annualized wage amount is greater than the OverAmount and Less than or equal to the corresponding NotOverAmount.
(See also OverAmount)  */  
   "NotOverAmount":number,
      /**   The Base tax amount for this tax table entry.  The actual tax is calculated as...
TaxAmount + ((AnnualizedWages - OverAmount) * OverTaxPct)).  */  
   "TaxAmount":number,
      /**  The Tax percent at which the amount of the annualized wages are over the lower limit  (OverAmount) are taxed at.  */  
   "OverTaxPct":number,
      /**  Week Tax ID 1  */  
   "WkTaxID1":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "TaxTblIDDescription":string,
   "TaxYearFileStatusDesc":string,
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
      @param taxTblID
   */  
export interface CheckForDetails_input{
      /**  Tax Table ID of the Tax Table record to validate  */  
   taxTblID:string,
}

export interface CheckForDetails_output{
parameters : {
      /**  output parameters  */  
   errorMsg:string,
}
}

   /** Required : 
      @param taxTblID
      @param fileStat
      @param fromYear
      @param toYear
      @param ds
   */  
export interface CopyDetails_input{
      /**  TaxTblID to copy from  */  
   taxTblID:string,
      /**  Filing Status to copy from  */  
   fileStat:string,
      /**  Tax year to copy from  */  
   fromYear:number,
      /**  Tax year to copy to  */  
   toYear:number,
   ds:Erp_Tablesets_PayrollTaxTableset[],
}

export interface CopyDetails_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollTaxTableset,
}
}

   /** Required : 
      @param taxTblID
   */  
export interface DeleteByID_input{
   taxTblID:string,
}

export interface DeleteByID_output{
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

export interface Erp_Tablesets_PRTaxCrdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Tax Table ID  */  
   TaxTblID:string,
      /**   Mirror image of related PRTaxDtl.TaxYear.
(See PRTaxDtl.TaxYear)  */  
   TaxYear:number,
      /**  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   FileStatus:string,
      /**  An integer assigned by the system which is used to uniquely identify an individual table record within its related tax/filing status. This is assigned by reading last record and adding 1.  */  
   TaxTblLine:number,
      /**   The lower amount range which the annualized range is compared to when selecting the proper table entry.
(See also NotOverAmount)  */  
   OverAmount:number,
      /**   The higher amount range which the annualized range is compared to when selecting the proper table entry.  A  table entry is selected when the annualized wage amount is greater than the OverAmount and Less than or equal to the corresponding NotOverAmount.
(See also OverAmount)  */  
   NotOverAmount:number,
      /**  Personal Tax Credit Percent.  */  
   CreditPercent:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   TaxTblIDDescription:string,
   TaxYearFileStatusDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRTaxDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Tax Table ID  */  
   TaxTblID:string,
      /**  Tax year identifies the year in which this tax becomes effective. Note: The system uses the tax master which has a year equal or less than the check date when determining which tax master to use.  That means that the tax master does not have to be recreated every year if  there is no change from the previous year.  */  
   TaxYear:number,
      /**  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   FileStatus:string,
      /**  Description of this tax filing status master.  Ex: Married, Single.  */  
   FileStatusDesc:string,
      /**   Indicates the amount upon which the tax is calculated.  Valid values are G - % of Gross,  F - % of FIT,  S - % of SIT, or H - % of Hours. Note: The state of Oregon has a tax based on % of hours.
Note: This does not apply to supplemental tax calculations, they are always a percent of taxable gross wages.  */  
   TaxBasis:string,
      /**  The limit of annual wages after which taxes are no longer taken.  A wage limit is common in such taxes as Soc. Security, FUTA, SDI...  */  
   TaxableWageLimit:number,
      /**  This percentage is used when the tax is not based on a graduated table.  That is, it's a fixed percentage regardless of wage amount.  */  
   TaxPercent:number,
      /**  The annual  minimum deduction amount.  This is the minimum annual deduction amount which is used when the deduction is a percent of wages within minimum and maximum limits.  */  
   StdDeductionMin:number,
      /**  The annual maximum deduction amount.  This is the maximum annual deduction amount which is used when the tax deduction is a percent of wages with minimum and maximum limits.  */  
   StdDeductionMax:number,
      /**  Standard deduction percentage.  (See also StdDeductionMin, Max)  */  
   StdDeductionPct:number,
      /**  An annual deduction amount which some states use when personal exemptions = 0.  */  
   StdDeduction0:number,
      /**  An annual deduction amount which some states use when personal exemptions = 1.  */  
   StdDeduction1:number,
      /**  An annual deduction amount which some states use when personal exemptions = 1.  */  
   StdDeduction2:number,
      /**  The annual exemption amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  */  
   PersonalExAmt:number,
      /**  The annual exemption amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.  */  
   DependentExAmt:number,
      /**  The annual credit amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  */  
   PersonalCrAmt:number,
      /**  The annual credit amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.
Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  */  
   DependentCrAmt:number,
      /**  The percentage of Federal Income Tax that is exempt from taxes for this taxing locality.  (See also FITExMax)  */  
   FITExPct:number,
      /**  Maximum amount of FIT exemption for this tax locality. (see FITExPct).  */  
   FITExMax:number,
      /**  The percentage of FICA that is tax exempt for this tax locality. Note: FICA include both Medicare & Soc. Security (See also FITExMax)  */  
   FICAExPct:number,
      /**   Maximum amount of FICA exemption for this locality. (see FICAExPct).
Note: FICA include both Medicare & Soc. Security.  */  
   FICAExMax:number,
      /**  The weekly limit that is withheld.  Ex: SDI in New York is .05% of weekly wages with a max of .60 cents per week.  */  
   WeeklyLimit:number,
      /**   The tax rate that is used for supplemental wages such as bonuses and commissions.
Note: Supplemental tax is always a percent of taxable gross.  */  
   SupplementalPercent:number,
      /**  This percentage is used for Oklahoma.  It is the additional tax percentage on gross wages over PRTaxDtl.AddTaxAmount.  */  
   AddTaxPercent:number,
      /**  This amount is used for Oklahoma.  It is the maximum wage amount before additional tax is calculated using field PRTaxDtl.AddTaxPercent.  */  
   AddTaxAmount:number,
      /**  This percent is used for Oklahoma.  It is the percentage used in calculating the additional deductions.  */  
   AddDeductionPercent:number,
      /**  This amount is used for Oklahoma.  It is the deduction amount per exemption used in calculating the additional deductions.  */  
   AddDeductionAmt1:number,
      /**  This amount is used for Oklahoma.  It is the flat deduction amount used in calculating the additional deductions.  */  
   AddDeductionAmt2:number,
      /**  Added for OK payroll.  Wages above this threshold will recieve the Above Threshold Tax Percent.  */  
   TaxableThreshold:number,
      /**  Added for OK payroll.  Wages above the threshold amount will recieve this tax percent.  */  
   AboveThresholdPercent:number,
      /**  Added for OK payroll.  Additional tax amount for wages above threshold.  */  
   AboveThresholdAdditionalAmt:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   TaxTblIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRTaxExpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Tax Table ID  */  
   TaxTblID:string,
      /**   Mirror image of related PRTaxDtl.TaxYear.
(See PRTaxDtl.TaxYear)  */  
   TaxYear:number,
      /**  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   FileStatus:string,
      /**  An integer assigned by the system which is used to uniquely identify an individual table record within its related tax/filing status. This is assigned by reading last record and adding 1.  */  
   TaxTblLine:number,
      /**   The lower amount range which the annualized range is compared to when selecting the proper table entry.
(See also NotOverAmount)  */  
   OverAmount:number,
      /**   The higher amount range which the annualized range is compared to when selecting the proper table entry.  A  table entry is selected when the annualized wage amount is greater than the OverAmount and Less than or equal to the corresponding NotOverAmount.
(See also OverAmount)  */  
   NotOverAmount:number,
      /**  Exemption amount.  */  
   ExemptionAmount:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   TaxTblIDDescription:string,
   TaxYearFileStatusDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRTaxMasListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A character set which is used as a component of the index to uniquely identify a tax master. Some tax types have system assigned values and some are assigned by the user. The system assigned values are as follows ( TaxType/TaxTblID); FIT/FED, FUTA/FUTA, SSEE/SSEE(Soc Sec Employee), SSER/SSER (Soc Sec Employer),  MDEE/MEDEE (Medicare Employee), MDER/MEDER (Medicare Employer).  */  
   TaxTblID:string,
      /**   Identifies the type of tax table.  Valid values are "FIT" - Federal, "SIT" - State, "FUTA" - Federal Unemployment, "SUTA" - State Unemployment,  "SSEE" - Social Security employee paid, "SSER" - Social Security employer paid,  "MDEE" - Medicare employee paid, "MDER" - Medicare employer paid, "Locl" - Local.
Supplemental Percent is only allowed for FIT, SIT & Locl.  */  
   TaxType:string,
      /**   An internally used field to control the order in which taxes are calculated.  This is need because some taxes are based on a % of  FIT, SIT and others may have an exemption percent on FIT, SIT...
Values are assigned based on TaxType as follows:
FIT = 10, SSEE/SSER = 20, MDEE/MDER = 30, SIT = 4), Locl = 50, , FUTA = 80 and SUTA = 90  */  
   CalcOrder:number,
      /**  Description  */  
   Description:string,
      /**  This State ID is used for printing on the W2 forms.  */  
   W2State:string,
      /**  Indicates if this tax is an expense to the employer. This is automatically set = Yes and disabled for FUTA & SUTA. The user would set this to yes for the employer's side of FICA.  */  
   EmployerExp:boolean,
      /**  This is the number by which your company is known to the taxing authority.  */  
   TaxID:string,
      /**   Indicates whether or not this tax master represents unemployment insurance, such as FUTA or SUTA.  This is only used for reference purposes.
This is automatically set = Yes and disabled for FUTA & SUTA  */  
   UnemploymentIns:boolean,
      /**  Some states require that withholding amounts per paycheck be rounded to the nearest dollar, this field will determine if withholding amounds will be rounded to the nearest dollar.  */  
   RoundWithholdings:boolean,
      /**  Tax ID Reference  */  
   TaxIDRef:string,
      /**  State Tax ID  */  
   StateTaxID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRTaxMasListTableset{
   PRTaxMasList:Erp_Tablesets_PRTaxMasListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PRTaxMasRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A character set which is used as a component of the index to uniquely identify a tax master. Some tax types have system assigned values and some are assigned by the user. The system assigned values are as follows ( TaxType/TaxTblID); FIT/FED, FUTA/FUTA, SSEE/SSEE(Soc Sec Employee), SSER/SSER (Soc Sec Employer),  MDEE/MEDEE (Medicare Employee), MDER/MEDER (Medicare Employer).  */  
   TaxTblID:string,
      /**   Identifies the type of tax table.  Valid values are "FIT" - Federal, "SIT" - State, "FUTA" - Federal Unemployment, "SUTA" - State Unemployment,  "SSEE" - Social Security employee paid, "SSER" - Social Security employer paid,  "MDEE" - Medicare employee paid, "MDER" - Medicare employer paid, "Locl" - Local.
Supplemental Percent is only allowed for FIT, SIT & Locl.  */  
   TaxType:string,
      /**   An internally used field to control the order in which taxes are calculated.  This is need because some taxes are based on a % of  FIT, SIT and others may have an exemption percent on FIT, SIT...
Values are assigned based on TaxType as follows:
FIT = 10, SSEE/SSER = 20, MDEE/MDER = 30, SIT = 4), Locl = 50, , FUTA = 80 and SUTA = 90  */  
   CalcOrder:number,
      /**  Description  */  
   Description:string,
      /**  This State ID is used for printing on the W2 forms.  */  
   W2State:string,
      /**  Indicates if this tax is an expense to the employer. This is automatically set = Yes and disabled for FUTA & SUTA. The user would set this to yes for the employer's side of FICA.  */  
   EmployerExp:boolean,
      /**  This is the number by which your company is known to the taxing authority.  */  
   TaxID:string,
      /**   Indicates whether or not this tax master represents unemployment insurance, such as FUTA or SUTA.  This is only used for reference purposes.
This is automatically set = Yes and disabled for FUTA & SUTA  */  
   UnemploymentIns:boolean,
      /**  Some states require that withholding amounts per paycheck be rounded to the nearest dollar, this field will determine if withholding amounds will be rounded to the nearest dollar.  */  
   RoundWithholdings:boolean,
      /**  Tax ID Reference  */  
   TaxIDRef:string,
      /**  State Tax ID  */  
   StateTaxID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRTaxTblRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Tax Table ID  */  
   TaxTblID:string,
      /**   Mirror image of related PRTaxDtl.TaxYear.
(See PRTaxDtl.TaxYear)  */  
   TaxYear:number,
      /**  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   FileStatus:string,
      /**  An integer assigned by the system which is used to uniquely identify an individual tax table record within its related tax/filing status. This is assigned by reading last record and adding 1.  */  
   TaxTblLine:number,
      /**   The lower amount range which the annualized range is compared to when selecting the proper tax table entry.
(See also NotOverAmount)  */  
   OverAmount:number,
      /**   The higher amount range which the annualized range is compared to when selecting the proper tax table entry.  A  tax table entry is selected when the annualized wage amount is greater than the OverAmount and Less than or equal to the corresponding NotOverAmount.
(See also OverAmount)  */  
   NotOverAmount:number,
      /**   The Base tax amount for this tax table entry.  The actual tax is calculated as...
TaxAmount + ((AnnualizedWages - OverAmount) * OverTaxPct)).  */  
   TaxAmount:number,
      /**  The Tax percent at which the amount of the annualized wages are over the lower limit  (OverAmount) are taxed at.  */  
   OverTaxPct:number,
      /**  Week Tax ID 1  */  
   WkTaxID1:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   TaxTblIDDescription:string,
   TaxYearFileStatusDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PayrollTaxTableset{
   PRTaxMas:Erp_Tablesets_PRTaxMasRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   PRTaxDtl:Erp_Tablesets_PRTaxDtlRow[],
   PRTaxCrd:Erp_Tablesets_PRTaxCrdRow[],
   PRTaxExp:Erp_Tablesets_PRTaxExpRow[],
   PRTaxTbl:Erp_Tablesets_PRTaxTblRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPayrollTaxTableset{
   PRTaxMas:Erp_Tablesets_PRTaxMasRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   PRTaxDtl:Erp_Tablesets_PRTaxDtlRow[],
   PRTaxCrd:Erp_Tablesets_PRTaxCrdRow[],
   PRTaxExp:Erp_Tablesets_PRTaxExpRow[],
   PRTaxTbl:Erp_Tablesets_PRTaxTblRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param taxTblID
   */  
export interface GetByID_input{
   taxTblID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PayrollTaxTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PayrollTaxTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PayrollTaxTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  Tax Table ID  */  
   tableName:string,
      /**  field name ID  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
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
   returnObj:Erp_Tablesets_PRTaxMasListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
   ds:Erp_Tablesets_PayrollTaxTableset[],
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
   ds:Erp_Tablesets_PayrollTaxTableset,
}
}

   /** Required : 
      @param ds
      @param taxTblID
      @param taxYear
      @param fileStatus
   */  
export interface GetNewPRTaxCrd_input{
   ds:Erp_Tablesets_PayrollTaxTableset[],
   taxTblID:string,
   taxYear:number,
   fileStatus:string,
}

export interface GetNewPRTaxCrd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollTaxTableset,
}
}

   /** Required : 
      @param ds
      @param taxTblID
      @param fileStatus
   */  
export interface GetNewPRTaxDtl_input{
   ds:Erp_Tablesets_PayrollTaxTableset[],
   taxTblID:string,
   fileStatus:string,
}

export interface GetNewPRTaxDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollTaxTableset,
}
}

   /** Required : 
      @param ds
      @param taxTblID
      @param taxYear
      @param fileStatus
   */  
export interface GetNewPRTaxExp_input{
   ds:Erp_Tablesets_PayrollTaxTableset[],
   taxTblID:string,
   taxYear:number,
   fileStatus:string,
}

export interface GetNewPRTaxExp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollTaxTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPRTaxMas_input{
   ds:Erp_Tablesets_PayrollTaxTableset[],
}

export interface GetNewPRTaxMas_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollTaxTableset,
}
}

   /** Required : 
      @param ds
      @param taxTblID
      @param taxYear
      @param fileStatus
   */  
export interface GetNewPRTaxTbl_input{
   ds:Erp_Tablesets_PayrollTaxTableset[],
   taxTblID:string,
   taxYear:number,
   fileStatus:string,
}

export interface GetNewPRTaxTbl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollTaxTableset,
}
}

   /** Required : 
      @param ds
      @param taxType
   */  
export interface GetNewTaxMaster_input{
   ds:Erp_Tablesets_PayrollTaxTableset[],
      /**  Payroll Tax Master's Tax Type for new record  */  
   taxType:string,
}

export interface GetNewTaxMaster_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollTaxTableset,
}
}

   /** Required : 
      @param whereClausePRTaxMas
      @param whereClauseEntityGLC
      @param whereClausePRTaxDtl
      @param whereClausePRTaxCrd
      @param whereClausePRTaxExp
      @param whereClausePRTaxTbl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePRTaxMas:string,
   whereClauseEntityGLC:string,
   whereClausePRTaxDtl:string,
   whereClausePRTaxCrd:string,
   whereClausePRTaxExp:string,
   whereClausePRTaxTbl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PayrollTaxTableset[],
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
      @param ds
   */  
export interface SetFilingDescription_input{
   ds:Erp_Tablesets_PayrollTaxTableset[],
}

export interface SetFilingDescription_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollTaxTableset,
}
}

   /** Required : 
      @param taxTblID
      @param fileStatus
      @param taxYear
      @param taxTblLine
      @param newNotOverAmt
      @param tableType
      @param ds
   */  
export interface SetNextOverAmount_input{
      /**  current taxTblID being manipulated  */  
   taxTblID:string,
      /**  current fileStatus bing manipulated  */  
   fileStatus:string,
      /**  current taxYear being manipulated  */  
   taxYear:number,
      /**  current taxTblLine being manipulated  */  
   taxTblLine:number,
      /**  new NotOverAmount entered in UI  */  
   newNotOverAmt:number,
      /**  identifies which table is being manipulated  */  
   tableType:string,
   ds:Erp_Tablesets_PayrollTaxTableset[],
}

export interface SetNextOverAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollTaxTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface SetW2State_input{
   ds:Erp_Tablesets_PayrollTaxTableset[],
}

export interface SetW2State_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollTaxTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPayrollTaxTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPayrollTaxTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PayrollTaxTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollTaxTableset,
}
}

