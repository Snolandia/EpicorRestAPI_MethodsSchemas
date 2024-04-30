import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.VendorSvc
// Description: Vendor BO
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/$metadata", {
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
   Description: Get Vendors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Vendors
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorRow
   */  
export function get_Vendors(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Vendors
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VendorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Vendors(requestBody:Erp_Tablesets_VendorRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the Vendor item
   Description: Calls GetByID to retrieve the Vendor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Vendor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendorRow
   */  
export function get_Vendors_Company_VendorNum(Company:string, VendorNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")", {
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
         resolve(data as Erp_Tablesets_VendorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Vendor for the service
   Description: Calls UpdateExt to update Vendor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Vendor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Vendors_Company_VendorNum(Company:string, VendorNum:string, requestBody:Erp_Tablesets_VendorRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")", {
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
   Summary: Call UpdateExt to delete Vendor item
   Description: Call UpdateExt to delete Vendor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Vendor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Vendors_Company_VendorNum(Company:string, VendorNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")", {
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
      @param VendorNum Desc: VendorNum   Required: True
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
export function get_Vendors_Company_VendorNum_EntityGLCs(Company:string, VendorNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/EntityGLCs", {
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
      @param VendorNum Desc: VendorNum   Required: True
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
export function get_Vendors_Company_VendorNum_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, VendorNum:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get TaxExempts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxExempts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxExemptRow
   */  
export function get_Vendors_Company_VendorNum_TaxExempts(Company:string, VendorNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxExemptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/TaxExempts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxExemptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaxExempt item
   Description: Calls GetByID to retrieve the TaxExempt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxExempt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaxExemptRow
   */  
export function get_Vendors_Company_VendorNum_TaxExempts_Company_RelatedToFile_Key1_Key2_TaxCode_RateCode_EffectiveFrom(Company:string, VendorNum:string, RelatedToFile:string, Key1:string, Key2:string, TaxCode:string, RateCode:string, EffectiveFrom:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxExemptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/TaxExempts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")", {
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
         resolve(data as Erp_Tablesets_TaxExemptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PEVendWhldHists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PEVendWhldHists1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PEVendWhldHistRow
   */  
export function get_Vendors_Company_VendorNum_PEVendWhldHists(Company:string, VendorNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PEVendWhldHistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/PEVendWhldHists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PEVendWhldHistRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PEVendWhldHist item
   Description: Calls GetByID to retrieve the PEVendWhldHist item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PEVendWhldHist1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RecordSeq Desc: RecordSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PEVendWhldHistRow
   */  
export function get_Vendors_Company_VendorNum_PEVendWhldHists_Company_VendorNum_RecordSeq(Company:string, VendorNum:string, RecordSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PEVendWhldHistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/PEVendWhldHists(" + Company + "," + VendorNum + "," + RecordSeq + ")", {
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
         resolve(data as Erp_Tablesets_PEVendWhldHistRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VendRestrictions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendRestrictions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendRestrictionRow
   */  
export function get_Vendors_Company_VendorNum_VendRestrictions(Company:string, VendorNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendRestrictions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendRestriction item
   Description: Calls GetByID to retrieve the VendRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendRestriction1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendRestrictionRow
   */  
export function get_Vendors_Company_VendorNum_VendRestrictions_Company_VendorNum_RestrictionTypeID(Company:string, VendorNum:string, RestrictionTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendRestrictions(" + Company + "," + VendorNum + "," + RestrictionTypeID + ")", {
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
         resolve(data as Erp_Tablesets_VendRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VendBanks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendBanks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendBankRow
   */  
export function get_Vendors_Company_VendorNum_VendBanks(Company:string, VendorNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendBanks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendBank item
   Description: Calls GetByID to retrieve the VendBank item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendBank1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param BankID Desc: BankID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendBankRow
   */  
export function get_Vendors_Company_VendorNum_VendBanks_Company_VendorNum_BankID(Company:string, VendorNum:string, BankID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendBankRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendBanks(" + Company + "," + VendorNum + "," + BankID + ")", {
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
         resolve(data as Erp_Tablesets_VendBankRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VendCntMains items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendCntMains1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntMainRow
   */  
export function get_Vendors_Company_VendorNum_VendCntMains(Company:string, VendorNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntMainRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendCntMains", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntMainRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendCntMain item
   Description: Calls GetByID to retrieve the VendCntMain item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCntMain1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendCntMainRow
   */  
export function get_Vendors_Company_VendorNum_VendCntMains_Company_VendorNum_PurPoint_ConNum(Company:string, VendorNum:string, PurPoint:string, ConNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendCntMainRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendCntMains(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")", {
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
         resolve(data as Erp_Tablesets_VendCntMainRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VenMFBills items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VenMFBills1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenMFBillRow
   */  
export function get_Vendors_Company_VendorNum_VenMFBills(Company:string, VendorNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenMFBillRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VenMFBills", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenMFBillRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VenMFBill item
   Description: Calls GetByID to retrieve the VenMFBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenMFBill1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PayBTFlag Desc: PayBTFlag   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VenMFBillRow
   */  
export function get_Vendors_Company_VendorNum_VenMFBills_Company_VendorNum_PayBTFlag(Company:string, VendorNum:string, PayBTFlag:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VenMFBillRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VenMFBills(" + Company + "," + VendorNum + "," + PayBTFlag + ")", {
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
         resolve(data as Erp_Tablesets_VenMFBillRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VendorPPs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendorPPs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorPPRow
   */  
export function get_Vendors_Company_VendorNum_VendorPPs(Company:string, VendorNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendorPPs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendorPP item
   Description: Calls GetByID to retrieve the VendorPP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendorPP1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendorPPRow
   */  
export function get_Vendors_Company_VendorNum_VendorPPs_Company_VendorNum_PurPoint(Company:string, VendorNum:string, PurPoint:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendorPPRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")", {
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
         resolve(data as Erp_Tablesets_VendorPPRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VenUPSEmails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VenUPSEmails1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenUPSEmailRow
   */  
export function get_Vendors_Company_VendorNum_VenUPSEmails(Company:string, VendorNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenUPSEmailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VenUPSEmails", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenUPSEmailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VenUPSEmail item
   Description: Calls GetByID to retrieve the VenUPSEmail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenUPSEmail1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VenUPSEmailRow
   */  
export function get_Vendors_Company_VendorNum_VenUPSEmails_Company_VendorNum_UPSQVSeq(Company:string, VendorNum:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VenUPSEmailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VenUPSEmails(" + Company + "," + VendorNum + "," + UPSQVSeq + ")", {
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
         resolve(data as Erp_Tablesets_VenUPSEmailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VendorAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendorAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorAttchRow
   */  
export function get_Vendors_Company_VendorNum_VendorAttches(Company:string, VendorNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendorAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendorAttch item
   Description: Calls GetByID to retrieve the VendorAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendorAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendorAttchRow
   */  
export function get_Vendors_Company_VendorNum_VendorAttches_Company_VendorNum_DrawingSeq(Company:string, VendorNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendorAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendorAttches(" + Company + "," + VendorNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_VendorAttchRow)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/EntityGLCs", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/EntityGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get TaxExempts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxExempts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxExemptRow
   */  
export function get_TaxExempts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxExemptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/TaxExempts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxExemptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxExempts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxExemptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TaxExemptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxExempts(requestBody:Erp_Tablesets_TaxExemptRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/TaxExempts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the TaxExempt item
   Description: Calls GetByID to retrieve the TaxExempt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxExempt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaxExemptRow
   */  
export function get_TaxExempts_Company_RelatedToFile_Key1_Key2_TaxCode_RateCode_EffectiveFrom(Company:string, RelatedToFile:string, Key1:string, Key2:string, TaxCode:string, RateCode:string, EffectiveFrom:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxExemptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/TaxExempts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")", {
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
         resolve(data as Erp_Tablesets_TaxExemptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxExempt for the service
   Description: Calls UpdateExt to update TaxExempt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxExempt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxExemptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxExempts_Company_RelatedToFile_Key1_Key2_TaxCode_RateCode_EffectiveFrom(Company:string, RelatedToFile:string, Key1:string, Key2:string, TaxCode:string, RateCode:string, EffectiveFrom:string, requestBody:Erp_Tablesets_TaxExemptRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/TaxExempts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")", {
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
   Summary: Call UpdateExt to delete TaxExempt item
   Description: Call UpdateExt to delete TaxExempt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxExempt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxExempts_Company_RelatedToFile_Key1_Key2_TaxCode_RateCode_EffectiveFrom(Company:string, RelatedToFile:string, Key1:string, Key2:string, TaxCode:string, RateCode:string, EffectiveFrom:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/TaxExempts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")", {
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
   Description: Get PEVendWhldHists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PEVendWhldHists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PEVendWhldHistRow
   */  
export function get_PEVendWhldHists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PEVendWhldHistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/PEVendWhldHists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PEVendWhldHistRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PEVendWhldHists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PEVendWhldHistRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PEVendWhldHistRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PEVendWhldHists(requestBody:Erp_Tablesets_PEVendWhldHistRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/PEVendWhldHists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PEVendWhldHist item
   Description: Calls GetByID to retrieve the PEVendWhldHist item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PEVendWhldHist
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RecordSeq Desc: RecordSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PEVendWhldHistRow
   */  
export function get_PEVendWhldHists_Company_VendorNum_RecordSeq(Company:string, VendorNum:string, RecordSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PEVendWhldHistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/PEVendWhldHists(" + Company + "," + VendorNum + "," + RecordSeq + ")", {
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
         resolve(data as Erp_Tablesets_PEVendWhldHistRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PEVendWhldHist for the service
   Description: Calls UpdateExt to update PEVendWhldHist. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PEVendWhldHist
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RecordSeq Desc: RecordSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PEVendWhldHistRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PEVendWhldHists_Company_VendorNum_RecordSeq(Company:string, VendorNum:string, RecordSeq:string, requestBody:Erp_Tablesets_PEVendWhldHistRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/PEVendWhldHists(" + Company + "," + VendorNum + "," + RecordSeq + ")", {
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
   Summary: Call UpdateExt to delete PEVendWhldHist item
   Description: Call UpdateExt to delete PEVendWhldHist item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PEVendWhldHist
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RecordSeq Desc: RecordSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PEVendWhldHists_Company_VendorNum_RecordSeq(Company:string, VendorNum:string, RecordSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/PEVendWhldHists(" + Company + "," + VendorNum + "," + RecordSeq + ")", {
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
   Description: Get VendRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendRestrictions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendRestrictionRow
   */  
export function get_VendRestrictions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRestrictions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendRestrictions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendRestrictionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VendRestrictionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendRestrictions(requestBody:Erp_Tablesets_VendRestrictionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRestrictions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VendRestriction item
   Description: Calls GetByID to retrieve the VendRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendRestrictionRow
   */  
export function get_VendRestrictions_Company_VendorNum_RestrictionTypeID(Company:string, VendorNum:string, RestrictionTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRestrictions(" + Company + "," + VendorNum + "," + RestrictionTypeID + ")", {
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
         resolve(data as Erp_Tablesets_VendRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendRestriction for the service
   Description: Calls UpdateExt to update VendRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendRestrictionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendRestrictions_Company_VendorNum_RestrictionTypeID(Company:string, VendorNum:string, RestrictionTypeID:string, requestBody:Erp_Tablesets_VendRestrictionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRestrictions(" + Company + "," + VendorNum + "," + RestrictionTypeID + ")", {
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
   Summary: Call UpdateExt to delete VendRestriction item
   Description: Call UpdateExt to delete VendRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendRestrictions_Company_VendorNum_RestrictionTypeID(Company:string, VendorNum:string, RestrictionTypeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRestrictions(" + Company + "," + VendorNum + "," + RestrictionTypeID + ")", {
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
   Description: Get VendBanks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendBanks
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendBankRow
   */  
export function get_VendBanks(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendBanks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendBankRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VendBankRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendBanks(requestBody:Erp_Tablesets_VendBankRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VendBank item
   Description: Calls GetByID to retrieve the VendBank item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendBank
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param BankID Desc: BankID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendBankRow
   */  
export function get_VendBanks_Company_VendorNum_BankID(Company:string, VendorNum:string, BankID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendBankRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks(" + Company + "," + VendorNum + "," + BankID + ")", {
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
         resolve(data as Erp_Tablesets_VendBankRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendBank for the service
   Description: Calls UpdateExt to update VendBank. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendBank
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param BankID Desc: BankID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendBankRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendBanks_Company_VendorNum_BankID(Company:string, VendorNum:string, BankID:string, requestBody:Erp_Tablesets_VendBankRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks(" + Company + "," + VendorNum + "," + BankID + ")", {
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
   Summary: Call UpdateExt to delete VendBank item
   Description: Call UpdateExt to delete VendBank item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendBank
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param BankID Desc: BankID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendBanks_Company_VendorNum_BankID(Company:string, VendorNum:string, BankID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks(" + Company + "," + VendorNum + "," + BankID + ")", {
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
   Description: Get VendBankAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendBankAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param BankID Desc: BankID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendBankAttchRow
   */  
export function get_VendBanks_Company_VendorNum_BankID_VendBankAttches(Company:string, VendorNum:string, BankID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks(" + Company + "," + VendorNum + "," + BankID + ")/VendBankAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendBankAttch item
   Description: Calls GetByID to retrieve the VendBankAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendBankAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param BankID Desc: BankID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendBankAttchRow
   */  
export function get_VendBanks_Company_VendorNum_BankID_VendBankAttches_Company_VendorNum_BankID_DrawingSeq(Company:string, VendorNum:string, BankID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendBankAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks(" + Company + "," + VendorNum + "," + BankID + ")/VendBankAttches(" + Company + "," + VendorNum + "," + BankID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_VendBankAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get VendBankAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendBankAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendBankAttchRow
   */  
export function get_VendBankAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBankAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendBankAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendBankAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VendBankAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendBankAttches(requestBody:Erp_Tablesets_VendBankAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBankAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VendBankAttch item
   Description: Calls GetByID to retrieve the VendBankAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendBankAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param BankID Desc: BankID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendBankAttchRow
   */  
export function get_VendBankAttches_Company_VendorNum_BankID_DrawingSeq(Company:string, VendorNum:string, BankID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendBankAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBankAttches(" + Company + "," + VendorNum + "," + BankID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_VendBankAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendBankAttch for the service
   Description: Calls UpdateExt to update VendBankAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendBankAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param BankID Desc: BankID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendBankAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendBankAttches_Company_VendorNum_BankID_DrawingSeq(Company:string, VendorNum:string, BankID:string, DrawingSeq:string, requestBody:Erp_Tablesets_VendBankAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBankAttches(" + Company + "," + VendorNum + "," + BankID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete VendBankAttch item
   Description: Call UpdateExt to delete VendBankAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendBankAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param BankID Desc: BankID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendBankAttches_Company_VendorNum_BankID_DrawingSeq(Company:string, VendorNum:string, BankID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBankAttches(" + Company + "," + VendorNum + "," + BankID + "," + DrawingSeq + ")", {
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
   Description: Get VendCntMains items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendCntMains
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntMainRow
   */  
export function get_VendCntMains(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntMainRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntMains", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntMainRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendCntMains
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendCntMainRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VendCntMainRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendCntMains(requestBody:Erp_Tablesets_VendCntMainRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntMains", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VendCntMain item
   Description: Calls GetByID to retrieve the VendCntMain item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCntMain
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendCntMainRow
   */  
export function get_VendCntMains_Company_VendorNum_PurPoint_ConNum(Company:string, VendorNum:string, PurPoint:string, ConNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendCntMainRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntMains(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")", {
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
         resolve(data as Erp_Tablesets_VendCntMainRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendCntMain for the service
   Description: Calls UpdateExt to update VendCntMain. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendCntMain
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendCntMainRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendCntMains_Company_VendorNum_PurPoint_ConNum(Company:string, VendorNum:string, PurPoint:string, ConNum:string, requestBody:Erp_Tablesets_VendCntMainRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntMains(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")", {
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
   Summary: Call UpdateExt to delete VendCntMain item
   Description: Call UpdateExt to delete VendCntMain item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendCntMain
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendCntMains_Company_VendorNum_PurPoint_ConNum(Company:string, VendorNum:string, PurPoint:string, ConNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntMains(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")", {
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
   Description: Get VenMFBills items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VenMFBills
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenMFBillRow
   */  
export function get_VenMFBills(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenMFBillRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenMFBills", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenMFBillRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VenMFBills
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VenMFBillRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VenMFBillRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VenMFBills(requestBody:Erp_Tablesets_VenMFBillRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenMFBills", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VenMFBill item
   Description: Calls GetByID to retrieve the VenMFBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenMFBill
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PayBTFlag Desc: PayBTFlag   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VenMFBillRow
   */  
export function get_VenMFBills_Company_VendorNum_PayBTFlag(Company:string, VendorNum:string, PayBTFlag:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VenMFBillRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenMFBills(" + Company + "," + VendorNum + "," + PayBTFlag + ")", {
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
         resolve(data as Erp_Tablesets_VenMFBillRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VenMFBill for the service
   Description: Calls UpdateExt to update VenMFBill. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VenMFBill
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PayBTFlag Desc: PayBTFlag   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VenMFBillRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VenMFBills_Company_VendorNum_PayBTFlag(Company:string, VendorNum:string, PayBTFlag:string, requestBody:Erp_Tablesets_VenMFBillRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenMFBills(" + Company + "," + VendorNum + "," + PayBTFlag + ")", {
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
   Summary: Call UpdateExt to delete VenMFBill item
   Description: Call UpdateExt to delete VenMFBill item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VenMFBill
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PayBTFlag Desc: PayBTFlag   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VenMFBills_Company_VendorNum_PayBTFlag(Company:string, VendorNum:string, PayBTFlag:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenMFBills(" + Company + "," + VendorNum + "," + PayBTFlag + ")", {
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
   Description: Get VendorPPs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendorPPs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorPPRow
   */  
export function get_VendorPPs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendorPPs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendorPPRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VendorPPRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendorPPs(requestBody:Erp_Tablesets_VendorPPRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VendorPP item
   Description: Calls GetByID to retrieve the VendorPP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendorPP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendorPPRow
   */  
export function get_VendorPPs_Company_VendorNum_PurPoint(Company:string, VendorNum:string, PurPoint:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendorPPRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")", {
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
         resolve(data as Erp_Tablesets_VendorPPRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendorPP for the service
   Description: Calls UpdateExt to update VendorPP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendorPP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendorPPRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendorPPs_Company_VendorNum_PurPoint(Company:string, VendorNum:string, PurPoint:string, requestBody:Erp_Tablesets_VendorPPRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")", {
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
   Summary: Call UpdateExt to delete VendorPP item
   Description: Call UpdateExt to delete VendorPP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendorPP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendorPPs_Company_VendorNum_PurPoint(Company:string, VendorNum:string, PurPoint:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")", {
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
   Description: Get VenPPMFBills items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VenPPMFBills1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenPPMFBillRow
   */  
export function get_VendorPPs_Company_VendorNum_PurPoint_VenPPMFBills(Company:string, VendorNum:string, PurPoint:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenPPMFBillRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VenPPMFBills", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenPPMFBillRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VenPPMFBill item
   Description: Calls GetByID to retrieve the VenPPMFBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenPPMFBill1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PayBTFlag Desc: PayBTFlag   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VenPPMFBillRow
   */  
export function get_VendorPPs_Company_VendorNum_PurPoint_VenPPMFBills_Company_VendorNum_PurPoint_PayBTFlag(Company:string, VendorNum:string, PurPoint:string, PayBTFlag:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VenPPMFBillRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VenPPMFBills(" + Company + "," + VendorNum + "," + PurPoint + "," + PayBTFlag + ")", {
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
         resolve(data as Erp_Tablesets_VenPPMFBillRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VenPPUPSEmails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VenPPUPSEmails1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenPPUPSEmailRow
   */  
export function get_VendorPPs_Company_VendorNum_PurPoint_VenPPUPSEmails(Company:string, VendorNum:string, PurPoint:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenPPUPSEmailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VenPPUPSEmails", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenPPUPSEmailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VenPPUPSEmail item
   Description: Calls GetByID to retrieve the VenPPUPSEmail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenPPUPSEmail1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VenPPUPSEmailRow
   */  
export function get_VendorPPs_Company_VendorNum_PurPoint_VenPPUPSEmails_Company_VendorNum_PurPoint_UPSQVSeq(Company:string, VendorNum:string, PurPoint:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VenPPUPSEmailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VenPPUPSEmails(" + Company + "," + VendorNum + "," + PurPoint + "," + UPSQVSeq + ")", {
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
         resolve(data as Erp_Tablesets_VenPPUPSEmailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VendPPRestrictions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendPPRestrictions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPPRestrictionRow
   */  
export function get_VendorPPs_Company_VendorNum_PurPoint_VendPPRestrictions(Company:string, VendorNum:string, PurPoint:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPPRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VendPPRestrictions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPPRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendPPRestriction item
   Description: Calls GetByID to retrieve the VendPPRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPPRestriction1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendPPRestrictionRow
   */  
export function get_VendorPPs_Company_VendorNum_PurPoint_VendPPRestrictions_Company_VendorNum_PurPoint_RestrictionTypeID(Company:string, VendorNum:string, PurPoint:string, RestrictionTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendPPRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VendPPRestrictions(" + Company + "," + VendorNum + "," + PurPoint + "," + RestrictionTypeID + ")", {
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
         resolve(data as Erp_Tablesets_VendPPRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VendCnts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendCnts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntRow
   */  
export function get_VendorPPs_Company_VendorNum_PurPoint_VendCnts(Company:string, VendorNum:string, PurPoint:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VendCnts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendCnt item
   Description: Calls GetByID to retrieve the VendCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCnt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendCntRow
   */  
export function get_VendorPPs_Company_VendorNum_PurPoint_VendCnts_Company_VendorNum_PurPoint_ConNum(Company:string, VendorNum:string, PurPoint:string, ConNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VendCnts(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")", {
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
         resolve(data as Erp_Tablesets_VendCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get VenPPMFBills items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VenPPMFBills
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenPPMFBillRow
   */  
export function get_VenPPMFBills(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenPPMFBillRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPMFBills", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenPPMFBillRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VenPPMFBills
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VenPPMFBillRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VenPPMFBillRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VenPPMFBills(requestBody:Erp_Tablesets_VenPPMFBillRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPMFBills", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VenPPMFBill item
   Description: Calls GetByID to retrieve the VenPPMFBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenPPMFBill
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PayBTFlag Desc: PayBTFlag   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VenPPMFBillRow
   */  
export function get_VenPPMFBills_Company_VendorNum_PurPoint_PayBTFlag(Company:string, VendorNum:string, PurPoint:string, PayBTFlag:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VenPPMFBillRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPMFBills(" + Company + "," + VendorNum + "," + PurPoint + "," + PayBTFlag + ")", {
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
         resolve(data as Erp_Tablesets_VenPPMFBillRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VenPPMFBill for the service
   Description: Calls UpdateExt to update VenPPMFBill. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VenPPMFBill
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PayBTFlag Desc: PayBTFlag   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VenPPMFBillRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VenPPMFBills_Company_VendorNum_PurPoint_PayBTFlag(Company:string, VendorNum:string, PurPoint:string, PayBTFlag:string, requestBody:Erp_Tablesets_VenPPMFBillRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPMFBills(" + Company + "," + VendorNum + "," + PurPoint + "," + PayBTFlag + ")", {
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
   Summary: Call UpdateExt to delete VenPPMFBill item
   Description: Call UpdateExt to delete VenPPMFBill item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VenPPMFBill
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PayBTFlag Desc: PayBTFlag   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VenPPMFBills_Company_VendorNum_PurPoint_PayBTFlag(Company:string, VendorNum:string, PurPoint:string, PayBTFlag:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPMFBills(" + Company + "," + VendorNum + "," + PurPoint + "," + PayBTFlag + ")", {
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
   Description: Get VenPPUPSEmails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VenPPUPSEmails
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenPPUPSEmailRow
   */  
export function get_VenPPUPSEmails(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenPPUPSEmailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPUPSEmails", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenPPUPSEmailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VenPPUPSEmails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VenPPUPSEmailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VenPPUPSEmailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VenPPUPSEmails(requestBody:Erp_Tablesets_VenPPUPSEmailRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPUPSEmails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VenPPUPSEmail item
   Description: Calls GetByID to retrieve the VenPPUPSEmail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenPPUPSEmail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VenPPUPSEmailRow
   */  
export function get_VenPPUPSEmails_Company_VendorNum_PurPoint_UPSQVSeq(Company:string, VendorNum:string, PurPoint:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VenPPUPSEmailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPUPSEmails(" + Company + "," + VendorNum + "," + PurPoint + "," + UPSQVSeq + ")", {
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
         resolve(data as Erp_Tablesets_VenPPUPSEmailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VenPPUPSEmail for the service
   Description: Calls UpdateExt to update VenPPUPSEmail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VenPPUPSEmail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VenPPUPSEmailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VenPPUPSEmails_Company_VendorNum_PurPoint_UPSQVSeq(Company:string, VendorNum:string, PurPoint:string, UPSQVSeq:string, requestBody:Erp_Tablesets_VenPPUPSEmailRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPUPSEmails(" + Company + "," + VendorNum + "," + PurPoint + "," + UPSQVSeq + ")", {
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
   Summary: Call UpdateExt to delete VenPPUPSEmail item
   Description: Call UpdateExt to delete VenPPUPSEmail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VenPPUPSEmail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VenPPUPSEmails_Company_VendorNum_PurPoint_UPSQVSeq(Company:string, VendorNum:string, PurPoint:string, UPSQVSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPUPSEmails(" + Company + "," + VendorNum + "," + PurPoint + "," + UPSQVSeq + ")", {
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
   Description: Get VendPPRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendPPRestrictions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPPRestrictionRow
   */  
export function get_VendPPRestrictions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPPRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendPPRestrictions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPPRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendPPRestrictions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendPPRestrictionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VendPPRestrictionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendPPRestrictions(requestBody:Erp_Tablesets_VendPPRestrictionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendPPRestrictions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VendPPRestriction item
   Description: Calls GetByID to retrieve the VendPPRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPPRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendPPRestrictionRow
   */  
export function get_VendPPRestrictions_Company_VendorNum_PurPoint_RestrictionTypeID(Company:string, VendorNum:string, PurPoint:string, RestrictionTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendPPRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendPPRestrictions(" + Company + "," + VendorNum + "," + PurPoint + "," + RestrictionTypeID + ")", {
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
         resolve(data as Erp_Tablesets_VendPPRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendPPRestriction for the service
   Description: Calls UpdateExt to update VendPPRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendPPRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendPPRestrictionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendPPRestrictions_Company_VendorNum_PurPoint_RestrictionTypeID(Company:string, VendorNum:string, PurPoint:string, RestrictionTypeID:string, requestBody:Erp_Tablesets_VendPPRestrictionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendPPRestrictions(" + Company + "," + VendorNum + "," + PurPoint + "," + RestrictionTypeID + ")", {
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
   Summary: Call UpdateExt to delete VendPPRestriction item
   Description: Call UpdateExt to delete VendPPRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendPPRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendPPRestrictions_Company_VendorNum_PurPoint_RestrictionTypeID(Company:string, VendorNum:string, PurPoint:string, RestrictionTypeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendPPRestrictions(" + Company + "," + VendorNum + "," + PurPoint + "," + RestrictionTypeID + ")", {
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
   Description: Get VendCnts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendCnts
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntRow
   */  
export function get_VendCnts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendCnts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendCntRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VendCntRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendCnts(requestBody:Erp_Tablesets_VendCntRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VendCnt item
   Description: Calls GetByID to retrieve the VendCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendCntRow
   */  
export function get_VendCnts_Company_VendorNum_PurPoint_ConNum(Company:string, VendorNum:string, PurPoint:string, ConNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")", {
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
         resolve(data as Erp_Tablesets_VendCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendCnt for the service
   Description: Calls UpdateExt to update VendCnt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendCntRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendCnts_Company_VendorNum_PurPoint_ConNum(Company:string, VendorNum:string, PurPoint:string, ConNum:string, requestBody:Erp_Tablesets_VendCntRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")", {
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
   Summary: Call UpdateExt to delete VendCnt item
   Description: Call UpdateExt to delete VendCnt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendCnts_Company_VendorNum_PurPoint_ConNum(Company:string, VendorNum:string, PurPoint:string, ConNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")", {
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
   Description: Get VendCntAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendCntAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntAttchRow
   */  
export function get_VendCnts_Company_VendorNum_PurPoint_ConNum_VendCntAttches(Company:string, VendorNum:string, PurPoint:string, ConNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")/VendCntAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendCntAttch item
   Description: Calls GetByID to retrieve the VendCntAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCntAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendCntAttchRow
   */  
export function get_VendCnts_Company_VendorNum_PurPoint_ConNum_VendCntAttches_Company_VendorNum_PurPoint_ConNum_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, ConNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendCntAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")/VendCntAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_VendCntAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get VendCntAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendCntAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntAttchRow
   */  
export function get_VendCntAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendCntAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendCntAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VendCntAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendCntAttches(requestBody:Erp_Tablesets_VendCntAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VendCntAttch item
   Description: Calls GetByID to retrieve the VendCntAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCntAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendCntAttchRow
   */  
export function get_VendCntAttches_Company_VendorNum_PurPoint_ConNum_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, ConNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendCntAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_VendCntAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendCntAttch for the service
   Description: Calls UpdateExt to update VendCntAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendCntAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendCntAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendCntAttches_Company_VendorNum_PurPoint_ConNum_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, ConNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_VendCntAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete VendCntAttch item
   Description: Call UpdateExt to delete VendCntAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendCntAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendCntAttches_Company_VendorNum_PurPoint_ConNum_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, ConNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + "," + DrawingSeq + ")", {
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
   Description: Get VenUPSEmails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VenUPSEmails
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenUPSEmailRow
   */  
export function get_VenUPSEmails(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenUPSEmailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenUPSEmails", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenUPSEmailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VenUPSEmails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VenUPSEmailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VenUPSEmailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VenUPSEmails(requestBody:Erp_Tablesets_VenUPSEmailRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenUPSEmails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VenUPSEmail item
   Description: Calls GetByID to retrieve the VenUPSEmail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenUPSEmail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VenUPSEmailRow
   */  
export function get_VenUPSEmails_Company_VendorNum_UPSQVSeq(Company:string, VendorNum:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VenUPSEmailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenUPSEmails(" + Company + "," + VendorNum + "," + UPSQVSeq + ")", {
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
         resolve(data as Erp_Tablesets_VenUPSEmailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VenUPSEmail for the service
   Description: Calls UpdateExt to update VenUPSEmail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VenUPSEmail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VenUPSEmailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VenUPSEmails_Company_VendorNum_UPSQVSeq(Company:string, VendorNum:string, UPSQVSeq:string, requestBody:Erp_Tablesets_VenUPSEmailRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenUPSEmails(" + Company + "," + VendorNum + "," + UPSQVSeq + ")", {
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
   Summary: Call UpdateExt to delete VenUPSEmail item
   Description: Call UpdateExt to delete VenUPSEmail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VenUPSEmail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VenUPSEmails_Company_VendorNum_UPSQVSeq(Company:string, VendorNum:string, UPSQVSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenUPSEmails(" + Company + "," + VendorNum + "," + UPSQVSeq + ")", {
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
   Description: Get VendorAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendorAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorAttchRow
   */  
export function get_VendorAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendorAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendorAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VendorAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendorAttches(requestBody:Erp_Tablesets_VendorAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VendorAttch item
   Description: Calls GetByID to retrieve the VendorAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendorAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendorAttchRow
   */  
export function get_VendorAttches_Company_VendorNum_DrawingSeq(Company:string, VendorNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendorAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorAttches(" + Company + "," + VendorNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_VendorAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendorAttch for the service
   Description: Calls UpdateExt to update VendorAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendorAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendorAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendorAttches_Company_VendorNum_DrawingSeq(Company:string, VendorNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_VendorAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorAttches(" + Company + "," + VendorNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete VendorAttch item
   Description: Call UpdateExt to delete VendorAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendorAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendorAttches_Company_VendorNum_DrawingSeq(Company:string, VendorNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorAttches(" + Company + "," + VendorNum + "," + DrawingSeq + ")", {
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
   Description: Get Partners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Partners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartnerRow
   */  
export function get_Partners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Partners", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Partners
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartnerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Partners(requestBody:Erp_Tablesets_PartnerRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Partners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the Partner item
   Description: Calls GetByID to retrieve the Partner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Partner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartnerNum Desc: PartnerNum   Required: True
      @param PartnerType Desc: PartnerType   Required: True
      @param PartnerID Desc: PartnerID   Required: True   Allow empty value : True
      @param SearchID Desc: SearchID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartnerRow
   */  
export function get_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company:string, PartnerNum:string, PartnerType:string, PartnerID:string, SearchID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartnerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
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
         resolve(data as Erp_Tablesets_PartnerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Partner for the service
   Description: Calls UpdateExt to update Partner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Partner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartnerNum Desc: PartnerNum   Required: True
      @param PartnerType Desc: PartnerType   Required: True
      @param PartnerID Desc: PartnerID   Required: True   Allow empty value : True
      @param SearchID Desc: SearchID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company:string, PartnerNum:string, PartnerType:string, PartnerID:string, SearchID:string, requestBody:Erp_Tablesets_PartnerRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
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
   Summary: Call UpdateExt to delete Partner item
   Description: Call UpdateExt to delete Partner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Partner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartnerNum Desc: PartnerNum   Required: True
      @param PartnerType Desc: PartnerType   Required: True
      @param PartnerID Desc: PartnerID   Required: True   Allow empty value : True
      @param SearchID Desc: SearchID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company:string, PartnerNum:string, PartnerType:string, PartnerID:string, SearchID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
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
   Description: Get VendRemitToes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendRemitToes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendRemitToRow
   */  
export function get_VendRemitToes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendRemitToRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRemitToes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendRemitToRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendRemitToes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendRemitToRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VendRemitToRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendRemitToes(requestBody:Erp_Tablesets_VendRemitToRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRemitToes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the VendRemitTo item
   Description: Calls GetByID to retrieve the VendRemitTo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendRemitTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RemitToSeq Desc: RemitToSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendRemitToRow
   */  
export function get_VendRemitToes_Company_VendorNum_RemitToSeq(Company:string, VendorNum:string, RemitToSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendRemitToRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRemitToes(" + Company + "," + VendorNum + "," + RemitToSeq + ")", {
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
         resolve(data as Erp_Tablesets_VendRemitToRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendRemitTo for the service
   Description: Calls UpdateExt to update VendRemitTo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendRemitTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RemitToSeq Desc: RemitToSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendRemitToRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendRemitToes_Company_VendorNum_RemitToSeq(Company:string, VendorNum:string, RemitToSeq:string, requestBody:Erp_Tablesets_VendRemitToRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRemitToes(" + Company + "," + VendorNum + "," + RemitToSeq + ")", {
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
   Summary: Call UpdateExt to delete VendRemitTo item
   Description: Call UpdateExt to delete VendRemitTo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendRemitTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RemitToSeq Desc: RemitToSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendRemitToes_Company_VendorNum_RemitToSeq(Company:string, VendorNum:string, RemitToSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRemitToes(" + Company + "," + VendorNum + "," + RemitToSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorListRow)
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
export function get_GetRows(whereClauseVendor:string, whereClauseVendorAttch:string, whereClauseEntityGLC:string, whereClauseTaxExempt:string, whereClausePartner:string, whereClausePEVendWhldHist:string, whereClauseVendRestriction:string, whereClauseVendBank:string, whereClauseVendBankAttch:string, whereClauseVendCntMain:string, whereClauseVenMFBill:string, whereClauseVendorPP:string, whereClauseVenPPMFBill:string, whereClauseVenPPUPSEmail:string, whereClauseVendPPRestriction:string, whereClauseVendCnt:string, whereClauseVendCntAttch:string, whereClauseVenUPSEmail:string, whereClauseVendRemitTo:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseVendor!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendor=" + whereClauseVendor
   }
   if(typeof whereClauseVendorAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendorAttch=" + whereClauseVendorAttch
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
   if(typeof whereClauseTaxExempt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxExempt=" + whereClauseTaxExempt
   }
   if(typeof whereClausePartner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartner=" + whereClausePartner
   }
   if(typeof whereClausePEVendWhldHist!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePEVendWhldHist=" + whereClausePEVendWhldHist
   }
   if(typeof whereClauseVendRestriction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendRestriction=" + whereClauseVendRestriction
   }
   if(typeof whereClauseVendBank!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendBank=" + whereClauseVendBank
   }
   if(typeof whereClauseVendBankAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendBankAttch=" + whereClauseVendBankAttch
   }
   if(typeof whereClauseVendCntMain!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendCntMain=" + whereClauseVendCntMain
   }
   if(typeof whereClauseVenMFBill!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVenMFBill=" + whereClauseVenMFBill
   }
   if(typeof whereClauseVendorPP!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendorPP=" + whereClauseVendorPP
   }
   if(typeof whereClauseVenPPMFBill!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVenPPMFBill=" + whereClauseVenPPMFBill
   }
   if(typeof whereClauseVenPPUPSEmail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVenPPUPSEmail=" + whereClauseVenPPUPSEmail
   }
   if(typeof whereClauseVendPPRestriction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendPPRestriction=" + whereClauseVendPPRestriction
   }
   if(typeof whereClauseVendCnt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendCnt=" + whereClauseVendCnt
   }
   if(typeof whereClauseVendCntAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendCntAttch=" + whereClauseVendCntAttch
   }
   if(typeof whereClauseVenUPSEmail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVenUPSEmail=" + whereClauseVenUPSEmail
   }
   if(typeof whereClauseVendRemitTo!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendRemitTo=" + whereClauseVendRemitTo
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetRows" + params, {
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
export function get_GetByID(vendorNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof vendorNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vendorNum=" + vendorNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetList" + params, {
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
   Summary: Invoke method GetNettingSupplierList
   Description: Returns a list of Netting Suppliers only rows that satisfy the where clause.
   OperationID: GetNettingSupplierList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNettingSupplierList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNettingSupplierList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNettingSupplierList(requestBody:GetNettingSupplierList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNettingSupplierList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNettingSupplierList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNettingSupplierList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeBankBranchCode
   Description: Check if the Bank Branch code changed.
   OperationID: ChangeBankBranchCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeBankBranchCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBankBranchCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBankBranchCode(requestBody:ChangeBankBranchCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeBankBranchCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeBankBranchCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeBankBranchCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCalendar
   Description: Change Calendar for new and updated vendors
   OperationID: ChangeCalendar
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCalendar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCalendar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCalendar(requestBody:ChangeCalendar_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCalendar_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeCalendar", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeCalendar_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaxRegion
   Description: This method validates TaxRegionCode and populates description for supplier.
   OperationID: ChangeTaxRegion
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTaxRegion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxRegion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxRegion(requestBody:ChangeTaxRegion_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTaxRegion_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeTaxRegion", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTaxRegion_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRemitToType
   Description: Future logic for scr 114469. Currently on hold. Check if the RemitToType changed.
   OperationID: ChangeRemitToType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRemitToType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRemitToType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRemitToType(requestBody:ChangeRemitToType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRemitToType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeRemitToType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRemitToType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRemitToID
   Description: Future logic for scr 114469. Currently on hold.  Check if the RemitToID changed.
   OperationID: ChangeRemitToID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRemitToID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRemitToID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRemitToID(requestBody:ChangeRemitToID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRemitToID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeRemitToID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRemitToID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendRemitToCountry
   Description: Future logic for scr 114469. Currently on hold.  Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendRemitToCountry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendRemitToCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendRemitToCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendRemitToCountry(requestBody:ChangeVendRemitToCountry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendRemitToCountry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVendRemitToCountry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendRemitToCountry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CompareCountryTaxLiabality
   Description: This method compares the Vendor TaxRegionCode with the Country TaxRegionCode
   OperationID: CompareCountryTaxLiabality
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CompareCountryTaxLiabality_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompareCountryTaxLiabality_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CompareCountryTaxLiabality(requestBody:CompareCountryTaxLiabality_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CompareCountryTaxLiabality_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/CompareCountryTaxLiabality", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CompareCountryTaxLiabality_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendCountry
   Description: Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendCountry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendCountry(requestBody:ChangeVendCountry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendCountry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVendCountry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendCountry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendBankPayMethod
   Description: Method to change the payment method.
   OperationID: ChangeVendBankPayMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendBankPayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendBankPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendBankPayMethod(requestBody:ChangeVendBankPayMethod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendBankPayMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVendBankPayMethod", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendBankPayMethod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendPayMethod
   Description: Method to change the payment method.
   OperationID: ChangeVendPayMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendPayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendPayMethod(requestBody:ChangeVendPayMethod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendPayMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVendPayMethod", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendPayMethod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVenMFBillCountry
   Description: Method to change related fields to the county within Manifest Billing. Run when the country changes.
   OperationID: ChangeVenMFBillCountry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVenMFBillCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVenMFBillCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVenMFBillCountry(requestBody:ChangeVenMFBillCountry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVenMFBillCountry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVenMFBillCountry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVenMFBillCountry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVenPPMFBillCountry
   Description: Method to change related fields to the county within Purchase Points Manifest Billing. Run when the country changes.
   OperationID: ChangeVenPPMFBillCountry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVenPPMFBillCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVenPPMFBillCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVenPPMFBillCountry(requestBody:ChangeVenPPMFBillCountry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVenPPMFBillCountry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVenPPMFBillCountry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVenPPMFBillCountry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendGlobalVendor
   Description: Method to call when changing the global vendor flag on a vendor.
Assigns the GlbFlag base on the new value.
   OperationID: ChangeVendGlobalVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendGlobalVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendGlobalVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendGlobalVendor(requestBody:ChangeVendGlobalVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendGlobalVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVendGlobalVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendGlobalVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendICTrader
   Description: Method to call when changing the ICTrader flag on a vendor.
Assigns the EnableGlobalVendor based on the new value.
   OperationID: ChangeVendICTrader
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendICTrader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendICTrader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendICTrader(requestBody:ChangeVendICTrader_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendICTrader_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVendICTrader", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendICTrader_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendPPCountry
   Description: Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendPPCountry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendPPCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendPPCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendPPCountry(requestBody:ChangeVendPPCountry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendPPCountry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVendPPCountry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendPPCountry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendPPFFCountry
   Description: Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendPPFFCountry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendPPFFCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendPPFFCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendPPFFCountry(requestBody:ChangeVendPPFFCountry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendPPFFCountry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVendPPFFCountry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendPPFFCountry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendBankCountry
   Description: Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendBankCountry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendBankCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendBankCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendBankCountry(requestBody:ChangeVendBankCountry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendBankCountry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVendBankCountry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendBankCountry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendBankBCountry
   Description: Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendBankBCountry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendBankBCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendBankBCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendBankBCountry(requestBody:ChangeVendBankBCountry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendBankBCountry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVendBankBCountry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendBankBCountry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendFFCountry
   Description: Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendFFCountry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendFFCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendFFCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendFFCountry(requestBody:ChangeVendFFCountry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendFFCountry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ChangeVendFFCountry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendFFCountry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckRUC
   Description: CSF Peru - This method test the validity of the Tax ID (RUC)
   OperationID: CheckRUC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckRUC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRUC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRUC(requestBody:CheckRUC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckRUC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/CheckRUC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckRUC_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckVATFormat
   Description: This method test the validity of the VAT format
   OperationID: CheckVATFormat
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckVATFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckVATFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckVATFormat(requestBody:CheckVATFormat_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckVATFormat_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/CheckVATFormat", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckVATFormat_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultName
   Description: If the Vendor Contact name is updated this method will parse the name into
firstname middlename and lastname fields.
If one of the name components is updated the components will be assembled into
the Vendor Contact name field
            
The contact must exist in the database before this method can be run. This means
that the update method must be run first.
            
The rowmod column must be set to 'U' in order for the method to process the record.
            
This procedure passes a dataset in and out,
   OperationID: DefaultName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultName(requestBody:DefaultName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/DefaultName", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EnablePriceList
   Description: This method checks to see if the price list option should be enabled or not
based on security rights.
   OperationID: EnablePriceList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnablePriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnablePriceList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<EnablePriceList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/EnablePriceList", {
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
         resolve(data as EnablePriceList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAddrElementList
   Description: This method calculates Address Element List
   OperationID: GetAddrElementList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAddrElementList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAddrElementList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAddrElementList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetAddrElementList", {
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
         resolve(data as GetAddrElementList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByVendID
   Description: Get vendor by ID
   OperationID: GetByVendID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByVendID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByVendID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByVendID(requestBody:GetByVendID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByVendID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetByVendID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByVendID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGlbVendorList
   Description: This method returns the GlbVendor dataset based on a delimited list of
GlbVendorNum values passed in.
If GlbVendor.VendorNum = -1 that means the record has been skipped and should be shown
at the bottom of the browser. (GlbVendor only)
   OperationID: GetGlbVendorList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGlbVendorList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlbVendorList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGlbVendorList(requestBody:GetGlbVendorList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGlbVendorList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetGlbVendorList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetGlbVendorList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPerConData
   Description: Gets the person contact information.
   OperationID: GetPerConData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPerConData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPerConData(requestBody:GetPerConData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPerConData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetPerConData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPerConData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVendorForLink
   Description: This returns the Vendor dataset for linking.
   OperationID: GetVendorForLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetVendorForLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorForLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendorForLink(requestBody:GetVendorForLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVendorForLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetVendorForLink", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetVendorForLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVendorGlobalFieldsWithoutGlobalLock
   Description: Returns the list of fields that are maintained by the "Master/Owner" of the global record without the GlobalLock field.
   OperationID: GetVendorGlobalFieldsWithoutGlobalLock
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetVendorGlobalFieldsWithoutGlobalLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorGlobalFieldsWithoutGlobalLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendorGlobalFieldsWithoutGlobalLock(requestBody:GetVendorGlobalFieldsWithoutGlobalLock_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVendorGlobalFieldsWithoutGlobalLock_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetVendorGlobalFieldsWithoutGlobalLock", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetVendorGlobalFieldsWithoutGlobalLock_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetvendorGlobalFields
   Description: return the list of fields that are maintained by the "Master/Owner" of global record
   OperationID: GetvendorGlobalFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetvendorGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetvendorGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetvendorGlobalFields(requestBody:GetvendorGlobalFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetvendorGlobalFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetvendorGlobalFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetvendorGlobalFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVendorPPGlobalFieldsWithPrimaryPP
   Description: Returns the list of fields that are maintained by the "Master/Owner" of the global record with the PrimaryPP field.
   OperationID: GetVendorPPGlobalFieldsWithPrimaryPP
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetVendorPPGlobalFieldsWithPrimaryPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorPPGlobalFieldsWithPrimaryPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendorPPGlobalFieldsWithPrimaryPP(requestBody:GetVendorPPGlobalFieldsWithPrimaryPP_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVendorPPGlobalFieldsWithPrimaryPP_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetVendorPPGlobalFieldsWithPrimaryPP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetVendorPPGlobalFieldsWithPrimaryPP_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetvendorPPGlobalFields
   Description: return the list of fields that are maintained by the "Master/Owner" of global record
   OperationID: GetvendorPPGlobalFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetvendorPPGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetvendorPPGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetvendorPPGlobalFields(requestBody:GetvendorPPGlobalFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetvendorPPGlobalFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetvendorPPGlobalFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetvendorPPGlobalFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVendCntGlobalFieldsWithPrimaryContact
   Description: Returns the list of fields that are maintained by the "Master/Owner" of the global record with the PerConName and PrimaryContact fields.
   OperationID: GetVendCntGlobalFieldsWithPrimaryContact
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetVendCntGlobalFieldsWithPrimaryContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendCntGlobalFieldsWithPrimaryContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendCntGlobalFieldsWithPrimaryContact(requestBody:GetVendCntGlobalFieldsWithPrimaryContact_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVendCntGlobalFieldsWithPrimaryContact_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetVendCntGlobalFieldsWithPrimaryContact", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetVendCntGlobalFieldsWithPrimaryContact_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetvendCntGlobalFields
   Description: return the list of fields that are maintained by the "Master/Owner" of global record
   OperationID: GetvendCntGlobalFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetvendCntGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetvendCntGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetvendCntGlobalFields(requestBody:GetvendCntGlobalFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetvendCntGlobalFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetvendCntGlobalFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetvendCntGlobalFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVendorPPForLink
   Description: This returns the VendorPP record in the Vendor dataset for linking.
   OperationID: GetVendorPPForLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetVendorPPForLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorPPForLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendorPPForLink(requestBody:GetVendorPPForLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVendorPPForLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetVendorPPForLink", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetVendorPPForLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GlbVendorsExist
   Description: This method checks if GlbVendor records exists or not.  Can be used
to determine if the option to link/unlink vendors is available.
   OperationID: GlbVendorsExist
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlbVendorsExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbVendorsExist(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GlbVendorsExist_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GlbVendorsExist", {
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
         resolve(data as GlbVendorsExist_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LinkGlbVendCnt
   Description: This method performs the actual logic to link VendCnt records for a linked vendor.
It will only allow VendCnt's of linked vendors to be processed, otherwise an exception
will be raised.  The ability to link VendCnt's for a linked Vendor should be offered
immediately after performing the update method on a Linked Vendor or a Linked Purchase Point
but it does not have to be limited to that time only.
If the Contact is for a VendCnt that already exists, the GlbVendCnt information is
translated and then copied to the VendorDataSet as an update.
If the Contact is for a new Vendor or Purchase Point, the GlbVendCnt information is translated
and then copied to the VendorDataSet as an Add.  Until the update method is run on the Contact
record the Link process is not completed.
If this link is for a contact on the Vendor, the contact data in the VendorDataSet
will be returned in the VendCntMain datatable.  If it is for a purchase point, the data will
returned in the VendCnt datatable.  This is determined by the value of glbPurPoint.  If it is
blank, it is processed as a contact for the vendor; otherwise it is process as a contact for
the purchase point.
   OperationID: LinkGlbVendCnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LinkGlbVendCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbVendCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LinkGlbVendCnt(requestBody:LinkGlbVendCnt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LinkGlbVendCnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/LinkGlbVendCnt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LinkGlbVendCnt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LinkGlbVendor
   Description: This method performs the actual logic behind linking a Vendor.  It is run after
the PreLinkGlbVendor method which determines the Vendor ID to link to.
If the Vendor Id is for a Vendor that already exists, the GlbVendor information is
translated and then copied to the VendorDataSet as an update.
If the Vendor ID is for a new Vendor, the GlbVendor information is translated and then
copied to the VendorDataSet as an Add.  Until the update method is run on Vendor record
the Link process is not completed.
Once the Vendor record has been linked, the GlbVendorPP and GlbVendCnt records needs to
be offered up to be linked as well.
   OperationID: LinkGlbVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LinkGlbVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LinkGlbVendor(requestBody:LinkGlbVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LinkGlbVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/LinkGlbVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LinkGlbVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LinkGlbVendorPP
   Description: This method performs the actual logic to link VendorPP records for a linked vendor.
It will only allow VendorPP's of linked vendors to be processed, otherwise an exception
will be raised.  The ability to link VendorPP's for a linked Vendor should be offered
immediately after performing the update method on a Linked Vendor but it does not have
to be limited to that time only.
It is run after the PreLinkGlbVendorPP method which determines the PurPoint to link to.
If the PurPoint is for a VendorPP that already exists, the GlbVendorPP information is
translated and then copied to the VendorDataSet as an update.
If the PurPoint is for a new VendorPP, the GlbVendorPP information is translated and then
copied to the VendorDataSet as an Add.  Until the update method is run on the VendorPP
record the Link process is not completed.
Once the VendorPP record has been linked, the GlbVendCnt records need to be offered up
to be linked as well.
   OperationID: LinkGlbVendorPP
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LinkGlbVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LinkGlbVendorPP(requestBody:LinkGlbVendorPP_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LinkGlbVendorPP_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/LinkGlbVendorPP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LinkGlbVendorPP_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshGlbVendor
   Description: Refresh global vendor row
   OperationID: RefreshGlbVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshGlbVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshGlbVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshGlbVendor(requestBody:RefreshGlbVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshGlbVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/RefreshGlbVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RefreshGlbVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshGlbVendorPP
   Description: Refresh global purchase point row
   OperationID: RefreshGlbVendorPP
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshGlbVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshGlbVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshGlbVendorPP(requestBody:RefreshGlbVendorPP_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshGlbVendorPP_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/RefreshGlbVendorPP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RefreshGlbVendorPP_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshGlbVendCnt
   Description: Refresh global contact row
   OperationID: RefreshGlbVendCnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshGlbVendCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshGlbVendCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshGlbVendCnt(requestBody:RefreshGlbVendCnt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshGlbVendCnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/RefreshGlbVendCnt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RefreshGlbVendCnt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SkipGlbVendorPP
   Description: Mark unlinked GlbVendorPP records as skipped
   OperationID: SkipGlbVendorPP
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SkipGlbVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SkipGlbVendorPP(requestBody:SkipGlbVendorPP_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SkipGlbVendorPP_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/SkipGlbVendorPP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SkipGlbVendorPP_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SkipSingleGlbVendorPP
   Description: Mark a specific GlbVendorPP records as skipped
   OperationID: SkipSingleGlbVendorPP
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SkipSingleGlbVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipSingleGlbVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SkipSingleGlbVendorPP(requestBody:SkipSingleGlbVendorPP_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SkipSingleGlbVendorPP_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/SkipSingleGlbVendorPP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SkipSingleGlbVendorPP_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SkipGlbVendCnt
   Description: Mark unlinked GlbVendCnt records as skipped
   OperationID: SkipGlbVendCnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SkipGlbVendCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbVendCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SkipGlbVendCnt(requestBody:SkipGlbVendCnt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SkipGlbVendCnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/SkipGlbVendCnt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SkipGlbVendCnt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SkipSingleGlbVendCnt
   Description: Mark a specific GlbVendCnt records as skipped
   OperationID: SkipSingleGlbVendCnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SkipSingleGlbVendCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipSingleGlbVendCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SkipSingleGlbVendCnt(requestBody:SkipSingleGlbVendCnt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SkipSingleGlbVendCnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/SkipSingleGlbVendCnt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SkipSingleGlbVendCnt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ModifySearchIDs
   Description: Modify Search ID.
   OperationID: ModifySearchIDs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ModifySearchIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifySearchIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ModifySearchIDs(requestBody:ModifySearchIDs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ModifySearchIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ModifySearchIDs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ModifySearchIDs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreLinkGlbVendor
   Description: Linking a GlbVendor record ties a global record to a new or existing Vendor record so
that any changes made to the GlbVendor record in another company are automatically copied
to any linked Vendors.
This method performs the pre link logic to check of okay to link or get the new vendid
to create/link to.  Will be run before LinkGlbVendor which actually creates/updates a
Vendor record and will send the modified record back for update.  When the Link "button" is
originally selected, the LinkVendID will be defaulted to the GlbVendorId field.  It will then
check to see if this ID is available for Use.  If available for use the system will return a
question asking the user if they want to use this number.  If the answer is no, then the user
either needs to select an existing Vendor's ID to link to or enter a brand new ID.  You will
run this method until the user answer is yes.  Then the LinkGlbVendor method is called.
   OperationID: PreLinkGlbVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreLinkGlbVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreLinkGlbVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreLinkGlbVendor(requestBody:PreLinkGlbVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreLinkGlbVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/PreLinkGlbVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PreLinkGlbVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreLinkGlbVendorPP
   Description: Linking a GlbVendorPP record ties a global record to a new or existing Purchase Point record so
that any changes made to the GlbVendorPP record in another company are automatically copied
to any linked purchase points.
This method performs the pre link logic to check of okay to link or get the new PurPoint
to create/link to.  Will be run before LinkGlbVendorPP which actually creates/updates a
purchase point record and will send the modified record back for update.  When the Link "button" is
originally selected, the LinkPurPoint will be defaulted to the glbPurPoint field.
It will then check to see if this ID is available for use.  If available for use the system
will return a question asking the user if they want to use this number.  If the answer is no,
then the user either needs to select an existing PurPoint for the current customer to link
to or enter a brand new PurPoint for the vendor.  You will run this method until the
user's answer is yes.  Then the LinkGlbVendorPP method is called.
   OperationID: PreLinkGlbVendorPP
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreLinkGlbVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreLinkGlbVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreLinkGlbVendorPP(requestBody:PreLinkGlbVendorPP_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreLinkGlbVendorPP_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/PreLinkGlbVendorPP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PreLinkGlbVendorPP_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResetPPIntl
   Description: Purpose:
Parameters:
<param name="ds">The Vendor data set</param>
Notes:
   OperationID: ResetPPIntl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ResetPPIntl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetPPIntl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetPPIntl(requestBody:ResetPPIntl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ResetPPIntl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ResetPPIntl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ResetPPIntl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetUPSQVEnable
   Description: Purpose:
Parameters:
<param name="ipQVEnable">logical indicating if the quantum view is to enabled/disabled</param><param name="ipUpdVenUPS">Yes, if the VenUPSEmail table is to be updated</param><param name="ipUPDVenPPUPS">Yes, if the VenUPSPPEmail talbe is to be updated</param><param name="ds">The Vendor data set</param>
Notes:
   OperationID: SetUPSQVEnable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetUPSQVEnable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVEnable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetUPSQVEnable(requestBody:SetUPSQVEnable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetUPSQVEnable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/SetUPSQVEnable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetUPSQVEnable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SkipGlbVendor
   Description: This method performs the logic behind the skip option for GlbVendor
Skip - marks the VendorNum field with a -1 to move the record to the bottom of the list
if the VendorNum field is not 0 will error out
   OperationID: SkipGlbVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SkipGlbVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SkipGlbVendor(requestBody:SkipGlbVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SkipGlbVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/SkipGlbVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SkipGlbVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnlinkGlbVendor
   Description: This method performs the logic behind the unlink option for GlbVendor
Unlink - clears the VendorNum and VendorID field in GlbVendor.  Returns the Vendor DataSet
   OperationID: UnlinkGlbVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnlinkGlbVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlinkGlbVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlinkGlbVendor(requestBody:UnlinkGlbVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnlinkGlbVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/UnlinkGlbVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnlinkGlbVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePayBTFlag
   Description: Purpose:
Parameters:
<param name="ipPayBTFlag">requested pay bt flag to edit</param><param name="ipValVen"> logical indicating if the pay flag on the venMFBill is to be checked</param><param name="ipValVenPP">logical indicating if the pay flag on the venPPMFBill is to be checked</param><param name="ipVendorNum">Vendor Number</param><param name="ipPurPoint">Purchase Point</param>
Notes:
   OperationID: ValidatePayBTFlag
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePayBTFlag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePayBTFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePayBTFlag(requestBody:ValidatePayBTFlag_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePayBTFlag_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ValidatePayBTFlag", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidatePayBTFlag_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VendorBankExists
   Description: This method checks vendor bank existence.
   OperationID: VendorBankExists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VendorBankExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VendorBankExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendorBankExists(requestBody:VendorBankExists_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VendorBankExists_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorBankExists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as VendorBankExists_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBankCustNum
   Description: Check Bank Customer Number
At this time this method is specific to Switzerland localization
   OperationID: CheckBankCustNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckBankCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBankCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBankCustNum(requestBody:CheckBankCustNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckBankCustNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/CheckBankCustNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckBankCustNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBankCustNumSetup
   Description: Check Bank Customer Number Setup
At this time this method is specific to Switzerland localization
   OperationID: CheckBankCustNumSetup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckBankCustNumSetup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBankCustNumSetup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBankCustNumSetup(requestBody:CheckBankCustNumSetup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckBankCustNumSetup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/CheckBankCustNumSetup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckBankCustNumSetup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckISRPartyID
   Description: Check ISR Party ID
At this time this method is specific to Switzerland localization
   OperationID: CheckISRPartyID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckISRPartyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckISRPartyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckISRPartyID(requestBody:CheckISRPartyID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckISRPartyID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/CheckISRPartyID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckISRPartyID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPOBankAcctNum
   Description: Check Postal Account
At this time this method is specific to Switzerland localization
   OperationID: CheckPOBankAcctNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPOBankAcctNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPOBankAcctNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPOBankAcctNum(requestBody:CheckPOBankAcctNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPOBankAcctNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/CheckPOBankAcctNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckPOBankAcctNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: Retrieve Validation from Service designer
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/StorePartner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method OnChangeCode1099
   Description: Call this method when the user enters the ttVendor.Code1099ID
   OperationID: OnChangeCode1099
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCode1099_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCode1099_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCode1099(requestBody:OnChangeCode1099_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCode1099_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/OnChangeCode1099", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeCode1099_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFormType
   Description: Call this method when the user enters the ttVendor.FormTypeID
   OperationID: OnChangeFormType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFormType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFormType(requestBody:OnChangeFormType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFormType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/OnChangeFormType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeFormType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultFormType
   Description: Get Default 1099 Type.
   OperationID: GetDefaultFormType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefaultFormType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultFormType(requestBody:GetDefaultFormType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultFormType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetDefaultFormType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDefaultFormType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TypeTINVendor
   Description: Return true if vendor TIN and TINType record exists
   OperationID: TypeTINVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/TypeTINVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TypeTINVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TypeTINVendor(requestBody:TypeTINVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<TypeTINVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/TypeTINVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as TypeTINVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method getPrimaryBankID
   Description: Retrieve BankID from vendor returning true if found
   OperationID: getPrimaryBankID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/getPrimaryBankID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getPrimaryBankID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getPrimaryBankID(requestBody:getPrimaryBankID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<getPrimaryBankID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/getPrimaryBankID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as getPrimaryBankID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVendorListRemmitance
   Description: Returns a List Dataset for Remittance Advice report
   OperationID: GetVendorListRemmitance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetVendorListRemmitance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorListRemmitance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendorListRemmitance(requestBody:GetVendorListRemmitance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVendorListRemmitance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetVendorListRemmitance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetVendorListRemmitance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVendorListSorted
   Description: Returns a List Dataset for advanced sorting
   OperationID: GetVendorListSorted
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetVendorListSorted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorListSorted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendorListSorted(requestBody:GetVendorListSorted_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVendorListSorted_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetVendorListSorted", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetVendorListSorted_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateTaxID
   Description: Supplier Tax Id validation
   OperationID: ValidateTaxID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateTaxID(requestBody:ValidateTaxID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateTaxID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/ValidateTaxID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateTaxID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendor
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendor(requestBody:GetNewVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendorAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendorAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVendorAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendorAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendorAttch(requestBody:GetNewVendorAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVendorAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVendorAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVendorAttch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewEntityGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewTaxExempt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxExempt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTaxExempt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxExempt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxExempt(requestBody:GetNewTaxExempt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTaxExempt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewTaxExempt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewTaxExempt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartner
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartner(requestBody:GetNewPartner_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartner_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewPartner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPartner_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendRestriction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendRestriction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVendRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendRestriction(requestBody:GetNewVendRestriction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVendRestriction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVendRestriction", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVendRestriction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendBank
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendBank
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVendBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendBank(requestBody:GetNewVendBank_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVendBank_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVendBank", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVendBank_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendBankAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendBankAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVendBankAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendBankAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendBankAttch(requestBody:GetNewVendBankAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVendBankAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVendBankAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVendBankAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendCntMain
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendCntMain
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVendCntMain_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendCntMain_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendCntMain(requestBody:GetNewVendCntMain_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVendCntMain_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVendCntMain", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVendCntMain_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVenMFBill
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVenMFBill
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVenMFBill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVenMFBill_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVenMFBill(requestBody:GetNewVenMFBill_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVenMFBill_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVenMFBill", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVenMFBill_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendorPP
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendorPP
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendorPP(requestBody:GetNewVendorPP_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVendorPP_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVendorPP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVendorPP_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVenPPMFBill
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVenPPMFBill
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVenPPMFBill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVenPPMFBill_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVenPPMFBill(requestBody:GetNewVenPPMFBill_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVenPPMFBill_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVenPPMFBill", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVenPPMFBill_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVenPPUPSEmail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVenPPUPSEmail
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVenPPUPSEmail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVenPPUPSEmail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVenPPUPSEmail(requestBody:GetNewVenPPUPSEmail_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVenPPUPSEmail_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVenPPUPSEmail", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVenPPUPSEmail_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendPPRestriction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendPPRestriction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVendPPRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendPPRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendPPRestriction(requestBody:GetNewVendPPRestriction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVendPPRestriction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVendPPRestriction", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVendPPRestriction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendCnt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendCnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVendCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendCnt(requestBody:GetNewVendCnt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVendCnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVendCnt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVendCnt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendCntAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendCntAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVendCntAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendCntAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendCntAttch(requestBody:GetNewVendCntAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVendCntAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVendCntAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVendCntAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVenUPSEmail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVenUPSEmail
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVenUPSEmail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVenUPSEmail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVenUPSEmail(requestBody:GetNewVenUPSEmail_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVenUPSEmail_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVenUPSEmail", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVenUPSEmail_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendRemitTo
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendRemitTo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVendRemitTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendRemitTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendRemitTo(requestBody:GetNewVendRemitTo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVendRemitTo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetNewVendRemitTo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewVendRemitTo_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PEVendWhldHistRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PEVendWhldHistRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartnerRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxExemptRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxExemptRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenMFBillRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VenMFBillRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenPPMFBillRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VenPPMFBillRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenPPUPSEmailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VenPPUPSEmailRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenUPSEmailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VenUPSEmailRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendBankAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendBankRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendCntAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntMainRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendCntMainRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendCntRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPPRestrictionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendPPRestrictionRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendRemitToRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendRemitToRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendRestrictionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendRestrictionRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendorAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendorListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendorPPRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendorRow,
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

export interface Erp_Tablesets_PEVendWhldHistRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Vendor Number  */  
   "VendorNum":number,
      /**  Record Sequence  */  
   "RecordSeq":number,
      /**  Create Date  */  
   "CreateDate":string,
      /**  User Identifier  */  
   "UserID":string,
      /**  Displays the Identity DocumentType  */  
   "IdentityDocType":string,
      /**  Indicates if supplier has a Good Contributor status  */  
   "GoodContributor":boolean,
      /**  Indicates if supplier is a Withholding Agent  */  
   "WithholdingAgent":boolean,
      /**  Indicates the status of Collection Agent  */  
   "CollectionAgent":boolean,
      /**  Not Found withholding status  */  
   "NotFound":boolean,
      /**  No Address Provided withholding status  */  
   "NoAddress":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartnerRow{
      /**  Company  */  
   "Company":string,
      /**  PartnerNum  */  
   "PartnerNum":number,
      /**  PartnerType  */  
   "PartnerType":number,
      /**  SearchID  */  
   "SearchID":string,
      /**  IsActive  */  
   "IsActive":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  PartnerID  */  
   "PartnerID":string,
   "DspSearchID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxExemptRow{
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
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code  */  
   "RateCode":string,
      /**  Exemption Effective Start Date  */  
   "EffectiveFrom":string,
      /**  Exemption Effective End Date  */  
   "EffectiveTo":string,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Tax Legal Text Code  */  
   "TextCode":string,
      /**  Tax Resolution Number  */  
   "ResolutionNum":string,
      /**  Tax Resolution Date  */  
   "ResolutionDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  A unique Customer identifier.  */  
   "CustNum":number,
      /**  The PartNum field identifies the Part.  */  
   "PartNum":string,
      /**  A unique Vendor identifier.  */  
   "VendorNum":number,
   "BitFlag":number,
   "SalesTaxDescription":string,
   "SalesTRCDescription":string,
   "TaxTextDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VenMFBillRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   "PayBTFlag":string,
      /**   Describes the billing type.  Valid values and their description are:
1 - Shipper
2 - FedEx  Collect
3 - Third Party
4 - UPS Prepaid
5 - FedEx Recipient
6 - UPS Consignee
7 - UPS Freight Collect
8 - UPS Free On Board
9 - UPS Cost and Freight
10 - UPS Delivery Duty Paid
11 - UPS Shpping Duty and Tax Consignee  */  
   "PayTypeDesc":string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   "PayAccount":string,
      /**  Shipping Billing Address  */  
   "PayBTAddress1":string,
      /**  Shipping biling address line 2  */  
   "PayBTAddress2":string,
      /**  Shipping biling address line 3.  */  
   "PayBTAddress3":string,
      /**  Shipping billing city  */  
   "PayBTCity":string,
      /**  Shipping Billing state or province  */  
   "PayBTState":string,
      /**  Manifest Bililng postal code.  */  
   "PayBTZip":string,
      /**  Shipping biling country  */  
   "PayBTCountry":string,
      /**  Internal field used to store the country number.  */  
   "PayBTCountryNum":number,
      /**  Shipping billing phone number  */  
   "PayBTPhone":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PayBTCountryNumDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VenPPMFBillRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
      /**  Purchase Point  */  
   "PurPoint":string,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   "PayBTFlag":string,
      /**   Describes the billing type.  Valid values and their description are:
1 - Shipper
2 - FedEx  Collect
3 - Third Party
4 - UPS Prepaid
5 - FedEx Recipient
6 - UPS Consignee
7 - UPS Freight Collect
8 - UPS Free On Board
9 - UPS Cost and Freight
10 - UPS Delivery Duty Paid
11 - UPS Shpping Duty and Tax Consignee  */  
   "PayTypeDesc":string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   "PayAccount":string,
      /**  Shipping Billing Address  */  
   "PayBTAddress1":string,
      /**  Shipping biling address line 2  */  
   "PayBTAddress2":string,
      /**  Shipping biling address line 3.  */  
   "PayBTAddress3":string,
      /**  Shipping billing city  */  
   "PayBTCity":string,
      /**  Pay manifest billing postal code.  */  
   "PayBTZip":string,
      /**  Shipping Billing state or province  */  
   "PayBTState":string,
      /**  Shipping biling country  */  
   "PayBTCountry":string,
      /**  Internal field used to store the country number.  */  
   "PayBTCountryNum":number,
      /**  Shipping billing phone number  */  
   "PayBTPhone":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PayBTCountryNumDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VenPPUPSEmailRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Purchase Point  */  
   "PurPoint":string,
      /**  UPS Quantum View Sequence  */  
   "UPSQVSeq":number,
      /**  Email address to notify for a UPS shipment  */  
   "EmailAddress":string,
      /**  Logical indicating if the EmailAddress is to be updated at shipping.  */  
   "ShipmentNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   "FailureNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   "DeliveryNotify":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Logical indicating if the ups quantum view fields are to be enabled.  */  
   "EnableQuantumView":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VenUPSEmailRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
      /**  UPS Quantum View Sequence  */  
   "UPSQVSeq":number,
      /**  Email address to notify for a UPS shipment  */  
   "EmailAddress":string,
      /**  Logical indicating if the EmailAddress is to be updated at shipping.  */  
   "ShipmentNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   "FailureNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   "DeliveryNotify":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  logical indicating if the UPS quantum view fields are to be enabled.  */  
   "EnableQuantumView":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendBankAttchRow{
   "Company":string,
   "VendorNum":number,
   "BankID":string,
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

export interface Erp_Tablesets_VendBankRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Supplier Number  */  
   "VendorNum":number,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Supplier Bank Name  */  
   "BankName":string,
      /**  First Address Line of the Supplier Bank  */  
   "Address1":string,
      /**  Second Address Line of the Supplier Bank  */  
   "Address2":string,
      /**  Third Address Line of the Supplier Bank  */  
   "Address3":string,
      /**  City portion of the address of the Supplier Bank  */  
   "City":string,
      /**  Can be blank.  */  
   "State":string,
      /**  Postal Code or Zip code portion of the address of the Supplier Bank  */  
   "PostalCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   "BankAcctNumber":string,
      /**  Name on the Bank Account.  */  
   "NameOnAccount":string,
      /**  Swift number of the bank.  */  
   "SwiftNum":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Bank Branch Code of the Supplier Bank  */  
   "BankBranchCode":string,
      /**  IBAN Code of the Supplier Bank  */  
   "IBANCode":string,
      /**  Sweden localization field, Credit Transfer Number  */  
   "SECreditTransNum":string,
      /**  Full Legal name  */  
   "LegalName":string,
      /**  Correspondence Account of the Supplier Bank  */  
   "CorrespAccount":string,
      /**  Local BIC of the Supplier Bank  */  
   "LocalBIC":string,
      /**  Free Form Bank Person Code. Used in localizations.  */  
   "BankPersonCode":string,
      /**  Supplier bank Account Type. Used in localizations.  */  
   "VendAccountType":string,
      /**   Denmark Localization
Card (payment) code  */  
   "CardCode":string,
      /**   Denmark Localization
Account Number  */  
   "BankGiroAcctNbr":string,
      /**   Denmark Localization
Bank Reference code  */  
   "BankRefCode":string,
      /**  AllowAsAltRemitToBank  */  
   "AllowAsAltRemitToBank":boolean,
      /**  DFIIdentification  */  
   "DFIIdentification":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CHDTAID  */  
   "CHDTAID":string,
      /**  CHISRPartyID  */  
   "CHISRPartyID":string,
      /**  FeeOwnership  */  
   "FeeOwnership":string,
      /**  POBankAcctNum  */  
   "POBankAcctNum":string,
      /**  BankCustNum  */  
   "BankCustNum":string,
      /**  BankCustNumberStartPos  */  
   "BankCustNumberStartPos":number,
      /**  BankCustNumberLen  */  
   "BankCustNumberLen":number,
      /**  Specifies the supplier's bank address.  */  
   "BAddress1":string,
      /**  Specifies the supplier's bank address.  */  
   "BAddress2":string,
      /**  Specifies the supplier's bank address.  */  
   "BAddress3":string,
      /**  Bank Charges (Used for Czech Republic CSF)  */  
   "BankCharges":string,
      /**  Bank Constant Symbol (Used for Czech Republic CSF)  */  
   "BankCnstSymbol":string,
      /**  Bank Special Symbol (Used for Czech Republic CSF)  */  
   "BankSpecSymbol":string,
      /**  Bank type of electronic payment transactions  */  
   "BankType":string,
      /**  Specifies the supplier's bank city.  */  
   "BCity":string,
      /**  Specifies the supplier's bank country.  */  
   "BCountryNum":number,
      /**  Specifies the supplier's postal code.  */  
   "BPostalCode":string,
      /**  Specifies the supplier's bank state/province.  */  
   "BState":string,
      /**  Norway CSF: Determines where bank cheque is sent.  */  
   "NOChequeCode":string,
      /**  Norway CSF: Determines how the bank fee cost will be settled between the company and supplier during the fund transfers between two entities.  */  
   "NOFeeCostCode":string,
      /**  Receiver Name.  Used in Japan localizations.  */  
   "ReceiverName":string,
      /**  Receiving Bank Name.  Used in Japan localizations.  */  
   "ReceivingBankName":string,
      /**  Receiving Bank Number.  Used in Japan localizations.  */  
   "ReceivingBankNum":string,
      /**  Receiving Branch Name.  Used in Japan localizations.  */  
   "ReceivingBranchName":string,
      /**  Receiving Branch Number.  Used in Japan localizations.  */  
   "ReceivingBranchNum":string,
      /**  SEBankFeeCostOwner  */  
   "SEBankFeeCostOwner":string,
      /**  PEDetractionsNBA  */  
   "PEDetractionsNBA":boolean,
      /**  MX SAT Code  */  
   "MXSATCode":string,
      /**  MX SAT Name Short  */  
   "MXSATNameShort":string,
      /**  MX SAT Name Full  */  
   "MXSATNameFull":string,
      /**  DKCreditorNum  */  
   "DKCreditorNum":string,
      /**  A supplier alias used to make and receive payments.  */  
   "PayID":string,
      /**  ClearSystemIDCode  */  
   "ClearSystemIDCode":string,
      /**  MemberID  */  
   "MemberID":string,
   "BCountry":number,
      /**  Postal Account Number in format XX-#####V-P (CSF Switzerland)  */  
   "CHScrPOBankAcctNum":string,
   "PrimaryBank":boolean,
      /**  ISR Party Number in format XX-#####V-P (CSF Switzerland)  */  
   "CHScrISRPartyID":string,
   "BitFlag":number,
   "BankBranchCodeDescDescription":string,
   "BankBranchCodeDescBankBranchCode":string,
   "BCountryNumDescription":string,
   "CountryNumDescription":string,
   "PayMethodType":number,
   "PayMethodSummarizePerCustomer":boolean,
   "PayMethodName":string,
   "VendorNumCity":string,
   "VendorNumState":string,
   "VendorNumVendorID":string,
   "VendorNumAddress1":string,
   "VendorNumName":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCountry":string,
   "VendorNumAddress2":string,
   "VendorNumAddress3":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendCntAttchRow{
   "Company":string,
   "VendorNum":number,
   "PurPoint":string,
   "ConNum":number,
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

export interface Erp_Tablesets_VendCntMainRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  This key links the record to the Vendor file.  */  
   "VendorNum":number,
      /**  Purchase point from Vendor.  */  
   "PurPoint":string,
      /**  Contact number.  Unique identifier for the contact record.  */  
   "ConNum":number,
      /**  Contact name.  */  
   "Name":string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   "Func":string,
      /**  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  */  
   "FaxNum":string,
      /**  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  */  
   "PhoneNum":string,
      /**  Contact email address.  */  
   "EmailAddress":string,
      /**  Password for SF/Portal, should not be easily editable from the Manufacturing System.  */  
   "WebPassword":string,
      /**  Indicates if able to access the Supplier Workbench  */  
   "WebUser":boolean,
      /**  Code that identifies the role of this person. Link to the RoleCD table.  */  
   "RoleCode":string,
      /**  The contacts Cell phone number.  */  
   "CellPhoneNum":string,
      /**  The contacts Pager number.  */  
   "PagerNum":string,
      /**  The contacts Home number.  */  
   "HomeNum":string,
      /**  The contacts Alternate number.  */  
   "AltNum":string,
      /**  The Contacts Title  */  
   "ContactTitle":string,
      /**  The name if the person this contact reports to.  */  
   "ReportsTo":string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   "Comment":string,
      /**  Indicates that this contact is no longer contacted.  */  
   "NoContact":boolean,
      /**  The date the task was created.  */  
   "CreateDate":string,
      /**  The UserID that created the task  */  
   "CreateDcdUserID":string,
      /**  The date the task was last changed.  */  
   "ChangeDate":string,
      /**  The UserID that last changed the task  */  
   "ChangeDcdUserID":string,
      /**  This contact does not get used on new LOQs  */  
   "Inactive":boolean,
      /**  First Name  */  
   "FirstName":string,
      /**  Middle Name  */  
   "MiddleName":string,
      /**  Last Name  */  
   "LastName":string,
      /**  Prefix  */  
   "Prefix":string,
      /**  Suffix  */  
   "Suffix":string,
      /**  Initials  */  
   "Initials":string,
      /**  Unique identifier from an external G/L interface  */  
   "ExternalId":string,
      /**  Disable this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   "SyncEmailToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  */  
   "SyncLinksToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   "SyncNameToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   "SyncPhoneToPerCon":boolean,
      /**  Contact's website.  */  
   "WebSite":string,
      /**  Contact's IM.  */  
   "IM":string,
      /**  Contact's Twitter.  */  
   "Twitter":string,
      /**  Contact's LinkedIn.  */  
   "LinkedIn":string,
      /**  Contact's FaceBook.  */  
   "FaceBook":string,
      /**  User defined Link 1.  */  
   "WebLink1":string,
      /**  User defined Link 2.  */  
   "WebLink2":string,
      /**  User defined Link 3.  */  
   "WebLink3":string,
      /**  User defined Link 4.  */  
   "WebLink4":string,
      /**  User defined Link 5.  */  
   "WebLink5":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "GlbFlag":boolean,
   "PrimaryContact":boolean,
   "VendCntAttrStrng":string,
      /**  GlbVendCnt fields in a linked list to find the linking record  */  
   "GlbLink":string,
   "PerConName":string,
   "BitFlag":number,
   "RoleCodeRoleDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendCntRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  This key links the record to the Vendor file.  */  
   "VendorNum":number,
      /**  Purchase point from Vendor.  */  
   "PurPoint":string,
      /**  Contact number.  Unique identifier for the contact record.  */  
   "ConNum":number,
      /**  Contact name.  */  
   "Name":string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   "Func":string,
      /**  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  */  
   "FaxNum":string,
      /**  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  */  
   "PhoneNum":string,
      /**  Contact email address.  */  
   "EmailAddress":string,
      /**  Password for SF/Portal, should not be easily editable from the Manufacturing System.  */  
   "WebPassword":string,
      /**  Indicates if able to access the Supplier Workbench  */  
   "WebUser":boolean,
      /**  Code that identifies the role of this person. Link to the RoleCD table.  */  
   "RoleCode":string,
      /**  The contacts Cell phone number.  */  
   "CellPhoneNum":string,
      /**  The contacts Pager number.  */  
   "PagerNum":string,
      /**  The contacts Home number.  */  
   "HomeNum":string,
      /**  The contacts Alternate number.  */  
   "AltNum":string,
      /**  The Contacts Title  */  
   "ContactTitle":string,
      /**  The name if the person this contact reports to.  */  
   "ReportsTo":string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   "Comment":string,
      /**  Indicates that this contact is no longer contacted.  */  
   "NoContact":boolean,
      /**  The date the task was created.  */  
   "CreateDate":string,
      /**  The UserID that created the task  */  
   "CreateDcdUserID":string,
      /**  The date the task was last changed.  */  
   "ChangeDate":string,
      /**  The UserID that last changed the task  */  
   "ChangeDcdUserID":string,
      /**  This contact does not get used on new LOQs  */  
   "Inactive":boolean,
      /**  First Name  */  
   "FirstName":string,
      /**  Middle Name  */  
   "MiddleName":string,
      /**  Last Name  */  
   "LastName":string,
      /**  Prefix  */  
   "Prefix":string,
      /**  Suffix  */  
   "Suffix":string,
      /**  Initials  */  
   "Initials":string,
      /**  Unique identifier from an external G/L interface  */  
   "ExternalId":string,
      /**  Disable this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   "SyncEmailToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  */  
   "SyncLinksToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   "SyncNameToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   "SyncPhoneToPerCon":boolean,
      /**  Contact's website.  */  
   "WebSite":string,
      /**  Contact's IM.  */  
   "IM":string,
      /**  Contact's Twitter.  */  
   "Twitter":string,
      /**  Contact's LinkedIn.  */  
   "LinkedIn":string,
      /**  Contact's FaceBook.  */  
   "FaceBook":string,
      /**  User defined Link 1.  */  
   "WebLink1":string,
      /**  User defined Link 2.  */  
   "WebLink2":string,
      /**  User defined Link 3.  */  
   "WebLink3":string,
      /**  User defined Link 4.  */  
   "WebLink4":string,
      /**  User defined Link 5.  */  
   "WebLink5":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "PrimaryContact":boolean,
   "GlbFlag":boolean,
   "VendCntAttrStrng":string,
      /**  GlbVendCnt fields in a linked list to find the linking record  */  
   "GlbLink":string,
      /**  The name of the person contact.  */  
   "PerConName":string,
   "BitFlag":number,
   "PurPointZip":string,
   "PurPointAddress2":string,
   "PurPointState":string,
   "PurPointName":string,
   "PurPointPrimPCon":number,
   "PurPointCity":string,
   "PurPointAddress1":string,
   "PurPointCountry":string,
   "PurPointAddress3":string,
   "RoleCodeRoleDescription":string,
   "VendorNumDefaultFOB":string,
   "VendorNumState":string,
   "VendorNumAddress2":string,
   "VendorNumAddress1":string,
   "VendorNumVendorID":string,
   "VendorNumAddress3":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCountry":string,
   "VendorNumZIP":string,
   "VendorNumName":string,
   "VendorNumCity":string,
   "VendorNumTermsCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendPPRestrictionRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
      /**  Purchase Point  */  
   "PurPoint":string,
      /**  Restriction Type identification.  */  
   "RestrictionTypeID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PurPointName":string,
   "PurPointState":string,
   "PurPointAddress3":string,
   "PurPointAddress1":string,
   "PurPointZip":string,
   "PurPointCity":string,
   "PurPointAddress2":string,
   "PurPointPrimPCon":number,
   "PurPointCountry":string,
   "RestrictionTypeDescription":string,
   "VendorNumCountry":string,
   "VendorNumTermsCode":string,
   "VendorNumCurrencyCode":string,
   "VendorNumZIP":string,
   "VendorNumVendorID":string,
   "VendorNumAddress2":string,
   "VendorNumAddress1":string,
   "VendorNumAddress3":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCity":string,
   "VendorNumName":string,
   "VendorNumState":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendRemitToRow{
      /**  Company  */  
   "Company":string,
      /**  VendorNum  */  
   "VendorNum":number,
      /**  RemitToSeq  */  
   "RemitToSeq":number,
      /**  RemitToType  */  
   "RemitToType":string,
      /**  RemitCustNum  */  
   "RemitCustNum":number,
      /**  RemitEmpID  */  
   "RemitEmpID":string,
      /**  RemitVendorNum  */  
   "RemitVendorNum":number,
      /**  RemitToName  */  
   "RemitToName":string,
      /**  DefaultRemitTo  */  
   "DefaultRemitTo":boolean,
      /**  Inactive  */  
   "Inactive":boolean,
      /**  OneCheck  */  
   "OneCheck":boolean,
      /**  Comments  */  
   "Comments":string,
      /**  RemitToAddress1  */  
   "RemitToAddress1":string,
      /**  RemitToAddress2  */  
   "RemitToAddress2":string,
      /**  RemitToAddress3  */  
   "RemitToAddress3":string,
      /**  RemitToCity  */  
   "RemitToCity":string,
      /**  RemitToState  */  
   "RemitToState":string,
      /**  RemitToZip  */  
   "RemitToZip":string,
      /**  RemitToCountry  */  
   "RemitToCountry":number,
      /**  RemitToPhoneNum  */  
   "RemitToPhoneNum":string,
      /**  RemitToFaxNum  */  
   "RemitToFaxNum":string,
      /**  RemitToEmail  */  
   "RemitToEmail":string,
      /**  TermsCode  */  
   "TermsCode":string,
      /**  CurrencyCode  */  
   "CurrencyCode":string,
      /**  PMUID  */  
   "PMUID":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  This can either be a CustID, EmpID, or VendID depending on the RemitToType  */  
   "RemitToID":string,
   "BitFlag":number,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrencyID":string,
   "TermsCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendRestrictionRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
      /**  Restriction Type identification.  */  
   "RestrictionTypeID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "RestrictionTypeDescription":string,
   "VendorNumVendorID":string,
   "VendorNumCurrencyCode":string,
   "VendorNumZIP":string,
   "VendorNumCity":string,
   "VendorNumAddress2":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress3":string,
   "VendorNumCountry":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress1":string,
   "VendorNumName":string,
   "VendorNumState":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendorAttchRow{
   "Company":string,
   "VendorNum":number,
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

export interface Erp_Tablesets_VendorListRow{
      /**  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  */  
   "Inactive":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the system, for linking other records to the Vendor.  */  
   "VendorID":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "Name":string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
      /**  First address line of the Supplier  */  
   "Address1":string,
      /**  Second address line of the Supplier  */  
   "Address2":string,
      /**  Third address line of the Supplier  */  
   "Address3":string,
      /**  City portion of the address of the Supplier  */  
   "City":string,
      /**  Can be blank.  */  
   "State":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "ZIP":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "Country":string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   "TaxPayerID":string,
      /**  Currency Code Description  */  
   "CurrDesc":string,
      /**  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  */  
   "GroupCode":string,
      /**  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  */  
   "PhoneNum":string,
      /**  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  */  
   "PayHold":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Taxpayer Identification Number  */  
   "TIN":string,
      /**  INTaxRegistrationID  */  
   "INTaxRegistrationID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendorPPRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Purchase Point  */  
   "PurPoint":string,
      /**  Purchase Point Name...can't be blank.  */  
   "Name":string,
      /**  First address line  */  
   "Address1":string,
      /**  Second address line  */  
   "Address2":string,
      /**  Third address line  */  
   "Address3":string,
      /**  City portion of the address  */  
   "City":string,
      /**  State portion of the address  */  
   "State":string,
      /**  Postal Code or Zip code portion of the address  */  
   "Zip":string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   "Country":string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   "PrimPCon":number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   "LangNameID":string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   "BorderCrossing":string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   "FormatStr":string,
      /**  Email address of the vendor purchase point.  */  
   "EMailAddress":string,
      /**  Unique Identifier from an external G/L interface  */  
   "ExternalId":string,
      /**  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   "TaxAuthorityCode":string,
      /**  Disable this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   "EDICode":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Override Carrier Defaults.  If not checked then the vendor values will be used if overriden else the Site values  */  
   "OverrideCarrier":boolean,
      /**  Override Service Options.  If not checked then the vendor values will be used if overriden else the Site values  */  
   "OverrideService":boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Indicates if the shipment is international.  */  
   "IntrntlShip":boolean,
      /**  Certificate of Origin flag  */  
   "CertOfOrigin":boolean,
      /**  Commercial Invoice flag.  */  
   "CommercialInvoice":boolean,
      /**  Ship Export Declaration flag  */  
   "ShipExprtDeclartn":boolean,
      /**  Letter of Instruction flag  */  
   "LetterOfInstr":boolean,
      /**  Freight Forwarder ID  */  
   "FFID":string,
      /**  Freight Forwarder Company Name  */  
   "FFCompName":string,
      /**  Freight Forwarder contact person  */  
   "FFContact":string,
      /**  First address line of the Freight Forwarder  */  
   "FFAddress1":string,
      /**  Second address line of the Freight Forwarder  */  
   "FFAddress2":string,
      /**  Third address line of the Freight Forwarder  */  
   "FFAddress3":string,
      /**  Freight Forwarder city portion of address.  */  
   "FFCity":string,
      /**  Freight Forwarder state portion of address.  */  
   "FFState":string,
      /**  Freight Forwarder Zip code portion of the address  */  
   "FFZip":string,
      /**  Freight Forwarder Country portion of the address  */  
   "FFCountry":string,
      /**  Non Standard Packaging  */  
   "NonStdPkg":boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling flag  */  
   "AddlHdlgFlag":boolean,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View Ship from Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Freight Forwarder Phone Number  */  
   "FFPhoneNum":string,
      /**  Freight Forwarder Country Number  */  
   "FFCountryNum":number,
      /**  Legal Name  */  
   "LegalName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  INExciseRegNumber  */  
   "INExciseRegNumber":string,
      /**  INExciseDivision  */  
   "INExciseDivision":string,
      /**  INExciseRange  */  
   "INExciseRange":string,
      /**  INCommissionarate  */  
   "INCommissionarate":string,
      /**  INVATNumber  */  
   "INVATNumber":string,
      /**  INServiceTaxRegNum  */  
   "INServiceTaxRegNum":string,
      /**  INTaxRegionCode  */  
   "INTaxRegionCode":string,
      /**  Organization Registration Code  */  
   "OrgRegCode":string,
      /**  INTaxRegistrationID  */  
   "INTaxRegistrationID":string,
      /**  Municipio Code  */  
   "MXMunicipio":string,
   "GroupCode":string,
   "IntegrationFlag":boolean,
   "PhoneNum":string,
   "PrimaryPP":boolean,
   "VendAttrString":string,
      /**  Indicates if ShipTo is a global record  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany, GlbVendorNum and GlbPurPoint that is linking to this purchase point  */  
   "GlbLink":string,
      /**  Sales Tax ID  */  
   "SalesTaxID":string,
      /**  Service Tax ID  */  
   "ServiceTaxID":string,
   "LangNameIDDescription":string,
      /**  Area of ISTMO de Tehuantepec (Polos de Desarrollo). Value is from MXLocISTMO User Code.  */  
   "MXISTMO":string,
   "BitFlag":number,
   "CountryNumDescription":string,
   "DeliveryTypeDescription":string,
   "INTaxRegionCodeDescription":string,
   "TACodeTaxAuthorityDescription":string,
   "VendorNumState":string,
   "VendorNumAddress3":string,
   "VendorNumAddress2":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress1":string,
   "VendorNumCity":string,
   "VendorNumVendorID":string,
   "VendorNumZIP":string,
   "VendorNumCountry":string,
   "VendorNumTermsCode":string,
   "VendorNumName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendorRow{
      /**  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  */  
   "Inactive":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the system, for linking other records to the Vendor.  */  
   "VendorID":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "Name":string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
      /**  First address line of the Supplier  */  
   "Address1":string,
      /**  Second address line of the Supplier  */  
   "Address2":string,
      /**  Third address line of the Supplier  */  
   "Address3":string,
      /**  City portion of the address of the Supplier  */  
   "City":string,
      /**  Can be blank.  */  
   "State":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "ZIP":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "Country":string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   "TaxPayerID":string,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   "PurPoint":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "TermsCode":string,
      /**  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  */  
   "GroupCode":string,
      /**  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  */  
   "Print1099":boolean,
      /**  Indicates that for this vendor all invoices must be paid on separate checks.  */  
   "OneCheck":boolean,
      /**  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  */  
   "PrintLabels":boolean,
      /**  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  */  
   "FaxNum":string,
      /**  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  */  
   "PhoneNum":string,
      /**   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   "Comment":string,
      /**  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  */  
   "PayHold":boolean,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  */  
   "PrimPCon":number,
      /**  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  */  
   "AccountRef":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "DefaultFOB":string,
      /**  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Tax Liability of the Supplier  */  
   "TaxRegionCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   "LangNameID":string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   "BorderCrossing":string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   "FormatStr":string,
      /**  Payments to this vendors are made via electronic transfer.  */  
   "ElecPayment":boolean,
      /**  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  */  
   "PrimaryBankID":string,
      /**   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  */  
   "Approved":boolean,
      /**  This is an inter-company vendor.  */  
   "ICVend":boolean,
      /**  Email address of the vendor.  */  
   "EMailAddress":string,
      /**  This vendor is web enabled  */  
   "WebVendor":boolean,
      /**  Vendor URL.  */  
   "VendURL":string,
      /**  Used to calculate on-time delivery performance rating  */  
   "EarlyBuffer":number,
      /**  Used to calculate on-time delivery performance rating  */  
   "LateBuffer":number,
      /**  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   "OnTimeRating":string,
      /**  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  */  
   "QualityRating":string,
      /**  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   "PriceRating":string,
      /**  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   "ServiceRating":string,
      /**  Unique identifier from an external G/L interface  */  
   "ExternalId":string,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   "VendPILimit":number,
      /**  Marks the vendor as a global vendor, available to be sent out to other companies  */  
   "GlobalVendor":boolean,
      /**  Indicates if this vendor participates in the Inter-Company Trading.  */  
   "ICTrader":boolean,
      /**  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   "TaxAuthorityCode":string,
      /**  Disable this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  MinOrderValue  */  
   "MinOrderValue":number,
      /**  Identifies the production calendar for this Vendor.   If this equals "", then the ProdCal record is the Company Level production calendar.  */  
   "CalendarID":string,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   "EDICode":string,
      /**  Should this Supplier be included in Consolidated Purchasing?  */  
   "ConsolidatedPurchasing":boolean,
      /**  If the Part Class being purchased is included in Consolidated Purchasing, should purchasing it from this Supplier override that so it will be purchased in this company?  */  
   "LocalPurchasing":boolean,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Flag to indicate if the Vendor participates in the Centralized Payment process.  */  
   "CPay":boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Indicates if the shipment is international.  */  
   "IntrntlShip":boolean,
      /**  Certificate of Origin flag  */  
   "CertOfOrigin":boolean,
      /**  Commercial Invoice flag.  */  
   "CommercialInvoice":boolean,
      /**  Ship Export Declaration flag  */  
   "ShipExprtDeclartn":boolean,
      /**  Letter of Instruction flag  */  
   "LetterOfInstr":boolean,
      /**  Freight Forwarder ID  */  
   "FFID":string,
      /**  Freight Forwarder Company Name  */  
   "FFCompName":string,
      /**  Freight Forwarder contact person  */  
   "FFContact":string,
      /**  First address line of the Freight Forwarder  */  
   "FFAddress1":string,
      /**  Second address line of the Freight Forwarder  */  
   "FFAddress2":string,
      /**  Third address line of the Freight Forwarder  */  
   "FFAddress3":string,
      /**  Freight Forwarder city portion of address.  */  
   "FFCity":string,
      /**  Freight Forwarder state portion of address.  */  
   "FFState":string,
      /**  Freight Forwarder Zip code portion of the address  */  
   "FFZip":string,
      /**  Freight Forwarder Country portion of the address  */  
   "FFCountry":string,
      /**  Non Standard Packaging  */  
   "NonStdPkg":boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling flag  */  
   "AddlHdlgFlag":boolean,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View Ship from Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Freight Forwarder Phone Number  */  
   "FFPhoneNum":string,
      /**  Freight Forwarder Country Number  */  
   "FFCountryNum":number,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this Supplier.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AP invoice line for this Supplier.  */  
   "RevChargeMethod":string,
      /**  Flag indicating whether this vendor is associated with a 3PL customer.  */  
   "ManagedCust":boolean,
      /**  CustID of the associated managed customer.  Only populated if ManagedCust flag = true.  */  
   "ManagedCustID":string,
      /**  CustNum associated with CustID of managed customer.  Only populated if ManagedCust flag = true.  */  
   "ManagedCustNum":number,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  If yes, indicates that Vendor has at least one assoicated VendBank record.  */  
   "HasBank":boolean,
      /**  The Payment Banking Reference assigned by the supplier  */  
   "PmtAcctRef":string,
      /**  Full Legal Name  */  
   "LegalName":string,
      /**  Tax Payer Registration Reason Code  */  
   "TaxRegReason":string,
      /**  Organization Registration Code  */  
   "OrgRegCode":string,
      /**   Indicates Advanced Tax invoice is expected from supplier
after prepayment is done. If this field is set to yes, prepayment
invoice is not crated automatically.  */  
   "AdvTaxInv":boolean,
      /**  AllowAsAltRemitTo  */  
   "AllowAsAltRemitTo":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  THBranchID  */  
   "THBranchID":string,
      /**  ParamCode  */  
   "ParamCode":string,
      /**  AGAFIPResponsibilityCode  */  
   "AGAFIPResponsibilityCode":string,
      /**  AGGrossIncomeTaxID  */  
   "AGGrossIncomeTaxID":string,
      /**  AGIDDocumentTypeCode  */  
   "AGIDDocumentTypeCode":string,
      /**  AGProvinceCode  */  
   "AGProvinceCode":string,
      /**  AGUseGoodDefaultMark  */  
   "AGUseGoodDefaultMark":boolean,
      /**  AGApartment  */  
   "AGApartment":string,
      /**  AGExtraStreetNumber  */  
   "AGExtraStreetNumber":string,
      /**  AGFloor  */  
   "AGFloor":string,
      /**  AGLocationCode  */  
   "AGLocationCode":string,
      /**  AGNeighborhood  */  
   "AGNeighborhood":string,
      /**  AGStreet  */  
   "AGStreet":string,
      /**  AGStreetNumber  */  
   "AGStreetNumber":string,
      /**  Colombia Loc Field. OneTimeCustVend new table ID  */  
   "COOneTimeID":string,
      /**  No Banking Reference  */  
   "NoBankingReference":boolean,
      /**  Peru Goods Contributor withholding status.  */  
   "PEGoodsContributor":boolean,
      /**  Indicates the status of Peru Withholding Agent  */  
   "PEWithholdAgent":boolean,
      /**  Indicates the status of Peru Collection Agent  */  
   "PECollectionAgent":boolean,
      /**  Peru Not Found withholding status.  */  
   "PENotFound":boolean,
      /**  Peru No Address Provided withholding status.  */  
   "PENoAddress":boolean,
      /**  Displays the Peru Identity Document Type.  */  
   "PEIdentityDocType":string,
      /**  Colombia Loc Field.  */  
   "COIsOneTimeVend":boolean,
      /**  Peru Document ID.  */  
   "PEDocumentID":string,
      /**  Defines the Number of Days from the PO release date the schedule engine considers a late PO Release or discard it. If the PO release date plus the supplier due date horizon is before today then the PO Release is discarded. If the PO release date plus the supplier due date horizon is today or later then the PO Release is considered late.  */  
   "MaxLateDaysPORel":number,
      /**  1099 Code  */  
   "Code1099ID":string,
      /**  Taxpayer Identification Number  */  
   "TIN":string,
      /**  TIN Type. Values are 1 for EIN, 2 for SSNs, ITINs, and ATINs and 0 if type of TIN is not terminable.  */  
   "TINType":string,
      /**  Second TIN Notice  */  
   "SecondTINNotice":boolean,
      /**  Name Control. Optional and used for electronic export.  */  
   "NameControl":string,
      /**  Specifies the method of shipment. The Ship Via associated with this supplier appears by default, but you can select a different option from the list.  */  
   "ShipViaCode":string,
      /**  Non US Supplier  */  
   "NonUS":boolean,
      /**  Form Type ID for the 1099 Code  */  
   "FormTypeID":string,
      /**  INSupplierType  */  
   "INSupplierType":string,
      /**  INCSTNumber  */  
   "INCSTNumber":string,
      /**  INPANNumber  */  
   "INPANNumber":string,
      /**  DEOrgType  */  
   "DEOrgType":string,
      /**  PaymentReporting  */  
   "PaymentReporting":boolean,
      /**  This field indicates that this record should be sent over to an external system whenever it is changed/created/deleted, etc.  */  
   "ExternalPurchasing":boolean,
      /**  MXRetentionCode  */  
   "MXRetentionCode":string,
      /**  Recipient's name for US 1099 reporting  */  
   "Reporting1099Name":string,
      /**  Reporting1099Name2  */  
   "Reporting1099Name2":string,
      /**  FATCA  */  
   "FATCA":boolean,
      /**  AccountNum  */  
   "AccountNum":string,
      /**  TW GUI Code  */  
   "TWGUIRegNum":string,
      /**  MXTARCode  */  
   "MXTARCode":string,
      /**  PEAddressID  */  
   "PEAddressID":string,
      /**  PERetentionRegime  */  
   "PERetentionRegime":string,
      /**  TaxEntityType  */  
   "TaxEntityType":string,
      /**  GST Compliance Rate for India  */  
   "INGSTComplianceRate":number,
      /**  INTaxRegistrationID  */  
   "INTaxRegistrationID":string,
      /**  Validation Status of Taxpayer Identification Number  */  
   "TINValidationStatus":number,
      /**  Indicates whether this supplier is importer of records or not. Used for Avalara Tax Connect calculation.  */  
   "ImporterOfRecord":boolean,
      /**  PLAutomaticAPInvoiceNum  */  
   "PLAutomaticAPInvoiceNum":boolean,
      /**  Standard Entry Class Code  */  
   "SEC":string,
      /**  CSF Mexico DIOT Transaction Type  */  
   "MXDIOTTranType":string,
      /**  Form 1099-K Merchant Category Code  */  
   "US1099KMerchCatCode":string,
      /**  CSF Mexico Taxpayer Type  */  
   "MXTaxpayerType":string,
      /**  CSF Mexico Legal Representative RFC  */  
   "MXLegalRepRFC":string,
      /**  CSF Mexico Legal Representative CURP  */  
   "MXLegalRepCURP":string,
      /**  CSF Mexico Legal Representative Name  */  
   "MXLegalRepName":string,
      /**  CSF Mexico Legal Representative Taxpayer Type  */  
   "MXLegalRepTaxpayerType":string,
      /**  US 1099 State  */  
   "US1099State":string,
      /**  Tax ID Validation Status: Not Validated – 0, Valid – 1, Invalid – 2.  */  
   "TaxValidationStatus":number,
      /**  Tax Validation Date  */  
   "TaxValidationDate":string,
      /**  HMRCTaxValidationLog  */  
   "HMRCTaxValidationLog":string,
      /**  Supplier Scheme ID  */  
   "ExternalSchemeID":string,
      /**  Municipio Code  */  
   "MXMunicipio":string,
      /**  EInvoice  */  
   "EInvoice":boolean,
      /**  Flag used to mark a Supplier as EDI.  */  
   "EDISupplier":boolean,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
      /**  Delimited list of Business Categories  */  
   "BusinessCatList":string,
      /**  List of fields which are referenced by COA segments.  */  
   "COASegReferences":string,
   "CountryDescription":string,
      /**  Currency Description.  */  
   "CurrDesc":string,
   "DocumentMaskID":string,
   "EnableGlobalLock":boolean,
   "EnableGlobalVendor":boolean,
   "EnableMultiCompany":boolean,
      /**  Indicates if Reverse Charge Method should be enabled.  */  
   "EnableRevCharge":boolean,
   "FOBDescription":string,
      /**  Indicates if the Vendor is a global vendor (either master or child)  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany and GlbVendorNum that is linking to this vendor  */  
   "GlbLink":string,
   "Integrationflag":boolean,
      /**  A user defined external Netting Customer ID.  This must be existing Customer ID within the file  */  
   "NettingCustID":string,
      /**  A user defined external Netting Customer Number.  This must be existing Customer Number within the file  */  
   "NettingCustNum":number,
      /**  Reverse Charge Method description  */  
   "RevChargeMethodDesc":string,
      /**  Sales Tax ID  */  
   "SalesTaxID":string,
      /**  Automated Bank reconciliation.  */  
   "SearchIDs":string,
      /**  Service Tax ID  */  
   "ServiceTaxID":string,
   "ShipViaDescription":string,
      /**  Delimited string of vendor attributes  */  
   "VendAttrString":string,
   "LangNameIDDescription":string,
      /**  Area of ISTMO de Tehuantepec (Polos de Desarrollo). Value is from MXLocISTMO User Code.  */  
   "MXISTMO":string,
   "BitFlag":number,
   "AGAFIPResponsibilityDescription":string,
   "AGIDDocTypeDescription":string,
   "AGLocationDescription":string,
   "AGProvinceCodeDescription":string,
   "CalendarIDDescription":string,
   "Code1099Description":string,
   "CountryNumEUMember":boolean,
   "CountryNumISOCode":string,
   "CountryNumDescription":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrDesc":string,
   "DeliveryTypeDescription":string,
   "FormTypeDescription":string,
   "GroupCodeGroupDesc":string,
   "PayMethodType":number,
   "PayMethodName":string,
   "PayMethodSummarizePerCustomer":boolean,
   "PurPointAddress3":string,
   "PurPointAddress1":string,
   "PurPointPrimPCon":number,
   "PurPointName":string,
   "PurPointZip":string,
   "PurPointCountry":string,
   "PurPointCity":string,
   "PurPointState":string,
   "PurPointAddress2":string,
   "TaxAuthCdTaxAuthorityDescription":string,
   "TaxRegionCodeDescription":string,
   "TermsCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "Week1Pymt_c":number,
   "Week2Pymt_c":number,
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
      @param proposedBankBranchCode
      @param ds
   */  
export interface ChangeBankBranchCode_input{
      /**  The proposed Bank Branch code  */  
   proposedBankBranchCode:string,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeBankBranchCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ic_CalendarID
      @param ds
   */  
export interface ChangeCalendar_input{
      /**  Calendar Code  */  
   ic_CalendarID:string,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeCalendar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param proposedRemitToID
      @param ds
   */  
export interface ChangeRemitToID_input{
      /**  The proposed RemitTo ID  */  
   proposedRemitToID:string,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeRemitToID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param proposedRemitToType
      @param ds
   */  
export interface ChangeRemitToType_input{
      /**  The proposed RemitTo type  */  
   proposedRemitToType:string,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeRemitToType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param iProposedTaxRgnCode
      @param ds
   */  
export interface ChangeTaxRegion_input{
      /**  The proposed TaxCode value  */  
   iProposedTaxRgnCode:string,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeTaxRegion_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param i_CountryNum
      @param ds
   */  
export interface ChangeVenMFBillCountry_input{
      /**  Country Number  */  
   i_CountryNum:number,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVenMFBillCountry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param i_CountryNum
      @param ds
   */  
export interface ChangeVenPPMFBillCountry_input{
      /**  Country Number  */  
   i_CountryNum:number,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVenPPMFBillCountry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param i_CountryNum
      @param ds
   */  
export interface ChangeVendBankBCountry_input{
      /**  Country Number  */  
   i_CountryNum:number,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVendBankBCountry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param i_CountryNum
      @param ds
   */  
export interface ChangeVendBankCountry_input{
      /**  Country Number  */  
   i_CountryNum:number,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVendBankCountry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param i_PayMethodNum
      @param ds
   */  
export interface ChangeVendBankPayMethod_input{
      /**  Payment Method Number  */  
   i_PayMethodNum:number,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVendBankPayMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param i_CountryNum
      @param ds
   */  
export interface ChangeVendCountry_input{
      /**  Country Number  */  
   i_CountryNum:number,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVendCountry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param i_CountryNum
      @param ds
   */  
export interface ChangeVendFFCountry_input{
      /**  FFCountry Number  */  
   i_CountryNum:number,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVendFFCountry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param proposedGlobalVendor
      @param ds
   */  
export interface ChangeVendGlobalVendor_input{
      /**  The proposed global vendor value  */  
   proposedGlobalVendor:boolean,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVendGlobalVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param proposedICTrader
      @param ds
   */  
export interface ChangeVendICTrader_input{
      /**  The proposed ICTrader value  */  
   proposedICTrader:boolean,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVendICTrader_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param i_CountryNum
      @param ds
   */  
export interface ChangeVendPPCountry_input{
      /**  Country Number  */  
   i_CountryNum:number,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVendPPCountry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param i_CountryNum
      @param ds
   */  
export interface ChangeVendPPFFCountry_input{
      /**  Country Number  */  
   i_CountryNum:number,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVendPPFFCountry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param i_PayMethodNum
      @param ds
   */  
export interface ChangeVendPayMethod_input{
      /**  Payment Method Number  */  
   i_PayMethodNum:number,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVendPayMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param i_CountryNum
      @param ds
   */  
export interface ChangeVendRemitToCountry_input{
      /**  Country Number  */  
   i_CountryNum:number,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ChangeVendRemitToCountry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckBankCustNumSetup_input{
   ds:Erp_Tablesets_VendorTableset[],
}

export interface CheckBankCustNumSetup_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   OpMessage:string,
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ipBankCustNum
   */  
export interface CheckBankCustNum_input{
      /**  New value of Bank Customer Number.  */  
   ipBankCustNum:string,
}

export interface CheckBankCustNum_output{
}

   /** Required : 
      @param ipISRPartyID
      @param ds
   */  
export interface CheckISRPartyID_input{
      /**  New value of ISR Party ID.  */  
   ipISRPartyID:string,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface CheckISRPartyID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ipPOBankAcctNum
      @param ds
   */  
export interface CheckPOBankAcctNum_input{
      /**  New value of Postal Account.  */  
   ipPOBankAcctNum:string,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface CheckPOBankAcctNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckRUC_input{
   ds:Erp_Tablesets_VendorTableset[],
}

export interface CheckRUC_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckVATFormat_input{
   ds:Erp_Tablesets_VendorTableset[],
}

export interface CheckVATFormat_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CompareCountryTaxLiabality_input{
   ds:Erp_Tablesets_VendorTableset[],
}

export interface CompareCountryTaxLiabality_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   countryTaxRegionCode:string,
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param targetField
      @param ds
   */  
export interface DefaultName_input{
      /**  Indicates which fields to populate either "Detail" or "Name"  */  
   targetField:string,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface DefaultName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param vendorNum
   */  
export interface DeleteByID_input{
   vendorNum:number,
}

export interface DeleteByID_output{
}

export interface EnablePriceList_output{
parameters : {
      /**  output parameters  */  
   lEnablePriceList:boolean,
}
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

export interface Erp_Tablesets_GlbVendCntRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  This key links the record to the Vendor file.  */  
   VendorNum:number,
      /**  Purchase point from Vendor.  */  
   PurPoint:string,
      /**  Contact number.  Unique identifier for the contact record.  */  
   ConNum:number,
      /**  Contact name.  */  
   Name:string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   Func:string,
      /**  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  */  
   FaxNum:string,
      /**  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  Contact email address.  */  
   EmailAddress:string,
      /**  Password for SF/Portal, should not be easily editable from the Manufacturing System.  */  
   WebPassword:string,
      /**  Indicates if able to access the Supplier Workbench  */  
   WebUser:boolean,
      /**  Code that identifies the role of this person. Link to the RoleCD table.  */  
   RoleCode:string,
      /**  The contacts Cell phone number.  */  
   CellPhoneNum:string,
      /**  The contacts Pager number.  */  
   PagerNum:string,
      /**  The contacts Home number.  */  
   HomeNum:string,
      /**  The contacts Alternate number.  */  
   AltNum:string,
      /**  The Contacts Title  */  
   ContactTitle:string,
      /**  The name if the person this contact reports to.  */  
   ReportsTo:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Indicates that this contact is no longer contacted.  */  
   NoContact:boolean,
      /**  The date the task was created.  */  
   CreateDate:string,
      /**  The UserID that created the task  */  
   CreateDcdUserID:string,
      /**  The date the task was last changed.  */  
   ChangeDate:string,
      /**  The UserID that last changed the task  */  
   ChangeDcdUserID:string,
      /**  This contact does not get used on new LOQs  */  
   Inactive:boolean,
      /**  First Name  */  
   FirstName:string,
      /**  Middle Name  */  
   MiddleName:string,
      /**  Last Name  */  
   LastName:string,
      /**  Prefix  */  
   Prefix:string,
      /**  Suffix  */  
   Suffix:string,
      /**  Initials  */  
   Initials:string,
      /**  Unique identifier from an external G/L interface  */  
   ExternalId:string,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   GlbVendorNum:number,
      /**  Owner's Purchase Point  */  
   GlbPurPoint:string,
      /**  Global Contact number.  Unique identifier for the contact record.  */  
   GlbConNum:number,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  */  
   OldVendorNum:number,
      /**  Original Owner's Purchase Point - NOT CURRENTLY IN USE  */  
   OldPurPoint:string,
      /**  Original owner's Contact number.  Unique identifier for the contact record. - NOT CURRENTLY IN USE  */  
   OldConNum:number,
      /**  Indicates if the user chose to skip this record when linking global vendor contacts.  The user can come back at a later time and choose to link a skipped vendor contact if they need to.  */  
   Skipped:boolean,
   FaceBook:string,
   IM:string,
   LinkedIn:string,
   PerConID:number,
   SyncAddressToPerCon:boolean,
   SyncEmailToPerCon:boolean,
   SyncLinksToPerCon:boolean,
   SyncNameToPerCon:boolean,
   SyncPhoneToPerCon:boolean,
   Twitter:string,
   WebLink1:string,
   WebLink2:string,
   WebLink3:string,
   WebLink4:string,
   WebLink5:string,
   WebSite:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   GlbSysRowID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   LinkConNum:number,
      /**  Indicates the record is linked  */  
   IsLinked:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbVendorPPRow{
      /**  Company Identifier.  */  
   Company:string,
   PurPoint:string,
      /**  Purchase Point Name...can't be blank.  */  
   Name:string,
   Address1:string,
   Address2:string,
   Address3:string,
   City:string,
   State:string,
   Zip:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   Country:string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   PrimPCon:number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   FormatStr:string,
      /**  Email address of the vendor purchase point.  */  
   EMailAddress:string,
      /**  Unique Identifier from an external G/L interface  */  
   ExternalId:string,
      /**  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   TaxAuthorityCode:string,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   GlbVendorNum:number,
   EDICode:string,
      /**  Owner's Purchase Point  */  
   GlbPurPoint:string,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  */  
   OldVendorNum:number,
      /**  Original Owner's Purchase Point - NOT CURRENTLY IN USE  */  
   OldPurPoint:string,
      /**  Indicates if the user chose to skip this record when linking global vendor purchse points.  The user can come back at a later time and choose to link a skipped purchase point if they need to.  */  
   Skipped:boolean,
   ApplyChrg:boolean,
   ChrgAmount:number,
   COD:boolean,
   CODAmount:number,
   CODCheck:boolean,
   CODFreight:boolean,
   DeclaredAmt:number,
   DeclaredIns:boolean,
   DocOnly:boolean,
   GroundType:string,
   Hazmat:boolean,
   NotifyEMail:string,
   NotifyFlag:boolean,
   RefNotes:string,
   ResDelivery:boolean,
   SatDelivery:boolean,
   SatPickup:boolean,
   VerbalConf:boolean,
   DeliveryType:string,
   ServAlert:boolean,
   ServAOD:boolean,
   ServAuthNum:string,
   ServDeliveryDate:string,
   ServHomeDel:boolean,
   ServInstruct:string,
   ServPhone:string,
   ServPOD:boolean,
   ServRef1:string,
   ServRef2:string,
   ServRef3:string,
   ServRef4:string,
   ServRef5:string,
   ServRelease:boolean,
   ServSatDelivery:boolean,
   ServSatPickup:boolean,
   ServSignature:boolean,
   OverrideCarrier:boolean,
   OverrideService:boolean,
   AddlHdlgFlag:boolean,
   CertOfOrigin:boolean,
   CommercialInvoice:boolean,
   DeliveryConf:number,
   FFAddress1:string,
   FFAddress2:string,
   FFAddress3:string,
   FFCity:string,
   FFCompName:string,
   FFContact:string,
   FFCountry:string,
   FFCountryNum:number,
   FFID:string,
   FFPhoneNum:string,
   FFState:string,
   FFZip:string,
   IndividualPackIDs:boolean,
   IntrntlShip:boolean,
   LetterOfInstr:boolean,
   NonStdPkg:boolean,
   ShipExprtDeclartn:boolean,
   UPSQuantumView:boolean,
   UPSQVEmailType:string,
   UPSQVMemo:string,
   UPSQVShipFromName:string,
   LegalName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  INExciseRegNumber  */  
   INExciseRegNumber:string,
      /**  INExciseDivision  */  
   INExciseDivision:string,
      /**  INExciseRange  */  
   INExciseRange:string,
      /**  INCommissionarate  */  
   INCommissionarate:string,
      /**  INVATNumber  */  
   INVATNumber:string,
      /**  INServiceTaxRegNum  */  
   INServiceTaxRegNum:string,
      /**  INTaxRegionCode  */  
   INTaxRegionCode:string,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**  INTaxRegistrationID  */  
   INTaxRegistrationID:string,
      /**  Municipio Code  */  
   MXMunicipio:string,
   LinkPurPoint:string,
      /**  Indicates the record is linked  */  
   IsLinked:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbVendorRow{
      /**  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  */  
   Inactive:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  A descriptive Code assigned by the user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  */  
   VendorID:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   Name:string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
   Address1:string,
   Address2:string,
   Address3:string,
   City:string,
      /**  Can be blank.  */  
   State:string,
   ZIP:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   Country:string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   TaxPayerID:string,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   PurPoint:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   TermsCode:string,
      /**  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  */  
   GroupCode:string,
      /**  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  */  
   Print1099:boolean,
      /**  A user definable field which controls in which box on the 1099 that the amount should be printed.  */  
   Box1099:number,
      /**  Indicates that for this vendor all invoices must be paid on separate checks.  */  
   OneCheck:boolean,
      /**  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  */  
   PrintLabels:boolean,
      /**  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  */  
   FaxNum:string,
      /**  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   Comment:string,
      /**  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  */  
   PayHold:boolean,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  */  
   PrimPCon:number,
      /**  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  */  
   AccountRef:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   DefaultFOB:string,
      /**  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
   TaxRegionCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   FormatStr:string,
      /**  Payments to this vendors are made via electronic transfer.  */  
   ElecPayment:boolean,
      /**  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  */  
   PrimaryBankID:string,
      /**   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  */  
   Approved:boolean,
      /**  This is an inter-company vendor.  */  
   ICVend:boolean,
      /**  Email address of the vendor.  */  
   EMailAddress:string,
      /**  This vendor is web enabled  */  
   WebVendor:boolean,
      /**  Vendor URL.  */  
   VendURL:string,
      /**  Used to calculate on-time delivery performance rating  */  
   EarlyBuffer:number,
      /**  Used to calculate on-time delivery performance rating  */  
   LateBuffer:number,
      /**  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   OnTimeRating:string,
      /**  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  */  
   QualityRating:string,
      /**  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   PriceRating:string,
      /**  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   ServiceRating:string,
      /**  Unique identifier from an external G/L interface  */  
   ExternalId:string,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   VendPILimit:number,
      /**  Marks the vendor as a global vendor, available to be sent out to other companies  */  
   GlobalVendor:boolean,
      /**  Indicates if this vendor participates in the Inter-Company Trading.  */  
   ICTrader:boolean,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   TaxAuthorityCode:string,
      /**  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   GlbVendorNum:number,
      /**  A descriptive Code assigned by the parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  */  
   GlbVendorID:string,
      /**  MinOrderValue  */  
   MinOrderValue:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyBaseCurrCode:string,
   CalendarID:string,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
   EDICode:string,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  */  
   OldVendorNum:number,
      /**  A descriptive Code assigned by the original parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor. - NOT CURRENTLY IN USE  */  
   OldVendorID:string,
      /**  Indicates if the user chose to skip this record when linking global vendors.  The user can come back at a later time and choose to link a skipped vendor if they need to.  */  
   Skipped:boolean,
   ConsolidatedPurchasing:boolean,
   LocalPurchasing:boolean,
   ApplyChrg:boolean,
   ChrgAmount:number,
   COD:boolean,
   CODAmount:number,
   CODCheck:boolean,
   CODFreight:boolean,
   DeclaredAmt:number,
   DeclaredIns:boolean,
   DocOnly:boolean,
   GroundType:string,
   Hazmat:boolean,
   NotifyEMail:string,
   NotifyFlag:boolean,
   RefNotes:string,
   ResDelivery:boolean,
   SatDelivery:boolean,
   SatPickup:boolean,
   VerbalConf:boolean,
   DeliveryType:string,
   ServAlert:boolean,
   ServAOD:boolean,
   ServAuthNum:string,
   ServDeliveryDate:string,
   ServHomeDel:boolean,
   ServInstruct:string,
   ServPhone:string,
   ServPOD:boolean,
   ServRef1:string,
   ServRef2:string,
   ServRef3:string,
   ServRef4:string,
   ServRef5:string,
   ServRelease:boolean,
   ServSatDelivery:boolean,
   ServSatPickup:boolean,
   ServSignature:boolean,
   OverrideCarrier:boolean,
   OverrideService:boolean,
   CPay:boolean,
   AddlHdlgFlag:boolean,
   CertOfOrigin:boolean,
   CommercialInvoice:boolean,
   DeliveryConf:number,
   FFAddress1:string,
   FFAddress2:string,
   FFAddress3:string,
   FFCity:string,
   FFCompName:string,
   FFContact:string,
   FFCountry:string,
   FFCountryNum:number,
   FFID:string,
   FFPhoneNum:string,
   FFState:string,
   FFZip:string,
   IndividualPackIDs:boolean,
   IntrntlShip:boolean,
   LetterOfInstr:boolean,
   NonStdPkg:boolean,
   ShipExprtDeclartn:boolean,
   UPSQuantumView:boolean,
   UPSQVEmailType:string,
   UPSQVMemo:string,
   UPSQVShipFromName:string,
   RevChargeMethod:string,
   ManagedCust:boolean,
   ManagedCustID:string,
   ManagedCustNum:number,
   PartPayment:boolean,
   PMUID:number,
   HasBank:boolean,
   PmtAcctRef:string,
   LegalName:string,
   OrgRegCode:string,
   TaxRegReason:string,
   VendAccountType:string,
   AdvTaxInv:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AllowAsAltRemitTo  */  
   AllowAsAltRemitTo:boolean,
      /**  THBranchID  */  
   THBranchID:string,
      /**  ParamCode  */  
   ParamCode:string,
      /**  AGAFIPResponsibilityCode  */  
   AGAFIPResponsibilityCode:string,
      /**  AGGrossIncomeTaxID  */  
   AGGrossIncomeTaxID:string,
      /**  AGIDDocumentTypeCode  */  
   AGIDDocumentTypeCode:string,
      /**  AGProvinceCode  */  
   AGProvinceCode:string,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  AGApartment  */  
   AGApartment:string,
      /**  AGExtraStreetNumber  */  
   AGExtraStreetNumber:string,
      /**  AGFloor  */  
   AGFloor:string,
      /**  AGLocationCode  */  
   AGLocationCode:string,
      /**  AGNeighborhood  */  
   AGNeighborhood:string,
      /**  AGStreet  */  
   AGStreet:string,
      /**  AGStreetNumber  */  
   AGStreetNumber:string,
      /**  COOneTimeID  */  
   COOneTimeID:string,
      /**  NoBankingReference  */  
   NoBankingReference:boolean,
      /**  PEGoodsContributor  */  
   PEGoodsContributor:boolean,
      /**  PEWithholdAgent  */  
   PEWithholdAgent:boolean,
      /**  PECollectionAgent  */  
   PECollectionAgent:boolean,
      /**  PENotFound  */  
   PENotFound:boolean,
      /**  PENoAddress  */  
   PENoAddress:boolean,
      /**  PEIdentityDocType  */  
   PEIdentityDocType:string,
      /**  COIsOneTimeVend  */  
   COIsOneTimeVend:boolean,
      /**  PEDocumentID  */  
   PEDocumentID:string,
      /**  MaxLateDaysPORel  */  
   MaxLateDaysPORel:number,
      /**  1099 Code  */  
   Code1099ID:string,
      /**  TIN  */  
   TIN:string,
      /**  TINType  */  
   TINType:string,
      /**  SecondTINNotice  */  
   SecondTINNotice:boolean,
      /**  NameControl  */  
   NameControl:string,
      /**  ShipViaCode  */  
   ShipViaCode:string,
      /**  NonUS  */  
   NonUS:boolean,
      /**  FormTypeID  */  
   FormTypeID:string,
      /**  INSupplierType  */  
   INSupplierType:string,
      /**  INCSTNumber  */  
   INCSTNumber:string,
      /**  INPANNumber  */  
   INPANNumber:string,
      /**  DEOrgType  */  
   DEOrgType:string,
      /**  PaymentReporting  */  
   PaymentReporting:boolean,
      /**  ExternalPurchasing  */  
   ExternalPurchasing:boolean,
      /**  MXRetentionCode  */  
   MXRetentionCode:string,
      /**  Reporting1099Name  */  
   Reporting1099Name:string,
      /**  Reporting1099Name2  */  
   Reporting1099Name2:string,
      /**  FATCA  */  
   FATCA:boolean,
      /**  AccountNum  */  
   AccountNum:string,
      /**  TWGUIRegNum  */  
   TWGUIRegNum:string,
      /**  MXTARCode  */  
   MXTARCode:string,
      /**  PEAddressID  */  
   PEAddressID:string,
      /**  PERetentionRegime  */  
   PERetentionRegime:string,
      /**  TaxEntityType  */  
   TaxEntityType:string,
      /**  INGSTComplianceRate  */  
   INGSTComplianceRate:number,
      /**  INTaxRegistrationID  */  
   INTaxRegistrationID:string,
      /**  TINValidationStatus  */  
   TINValidationStatus:number,
      /**  ImporterOfRecord  */  
   ImporterOfRecord:boolean,
      /**  PLAutomaticAPInvoiceNum  */  
   PLAutomaticAPInvoiceNum:boolean,
      /**  SEC  */  
   SEC:string,
      /**  MXDIOTTranType  */  
   MXDIOTTranType:string,
      /**  US1099KMerchCatCode  */  
   US1099KMerchCatCode:string,
      /**  MXTaxpayerType  */  
   MXTaxpayerType:string,
      /**  MXLegalRepRFC  */  
   MXLegalRepRFC:string,
      /**  MXLegalRepCURP  */  
   MXLegalRepCURP:string,
      /**  MXLegalRepName  */  
   MXLegalRepName:string,
      /**  MXLegalRepTaxpayerType  */  
   MXLegalRepTaxpayerType:string,
      /**  US1099State  */  
   US1099State:string,
      /**  TaxValidationStatus  */  
   TaxValidationStatus:number,
      /**  TaxValidationDate  */  
   TaxValidationDate:string,
      /**  HMRCTaxValidationLog  */  
   HMRCTaxValidationLog:string,
      /**  ExternalSchemeID  */  
   ExternalSchemeID:string,
      /**  Municipio Code  */  
   MXMunicipio:string,
      /**  EInvoice  */  
   EInvoice:boolean,
      /**  Flag used to mark a Supplier as EDI.  */  
   EDISupplier:boolean,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
   DispVendorID:string,
      /**  The VendorId to link to (new or existing)  */  
   LinkVendorID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbVendorTableset{
   GlbVendor:Erp_Tablesets_GlbVendorRow[],
   GlbVendCnt:Erp_Tablesets_GlbVendCntRow[],
   GlbVendorPP:Erp_Tablesets_GlbVendorPPRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PEVendWhldHistRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Vendor Number  */  
   VendorNum:number,
      /**  Record Sequence  */  
   RecordSeq:number,
      /**  Create Date  */  
   CreateDate:string,
      /**  User Identifier  */  
   UserID:string,
      /**  Displays the Identity DocumentType  */  
   IdentityDocType:string,
      /**  Indicates if supplier has a Good Contributor status  */  
   GoodContributor:boolean,
      /**  Indicates if supplier is a Withholding Agent  */  
   WithholdingAgent:boolean,
      /**  Indicates the status of Collection Agent  */  
   CollectionAgent:boolean,
      /**  Not Found withholding status  */  
   NotFound:boolean,
      /**  No Address Provided withholding status  */  
   NoAddress:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartnerRow{
      /**  Company  */  
   Company:string,
      /**  PartnerNum  */  
   PartnerNum:number,
      /**  PartnerType  */  
   PartnerType:number,
      /**  SearchID  */  
   SearchID:string,
      /**  IsActive  */  
   IsActive:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  PartnerID  */  
   PartnerID:string,
   DspSearchID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxExemptRow{
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
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code  */  
   RateCode:string,
      /**  Exemption Effective Start Date  */  
   EffectiveFrom:string,
      /**  Exemption Effective End Date  */  
   EffectiveTo:string,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Tax Legal Text Code  */  
   TextCode:string,
      /**  Tax Resolution Number  */  
   ResolutionNum:string,
      /**  Tax Resolution Date  */  
   ResolutionDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  A unique Customer identifier.  */  
   CustNum:number,
      /**  The PartNum field identifies the Part.  */  
   PartNum:string,
      /**  A unique Vendor identifier.  */  
   VendorNum:number,
   BitFlag:number,
   SalesTaxDescription:string,
   SalesTRCDescription:string,
   TaxTextDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtVendorTableset{
   Vendor:Erp_Tablesets_VendorRow[],
   VendorAttch:Erp_Tablesets_VendorAttchRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   TaxExempt:Erp_Tablesets_TaxExemptRow[],
   Partner:Erp_Tablesets_PartnerRow[],
   PEVendWhldHist:Erp_Tablesets_PEVendWhldHistRow[],
   VendRestriction:Erp_Tablesets_VendRestrictionRow[],
   VendBank:Erp_Tablesets_VendBankRow[],
   VendBankAttch:Erp_Tablesets_VendBankAttchRow[],
   VendCntMain:Erp_Tablesets_VendCntMainRow[],
   VenMFBill:Erp_Tablesets_VenMFBillRow[],
   VendorPP:Erp_Tablesets_VendorPPRow[],
   VenPPMFBill:Erp_Tablesets_VenPPMFBillRow[],
   VenPPUPSEmail:Erp_Tablesets_VenPPUPSEmailRow[],
   VendPPRestriction:Erp_Tablesets_VendPPRestrictionRow[],
   VendCnt:Erp_Tablesets_VendCntRow[],
   VendCntAttch:Erp_Tablesets_VendCntAttchRow[],
   VenUPSEmail:Erp_Tablesets_VenUPSEmailRow[],
   VendRemitTo:Erp_Tablesets_VendRemitToRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VenMFBillRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayBTFlag:string,
      /**   Describes the billing type.  Valid values and their description are:
1 - Shipper
2 - FedEx  Collect
3 - Third Party
4 - UPS Prepaid
5 - FedEx Recipient
6 - UPS Consignee
7 - UPS Freight Collect
8 - UPS Free On Board
9 - UPS Cost and Freight
10 - UPS Delivery Duty Paid
11 - UPS Shpping Duty and Tax Consignee  */  
   PayTypeDesc:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Billing Address  */  
   PayBTAddress1:string,
      /**  Shipping biling address line 2  */  
   PayBTAddress2:string,
      /**  Shipping biling address line 3.  */  
   PayBTAddress3:string,
      /**  Shipping billing city  */  
   PayBTCity:string,
      /**  Shipping Billing state or province  */  
   PayBTState:string,
      /**  Manifest Bililng postal code.  */  
   PayBTZip:string,
      /**  Shipping biling country  */  
   PayBTCountry:string,
      /**  Internal field used to store the country number.  */  
   PayBTCountryNum:number,
      /**  Shipping billing phone number  */  
   PayBTPhone:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PayBTCountryNumDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VenPPMFBillRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayBTFlag:string,
      /**   Describes the billing type.  Valid values and their description are:
1 - Shipper
2 - FedEx  Collect
3 - Third Party
4 - UPS Prepaid
5 - FedEx Recipient
6 - UPS Consignee
7 - UPS Freight Collect
8 - UPS Free On Board
9 - UPS Cost and Freight
10 - UPS Delivery Duty Paid
11 - UPS Shpping Duty and Tax Consignee  */  
   PayTypeDesc:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Billing Address  */  
   PayBTAddress1:string,
      /**  Shipping biling address line 2  */  
   PayBTAddress2:string,
      /**  Shipping biling address line 3.  */  
   PayBTAddress3:string,
      /**  Shipping billing city  */  
   PayBTCity:string,
      /**  Pay manifest billing postal code.  */  
   PayBTZip:string,
      /**  Shipping Billing state or province  */  
   PayBTState:string,
      /**  Shipping biling country  */  
   PayBTCountry:string,
      /**  Internal field used to store the country number.  */  
   PayBTCountryNum:number,
      /**  Shipping billing phone number  */  
   PayBTPhone:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PayBTCountryNumDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VenPPUPSEmailRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  UPS Quantum View Sequence  */  
   UPSQVSeq:number,
      /**  Email address to notify for a UPS shipment  */  
   EmailAddress:string,
      /**  Logical indicating if the EmailAddress is to be updated at shipping.  */  
   ShipmentNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   FailureNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   DeliveryNotify:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Logical indicating if the ups quantum view fields are to be enabled.  */  
   EnableQuantumView:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VenUPSEmailRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
      /**  UPS Quantum View Sequence  */  
   UPSQVSeq:number,
      /**  Email address to notify for a UPS shipment  */  
   EmailAddress:string,
      /**  Logical indicating if the EmailAddress is to be updated at shipping.  */  
   ShipmentNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   FailureNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   DeliveryNotify:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  logical indicating if the UPS quantum view fields are to be enabled.  */  
   EnableQuantumView:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendBankAttchRow{
   Company:string,
   VendorNum:number,
   BankID:string,
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

export interface Erp_Tablesets_VendBankRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Supplier Number  */  
   VendorNum:number,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Supplier Bank Name  */  
   BankName:string,
      /**  First Address Line of the Supplier Bank  */  
   Address1:string,
      /**  Second Address Line of the Supplier Bank  */  
   Address2:string,
      /**  Third Address Line of the Supplier Bank  */  
   Address3:string,
      /**  City portion of the address of the Supplier Bank  */  
   City:string,
      /**  Can be blank.  */  
   State:string,
      /**  Postal Code or Zip code portion of the address of the Supplier Bank  */  
   PostalCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   BankAcctNumber:string,
      /**  Name on the Bank Account.  */  
   NameOnAccount:string,
      /**  Swift number of the bank.  */  
   SwiftNum:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Bank Branch Code of the Supplier Bank  */  
   BankBranchCode:string,
      /**  IBAN Code of the Supplier Bank  */  
   IBANCode:string,
      /**  Sweden localization field, Credit Transfer Number  */  
   SECreditTransNum:string,
      /**  Full Legal name  */  
   LegalName:string,
      /**  Correspondence Account of the Supplier Bank  */  
   CorrespAccount:string,
      /**  Local BIC of the Supplier Bank  */  
   LocalBIC:string,
      /**  Free Form Bank Person Code. Used in localizations.  */  
   BankPersonCode:string,
      /**  Supplier bank Account Type. Used in localizations.  */  
   VendAccountType:string,
      /**   Denmark Localization
Card (payment) code  */  
   CardCode:string,
      /**   Denmark Localization
Account Number  */  
   BankGiroAcctNbr:string,
      /**   Denmark Localization
Bank Reference code  */  
   BankRefCode:string,
      /**  AllowAsAltRemitToBank  */  
   AllowAsAltRemitToBank:boolean,
      /**  DFIIdentification  */  
   DFIIdentification:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHDTAID  */  
   CHDTAID:string,
      /**  CHISRPartyID  */  
   CHISRPartyID:string,
      /**  FeeOwnership  */  
   FeeOwnership:string,
      /**  POBankAcctNum  */  
   POBankAcctNum:string,
      /**  BankCustNum  */  
   BankCustNum:string,
      /**  BankCustNumberStartPos  */  
   BankCustNumberStartPos:number,
      /**  BankCustNumberLen  */  
   BankCustNumberLen:number,
      /**  Specifies the supplier's bank address.  */  
   BAddress1:string,
      /**  Specifies the supplier's bank address.  */  
   BAddress2:string,
      /**  Specifies the supplier's bank address.  */  
   BAddress3:string,
      /**  Bank Charges (Used for Czech Republic CSF)  */  
   BankCharges:string,
      /**  Bank Constant Symbol (Used for Czech Republic CSF)  */  
   BankCnstSymbol:string,
      /**  Bank Special Symbol (Used for Czech Republic CSF)  */  
   BankSpecSymbol:string,
      /**  Bank type of electronic payment transactions  */  
   BankType:string,
      /**  Specifies the supplier's bank city.  */  
   BCity:string,
      /**  Specifies the supplier's bank country.  */  
   BCountryNum:number,
      /**  Specifies the supplier's postal code.  */  
   BPostalCode:string,
      /**  Specifies the supplier's bank state/province.  */  
   BState:string,
      /**  Norway CSF: Determines where bank cheque is sent.  */  
   NOChequeCode:string,
      /**  Norway CSF: Determines how the bank fee cost will be settled between the company and supplier during the fund transfers between two entities.  */  
   NOFeeCostCode:string,
      /**  Receiver Name.  Used in Japan localizations.  */  
   ReceiverName:string,
      /**  Receiving Bank Name.  Used in Japan localizations.  */  
   ReceivingBankName:string,
      /**  Receiving Bank Number.  Used in Japan localizations.  */  
   ReceivingBankNum:string,
      /**  Receiving Branch Name.  Used in Japan localizations.  */  
   ReceivingBranchName:string,
      /**  Receiving Branch Number.  Used in Japan localizations.  */  
   ReceivingBranchNum:string,
      /**  SEBankFeeCostOwner  */  
   SEBankFeeCostOwner:string,
      /**  PEDetractionsNBA  */  
   PEDetractionsNBA:boolean,
      /**  MX SAT Code  */  
   MXSATCode:string,
      /**  MX SAT Name Short  */  
   MXSATNameShort:string,
      /**  MX SAT Name Full  */  
   MXSATNameFull:string,
      /**  DKCreditorNum  */  
   DKCreditorNum:string,
      /**  A supplier alias used to make and receive payments.  */  
   PayID:string,
      /**  ClearSystemIDCode  */  
   ClearSystemIDCode:string,
      /**  MemberID  */  
   MemberID:string,
   BCountry:number,
      /**  Postal Account Number in format XX-#####V-P (CSF Switzerland)  */  
   CHScrPOBankAcctNum:string,
   PrimaryBank:boolean,
      /**  ISR Party Number in format XX-#####V-P (CSF Switzerland)  */  
   CHScrISRPartyID:string,
   BitFlag:number,
   BankBranchCodeDescDescription:string,
   BankBranchCodeDescBankBranchCode:string,
   BCountryNumDescription:string,
   CountryNumDescription:string,
   PayMethodType:number,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodName:string,
   VendorNumCity:string,
   VendorNumState:string,
   VendorNumVendorID:string,
   VendorNumAddress1:string,
   VendorNumName:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumCountry:string,
   VendorNumAddress2:string,
   VendorNumAddress3:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendCntAttchRow{
   Company:string,
   VendorNum:number,
   PurPoint:string,
   ConNum:number,
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

export interface Erp_Tablesets_VendCntMainRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  This key links the record to the Vendor file.  */  
   VendorNum:number,
      /**  Purchase point from Vendor.  */  
   PurPoint:string,
      /**  Contact number.  Unique identifier for the contact record.  */  
   ConNum:number,
      /**  Contact name.  */  
   Name:string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   Func:string,
      /**  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  */  
   FaxNum:string,
      /**  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  Contact email address.  */  
   EmailAddress:string,
      /**  Password for SF/Portal, should not be easily editable from the Manufacturing System.  */  
   WebPassword:string,
      /**  Indicates if able to access the Supplier Workbench  */  
   WebUser:boolean,
      /**  Code that identifies the role of this person. Link to the RoleCD table.  */  
   RoleCode:string,
      /**  The contacts Cell phone number.  */  
   CellPhoneNum:string,
      /**  The contacts Pager number.  */  
   PagerNum:string,
      /**  The contacts Home number.  */  
   HomeNum:string,
      /**  The contacts Alternate number.  */  
   AltNum:string,
      /**  The Contacts Title  */  
   ContactTitle:string,
      /**  The name if the person this contact reports to.  */  
   ReportsTo:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Indicates that this contact is no longer contacted.  */  
   NoContact:boolean,
      /**  The date the task was created.  */  
   CreateDate:string,
      /**  The UserID that created the task  */  
   CreateDcdUserID:string,
      /**  The date the task was last changed.  */  
   ChangeDate:string,
      /**  The UserID that last changed the task  */  
   ChangeDcdUserID:string,
      /**  This contact does not get used on new LOQs  */  
   Inactive:boolean,
      /**  First Name  */  
   FirstName:string,
      /**  Middle Name  */  
   MiddleName:string,
      /**  Last Name  */  
   LastName:string,
      /**  Prefix  */  
   Prefix:string,
      /**  Suffix  */  
   Suffix:string,
      /**  Initials  */  
   Initials:string,
      /**  Unique identifier from an external G/L interface  */  
   ExternalId:string,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   SyncEmailToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  */  
   SyncLinksToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   SyncNameToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   SyncPhoneToPerCon:boolean,
      /**  Contact's website.  */  
   WebSite:string,
      /**  Contact's IM.  */  
   IM:string,
      /**  Contact's Twitter.  */  
   Twitter:string,
      /**  Contact's LinkedIn.  */  
   LinkedIn:string,
      /**  Contact's FaceBook.  */  
   FaceBook:string,
      /**  User defined Link 1.  */  
   WebLink1:string,
      /**  User defined Link 2.  */  
   WebLink2:string,
      /**  User defined Link 3.  */  
   WebLink3:string,
      /**  User defined Link 4.  */  
   WebLink4:string,
      /**  User defined Link 5.  */  
   WebLink5:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   GlbFlag:boolean,
   PrimaryContact:boolean,
   VendCntAttrStrng:string,
      /**  GlbVendCnt fields in a linked list to find the linking record  */  
   GlbLink:string,
   PerConName:string,
   BitFlag:number,
   RoleCodeRoleDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendCntRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  This key links the record to the Vendor file.  */  
   VendorNum:number,
      /**  Purchase point from Vendor.  */  
   PurPoint:string,
      /**  Contact number.  Unique identifier for the contact record.  */  
   ConNum:number,
      /**  Contact name.  */  
   Name:string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   Func:string,
      /**  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  */  
   FaxNum:string,
      /**  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  Contact email address.  */  
   EmailAddress:string,
      /**  Password for SF/Portal, should not be easily editable from the Manufacturing System.  */  
   WebPassword:string,
      /**  Indicates if able to access the Supplier Workbench  */  
   WebUser:boolean,
      /**  Code that identifies the role of this person. Link to the RoleCD table.  */  
   RoleCode:string,
      /**  The contacts Cell phone number.  */  
   CellPhoneNum:string,
      /**  The contacts Pager number.  */  
   PagerNum:string,
      /**  The contacts Home number.  */  
   HomeNum:string,
      /**  The contacts Alternate number.  */  
   AltNum:string,
      /**  The Contacts Title  */  
   ContactTitle:string,
      /**  The name if the person this contact reports to.  */  
   ReportsTo:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Indicates that this contact is no longer contacted.  */  
   NoContact:boolean,
      /**  The date the task was created.  */  
   CreateDate:string,
      /**  The UserID that created the task  */  
   CreateDcdUserID:string,
      /**  The date the task was last changed.  */  
   ChangeDate:string,
      /**  The UserID that last changed the task  */  
   ChangeDcdUserID:string,
      /**  This contact does not get used on new LOQs  */  
   Inactive:boolean,
      /**  First Name  */  
   FirstName:string,
      /**  Middle Name  */  
   MiddleName:string,
      /**  Last Name  */  
   LastName:string,
      /**  Prefix  */  
   Prefix:string,
      /**  Suffix  */  
   Suffix:string,
      /**  Initials  */  
   Initials:string,
      /**  Unique identifier from an external G/L interface  */  
   ExternalId:string,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   SyncEmailToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  */  
   SyncLinksToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   SyncNameToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   SyncPhoneToPerCon:boolean,
      /**  Contact's website.  */  
   WebSite:string,
      /**  Contact's IM.  */  
   IM:string,
      /**  Contact's Twitter.  */  
   Twitter:string,
      /**  Contact's LinkedIn.  */  
   LinkedIn:string,
      /**  Contact's FaceBook.  */  
   FaceBook:string,
      /**  User defined Link 1.  */  
   WebLink1:string,
      /**  User defined Link 2.  */  
   WebLink2:string,
      /**  User defined Link 3.  */  
   WebLink3:string,
      /**  User defined Link 4.  */  
   WebLink4:string,
      /**  User defined Link 5.  */  
   WebLink5:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   PrimaryContact:boolean,
   GlbFlag:boolean,
   VendCntAttrStrng:string,
      /**  GlbVendCnt fields in a linked list to find the linking record  */  
   GlbLink:string,
      /**  The name of the person contact.  */  
   PerConName:string,
   BitFlag:number,
   PurPointZip:string,
   PurPointAddress2:string,
   PurPointState:string,
   PurPointName:string,
   PurPointPrimPCon:number,
   PurPointCity:string,
   PurPointAddress1:string,
   PurPointCountry:string,
   PurPointAddress3:string,
   RoleCodeRoleDescription:string,
   VendorNumDefaultFOB:string,
   VendorNumState:string,
   VendorNumAddress2:string,
   VendorNumAddress1:string,
   VendorNumVendorID:string,
   VendorNumAddress3:string,
   VendorNumCurrencyCode:string,
   VendorNumCountry:string,
   VendorNumZIP:string,
   VendorNumName:string,
   VendorNumCity:string,
   VendorNumTermsCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendPPRestrictionRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  Restriction Type identification.  */  
   RestrictionTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PurPointName:string,
   PurPointState:string,
   PurPointAddress3:string,
   PurPointAddress1:string,
   PurPointZip:string,
   PurPointCity:string,
   PurPointAddress2:string,
   PurPointPrimPCon:number,
   PurPointCountry:string,
   RestrictionTypeDescription:string,
   VendorNumCountry:string,
   VendorNumTermsCode:string,
   VendorNumCurrencyCode:string,
   VendorNumZIP:string,
   VendorNumVendorID:string,
   VendorNumAddress2:string,
   VendorNumAddress1:string,
   VendorNumAddress3:string,
   VendorNumDefaultFOB:string,
   VendorNumCity:string,
   VendorNumName:string,
   VendorNumState:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendRemitToRow{
      /**  Company  */  
   Company:string,
      /**  VendorNum  */  
   VendorNum:number,
      /**  RemitToSeq  */  
   RemitToSeq:number,
      /**  RemitToType  */  
   RemitToType:string,
      /**  RemitCustNum  */  
   RemitCustNum:number,
      /**  RemitEmpID  */  
   RemitEmpID:string,
      /**  RemitVendorNum  */  
   RemitVendorNum:number,
      /**  RemitToName  */  
   RemitToName:string,
      /**  DefaultRemitTo  */  
   DefaultRemitTo:boolean,
      /**  Inactive  */  
   Inactive:boolean,
      /**  OneCheck  */  
   OneCheck:boolean,
      /**  Comments  */  
   Comments:string,
      /**  RemitToAddress1  */  
   RemitToAddress1:string,
      /**  RemitToAddress2  */  
   RemitToAddress2:string,
      /**  RemitToAddress3  */  
   RemitToAddress3:string,
      /**  RemitToCity  */  
   RemitToCity:string,
      /**  RemitToState  */  
   RemitToState:string,
      /**  RemitToZip  */  
   RemitToZip:string,
      /**  RemitToCountry  */  
   RemitToCountry:number,
      /**  RemitToPhoneNum  */  
   RemitToPhoneNum:string,
      /**  RemitToFaxNum  */  
   RemitToFaxNum:string,
      /**  RemitToEmail  */  
   RemitToEmail:string,
      /**  TermsCode  */  
   TermsCode:string,
      /**  CurrencyCode  */  
   CurrencyCode:string,
      /**  PMUID  */  
   PMUID:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  This can either be a CustID, EmpID, or VendID depending on the RemitToType  */  
   RemitToID:string,
   BitFlag:number,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrencyID:string,
   TermsCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendRestrictionRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
      /**  Restriction Type identification.  */  
   RestrictionTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   RestrictionTypeDescription:string,
   VendorNumVendorID:string,
   VendorNumCurrencyCode:string,
   VendorNumZIP:string,
   VendorNumCity:string,
   VendorNumAddress2:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress3:string,
   VendorNumCountry:string,
   VendorNumTermsCode:string,
   VendorNumAddress1:string,
   VendorNumName:string,
   VendorNumState:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendorAttchRow{
   Company:string,
   VendorNum:number,
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

export interface Erp_Tablesets_VendorListRow{
      /**  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  */  
   Inactive:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the system, for linking other records to the Vendor.  */  
   VendorID:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   Name:string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
      /**  First address line of the Supplier  */  
   Address1:string,
      /**  Second address line of the Supplier  */  
   Address2:string,
      /**  Third address line of the Supplier  */  
   Address3:string,
      /**  City portion of the address of the Supplier  */  
   City:string,
      /**  Can be blank.  */  
   State:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   ZIP:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   Country:string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   TaxPayerID:string,
      /**  Currency Code Description  */  
   CurrDesc:string,
      /**  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  */  
   GroupCode:string,
      /**  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  */  
   PayHold:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Taxpayer Identification Number  */  
   TIN:string,
      /**  INTaxRegistrationID  */  
   INTaxRegistrationID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendorListTableset{
   VendorList:Erp_Tablesets_VendorListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VendorPPRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  Purchase Point Name...can't be blank.  */  
   Name:string,
      /**  First address line  */  
   Address1:string,
      /**  Second address line  */  
   Address2:string,
      /**  Third address line  */  
   Address3:string,
      /**  City portion of the address  */  
   City:string,
      /**  State portion of the address  */  
   State:string,
      /**  Postal Code or Zip code portion of the address  */  
   Zip:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   Country:string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   PrimPCon:number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   FormatStr:string,
      /**  Email address of the vendor purchase point.  */  
   EMailAddress:string,
      /**  Unique Identifier from an external G/L interface  */  
   ExternalId:string,
      /**  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   TaxAuthorityCode:string,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   EDICode:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Override Carrier Defaults.  If not checked then the vendor values will be used if overriden else the Site values  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the vendor values will be used if overriden else the Site values  */  
   OverrideService:boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Indicates if the shipment is international.  */  
   IntrntlShip:boolean,
      /**  Certificate of Origin flag  */  
   CertOfOrigin:boolean,
      /**  Commercial Invoice flag.  */  
   CommercialInvoice:boolean,
      /**  Ship Export Declaration flag  */  
   ShipExprtDeclartn:boolean,
      /**  Letter of Instruction flag  */  
   LetterOfInstr:boolean,
      /**  Freight Forwarder ID  */  
   FFID:string,
      /**  Freight Forwarder Company Name  */  
   FFCompName:string,
      /**  Freight Forwarder contact person  */  
   FFContact:string,
      /**  First address line of the Freight Forwarder  */  
   FFAddress1:string,
      /**  Second address line of the Freight Forwarder  */  
   FFAddress2:string,
      /**  Third address line of the Freight Forwarder  */  
   FFAddress3:string,
      /**  Freight Forwarder city portion of address.  */  
   FFCity:string,
      /**  Freight Forwarder state portion of address.  */  
   FFState:string,
      /**  Freight Forwarder Zip code portion of the address  */  
   FFZip:string,
      /**  Freight Forwarder Country portion of the address  */  
   FFCountry:string,
      /**  Non Standard Packaging  */  
   NonStdPkg:boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling flag  */  
   AddlHdlgFlag:boolean,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View Ship from Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Freight Forwarder Phone Number  */  
   FFPhoneNum:string,
      /**  Freight Forwarder Country Number  */  
   FFCountryNum:number,
      /**  Legal Name  */  
   LegalName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  INExciseRegNumber  */  
   INExciseRegNumber:string,
      /**  INExciseDivision  */  
   INExciseDivision:string,
      /**  INExciseRange  */  
   INExciseRange:string,
      /**  INCommissionarate  */  
   INCommissionarate:string,
      /**  INVATNumber  */  
   INVATNumber:string,
      /**  INServiceTaxRegNum  */  
   INServiceTaxRegNum:string,
      /**  INTaxRegionCode  */  
   INTaxRegionCode:string,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**  INTaxRegistrationID  */  
   INTaxRegistrationID:string,
      /**  Municipio Code  */  
   MXMunicipio:string,
   GroupCode:string,
   IntegrationFlag:boolean,
   PhoneNum:string,
   PrimaryPP:boolean,
   VendAttrString:string,
      /**  Indicates if ShipTo is a global record  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany, GlbVendorNum and GlbPurPoint that is linking to this purchase point  */  
   GlbLink:string,
      /**  Sales Tax ID  */  
   SalesTaxID:string,
      /**  Service Tax ID  */  
   ServiceTaxID:string,
   LangNameIDDescription:string,
      /**  Area of ISTMO de Tehuantepec (Polos de Desarrollo). Value is from MXLocISTMO User Code.  */  
   MXISTMO:string,
   BitFlag:number,
   CountryNumDescription:string,
   DeliveryTypeDescription:string,
   INTaxRegionCodeDescription:string,
   TACodeTaxAuthorityDescription:string,
   VendorNumState:string,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress1:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   VendorNumZIP:string,
   VendorNumCountry:string,
   VendorNumTermsCode:string,
   VendorNumName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendorRow{
      /**  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  */  
   Inactive:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the system, for linking other records to the Vendor.  */  
   VendorID:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   Name:string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
      /**  First address line of the Supplier  */  
   Address1:string,
      /**  Second address line of the Supplier  */  
   Address2:string,
      /**  Third address line of the Supplier  */  
   Address3:string,
      /**  City portion of the address of the Supplier  */  
   City:string,
      /**  Can be blank.  */  
   State:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   ZIP:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   Country:string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   TaxPayerID:string,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   PurPoint:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   TermsCode:string,
      /**  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  */  
   GroupCode:string,
      /**  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  */  
   Print1099:boolean,
      /**  Indicates that for this vendor all invoices must be paid on separate checks.  */  
   OneCheck:boolean,
      /**  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  */  
   PrintLabels:boolean,
      /**  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  */  
   FaxNum:string,
      /**  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   Comment:string,
      /**  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  */  
   PayHold:boolean,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  */  
   PrimPCon:number,
      /**  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  */  
   AccountRef:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   DefaultFOB:string,
      /**  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Tax Liability of the Supplier  */  
   TaxRegionCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   FormatStr:string,
      /**  Payments to this vendors are made via electronic transfer.  */  
   ElecPayment:boolean,
      /**  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  */  
   PrimaryBankID:string,
      /**   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  */  
   Approved:boolean,
      /**  This is an inter-company vendor.  */  
   ICVend:boolean,
      /**  Email address of the vendor.  */  
   EMailAddress:string,
      /**  This vendor is web enabled  */  
   WebVendor:boolean,
      /**  Vendor URL.  */  
   VendURL:string,
      /**  Used to calculate on-time delivery performance rating  */  
   EarlyBuffer:number,
      /**  Used to calculate on-time delivery performance rating  */  
   LateBuffer:number,
      /**  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   OnTimeRating:string,
      /**  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  */  
   QualityRating:string,
      /**  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   PriceRating:string,
      /**  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   ServiceRating:string,
      /**  Unique identifier from an external G/L interface  */  
   ExternalId:string,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   VendPILimit:number,
      /**  Marks the vendor as a global vendor, available to be sent out to other companies  */  
   GlobalVendor:boolean,
      /**  Indicates if this vendor participates in the Inter-Company Trading.  */  
   ICTrader:boolean,
      /**  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   TaxAuthorityCode:string,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  MinOrderValue  */  
   MinOrderValue:number,
      /**  Identifies the production calendar for this Vendor.   If this equals "", then the ProdCal record is the Company Level production calendar.  */  
   CalendarID:string,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   EDICode:string,
      /**  Should this Supplier be included in Consolidated Purchasing?  */  
   ConsolidatedPurchasing:boolean,
      /**  If the Part Class being purchased is included in Consolidated Purchasing, should purchasing it from this Supplier override that so it will be purchased in this company?  */  
   LocalPurchasing:boolean,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Flag to indicate if the Vendor participates in the Centralized Payment process.  */  
   CPay:boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Indicates if the shipment is international.  */  
   IntrntlShip:boolean,
      /**  Certificate of Origin flag  */  
   CertOfOrigin:boolean,
      /**  Commercial Invoice flag.  */  
   CommercialInvoice:boolean,
      /**  Ship Export Declaration flag  */  
   ShipExprtDeclartn:boolean,
      /**  Letter of Instruction flag  */  
   LetterOfInstr:boolean,
      /**  Freight Forwarder ID  */  
   FFID:string,
      /**  Freight Forwarder Company Name  */  
   FFCompName:string,
      /**  Freight Forwarder contact person  */  
   FFContact:string,
      /**  First address line of the Freight Forwarder  */  
   FFAddress1:string,
      /**  Second address line of the Freight Forwarder  */  
   FFAddress2:string,
      /**  Third address line of the Freight Forwarder  */  
   FFAddress3:string,
      /**  Freight Forwarder city portion of address.  */  
   FFCity:string,
      /**  Freight Forwarder state portion of address.  */  
   FFState:string,
      /**  Freight Forwarder Zip code portion of the address  */  
   FFZip:string,
      /**  Freight Forwarder Country portion of the address  */  
   FFCountry:string,
      /**  Non Standard Packaging  */  
   NonStdPkg:boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling flag  */  
   AddlHdlgFlag:boolean,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View Ship from Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Freight Forwarder Phone Number  */  
   FFPhoneNum:string,
      /**  Freight Forwarder Country Number  */  
   FFCountryNum:number,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this Supplier.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AP invoice line for this Supplier.  */  
   RevChargeMethod:string,
      /**  Flag indicating whether this vendor is associated with a 3PL customer.  */  
   ManagedCust:boolean,
      /**  CustID of the associated managed customer.  Only populated if ManagedCust flag = true.  */  
   ManagedCustID:string,
      /**  CustNum associated with CustID of managed customer.  Only populated if ManagedCust flag = true.  */  
   ManagedCustNum:number,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  If yes, indicates that Vendor has at least one assoicated VendBank record.  */  
   HasBank:boolean,
      /**  The Payment Banking Reference assigned by the supplier  */  
   PmtAcctRef:string,
      /**  Full Legal Name  */  
   LegalName:string,
      /**  Tax Payer Registration Reason Code  */  
   TaxRegReason:string,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**   Indicates Advanced Tax invoice is expected from supplier
after prepayment is done. If this field is set to yes, prepayment
invoice is not crated automatically.  */  
   AdvTaxInv:boolean,
      /**  AllowAsAltRemitTo  */  
   AllowAsAltRemitTo:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  THBranchID  */  
   THBranchID:string,
      /**  ParamCode  */  
   ParamCode:string,
      /**  AGAFIPResponsibilityCode  */  
   AGAFIPResponsibilityCode:string,
      /**  AGGrossIncomeTaxID  */  
   AGGrossIncomeTaxID:string,
      /**  AGIDDocumentTypeCode  */  
   AGIDDocumentTypeCode:string,
      /**  AGProvinceCode  */  
   AGProvinceCode:string,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  AGApartment  */  
   AGApartment:string,
      /**  AGExtraStreetNumber  */  
   AGExtraStreetNumber:string,
      /**  AGFloor  */  
   AGFloor:string,
      /**  AGLocationCode  */  
   AGLocationCode:string,
      /**  AGNeighborhood  */  
   AGNeighborhood:string,
      /**  AGStreet  */  
   AGStreet:string,
      /**  AGStreetNumber  */  
   AGStreetNumber:string,
      /**  Colombia Loc Field. OneTimeCustVend new table ID  */  
   COOneTimeID:string,
      /**  No Banking Reference  */  
   NoBankingReference:boolean,
      /**  Peru Goods Contributor withholding status.  */  
   PEGoodsContributor:boolean,
      /**  Indicates the status of Peru Withholding Agent  */  
   PEWithholdAgent:boolean,
      /**  Indicates the status of Peru Collection Agent  */  
   PECollectionAgent:boolean,
      /**  Peru Not Found withholding status.  */  
   PENotFound:boolean,
      /**  Peru No Address Provided withholding status.  */  
   PENoAddress:boolean,
      /**  Displays the Peru Identity Document Type.  */  
   PEIdentityDocType:string,
      /**  Colombia Loc Field.  */  
   COIsOneTimeVend:boolean,
      /**  Peru Document ID.  */  
   PEDocumentID:string,
      /**  Defines the Number of Days from the PO release date the schedule engine considers a late PO Release or discard it. If the PO release date plus the supplier due date horizon is before today then the PO Release is discarded. If the PO release date plus the supplier due date horizon is today or later then the PO Release is considered late.  */  
   MaxLateDaysPORel:number,
      /**  1099 Code  */  
   Code1099ID:string,
      /**  Taxpayer Identification Number  */  
   TIN:string,
      /**  TIN Type. Values are 1 for EIN, 2 for SSNs, ITINs, and ATINs and 0 if type of TIN is not terminable.  */  
   TINType:string,
      /**  Second TIN Notice  */  
   SecondTINNotice:boolean,
      /**  Name Control. Optional and used for electronic export.  */  
   NameControl:string,
      /**  Specifies the method of shipment. The Ship Via associated with this supplier appears by default, but you can select a different option from the list.  */  
   ShipViaCode:string,
      /**  Non US Supplier  */  
   NonUS:boolean,
      /**  Form Type ID for the 1099 Code  */  
   FormTypeID:string,
      /**  INSupplierType  */  
   INSupplierType:string,
      /**  INCSTNumber  */  
   INCSTNumber:string,
      /**  INPANNumber  */  
   INPANNumber:string,
      /**  DEOrgType  */  
   DEOrgType:string,
      /**  PaymentReporting  */  
   PaymentReporting:boolean,
      /**  This field indicates that this record should be sent over to an external system whenever it is changed/created/deleted, etc.  */  
   ExternalPurchasing:boolean,
      /**  MXRetentionCode  */  
   MXRetentionCode:string,
      /**  Recipient's name for US 1099 reporting  */  
   Reporting1099Name:string,
      /**  Reporting1099Name2  */  
   Reporting1099Name2:string,
      /**  FATCA  */  
   FATCA:boolean,
      /**  AccountNum  */  
   AccountNum:string,
      /**  TW GUI Code  */  
   TWGUIRegNum:string,
      /**  MXTARCode  */  
   MXTARCode:string,
      /**  PEAddressID  */  
   PEAddressID:string,
      /**  PERetentionRegime  */  
   PERetentionRegime:string,
      /**  TaxEntityType  */  
   TaxEntityType:string,
      /**  GST Compliance Rate for India  */  
   INGSTComplianceRate:number,
      /**  INTaxRegistrationID  */  
   INTaxRegistrationID:string,
      /**  Validation Status of Taxpayer Identification Number  */  
   TINValidationStatus:number,
      /**  Indicates whether this supplier is importer of records or not. Used for Avalara Tax Connect calculation.  */  
   ImporterOfRecord:boolean,
      /**  PLAutomaticAPInvoiceNum  */  
   PLAutomaticAPInvoiceNum:boolean,
      /**  Standard Entry Class Code  */  
   SEC:string,
      /**  CSF Mexico DIOT Transaction Type  */  
   MXDIOTTranType:string,
      /**  Form 1099-K Merchant Category Code  */  
   US1099KMerchCatCode:string,
      /**  CSF Mexico Taxpayer Type  */  
   MXTaxpayerType:string,
      /**  CSF Mexico Legal Representative RFC  */  
   MXLegalRepRFC:string,
      /**  CSF Mexico Legal Representative CURP  */  
   MXLegalRepCURP:string,
      /**  CSF Mexico Legal Representative Name  */  
   MXLegalRepName:string,
      /**  CSF Mexico Legal Representative Taxpayer Type  */  
   MXLegalRepTaxpayerType:string,
      /**  US 1099 State  */  
   US1099State:string,
      /**  Tax ID Validation Status: Not Validated – 0, Valid – 1, Invalid – 2.  */  
   TaxValidationStatus:number,
      /**  Tax Validation Date  */  
   TaxValidationDate:string,
      /**  HMRCTaxValidationLog  */  
   HMRCTaxValidationLog:string,
      /**  Supplier Scheme ID  */  
   ExternalSchemeID:string,
      /**  Municipio Code  */  
   MXMunicipio:string,
      /**  EInvoice  */  
   EInvoice:boolean,
      /**  Flag used to mark a Supplier as EDI.  */  
   EDISupplier:boolean,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  Delimited list of Business Categories  */  
   BusinessCatList:string,
      /**  List of fields which are referenced by COA segments.  */  
   COASegReferences:string,
   CountryDescription:string,
      /**  Currency Description.  */  
   CurrDesc:string,
   DocumentMaskID:string,
   EnableGlobalLock:boolean,
   EnableGlobalVendor:boolean,
   EnableMultiCompany:boolean,
      /**  Indicates if Reverse Charge Method should be enabled.  */  
   EnableRevCharge:boolean,
   FOBDescription:string,
      /**  Indicates if the Vendor is a global vendor (either master or child)  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany and GlbVendorNum that is linking to this vendor  */  
   GlbLink:string,
   Integrationflag:boolean,
      /**  A user defined external Netting Customer ID.  This must be existing Customer ID within the file  */  
   NettingCustID:string,
      /**  A user defined external Netting Customer Number.  This must be existing Customer Number within the file  */  
   NettingCustNum:number,
      /**  Reverse Charge Method description  */  
   RevChargeMethodDesc:string,
      /**  Sales Tax ID  */  
   SalesTaxID:string,
      /**  Automated Bank reconciliation.  */  
   SearchIDs:string,
      /**  Service Tax ID  */  
   ServiceTaxID:string,
   ShipViaDescription:string,
      /**  Delimited string of vendor attributes  */  
   VendAttrString:string,
   LangNameIDDescription:string,
      /**  Area of ISTMO de Tehuantepec (Polos de Desarrollo). Value is from MXLocISTMO User Code.  */  
   MXISTMO:string,
   BitFlag:number,
   AGAFIPResponsibilityDescription:string,
   AGIDDocTypeDescription:string,
   AGLocationDescription:string,
   AGProvinceCodeDescription:string,
   CalendarIDDescription:string,
   Code1099Description:string,
   CountryNumEUMember:boolean,
   CountryNumISOCode:string,
   CountryNumDescription:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrDesc:string,
   DeliveryTypeDescription:string,
   FormTypeDescription:string,
   GroupCodeGroupDesc:string,
   PayMethodType:number,
   PayMethodName:string,
   PayMethodSummarizePerCustomer:boolean,
   PurPointAddress3:string,
   PurPointAddress1:string,
   PurPointPrimPCon:number,
   PurPointName:string,
   PurPointZip:string,
   PurPointCountry:string,
   PurPointCity:string,
   PurPointState:string,
   PurPointAddress2:string,
   TaxAuthCdTaxAuthorityDescription:string,
   TaxRegionCodeDescription:string,
   TermsCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   Week1Pymt_c:number,
   Week2Pymt_c:number,
}

export interface Erp_Tablesets_VendorTableset{
   Vendor:Erp_Tablesets_VendorRow[],
   VendorAttch:Erp_Tablesets_VendorAttchRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   TaxExempt:Erp_Tablesets_TaxExemptRow[],
   Partner:Erp_Tablesets_PartnerRow[],
   PEVendWhldHist:Erp_Tablesets_PEVendWhldHistRow[],
   VendRestriction:Erp_Tablesets_VendRestrictionRow[],
   VendBank:Erp_Tablesets_VendBankRow[],
   VendBankAttch:Erp_Tablesets_VendBankAttchRow[],
   VendCntMain:Erp_Tablesets_VendCntMainRow[],
   VenMFBill:Erp_Tablesets_VenMFBillRow[],
   VendorPP:Erp_Tablesets_VendorPPRow[],
   VenPPMFBill:Erp_Tablesets_VenPPMFBillRow[],
   VenPPUPSEmail:Erp_Tablesets_VenPPUPSEmailRow[],
   VendPPRestriction:Erp_Tablesets_VendPPRestrictionRow[],
   VendCnt:Erp_Tablesets_VendCntRow[],
   VendCntAttch:Erp_Tablesets_VendCntAttchRow[],
   VenUPSEmail:Erp_Tablesets_VenUPSEmailRow[],
   VendRemitTo:Erp_Tablesets_VendRemitToRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetAddrElementList_output{
parameters : {
      /**  output parameters  */  
   addrElementList:string,
}
}

   /** Required : 
      @param vendorNum
   */  
export interface GetByID_input{
   vendorNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_VendorTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_VendorTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_VendorTableset[],
}

   /** Required : 
      @param vendorID
   */  
export interface GetByVendID_input{
      /**  Vendor ID  */  
   vendorID:string,
}

export interface GetByVendID_output{
   returnObj:Erp_Tablesets_VendorTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  Table to search  */  
   tableName:string,
      /**  Field to search  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface GetDefaultFormType_input{
   ds:Erp_Tablesets_VendorTableset[],
}

export interface GetDefaultFormType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param glbVendorNumList
   */  
export interface GetGlbVendorList_input{
      /**  Delimited list of GlbVendorNum values  */  
   glbVendorNumList:string,
}

export interface GetGlbVendorList_output{
   returnObj:Erp_Tablesets_GlbVendorTableset[],
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
   returnObj:Erp_Tablesets_VendorListTableset[],
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
export interface GetNettingSupplierList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetNettingSupplierList_output{
   returnObj:Erp_Tablesets_VendorListTableset[],
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
   ds:Erp_Tablesets_VendorTableset[],
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
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param partnerNum
      @param partnerType
      @param partnerID
   */  
export interface GetNewPartner_input{
   ds:Erp_Tablesets_VendorTableset[],
   partnerNum:number,
   partnerType:number,
   partnerID:string,
}

export interface GetNewPartner_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param taxCode
      @param rateCode
   */  
export interface GetNewTaxExempt_input{
   ds:Erp_Tablesets_VendorTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   taxCode:string,
   rateCode:string,
}

export interface GetNewTaxExempt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewVenMFBill_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
}

export interface GetNewVenMFBill_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
   */  
export interface GetNewVenPPMFBill_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
   purPoint:string,
}

export interface GetNewVenPPMFBill_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
   */  
export interface GetNewVenPPUPSEmail_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
   purPoint:string,
}

export interface GetNewVenPPUPSEmail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewVenUPSEmail_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
}

export interface GetNewVenUPSEmail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param bankID
   */  
export interface GetNewVendBankAttch_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
   bankID:string,
}

export interface GetNewVendBankAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewVendBank_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
}

export interface GetNewVendBank_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param conNum
   */  
export interface GetNewVendCntAttch_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
   purPoint:string,
   conNum:number,
}

export interface GetNewVendCntAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
   */  
export interface GetNewVendCntMain_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
   purPoint:string,
}

export interface GetNewVendCntMain_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
   */  
export interface GetNewVendCnt_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
   purPoint:string,
}

export interface GetNewVendCnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
   */  
export interface GetNewVendPPRestriction_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
   purPoint:string,
}

export interface GetNewVendPPRestriction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewVendRemitTo_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
}

export interface GetNewVendRemitTo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewVendRestriction_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
}

export interface GetNewVendRestriction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewVendorAttch_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
}

export interface GetNewVendorAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewVendorPP_input{
   ds:Erp_Tablesets_VendorTableset[],
   vendorNum:number,
}

export interface GetNewVendorPP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewVendor_input{
   ds:Erp_Tablesets_VendorTableset[],
}

export interface GetNewVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param targetTable
      @param perConID
      @param ds
   */  
export interface GetPerConData_input{
      /**  The table to fill with the PerCon data.
            Use empty string to fill all contact tables.  */  
   targetTable:string,
      /**  Person Contact ID  */  
   perConID:number,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface GetPerConData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param whereClauseVendor
      @param whereClauseVendorAttch
      @param whereClauseEntityGLC
      @param whereClauseTaxExempt
      @param whereClausePartner
      @param whereClausePEVendWhldHist
      @param whereClauseVendRestriction
      @param whereClauseVendBank
      @param whereClauseVendBankAttch
      @param whereClauseVendCntMain
      @param whereClauseVenMFBill
      @param whereClauseVendorPP
      @param whereClauseVenPPMFBill
      @param whereClauseVenPPUPSEmail
      @param whereClauseVendPPRestriction
      @param whereClauseVendCnt
      @param whereClauseVendCntAttch
      @param whereClauseVenUPSEmail
      @param whereClauseVendRemitTo
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseVendor:string,
   whereClauseVendorAttch:string,
   whereClauseEntityGLC:string,
   whereClauseTaxExempt:string,
   whereClausePartner:string,
   whereClausePEVendWhldHist:string,
   whereClauseVendRestriction:string,
   whereClauseVendBank:string,
   whereClauseVendBankAttch:string,
   whereClauseVendCntMain:string,
   whereClauseVenMFBill:string,
   whereClauseVendorPP:string,
   whereClauseVenPPMFBill:string,
   whereClauseVenPPUPSEmail:string,
   whereClauseVendPPRestriction:string,
   whereClauseVendCnt:string,
   whereClauseVendCntAttch:string,
   whereClauseVenUPSEmail:string,
   whereClauseVendRemitTo:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_VendorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param VendorNum
      @param PurPoint
      @param ConNum
   */  
export interface GetVendCntGlobalFieldsWithPrimaryContact_input{
      /**  Vendor Number  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  Contact Number  */  
   ConNum:number,
}

export interface GetVendCntGlobalFieldsWithPrimaryContact_output{
   returnObj:string,
}

   /** Required : 
      @param vendorID
   */  
export interface GetVendorForLink_input{
      /**  LinkVendorID field on the GlbVendor record to link  */  
   vendorID:string,
}

export interface GetVendorForLink_output{
   returnObj:Erp_Tablesets_VendorTableset[],
}

   /** Required : 
      @param VendorNum
      @param GlobalLock
   */  
export interface GetVendorGlobalFieldsWithoutGlobalLock_input{
      /**  Vendor Number  */  
   VendorNum:number,
      /**  If vendor is locked from receiving global updates  */  
   GlobalLock:boolean,
}

export interface GetVendorGlobalFieldsWithoutGlobalLock_output{
   returnObj:string,
}

   /** Required : 
      @param whereClause
      @param groupID
      @param vendorID
      @param vendorNums
      @param pageSize
      @param absolutePage
   */  
export interface GetVendorListRemmitance_input{
      /**  whereClause  */  
   whereClause:string,
      /**  ID of the group that contains the vendor looking for.  */  
   groupID:string,
      /**  specific VendorID to search  */  
   vendorID:string,
      /**  optional parameter to indicates a separate string of vendorNums, only used if vendorID is empty  */  
   vendorNums:string,
      /**  Maximum number of rows to return. Leave as zero for no maximum  */  
   pageSize:number,
      /**  Page of rows to return  */  
   absolutePage:number,
}

export interface GetVendorListRemmitance_output{
   returnObj:Erp_Tablesets_VendorListTableset[],
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
export interface GetVendorListSorted_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetVendorListSorted_output{
   returnObj:Erp_Tablesets_VendorListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param vendorID
      @param purPoint
   */  
export interface GetVendorPPForLink_input{
      /**  vendorID field on the GlbVendor record  */  
   vendorID:string,
      /**  LinkPurPoint field on the GlbVendorPP record  */  
   purPoint:string,
}

export interface GetVendorPPForLink_output{
   returnObj:Erp_Tablesets_VendorTableset[],
}

   /** Required : 
      @param VendorNum
      @param PurPoint
   */  
export interface GetVendorPPGlobalFieldsWithPrimaryPP_input{
      /**  Vendor Number  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
}

export interface GetVendorPPGlobalFieldsWithPrimaryPP_output{
   returnObj:string,
}

   /** Required : 
      @param VendorNum
      @param PurPoint
      @param ConNum
   */  
export interface GetvendCntGlobalFields_input{
      /**  Vendor Number  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  Contact Number  */  
   ConNum:number,
}

export interface GetvendCntGlobalFields_output{
   returnObj:string,
}

   /** Required : 
      @param VendorNum
      @param GlobalLock
   */  
export interface GetvendorGlobalFields_input{
      /**  Vendor Number  */  
   VendorNum:number,
      /**  If vendor is locked from receiving global updates  */  
   GlobalLock:boolean,
}

export interface GetvendorGlobalFields_output{
   returnObj:string,
}

   /** Required : 
      @param VendorNum
      @param PurPoint
   */  
export interface GetvendorPPGlobalFields_input{
      /**  Vendor Number  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
}

export interface GetvendorPPGlobalFields_output{
   returnObj:string,
}

export interface GlbVendorsExist_output{
parameters : {
      /**  output parameters  */  
   glbVendorsExist:boolean,
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
      @param glbCompany
      @param glbVendorNum
      @param glbPurPoint
      @param glbConNum
      @param ds
   */  
export interface LinkGlbVendCnt_input{
      /**  Global Company field on the GlbVendorPP record to link  */  
   glbCompany:string,
      /**  Global VendorNum field on the GlbVendCnt record to link  */  
   glbVendorNum:number,
      /**  Global PurPoint field on the GlbVendCnt record to link  */  
   glbPurPoint:string,
      /**  Global Contact Number field on the GlbVendCnt record to link  */  
   glbConNum:number,
   ds:Erp_Tablesets_GlbVendorTableset[],
}

export interface LinkGlbVendCnt_output{
   returnObj:Erp_Tablesets_VendorTableset[],
}

   /** Required : 
      @param glbCompany
      @param glbVendorNum
      @param glbPurPoint
      @param ds
      @param ds1
   */  
export interface LinkGlbVendorPP_input{
      /**  Global Company field on the GlbVendorPP record to link  */  
   glbCompany:string,
      /**  Global VendorNum field on the GlbVendorPP record to link  */  
   glbVendorNum:number,
      /**  Global PurPoint field on the GlbVendorPP record to link  */  
   glbPurPoint:string,
   ds:Erp_Tablesets_GlbVendorTableset[],
   ds1:Erp_Tablesets_VendorTableset[],
}

export interface LinkGlbVendorPP_output{
parameters : {
      /**  output parameters  */  
   ds1:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbVendorNum
      @param ds
      @param ds1
   */  
export interface LinkGlbVendor_input{
      /**  Global Company field on the GlbVendor record to link  */  
   glbCompany:string,
      /**  Global VendorNum field on the GlbVendor record to link  */  
   glbVendorNum:number,
   ds:Erp_Tablesets_GlbVendorTableset[],
   ds1:Erp_Tablesets_VendorTableset[],
}

export interface LinkGlbVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorTableset,
   ds1:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ModifySearchIDs_input{
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ModifySearchIDs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ipFormType
      @param code1099ID
      @param ds
   */  
export interface OnChangeCode1099_input{
      /**  1099 Form Type  */  
   ipFormType:string,
      /**  1099 Code ID  */  
   code1099ID:string,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface OnChangeCode1099_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ipFormType
      @param ds
   */  
export interface OnChangeFormType_input{
      /**  1099 Form Type  */  
   ipFormType:string,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface OnChangeFormType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbVendorNum
      @param glbPurPoint
      @param ds
   */  
export interface PreLinkGlbVendorPP_input{
      /**  Global Company field on the GlbVendorPP record to link  */  
   glbCompany:string,
      /**  Global VendorNum field on the GlbVendorPP record to link  */  
   glbVendorNum:number,
      /**  Global PurPoint field on the GlbVendorPP record to link  */  
   glbPurPoint:string,
   ds:Erp_Tablesets_GlbVendorTableset[],
}

export interface PreLinkGlbVendorPP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorTableset,
   vMessage:string,
   askQuestion:boolean,
}
}

   /** Required : 
      @param glbCompany
      @param glbVendorNum
      @param ds
   */  
export interface PreLinkGlbVendor_input{
      /**  Global Company field on the GlbVendor record to link  */  
   glbCompany:string,
      /**  Global VendorNum field on the GlbVendor record to link  */  
   glbVendorNum:number,
   ds:Erp_Tablesets_GlbVendorTableset[],
}

export interface PreLinkGlbVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorTableset,
   vMessage:string,
   askQuestion:boolean,
}
}

   /** Required : 
      @param glbCompany
      @param glbVendorNum
      @param glbPurPoint
      @param glbConNum
      @param ds
   */  
export interface RefreshGlbVendCnt_input{
      /**  Global Company  */  
   glbCompany:string,
      /**  Global vendor number  */  
   glbVendorNum:number,
      /**  Global purchase point  */  
   glbPurPoint:string,
      /**  Global contact number  */  
   glbConNum:number,
   ds:Erp_Tablesets_GlbVendorTableset[],
}

export interface RefreshGlbVendCnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbVendorNum
      @param glbPurPoint
      @param ds
   */  
export interface RefreshGlbVendorPP_input{
      /**  Global Company  */  
   glbCompany:string,
      /**  Global Vendor Number  */  
   glbVendorNum:number,
      /**  Global purchase point  */  
   glbPurPoint:string,
   ds:Erp_Tablesets_GlbVendorTableset[],
}

export interface RefreshGlbVendorPP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbVendorNum
      @param ds
   */  
export interface RefreshGlbVendor_input{
      /**  Global company  */  
   glbCompany:string,
      /**  Global Vendor Number  */  
   glbVendorNum:number,
   ds:Erp_Tablesets_GlbVendorTableset[],
}

export interface RefreshGlbVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ResetPPIntl_input{
   ds:Erp_Tablesets_VendorTableset[],
}

export interface ResetPPIntl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ipQVEnable
      @param ipUpdVenUPS
      @param ipUPDVenPPUPS
      @param ds
   */  
export interface SetUPSQVEnable_input{
   ipQVEnable:boolean,
   ipUpdVenUPS:boolean,
   ipUPDVenPPUPS:boolean,
   ds:Erp_Tablesets_VendorTableset[],
}

export interface SetUPSQVEnable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbVendorNum
      @param glbPurPoint
      @param ds
   */  
export interface SkipGlbVendCnt_input{
      /**  Global Company  */  
   glbCompany:string,
      /**  Global Vendor Number  */  
   glbVendorNum:number,
      /**  Global Purchase Point  */  
   glbPurPoint:string,
   ds:Erp_Tablesets_GlbVendorTableset[],
}

export interface SkipGlbVendCnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbVendorNum
      @param ds
   */  
export interface SkipGlbVendorPP_input{
      /**  Global Company  */  
   glbCompany:string,
      /**  Global Vendor Number  */  
   glbVendorNum:number,
   ds:Erp_Tablesets_GlbVendorTableset[],
}

export interface SkipGlbVendorPP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbVendorNum
      @param ds
   */  
export interface SkipGlbVendor_input{
      /**  Global Company field on the GlbVendor record to skip  */  
   glbCompany:string,
      /**  Global VendorNum field on the GlbVendor record to skip  */  
   glbVendorNum:number,
   ds:Erp_Tablesets_GlbVendorTableset[],
}

export interface SkipGlbVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorTableset,
}
}

   /** Required : 
      @param glbLink
      @param ds
   */  
export interface SkipSingleGlbVendCnt_input{
      /**  Delimited list of global values containing global company, supplier number, purchase point, and contact num  */  
   glbLink:string,
   ds:Erp_Tablesets_GlbVendorTableset[],
}

export interface SkipSingleGlbVendCnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorTableset,
}
}

   /** Required : 
      @param glbLink
      @param ds
   */  
export interface SkipSingleGlbVendorPP_input{
      /**  Delimited list of global values containing global company, supplier number, and purchase point  */  
   glbLink:string,
   ds:Erp_Tablesets_GlbVendorTableset[],
}

export interface SkipSingleGlbVendorPP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorTableset,
}
}

   /** Required : 
      @param ipPartnerNum
      @param ipSearchID
   */  
export interface StorePartner_input{
      /**  Partner Num  */  
   ipPartnerNum:number,
      /**  Search ID  */  
   ipSearchID:string,
}

export interface StorePartner_output{
      /**  boolean  */  
   returnObj:boolean,
}

   /** Required : 
      @param vendorNum
      @param TIN
      @param TINType
   */  
export interface TypeTINVendor_input{
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Taxpayer identification Number  */  
   TIN:string,
      /**  TIN Type  */  
   TINType:string,
}

export interface TypeTINVendor_output{
   returnObj:boolean,
}

   /** Required : 
      @param glbCompany
      @param glbVendorNum
      @param ds
   */  
export interface UnlinkGlbVendor_input{
      /**  Global Company field on the GlbVendor record to unlink  */  
   glbCompany:string,
      /**  Global VendorNum field on the GlbVendor record to unlink  */  
   glbVendorNum:number,
   ds:Erp_Tablesets_GlbVendorTableset[],
}

export interface UnlinkGlbVendor_output{
   returnObj:Erp_Tablesets_VendorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtVendorTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtVendorTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_VendorTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
}
}

   /** Required : 
      @param ipPayBTFlag
      @param ipValVen
      @param ipValVenPP
      @param ipVendorNum
      @param ipPurPoint
   */  
export interface ValidatePayBTFlag_input{
   ipPayBTFlag:string,
   ipValVen:boolean,
   ipValVenPP:boolean,
   ipVendorNum:number,
   ipPurPoint:string,
}

export interface ValidatePayBTFlag_output{
}

   /** Required : 
      @param ds
      @param manualValidation
      @param hmrcFraudPrevHeader
   */  
export interface ValidateTaxID_input{
   ds:Erp_Tablesets_VendorTableset[],
   manualValidation:boolean,
   hmrcFraudPrevHeader:string,
}

export interface ValidateTaxID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorTableset,
   opMessage:string,
}
}

   /** Required : 
      @param vendorNum
   */  
export interface VendorBankExists_input{
      /**  Vendor Number  */  
   vendorNum:number,
}

export interface VendorBankExists_output{
parameters : {
      /**  output parameters  */  
   vendBankExists:boolean,
}
}

   /** Required : 
      @param vendorID
   */  
export interface getPrimaryBankID_input{
      /**  Vendor ID  */  
   vendorID:string,
}

export interface getPrimaryBankID_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   bankID:string,
}
}

