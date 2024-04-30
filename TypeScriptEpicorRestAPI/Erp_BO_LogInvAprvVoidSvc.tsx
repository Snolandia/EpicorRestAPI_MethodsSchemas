import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.LogInvAprvVoidSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get LogInvAprvVoids items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LogInvAprvVoids
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogAPInvRow
   */  
export function get_LogInvAprvVoids(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LogInvAprvVoids
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LogAPInvRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LogAPInvRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LogInvAprvVoids(requestBody:Erp_Tablesets_LogAPInvRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LogInvAprvVoid item
   Description: Calls GetByID to retrieve the LogInvAprvVoid item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LogInvAprvVoid
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LogAPInvRow
   */  
export function get_LogInvAprvVoids_Company_VendorNum_InvoiceNum(Company:string, VendorNum:string, InvoiceNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LogAPInvRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LogAPInvRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LogInvAprvVoid for the service
   Description: Calls UpdateExt to update LogInvAprvVoid. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LogInvAprvVoid
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LogAPInvRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LogInvAprvVoids_Company_VendorNum_InvoiceNum(Company:string, VendorNum:string, InvoiceNum:string, requestBody:Erp_Tablesets_LogAPInvRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")", {
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
   Summary: Call UpdateExt to delete LogInvAprvVoid item
   Description: Call UpdateExt to delete LogInvAprvVoid item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LogInvAprvVoid
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LogInvAprvVoids_Company_VendorNum_InvoiceNum(Company:string, VendorNum:string, InvoiceNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")", {
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
   Description: Get LogAPInvTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LogAPInvTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogAPInvTaxRow
   */  
export function get_LogInvAprvVoids_Company_VendorNum_InvoiceNum_LogAPInvTaxes(Company:string, VendorNum:string, InvoiceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")/LogAPInvTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LogAPInvTax item
   Description: Calls GetByID to retrieve the LogAPInvTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LogAPInvTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param Void Desc: Void   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LogAPInvTaxRow
   */  
export function get_LogInvAprvVoids_Company_VendorNum_InvoiceNum_LogAPInvTaxes_Company_VendorNum_InvoiceNum_TaxCode_RateCode_ECAcquisitionSeq_Void(Company:string, VendorNum:string, InvoiceNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, Void:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LogAPInvTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")/LogAPInvTaxes(" + Company + "," + VendorNum + "," + InvoiceNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + "," + Void + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LogAPInvTaxRow)
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
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
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
export function get_LogInvAprvVoids_Company_VendorNum_InvoiceNum_EntityGLCs(Company:string, VendorNum:string, InvoiceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
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
export function get_LogInvAprvVoids_Company_VendorNum_InvoiceNum_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, VendorNum:string, InvoiceNum:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get LogAPInvAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LogAPInvAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogAPInvAttchRow
   */  
export function get_LogInvAprvVoids_Company_VendorNum_InvoiceNum_LogAPInvAttches(Company:string, VendorNum:string, InvoiceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")/LogAPInvAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LogAPInvAttch item
   Description: Calls GetByID to retrieve the LogAPInvAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LogAPInvAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LogAPInvAttchRow
   */  
export function get_LogInvAprvVoids_Company_VendorNum_InvoiceNum_LogAPInvAttches_Company_VendorNum_InvoiceNum_DrawingSeq(Company:string, VendorNum:string, InvoiceNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LogAPInvAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")/LogAPInvAttches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LogAPInvAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LogAPInvTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LogAPInvTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogAPInvTaxRow
   */  
export function get_LogAPInvTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LogAPInvTaxes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LogAPInvTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LogAPInvTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LogAPInvTaxes(requestBody:Erp_Tablesets_LogAPInvTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LogAPInvTax item
   Description: Calls GetByID to retrieve the LogAPInvTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LogAPInvTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param Void Desc: Void   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LogAPInvTaxRow
   */  
export function get_LogAPInvTaxes_Company_VendorNum_InvoiceNum_TaxCode_RateCode_ECAcquisitionSeq_Void(Company:string, VendorNum:string, InvoiceNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, Void:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LogAPInvTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvTaxes(" + Company + "," + VendorNum + "," + InvoiceNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + "," + Void + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LogAPInvTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LogAPInvTax for the service
   Description: Calls UpdateExt to update LogAPInvTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LogAPInvTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param Void Desc: Void   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LogAPInvTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LogAPInvTaxes_Company_VendorNum_InvoiceNum_TaxCode_RateCode_ECAcquisitionSeq_Void(Company:string, VendorNum:string, InvoiceNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, Void:string, requestBody:Erp_Tablesets_LogAPInvTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvTaxes(" + Company + "," + VendorNum + "," + InvoiceNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + "," + Void + ")", {
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
   Summary: Call UpdateExt to delete LogAPInvTax item
   Description: Call UpdateExt to delete LogAPInvTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LogAPInvTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param Void Desc: Void   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LogAPInvTaxes_Company_VendorNum_InvoiceNum_TaxCode_RateCode_ECAcquisitionSeq_Void(Company:string, VendorNum:string, InvoiceNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, Void:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvTaxes(" + Company + "," + VendorNum + "," + InvoiceNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + "," + Void + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/EntityGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get LogAPInvAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LogAPInvAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogAPInvAttchRow
   */  
export function get_LogAPInvAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LogAPInvAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LogAPInvAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LogAPInvAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LogAPInvAttches(requestBody:Erp_Tablesets_LogAPInvAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LogAPInvAttch item
   Description: Calls GetByID to retrieve the LogAPInvAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LogAPInvAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LogAPInvAttchRow
   */  
export function get_LogAPInvAttches_Company_VendorNum_InvoiceNum_DrawingSeq(Company:string, VendorNum:string, InvoiceNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LogAPInvAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvAttches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LogAPInvAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LogAPInvAttch for the service
   Description: Calls UpdateExt to update LogAPInvAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LogAPInvAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LogAPInvAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LogAPInvAttches_Company_VendorNum_InvoiceNum_DrawingSeq(Company:string, VendorNum:string, InvoiceNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_LogAPInvAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvAttches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete LogAPInvAttch item
   Description: Call UpdateExt to delete LogAPInvAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LogAPInvAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LogAPInvAttches_Company_VendorNum_InvoiceNum_DrawingSeq(Company:string, VendorNum:string, InvoiceNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvAttches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + DrawingSeq + ")", {
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
   Description: Get LegalNumberGenerates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumberGenerates
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumberGenerateRow
   */  
export function get_LegalNumberGenerates(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumberGenerateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LegalNumberGenerates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumberGenerateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumberGenerates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumberGenerates(requestBody:Erp_Tablesets_LegalNumberGenerateRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LegalNumberGenerates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LegalNumberGenerate item
   Description: Calls GetByID to retrieve the LegalNumberGenerate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumberGenerate
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
   */  
export function get_LegalNumberGenerates_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumberGenerateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LegalNumberGenerates(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumberGenerateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumberGenerate for the service
   Description: Calls UpdateExt to update LegalNumberGenerate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumberGenerate
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumberGenerates_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_LegalNumberGenerateRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LegalNumberGenerates(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete LegalNumberGenerate item
   Description: Call UpdateExt to delete LegalNumberGenerate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumberGenerate
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumberGenerates_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LegalNumberGenerates(" + SysRowID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogAPInvListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseLogAPInv:string, whereClauseLogAPInvAttch:string, whereClauseLogAPInvTax:string, whereClauseEntityGLC:string, whereClauseLegalNumberGenerate:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseLogAPInv!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLogAPInv=" + whereClauseLogAPInv
   }
   if(typeof whereClauseLogAPInvAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLogAPInvAttch=" + whereClauseLogAPInvAttch
   }
   if(typeof whereClauseLogAPInvTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLogAPInvTax=" + whereClauseLogAPInvTax
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
   if(typeof whereClauseLegalNumberGenerate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumberGenerate=" + whereClauseLegalNumberGenerate
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(vendorNum:string, invoiceNum:string, epicorHeaders?:Headers){
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
   if(typeof invoiceNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "invoiceNum=" + invoiceNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method CanUserVoid
   Description: Purpose:
Parameters:
<param name="ipInvoiceNum">Invoice Number user wants to void</param><param name="ipVendorNum">Vendor assigned to ipInvoiceNum</param><param name="opCanVoid"> indicates if the user can void the logged invoice</param><param name="opMessage">text indicating why a user cannot void</param>
Notes:
   OperationID: CanUserVoid
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CanUserVoid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanUserVoid_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CanUserVoid(requestBody:CanUserVoid_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CanUserVoid_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/CanUserVoid", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CanUserVoid_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeApproved
   Description: Method to call when changing the approved flag on the invoice.
   OperationID: ChangeApproved
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeApproved(requestBody:ChangeApproved_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeApproved_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/ChangeApproved", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeApproved_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/CheckDocumentIsLocked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method VoidLoggedInvoice
   Description: Purpose:
Parameters:
<param name="ds">The Logged Invoice Approval/Void data set</param>
Notes:
   OperationID: VoidLoggedInvoice
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VoidLoggedInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLoggedInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidLoggedInvoice(requestBody:VoidLoggedInvoice_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VoidLoggedInvoice_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/VoidLoggedInvoice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as VoidLoggedInvoice_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalcTaxes
   OperationID: CalcTaxes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalcTaxes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcTaxes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcTaxes(requestBody:CalcTaxes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalcTaxes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/CalcTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CalcTaxes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLogAPInv
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLogAPInv
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLogAPInv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLogAPInv_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLogAPInv(requestBody:GetNewLogAPInv_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLogAPInv_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/GetNewLogAPInv", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLogAPInv_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLogAPInvAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLogAPInvAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLogAPInvAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLogAPInvAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLogAPInvAttch(requestBody:GetNewLogAPInvAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLogAPInvAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/GetNewLogAPInvAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLogAPInvAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLogAPInvTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLogAPInvTax
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLogAPInvTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLogAPInvTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLogAPInvTax(requestBody:GetNewLogAPInvTax_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLogAPInvTax_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/GetNewLogAPInvTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLogAPInvTax_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/GetNewEntityGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewLegalNumberGenerate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLegalNumberGenerate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLegalNumberGenerate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLegalNumberGenerate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLegalNumberGenerate(requestBody:GetNewLegalNumberGenerate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLegalNumberGenerate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/GetNewLegalNumberGenerate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLegalNumberGenerate_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumberGenerateRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumberGenerateRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LogAPInvAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LogAPInvListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LogAPInvRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LogAPInvTaxRow,
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

export interface Erp_Tablesets_LegalNumberGenerateRow{
      /**  Company Identifier.  */  
   "Company":string,
   "NumberType":string,
   "NumberYear":number,
      /**  The legal number prefix  */  
   "NumberPrefix":string,
   "NumberSuffix":string,
   "PrefixList":string,
   "GenerationType":string,
   "EnableNumberPrefix":boolean,
   "EnableNumberSuffix":boolean,
   "NumberOption":string,
      /**  Unique identifier of the Legal Number record  */  
   "LegalNumberNum":number,
   "DocumentDate":string,
   "AdditionalParams":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LogAPInvAttchRow{
   "Company":string,
   "VendorNum":number,
   "InvoiceNum":string,
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

export interface Erp_Tablesets_LogAPInvListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "InvoiceNum":string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   "DebitMemo":boolean,
      /**  Yes indicates all necessary approvals have been received.  No indicates approvals are pending.  */  
   "Approved":boolean,
      /**  Date the Logged Invoice was approved.  */  
   "ApprovedDate":string,
      /**  Yes indicates this logged invoice has been matched to an AP Invoice.  No indicates it has not been matched.  */  
   "Matched":boolean,
      /**  Date the logged invoice was matched to an AP Invoice.  */  
   "MatchedDate":string,
      /**  Indicates whether or not this logged invoice has been posted to the GL.  */  
   "Posted":boolean,
      /**  Invoice date.  */  
   "InvoiceDate":string,
      /**  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   "TermsCode":string,
      /**  Indicates if this logged invoice has been voided.  */  
   "Void":boolean,
      /**  User ID that voided the invoice. This is not maintainable by the user.  */  
   "VoidedBy":string,
      /**  Text that explains why the logged invoice was voided.  */  
   "VoidReason":string,
      /**  Date the Logged Invoice was voided.  */  
   "VoidDate":string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   "TaxAmt":number,
      /**  Total sales tax amount for this invoice. Totals the DocTaxAmt from the LogAPInvTax records of this invoice.  */  
   "DocTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   "DueDate":string,
      /**  Apply Date  */  
   "ApplyDate":string,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  */  
   "Description":string,
      /**  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  */  
   "REFPONum":number,
      /**  For use by external G/L interfacing.  This field is sign flipped for debit memos.  */  
   "InvoiceVendorAmt":number,
      /**  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  */  
   "DocInvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceVendorAmt":number,
      /**  Total invoice Amount.   This field has a true sign. (debit memos are negative).  */  
   "InvoiceAmt":number,
      /**  Total invoice Amount.(Vendors Currency) This field has a true sign. (debit memos are negative).  */  
   "DocInvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceAmt":number,
      /**  The Tax Region for this invoice.  */  
   "TaxRegionCode":string,
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   "EntryPerson":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**   Reserved for future development.
Indicates if the approval process is required.  If yes, an approval code is not required and the invoice is automatically approved.  If no, an approval code is required.  */  
   "AutoApproved":boolean,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  */  
   "FiscalPeriod":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "DocRounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Reserved for Future Development.  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  */  
   "DiscountDate":string,
      /**  Reserved for Future development. Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   "DiscountAmt":number,
      /**  Reserved for future development. Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   "DocDiscountAmt":number,
      /**   Reserved for future development. This field is maintainable/viewable only for Debit Memos. It represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.
For Invoices it is equal to the InvoiceNum.
For Debit memos where they are not related to an invoice it is also set equal to the Debit memo's InvoiceNum. In this later case when InvcHead.DebitMemo = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   "InvoiceRef":string,
      /**  User ID that authorized the invoice. This is not maintainable by the user.  */  
   "AuthorizedBy":string,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscountAmt":number,
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
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   "InvExpense":number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   "DocInvExpense":number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   "Rpt1InvExpense":number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   "Rpt2InvExpense":number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   "Rpt3InvExpense":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations.  */  
   "ReadyToCalc":boolean,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Tax Rate Group Code  */  
   "TaxRateGrpCode":string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   "LockTaxRate":boolean,
      /**  Sweden and Finland Localization Field - Banking Reference  */  
   "SEBankRef":string,
      /**  Sweden and Finland Localization Field - Payment Code  */  
   "SEPayCode":string,
      /**  Sweden and Finland Localization field, Payment Method code  */  
   "SEPMUID":number,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Legal Number for the voiding.  */  
   "VoidLegalNumber":string,
      /**  Transaction Document Type for the voiding.  */  
   "VoidTranDocTypeID":string,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**   Denmark Localization
Card (payment) code  */  
   "CardCode":string,
      /**   Denmark Localization
Account Number  */  
   "BankGiroAcctNbr":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  TranType  */  
   "TranType":string,
      /**  PLInvoiceReference  */  
   "PLInvoiceReference":string,
   "ScrInvVendorAmt":number,
      /**  When the APInvHed record is created from this logged invoice and the APInvHed record is posted, this flag is set to true.  This is used by the UI.  */  
   "MatchInvoicePosted":boolean,
   "ScrTotDedTaxAmt":number,
   "ScrDocTotSelfAmt":number,
   "CurrencySwitch":boolean,
   "Rpt3ScrTotSelfAmt":number,
   "EnableExchangeRate":boolean,
   "EnableLockRate":boolean,
   "XRateLabel":string,
      /**  Indicates if the vendor is active  */  
   "VendorInactive":boolean,
   "ScrTaxAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt1ScrInvVendorAmt":number,
   "Rpt2ScrInvVendorAmt":number,
   "Rpt3ScrInvVendorAmt":number,
   "Rpt1ScrInvoiceAmt":number,
   "Rpt2ScrInvoiceAmt":number,
   "Rpt3ScrInvoiceAmt":number,
   "ScrInvoiceAmt":number,
   "ScrDocTaxAmt":number,
   "ScrDocInvVendorAmt":number,
   "ScrDocInvoiceAmt":number,
   "ScrTotTaxableAmt":number,
   "ScrDocTotTaxableAmt":number,
   "Rpt1ScrTotTaxableAmt":number,
   "Rpt2ScrTotTaxableAmt":number,
   "Rpt3ScrTotTaxableAmt":number,
   "ScrTotReportableAmt":number,
   "ScrDocTotReportableAmt":number,
   "Rpt1ScrTotReportableAmt":number,
   "Rpt2ScrTotReportableAmt":number,
   "Rpt3ScrTotReportableAmt":number,
   "ScrDocTotDedTaxAmt":number,
   "Rpt1ScrTotDedTaxAmt":number,
   "Rpt2ScrTotDedTaxAmt":number,
   "Rpt3ScrTotDedTaxAmt":number,
   "ScrTotWithholdingAmt":number,
   "ScrDocTotWithholdingAmt":number,
   "Rpt1ScrTotWithholdingAmt":number,
   "Rpt2ScrTotWithholdingAmt":number,
   "Rpt3ScrTotWithholdingAmt":number,
   "ScrTotSelfAmt":number,
   "Rpt1ScrTotSelfAmt":number,
   "Rpt2ScrTotSelfAmt":number,
   "ScrDocRounding":number,
   "Rpt2ScrRounding":number,
   "Rpt3ScrRounding":number,
   "BaseCurrSymbol":string,
   "CurrSymbol":string,
   "TaxLinesExist":boolean,
   "EnableDueDate":boolean,
   "InvoiceVariance":number,
   "Rpt1InvoiceVariance":number,
   "Rpt2InvoiceVariance":number,
   "Rpt3InvoiceVariance":number,
   "BillAddressList":string,
   "ScrRounding":number,
   "DocInvoiceVariance":number,
   "Rpt1ScrRounding":number,
   "TotalInvAmt":number,
   "ScrDiscountAmt":number,
   "ScrDocDiscountAmt":number,
   "ScrInvoiceRef":string,
   "ScrTotInvoiceAmt":number,
   "ScrDocTotInvoiceAmt":number,
   "LegalNumberMessage":string,
      /**  Intended for internal use  */  
   "AuthAdmins":string,
      /**  Intended for Internal Use  */  
   "AuthAdminNames":string,
      /**  Logical indicating whether or not the Logged Invoice Tracker is to enable the GL Transaction Tb  */  
   "EnableTaxesInTracker":boolean,
   "Rpt1ScrDocInvoiceAmt":number,
   "Rpt2ScrDocInvoiceAmt":number,
   "Rpt3ScrDocInvoiceAmt":number,
      /**  Not intended for external use.  Logical indicating that a default entity was created for the new logged invoice.  */  
   "UpdateEntity":boolean,
   "Rpt2ScrTotInvoiceAmt":number,
   "Rpt3ScrTotInvoiceAmt":number,
   "Rpt1ScrTotInvoiceAmt":number,
      /**  Not intended for external use.  Indicates if the user has Void authority.  */  
   "IsEligibleToVoid":boolean,
   "ScrInvExpense":number,
   "ScrDocInvExpense":number,
   "Rpt2ScrInvExpense":number,
   "Rpt3ScrInvExpense":number,
   "Rpt1ScrInvExpense":number,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "BaseCurrencyID":string,
      /**  This field is used when invoice is transferred form one Group to another and the user has a cance to change this invoice Apply Date.  */  
   "TransApplyDate":string,
      /**  Document Invoice Vendor Amout only for dispaly  */  
   "DocDspInvVendorAmt":number,
      /**  DspInvVendorAmt  */  
   "DspInvVendorAmt":number,
      /**  Invoice Vendor Amout only for dispaly in report currency  */  
   "Rpt1DspInvVendorAmt":number,
      /**  Invoice Vendor Amout only for dispaly in report currency  */  
   "Rpt2DspInvVendorAmt":number,
      /**  Invoice Vendor Amout only for dispaly in report currency  */  
   "Rpt3DspInvVendorAmt":number,
   "EnableTaxLock":boolean,
   "UseTaxRate":boolean,
   "TaxExchangeRate":number,
   "EnableTaxExRate":boolean,
   "TaxRateLinesExist":boolean,
      /**  Pay Method Type  */  
   "PayMethod":string,
      /**  Vendor Bank  */  
   "VendorBank":string,
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
      /**  Description  */  
   "RateGrpCodeDescription":string,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   "SEPayMethodType":number,
      /**  Name of the payment method  */  
   "SEPayMethodName":string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   "SEPayMethodSummarizePerCustomer":boolean,
      /**  Description  */  
   "TaxRateGrpDescription":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionCodeDescription":string,
      /**  Full description of terms....this is printed on purchase orders. Can't be blank.  */  
   "TermsCodeDescription":string,
      /**  User Name  */  
   "UserfileName":string,
      /**  Swift number of the bank.  */  
   "VendBankSwiftNum":string,
      /**  IBAN Code of the Supplier Bank  */  
   "VendBankIBANCode":string,
      /**   Denmark Localization          
Account Number  */  
   "VendBankBankGiroAcctNbr":string,
      /**  Local BIC of the Supplier Bank  */  
   "VendBankLocalBIC":string,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   "VendBankBankAcctNumber":string,
      /**  Supplier Bank Name  */  
   "VendBankBankName":string,
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
      /**  User Name  */  
   "VoidedByName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LogAPInvRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "InvoiceNum":string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   "DebitMemo":boolean,
      /**  Yes indicates all necessary approvals have been received.  No indicates approvals are pending.  */  
   "Approved":boolean,
      /**  Date the Logged Invoice was approved.  */  
   "ApprovedDate":string,
      /**  Yes indicates this logged invoice has been matched to an AP Invoice.  No indicates it has not been matched.  */  
   "Matched":boolean,
      /**  Date the logged invoice was matched to an AP Invoice.  */  
   "MatchedDate":string,
      /**  Indicates whether or not this logged invoice has been posted to the GL.  */  
   "Posted":boolean,
      /**  Invoice date.  */  
   "InvoiceDate":string,
      /**  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   "TermsCode":string,
      /**  Indicates if this logged invoice has been voided.  */  
   "Void":boolean,
      /**  User ID that voided the invoice. This is not maintainable by the user.  */  
   "VoidedBy":string,
      /**  Text that explains why the logged invoice was voided.  */  
   "VoidReason":string,
      /**  Date the Logged Invoice was voided.  */  
   "VoidDate":string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   "TaxAmt":number,
      /**  Total sales tax amount for this invoice. Totals the DocTaxAmt from the LogAPInvTax records of this invoice.  */  
   "DocTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   "DueDate":string,
      /**  Apply Date  */  
   "ApplyDate":string,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  */  
   "Description":string,
      /**  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  */  
   "REFPONum":number,
      /**  For use by external G/L interfacing.  This field is sign flipped for debit memos.  */  
   "InvoiceVendorAmt":number,
      /**  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  */  
   "DocInvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceVendorAmt":number,
      /**  Total invoice Amount.   This field has a true sign. (debit memos are negative).  */  
   "InvoiceAmt":number,
      /**  Total invoice Amount.(Vendors Currency) This field has a true sign. (debit memos are negative).  */  
   "DocInvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceAmt":number,
      /**  The Tax Region for this invoice.  */  
   "TaxRegionCode":string,
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   "EntryPerson":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**   Reserved for future development.
Indicates if the approval process is required.  If yes, an approval code is not required and the invoice is automatically approved.  If no, an approval code is required.  */  
   "AutoApproved":boolean,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  */  
   "FiscalPeriod":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "DocRounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Reserved for Future Development.  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  */  
   "DiscountDate":string,
      /**  Reserved for Future development. Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   "DiscountAmt":number,
      /**  Reserved for future development. Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   "DocDiscountAmt":number,
      /**   Reserved for future development. This field is maintainable/viewable only for Debit Memos. It represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.
For Invoices it is equal to the InvoiceNum.
For Debit memos where they are not related to an invoice it is also set equal to the Debit memo's InvoiceNum. In this later case when InvcHead.DebitMemo = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   "InvoiceRef":string,
      /**  User ID that authorized the invoice. This is not maintainable by the user.  */  
   "AuthorizedBy":string,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscountAmt":number,
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
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   "InvExpense":number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   "DocInvExpense":number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   "Rpt1InvExpense":number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   "Rpt2InvExpense":number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   "Rpt3InvExpense":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations.  */  
   "ReadyToCalc":boolean,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Tax Rate Group Code  */  
   "TaxRateGrpCode":string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   "LockTaxRate":boolean,
      /**  Sweden and Finland Localization Field - Banking Reference  */  
   "SEBankRef":string,
      /**  Sweden and Finland Localization Field - Payment Code  */  
   "SEPayCode":string,
      /**  Sweden and Finland Localization field, Payment Method code  */  
   "SEPMUID":number,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Legal Number for the voiding.  */  
   "VoidLegalNumber":string,
      /**  Transaction Document Type for the voiding.  */  
   "VoidTranDocTypeID":string,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**   Denmark Localization
Card (payment) code  */  
   "CardCode":string,
      /**   Denmark Localization
Account Number  */  
   "BankGiroAcctNbr":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CHISRCodeLine  */  
   "CHISRCodeLine":string,
      /**  CustomsNumber  */  
   "CustomsNumber":string,
      /**  ReceivedDate  */  
   "ReceivedDate":string,
      /**  TranType  */  
   "TranType":string,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  PLInvoiceReference  */  
   "PLInvoiceReference":string,
      /**  VoidDescription  */  
   "VoidDescription":string,
      /**  APTaxRoundOption  */  
   "APTaxRoundOption":number,
      /**  Intended for Internal Use  */  
   "AuthAdminNames":string,
      /**  Intended for internal use  */  
   "AuthAdmins":string,
   "BankName":string,
   "BaseCurrencyID":string,
   "BaseCurrSymbol":string,
   "BillAddressList":string,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
      /**  Document Invoice Vendor Amout only for dispaly  */  
   "DocDspInvVendorAmt":number,
   "DocInvoiceVariance":number,
      /**  DspInvVendorAmt  */  
   "DspInvVendorAmt":number,
   "EnableAssignLegNum":boolean,
   "EnableDueDate":boolean,
   "EnableExchangeRate":boolean,
   "EnableLockRate":boolean,
      /**  Logical indicating whether or not the Logged Invoice Tracker is to enable the GL Transaction Tb  */  
   "EnableTaxesInTracker":boolean,
   "EnableTaxExRate":boolean,
   "EnableTaxLock":boolean,
      /**  Enable setting of Transaction Document Type  */  
   "EnableTranDocType":boolean,
   "EnableVoidLegNum":boolean,
   "HasLegNumCnfg":boolean,
   "InvoiceVariance":number,
   "IsDiscountforDebitM":boolean,
      /**  Not intended for external use.  Indicates if the user has Void authority.  */  
   "IsEligibleToVoid":boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumberMessage":string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  When the APInvHed record is created from this logged invoice and the APInvHed record is posted, this flag is set to true.  This is used by the UI.  */  
   "MatchInvoicePosted":boolean,
      /**  Pay Method Type  */  
   "PayMethod":string,
      /**  CSF Poland. Vendor uses Invoice reference number  */  
   "PLVendorAutoInvoiceNum":boolean,
      /**  Invoice Vendor Amout only for dispaly in report currency  */  
   "Rpt1DspInvVendorAmt":number,
   "Rpt1InvoiceVariance":number,
   "Rpt1ScrDocInvoiceAmt":number,
   "Rpt1ScrInvExpense":number,
   "Rpt1ScrInvoiceAmt":number,
   "Rpt1ScrInvVendorAmt":number,
   "Rpt1ScrRounding":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTotDedTaxAmt":number,
   "Rpt1ScrTotInvoiceAmt":number,
   "Rpt1ScrTotReportableAmt":number,
   "Rpt1ScrTotSelfAmt":number,
   "Rpt1ScrTotTaxableAmt":number,
   "Rpt1ScrTotWithholdingAmt":number,
      /**  Invoice Vendor Amout only for dispaly in report currency  */  
   "Rpt2DspInvVendorAmt":number,
   "Rpt2InvoiceVariance":number,
   "Rpt2ScrDocInvoiceAmt":number,
   "Rpt2ScrInvExpense":number,
   "Rpt2ScrInvoiceAmt":number,
   "Rpt2ScrInvVendorAmt":number,
   "Rpt2ScrRounding":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTotDedTaxAmt":number,
   "Rpt2ScrTotInvoiceAmt":number,
   "Rpt2ScrTotReportableAmt":number,
   "Rpt2ScrTotSelfAmt":number,
   "Rpt2ScrTotTaxableAmt":number,
   "Rpt2ScrTotWithholdingAmt":number,
      /**  Invoice Vendor Amout only for dispaly in report currency  */  
   "Rpt3DspInvVendorAmt":number,
   "Rpt3InvoiceVariance":number,
   "Rpt3ScrDocInvoiceAmt":number,
   "Rpt3ScrInvExpense":number,
   "Rpt3ScrInvoiceAmt":number,
   "Rpt3ScrInvVendorAmt":number,
   "Rpt3ScrRounding":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTotDedTaxAmt":number,
   "Rpt3ScrTotInvoiceAmt":number,
   "Rpt3ScrTotReportableAmt":number,
   "Rpt3ScrTotSelfAmt":number,
   "Rpt3ScrTotTaxableAmt":number,
   "Rpt3ScrTotWithholdingAmt":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "ScrDiscountAmt":number,
   "ScrDocDiscountAmt":number,
   "ScrDocInvExpense":number,
   "ScrDocInvoiceAmt":number,
   "ScrDocInvVendorAmt":number,
   "ScrDocRounding":number,
   "ScrDocTaxAmt":number,
   "ScrDocTotDedTaxAmt":number,
   "ScrDocTotInvoiceAmt":number,
   "ScrDocTotReportableAmt":number,
   "ScrDocTotSelfAmt":number,
   "ScrDocTotTaxableAmt":number,
   "ScrDocTotWithholdingAmt":number,
   "ScrInvExpense":number,
   "ScrInvoiceAmt":number,
   "ScrInvoiceRef":string,
   "ScrInvVendorAmt":number,
   "ScrRounding":number,
   "ScrTaxAmt":number,
   "ScrTotDedTaxAmt":number,
   "ScrTotInvoiceAmt":number,
   "ScrTotReportableAmt":number,
   "ScrTotSelfAmt":number,
   "ScrTotTaxableAmt":number,
   "ScrTotWithholdingAmt":number,
      /**  System Transaction Type: APInvoice/DebitMemo is used in the filter of TranDocType combo box.  */  
   "SystemTranType":string,
   "TaxExchangeRate":number,
   "TaxLinesExist":boolean,
   "TaxRateLinesExist":boolean,
   "TotalInvAmt":number,
      /**  Link to TranDocType table, can be removed when path field TranDocTypeID is replaced with actual one.  */  
   "TranDocTypeDescription":string,
      /**  This field is used when invoice is transferred form one Group to another and the user has a cance to change this invoice Apply Date.  */  
   "TransApplyDate":string,
      /**  Not intended for external use.  Logical indicating that a default entity was created for the new logged invoice.  */  
   "UpdateEntity":boolean,
   "UseTaxRate":boolean,
      /**  Vendor Bank  */  
   "VendorBank":string,
      /**  Indicates if the vendor is active  */  
   "VendorInactive":boolean,
   "XRateLabel":string,
   "AllowChgAfterPrint":boolean,
      /**  Formatted Supplier Name and Address  */  
   "FormattedVendorNameAddress":string,
      /**  The flag t to indicate if Tax records created per Tax Liability assigned toLogged Invoiceare adjusted, deleted,  or any tax records were added by the user  */  
   "ManualTaxAdj":boolean,
      /**  Supplier Full Address. External field uses the Supplier Address1, Address2, Address3, City,State, zip  and  Country from the supplier catalog  */  
   "VendorNumFullAddress":string,
   "BitFlag":number,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrencyID":string,
   "PurPointName":string,
   "PurPointPrimPCon":number,
   "PurPointAddress1":string,
   "PurPointState":string,
   "PurPointAddress2":string,
   "PurPointAddress3":string,
   "PurPointZip":string,
   "PurPointCountry":string,
   "PurPointCity":string,
   "RateGrpCodeDescription":string,
   "SEPayMethodName":string,
   "SEPayMethodType":number,
   "SEPayMethodSummarizePerCustomer":boolean,
   "TaxRateGrpDescription":string,
   "TaxRegionCodeDescription":string,
   "TermsCodeDescription":string,
   "UserfileName":string,
   "VendBankSwiftNum":string,
   "VendBankBankName":string,
   "VendBankBankGiroAcctNbr":string,
   "VendBankIBANCode":string,
   "VendBankBankAcctNumber":string,
   "VendBankPMUID":number,
   "VendBankCardCode":string,
   "VendBankLocalBIC":string,
   "VendorNumCountry":string,
   "VendorNumName":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress1":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress2":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress3":string,
   "VendorNumVendorID":string,
   "VendorNumCity":string,
   "VendorNumState":string,
   "VendorNumZIP":string,
   "VoidedByName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LogAPInvTaxRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "InvoiceNum":string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  */  
   "ECAcquisitionSeq":number,
      /**  Rate Code  */  
   "RateCode":string,
      /**  Indicates if this logged invoice has been voided.  */  
   "Void":boolean,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   "DocTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**   Sales Tax amount for the corresponding taxable sales amount.
Manually entered if APInvTax.Manual = Yes.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   "DocTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   "DocReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  System calculated Taxable amount for this invoice.  */  
   "SysCalcTaxableAmt":number,
      /**  System calculated Taxable amount for this invoice in foreign currency.  */  
   "SysCalcDocTaxableAmt":number,
      /**  System calculated Taxable amount for this invoice.  */  
   "Rpt1SysCalcTaxableAmt":number,
      /**  System calculated Taxable amount for this invoice.  */  
   "Rpt2SysCalcTaxableAmt":number,
      /**  System calculated Taxable amount for this invoice.  */  
   "Rpt3SysCalcTaxableAmt":number,
      /**  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  */  
   "SysCalcReportableAmt":number,
      /**  System calculated reportable sales amount to the tax jurisdiction expressed in the Vendor's currency.  */  
   "SysCalcDocReportableAmt":number,
      /**  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  */  
   "Rpt1SysCalcReportableAmt":number,
      /**  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  */  
   "Rpt2SysCalcReportableAmt":number,
      /**  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  */  
   "Rpt3SysCalcReportableAmt":number,
      /**  Collection Type  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution number  */  
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
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MovementNum  */  
   "MovementNum":number,
   "BaseCurrSymbol":string,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
   "DebitMemo":boolean,
      /**  Collection Type Description  */  
   "DescCollectionType":string,
   "EnableSuperGRate":boolean,
   "GroupID":string,
   "Posted":boolean,
   "RateType":number,
   "Rpt1ScrDedTaxAmt":number,
      /**  Display field for Fixed Amount in Report Currency 1.  */  
   "Rpt1ScrFixedAmount":number,
   "Rpt1ScrReportableAmt":number,
   "Rpt1ScrTaxableAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTaxAmtVar":number,
   "Rpt2ScrDedTaxAmt":number,
      /**  Display field for Fixed Amount in Report Currency 2.  */  
   "Rpt2ScrFixedAmount":number,
   "Rpt2ScrReportableAm":number,
   "Rpt2ScrReportableAmt":number,
   "Rpt2ScrTaxableAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTaxAmtVar":number,
   "Rpt3ScrDedTaxAmt":number,
      /**  Display field for Fixed Amount in Report Currency 31.  */  
   "Rpt3ScrFixedAmount":number,
   "Rpt3ScrReportableAmt":number,
   "Rpt3ScrTaxableAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTaxAmtVar":number,
   "ScrDedTaxAmt":number,
   "ScrDocDedTaxAmt":number,
      /**  Display field for Fixed amount in document currency  */  
   "ScrDocFixedAmount":number,
   "ScrDocReportableAmt":number,
   "ScrDocTaxableAmt":number,
   "ScrDocTaxAmt":number,
   "ScrDocTaxAmtVar":number,
      /**  Display field for Fixed Amount  */  
   "ScrFixedAmount":number,
   "ScrReportableAmt":number,
   "ScrTaxableAmt":number,
   "ScrTaxAmt":number,
   "ScrTaxAmtVar":number,
      /**  Flag to indicate if Manual field on tax record should be disabled  */  
   "DisableManual":boolean,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
   "VendorNumCountry":string,
   "VendorNumZIP":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress2":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress1":string,
   "VendorNumName":string,
   "VendorNumTermsCode":string,
   "VendorNumState":string,
   "VendorNumAddress3":string,
   "VendorNumVendorID":string,
   "VendorNumCity":string,
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
      @param ipQuoteNum
      @param ipOrderNum
      @param ipInvoiceNum
      @param ipAPInvKey
      @param ipCashHeadNum
      @param ipPayHeadNum
      @param ipShipPackNum
      @param ipEmpID
      @param ipEmpExpenseNum
   */  
export interface CalcTaxes_input{
   ipQuoteNum:number,
   ipOrderNum:number,
   ipInvoiceNum:number,
   ipAPInvKey:string,
   ipCashHeadNum:string,
   ipPayHeadNum:number,
   ipShipPackNum:number,
   ipEmpID:string,
   ipEmpExpenseNum:number,
}

export interface CalcTaxes_output{
parameters : {
      /**  output parameters  */  
   opCommFailure:boolean,
   opMessage:string,
   opTCStatus:boolean,
}
}

   /** Required : 
      @param ipInvoiceNum
      @param ipVendorNum
   */  
export interface CanUserVoid_input{
   ipInvoiceNum:string,
   ipVendorNum:number,
}

export interface CanUserVoid_output{
parameters : {
      /**  output parameters  */  
   opCanVoid:boolean,
   opMessage:string,
}
}

   /** Required : 
      @param proposedApproved
      @param confirmCheck
      @param ds
   */  
export interface ChangeApproved_input{
      /**  The proposed approval flag value  */  
   proposedApproved:boolean,
      /**  Confirm Check  */  
   confirmCheck:boolean,
   ds:Erp_Tablesets_LogInvAprvVoidTableset[],
}

export interface ChangeApproved_output{
parameters : {
      /**  output parameters  */  
   confirmMsg:string,
   ds:Erp_Tablesets_LogInvAprvVoidTableset,
}
}

   /** Required : 
      @param keyValue
      @param keyValue2
   */  
export interface CheckDocumentIsLocked_input{
      /**  VendorNum  */  
   keyValue:string,
      /**  InvoiceNum  */  
   keyValue2:string,
}

export interface CheckDocumentIsLocked_output{
}

   /** Required : 
      @param vendorNum
      @param invoiceNum
   */  
export interface DeleteByID_input{
   vendorNum:number,
   invoiceNum:string,
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

export interface Erp_Tablesets_LegalNumberGenerateRow{
      /**  Company Identifier.  */  
   Company:string,
   NumberType:string,
   NumberYear:number,
      /**  The legal number prefix  */  
   NumberPrefix:string,
   NumberSuffix:string,
   PrefixList:string,
   GenerationType:string,
   EnableNumberPrefix:boolean,
   EnableNumberSuffix:boolean,
   NumberOption:string,
      /**  Unique identifier of the Legal Number record  */  
   LegalNumberNum:number,
   DocumentDate:string,
   AdditionalParams:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LogAPInvAttchRow{
   Company:string,
   VendorNum:number,
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

export interface Erp_Tablesets_LogAPInvListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   InvoiceNum:string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   DebitMemo:boolean,
      /**  Yes indicates all necessary approvals have been received.  No indicates approvals are pending.  */  
   Approved:boolean,
      /**  Date the Logged Invoice was approved.  */  
   ApprovedDate:string,
      /**  Yes indicates this logged invoice has been matched to an AP Invoice.  No indicates it has not been matched.  */  
   Matched:boolean,
      /**  Date the logged invoice was matched to an AP Invoice.  */  
   MatchedDate:string,
      /**  Indicates whether or not this logged invoice has been posted to the GL.  */  
   Posted:boolean,
      /**  Invoice date.  */  
   InvoiceDate:string,
      /**  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Indicates if this logged invoice has been voided.  */  
   Void:boolean,
      /**  User ID that voided the invoice. This is not maintainable by the user.  */  
   VoidedBy:string,
      /**  Text that explains why the logged invoice was voided.  */  
   VoidReason:string,
      /**  Date the Logged Invoice was voided.  */  
   VoidDate:string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   TaxAmt:number,
      /**  Total sales tax amount for this invoice. Totals the DocTaxAmt from the LogAPInvTax records of this invoice.  */  
   DocTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Apply Date  */  
   ApplyDate:string,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  */  
   Description:string,
      /**  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  */  
   REFPONum:number,
      /**  For use by external G/L interfacing.  This field is sign flipped for debit memos.  */  
   InvoiceVendorAmt:number,
      /**  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  */  
   DocInvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceVendorAmt:number,
      /**  Total invoice Amount.   This field has a true sign. (debit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount.(Vendors Currency) This field has a true sign. (debit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceAmt:number,
      /**  The Tax Region for this invoice.  */  
   TaxRegionCode:string,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**   Reserved for future development.
Indicates if the approval process is required.  If yes, an approval code is not required and the invoice is automatically approved.  If no, an approval code is required.  */  
   AutoApproved:boolean,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  */  
   FiscalPeriod:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reserved for Future Development.  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  */  
   DiscountDate:string,
      /**  Reserved for Future development. Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   DiscountAmt:number,
      /**  Reserved for future development. Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   DocDiscountAmt:number,
      /**   Reserved for future development. This field is maintainable/viewable only for Debit Memos. It represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.
For Invoices it is equal to the InvoiceNum.
For Debit memos where they are not related to an invoice it is also set equal to the Debit memo's InvoiceNum. In this later case when InvcHead.DebitMemo = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   InvoiceRef:string,
      /**  User ID that authorized the invoice. This is not maintainable by the user.  */  
   AuthorizedBy:string,
      /**  Reporting currency value of this field  */  
   Rpt1DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscountAmt:number,
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
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   InvExpense:number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   DocInvExpense:number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   Rpt1InvExpense:number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   Rpt2InvExpense:number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   Rpt3InvExpense:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations.  */  
   ReadyToCalc:boolean,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden and Finland Localization Field - Banking Reference  */  
   SEBankRef:string,
      /**  Sweden and Finland Localization Field - Payment Code  */  
   SEPayCode:string,
      /**  Sweden and Finland Localization field, Payment Method code  */  
   SEPMUID:number,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Legal Number for the voiding.  */  
   VoidLegalNumber:string,
      /**  Transaction Document Type for the voiding.  */  
   VoidTranDocTypeID:string,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**   Denmark Localization
Card (payment) code  */  
   CardCode:string,
      /**   Denmark Localization
Account Number  */  
   BankGiroAcctNbr:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  TranType  */  
   TranType:string,
      /**  PLInvoiceReference  */  
   PLInvoiceReference:string,
   ScrInvVendorAmt:number,
      /**  When the APInvHed record is created from this logged invoice and the APInvHed record is posted, this flag is set to true.  This is used by the UI.  */  
   MatchInvoicePosted:boolean,
   ScrTotDedTaxAmt:number,
   ScrDocTotSelfAmt:number,
   CurrencySwitch:boolean,
   Rpt3ScrTotSelfAmt:number,
   EnableExchangeRate:boolean,
   EnableLockRate:boolean,
   XRateLabel:string,
      /**  Indicates if the vendor is active  */  
   VendorInactive:boolean,
   ScrTaxAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt1ScrInvVendorAmt:number,
   Rpt2ScrInvVendorAmt:number,
   Rpt3ScrInvVendorAmt:number,
   Rpt1ScrInvoiceAmt:number,
   Rpt2ScrInvoiceAmt:number,
   Rpt3ScrInvoiceAmt:number,
   ScrInvoiceAmt:number,
   ScrDocTaxAmt:number,
   ScrDocInvVendorAmt:number,
   ScrDocInvoiceAmt:number,
   ScrTotTaxableAmt:number,
   ScrDocTotTaxableAmt:number,
   Rpt1ScrTotTaxableAmt:number,
   Rpt2ScrTotTaxableAmt:number,
   Rpt3ScrTotTaxableAmt:number,
   ScrTotReportableAmt:number,
   ScrDocTotReportableAmt:number,
   Rpt1ScrTotReportableAmt:number,
   Rpt2ScrTotReportableAmt:number,
   Rpt3ScrTotReportableAmt:number,
   ScrDocTotDedTaxAmt:number,
   Rpt1ScrTotDedTaxAmt:number,
   Rpt2ScrTotDedTaxAmt:number,
   Rpt3ScrTotDedTaxAmt:number,
   ScrTotWithholdingAmt:number,
   ScrDocTotWithholdingAmt:number,
   Rpt1ScrTotWithholdingAmt:number,
   Rpt2ScrTotWithholdingAmt:number,
   Rpt3ScrTotWithholdingAmt:number,
   ScrTotSelfAmt:number,
   Rpt1ScrTotSelfAmt:number,
   Rpt2ScrTotSelfAmt:number,
   ScrDocRounding:number,
   Rpt2ScrRounding:number,
   Rpt3ScrRounding:number,
   BaseCurrSymbol:string,
   CurrSymbol:string,
   TaxLinesExist:boolean,
   EnableDueDate:boolean,
   InvoiceVariance:number,
   Rpt1InvoiceVariance:number,
   Rpt2InvoiceVariance:number,
   Rpt3InvoiceVariance:number,
   BillAddressList:string,
   ScrRounding:number,
   DocInvoiceVariance:number,
   Rpt1ScrRounding:number,
   TotalInvAmt:number,
   ScrDiscountAmt:number,
   ScrDocDiscountAmt:number,
   ScrInvoiceRef:string,
   ScrTotInvoiceAmt:number,
   ScrDocTotInvoiceAmt:number,
   LegalNumberMessage:string,
      /**  Intended for internal use  */  
   AuthAdmins:string,
      /**  Intended for Internal Use  */  
   AuthAdminNames:string,
      /**  Logical indicating whether or not the Logged Invoice Tracker is to enable the GL Transaction Tb  */  
   EnableTaxesInTracker:boolean,
   Rpt1ScrDocInvoiceAmt:number,
   Rpt2ScrDocInvoiceAmt:number,
   Rpt3ScrDocInvoiceAmt:number,
      /**  Not intended for external use.  Logical indicating that a default entity was created for the new logged invoice.  */  
   UpdateEntity:boolean,
   Rpt2ScrTotInvoiceAmt:number,
   Rpt3ScrTotInvoiceAmt:number,
   Rpt1ScrTotInvoiceAmt:number,
      /**  Not intended for external use.  Indicates if the user has Void authority.  */  
   IsEligibleToVoid:boolean,
   ScrInvExpense:number,
   ScrDocInvExpense:number,
   Rpt2ScrInvExpense:number,
   Rpt3ScrInvExpense:number,
   Rpt1ScrInvExpense:number,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   BaseCurrencyID:string,
      /**  This field is used when invoice is transferred form one Group to another and the user has a cance to change this invoice Apply Date.  */  
   TransApplyDate:string,
      /**  Document Invoice Vendor Amout only for dispaly  */  
   DocDspInvVendorAmt:number,
      /**  DspInvVendorAmt  */  
   DspInvVendorAmt:number,
      /**  Invoice Vendor Amout only for dispaly in report currency  */  
   Rpt1DspInvVendorAmt:number,
      /**  Invoice Vendor Amout only for dispaly in report currency  */  
   Rpt2DspInvVendorAmt:number,
      /**  Invoice Vendor Amout only for dispaly in report currency  */  
   Rpt3DspInvVendorAmt:number,
   EnableTaxLock:boolean,
   UseTaxRate:boolean,
   TaxExchangeRate:number,
   EnableTaxExRate:boolean,
   TaxRateLinesExist:boolean,
      /**  Pay Method Type  */  
   PayMethod:string,
      /**  Vendor Bank  */  
   VendorBank:string,
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
      /**  Description  */  
   RateGrpCodeDescription:string,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   SEPayMethodType:number,
      /**  Name of the payment method  */  
   SEPayMethodName:string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   SEPayMethodSummarizePerCustomer:boolean,
      /**  Description  */  
   TaxRateGrpDescription:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionCodeDescription:string,
      /**  Full description of terms....this is printed on purchase orders. Can't be blank.  */  
   TermsCodeDescription:string,
      /**  User Name  */  
   UserfileName:string,
      /**  Swift number of the bank.  */  
   VendBankSwiftNum:string,
      /**  IBAN Code of the Supplier Bank  */  
   VendBankIBANCode:string,
      /**   Denmark Localization          
Account Number  */  
   VendBankBankGiroAcctNbr:string,
      /**  Local BIC of the Supplier Bank  */  
   VendBankLocalBIC:string,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   VendBankBankAcctNumber:string,
      /**  Supplier Bank Name  */  
   VendBankBankName:string,
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
      /**  User Name  */  
   VoidedByName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LogAPInvListTableset{
   LogAPInvList:Erp_Tablesets_LogAPInvListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LogAPInvRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   InvoiceNum:string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   DebitMemo:boolean,
      /**  Yes indicates all necessary approvals have been received.  No indicates approvals are pending.  */  
   Approved:boolean,
      /**  Date the Logged Invoice was approved.  */  
   ApprovedDate:string,
      /**  Yes indicates this logged invoice has been matched to an AP Invoice.  No indicates it has not been matched.  */  
   Matched:boolean,
      /**  Date the logged invoice was matched to an AP Invoice.  */  
   MatchedDate:string,
      /**  Indicates whether or not this logged invoice has been posted to the GL.  */  
   Posted:boolean,
      /**  Invoice date.  */  
   InvoiceDate:string,
      /**  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Indicates if this logged invoice has been voided.  */  
   Void:boolean,
      /**  User ID that voided the invoice. This is not maintainable by the user.  */  
   VoidedBy:string,
      /**  Text that explains why the logged invoice was voided.  */  
   VoidReason:string,
      /**  Date the Logged Invoice was voided.  */  
   VoidDate:string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   TaxAmt:number,
      /**  Total sales tax amount for this invoice. Totals the DocTaxAmt from the LogAPInvTax records of this invoice.  */  
   DocTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Apply Date  */  
   ApplyDate:string,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  */  
   Description:string,
      /**  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  */  
   REFPONum:number,
      /**  For use by external G/L interfacing.  This field is sign flipped for debit memos.  */  
   InvoiceVendorAmt:number,
      /**  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  */  
   DocInvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceVendorAmt:number,
      /**  Total invoice Amount.   This field has a true sign. (debit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount.(Vendors Currency) This field has a true sign. (debit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceAmt:number,
      /**  The Tax Region for this invoice.  */  
   TaxRegionCode:string,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**   Reserved for future development.
Indicates if the approval process is required.  If yes, an approval code is not required and the invoice is automatically approved.  If no, an approval code is required.  */  
   AutoApproved:boolean,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  */  
   FiscalPeriod:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reserved for Future Development.  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  */  
   DiscountDate:string,
      /**  Reserved for Future development. Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   DiscountAmt:number,
      /**  Reserved for future development. Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   DocDiscountAmt:number,
      /**   Reserved for future development. This field is maintainable/viewable only for Debit Memos. It represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.
For Invoices it is equal to the InvoiceNum.
For Debit memos where they are not related to an invoice it is also set equal to the Debit memo's InvoiceNum. In this later case when InvcHead.DebitMemo = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   InvoiceRef:string,
      /**  User ID that authorized the invoice. This is not maintainable by the user.  */  
   AuthorizedBy:string,
      /**  Reporting currency value of this field  */  
   Rpt1DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscountAmt:number,
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
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   InvExpense:number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   DocInvExpense:number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   Rpt1InvExpense:number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   Rpt2InvExpense:number,
      /**  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  */  
   Rpt3InvExpense:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations.  */  
   ReadyToCalc:boolean,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden and Finland Localization Field - Banking Reference  */  
   SEBankRef:string,
      /**  Sweden and Finland Localization Field - Payment Code  */  
   SEPayCode:string,
      /**  Sweden and Finland Localization field, Payment Method code  */  
   SEPMUID:number,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Legal Number for the voiding.  */  
   VoidLegalNumber:string,
      /**  Transaction Document Type for the voiding.  */  
   VoidTranDocTypeID:string,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**   Denmark Localization
Card (payment) code  */  
   CardCode:string,
      /**   Denmark Localization
Account Number  */  
   BankGiroAcctNbr:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHISRCodeLine  */  
   CHISRCodeLine:string,
      /**  CustomsNumber  */  
   CustomsNumber:string,
      /**  ReceivedDate  */  
   ReceivedDate:string,
      /**  TranType  */  
   TranType:string,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  PLInvoiceReference  */  
   PLInvoiceReference:string,
      /**  VoidDescription  */  
   VoidDescription:string,
      /**  APTaxRoundOption  */  
   APTaxRoundOption:number,
      /**  Intended for Internal Use  */  
   AuthAdminNames:string,
      /**  Intended for internal use  */  
   AuthAdmins:string,
   BankName:string,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
   BillAddressList:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
      /**  Document Invoice Vendor Amout only for dispaly  */  
   DocDspInvVendorAmt:number,
   DocInvoiceVariance:number,
      /**  DspInvVendorAmt  */  
   DspInvVendorAmt:number,
   EnableAssignLegNum:boolean,
   EnableDueDate:boolean,
   EnableExchangeRate:boolean,
   EnableLockRate:boolean,
      /**  Logical indicating whether or not the Logged Invoice Tracker is to enable the GL Transaction Tb  */  
   EnableTaxesInTracker:boolean,
   EnableTaxExRate:boolean,
   EnableTaxLock:boolean,
      /**  Enable setting of Transaction Document Type  */  
   EnableTranDocType:boolean,
   EnableVoidLegNum:boolean,
   HasLegNumCnfg:boolean,
   InvoiceVariance:number,
   IsDiscountforDebitM:boolean,
      /**  Not intended for external use.  Indicates if the user has Void authority.  */  
   IsEligibleToVoid:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumberMessage:string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  When the APInvHed record is created from this logged invoice and the APInvHed record is posted, this flag is set to true.  This is used by the UI.  */  
   MatchInvoicePosted:boolean,
      /**  Pay Method Type  */  
   PayMethod:string,
      /**  CSF Poland. Vendor uses Invoice reference number  */  
   PLVendorAutoInvoiceNum:boolean,
      /**  Invoice Vendor Amout only for dispaly in report currency  */  
   Rpt1DspInvVendorAmt:number,
   Rpt1InvoiceVariance:number,
   Rpt1ScrDocInvoiceAmt:number,
   Rpt1ScrInvExpense:number,
   Rpt1ScrInvoiceAmt:number,
   Rpt1ScrInvVendorAmt:number,
   Rpt1ScrRounding:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTotDedTaxAmt:number,
   Rpt1ScrTotInvoiceAmt:number,
   Rpt1ScrTotReportableAmt:number,
   Rpt1ScrTotSelfAmt:number,
   Rpt1ScrTotTaxableAmt:number,
   Rpt1ScrTotWithholdingAmt:number,
      /**  Invoice Vendor Amout only for dispaly in report currency  */  
   Rpt2DspInvVendorAmt:number,
   Rpt2InvoiceVariance:number,
   Rpt2ScrDocInvoiceAmt:number,
   Rpt2ScrInvExpense:number,
   Rpt2ScrInvoiceAmt:number,
   Rpt2ScrInvVendorAmt:number,
   Rpt2ScrRounding:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTotDedTaxAmt:number,
   Rpt2ScrTotInvoiceAmt:number,
   Rpt2ScrTotReportableAmt:number,
   Rpt2ScrTotSelfAmt:number,
   Rpt2ScrTotTaxableAmt:number,
   Rpt2ScrTotWithholdingAmt:number,
      /**  Invoice Vendor Amout only for dispaly in report currency  */  
   Rpt3DspInvVendorAmt:number,
   Rpt3InvoiceVariance:number,
   Rpt3ScrDocInvoiceAmt:number,
   Rpt3ScrInvExpense:number,
   Rpt3ScrInvoiceAmt:number,
   Rpt3ScrInvVendorAmt:number,
   Rpt3ScrRounding:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTotDedTaxAmt:number,
   Rpt3ScrTotInvoiceAmt:number,
   Rpt3ScrTotReportableAmt:number,
   Rpt3ScrTotSelfAmt:number,
   Rpt3ScrTotTaxableAmt:number,
   Rpt3ScrTotWithholdingAmt:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   ScrDiscountAmt:number,
   ScrDocDiscountAmt:number,
   ScrDocInvExpense:number,
   ScrDocInvoiceAmt:number,
   ScrDocInvVendorAmt:number,
   ScrDocRounding:number,
   ScrDocTaxAmt:number,
   ScrDocTotDedTaxAmt:number,
   ScrDocTotInvoiceAmt:number,
   ScrDocTotReportableAmt:number,
   ScrDocTotSelfAmt:number,
   ScrDocTotTaxableAmt:number,
   ScrDocTotWithholdingAmt:number,
   ScrInvExpense:number,
   ScrInvoiceAmt:number,
   ScrInvoiceRef:string,
   ScrInvVendorAmt:number,
   ScrRounding:number,
   ScrTaxAmt:number,
   ScrTotDedTaxAmt:number,
   ScrTotInvoiceAmt:number,
   ScrTotReportableAmt:number,
   ScrTotSelfAmt:number,
   ScrTotTaxableAmt:number,
   ScrTotWithholdingAmt:number,
      /**  System Transaction Type: APInvoice/DebitMemo is used in the filter of TranDocType combo box.  */  
   SystemTranType:string,
   TaxExchangeRate:number,
   TaxLinesExist:boolean,
   TaxRateLinesExist:boolean,
   TotalInvAmt:number,
      /**  Link to TranDocType table, can be removed when path field TranDocTypeID is replaced with actual one.  */  
   TranDocTypeDescription:string,
      /**  This field is used when invoice is transferred form one Group to another and the user has a cance to change this invoice Apply Date.  */  
   TransApplyDate:string,
      /**  Not intended for external use.  Logical indicating that a default entity was created for the new logged invoice.  */  
   UpdateEntity:boolean,
   UseTaxRate:boolean,
      /**  Vendor Bank  */  
   VendorBank:string,
      /**  Indicates if the vendor is active  */  
   VendorInactive:boolean,
   XRateLabel:string,
   AllowChgAfterPrint:boolean,
      /**  Formatted Supplier Name and Address  */  
   FormattedVendorNameAddress:string,
      /**  The flag t to indicate if Tax records created per Tax Liability assigned toLogged Invoiceare adjusted, deleted,  or any tax records were added by the user  */  
   ManualTaxAdj:boolean,
      /**  Supplier Full Address. External field uses the Supplier Address1, Address2, Address3, City,State, zip  and  Country from the supplier catalog  */  
   VendorNumFullAddress:string,
   BitFlag:number,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrencyID:string,
   PurPointName:string,
   PurPointPrimPCon:number,
   PurPointAddress1:string,
   PurPointState:string,
   PurPointAddress2:string,
   PurPointAddress3:string,
   PurPointZip:string,
   PurPointCountry:string,
   PurPointCity:string,
   RateGrpCodeDescription:string,
   SEPayMethodName:string,
   SEPayMethodType:number,
   SEPayMethodSummarizePerCustomer:boolean,
   TaxRateGrpDescription:string,
   TaxRegionCodeDescription:string,
   TermsCodeDescription:string,
   UserfileName:string,
   VendBankSwiftNum:string,
   VendBankBankName:string,
   VendBankBankGiroAcctNbr:string,
   VendBankIBANCode:string,
   VendBankBankAcctNumber:string,
   VendBankPMUID:number,
   VendBankCardCode:string,
   VendBankLocalBIC:string,
   VendorNumCountry:string,
   VendorNumName:string,
   VendorNumTermsCode:string,
   VendorNumAddress1:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress2:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress3:string,
   VendorNumVendorID:string,
   VendorNumCity:string,
   VendorNumState:string,
   VendorNumZIP:string,
   VoidedByName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LogAPInvTaxRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   InvoiceNum:string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  */  
   ECAcquisitionSeq:number,
      /**  Rate Code  */  
   RateCode:string,
      /**  Indicates if this logged invoice has been voided.  */  
   Void:boolean,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**   Sales Tax amount for the corresponding taxable sales amount.
Manually entered if APInvTax.Manual = Yes.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  System calculated Taxable amount for this invoice.  */  
   SysCalcTaxableAmt:number,
      /**  System calculated Taxable amount for this invoice in foreign currency.  */  
   SysCalcDocTaxableAmt:number,
      /**  System calculated Taxable amount for this invoice.  */  
   Rpt1SysCalcTaxableAmt:number,
      /**  System calculated Taxable amount for this invoice.  */  
   Rpt2SysCalcTaxableAmt:number,
      /**  System calculated Taxable amount for this invoice.  */  
   Rpt3SysCalcTaxableAmt:number,
      /**  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  */  
   SysCalcReportableAmt:number,
      /**  System calculated reportable sales amount to the tax jurisdiction expressed in the Vendor's currency.  */  
   SysCalcDocReportableAmt:number,
      /**  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  */  
   Rpt1SysCalcReportableAmt:number,
      /**  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  */  
   Rpt2SysCalcReportableAmt:number,
      /**  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  */  
   Rpt3SysCalcReportableAmt:number,
      /**  Collection Type  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution number  */  
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
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MovementNum  */  
   MovementNum:number,
   BaseCurrSymbol:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DebitMemo:boolean,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   EnableSuperGRate:boolean,
   GroupID:string,
   Posted:boolean,
   RateType:number,
   Rpt1ScrDedTaxAmt:number,
      /**  Display field for Fixed Amount in Report Currency 1.  */  
   Rpt1ScrFixedAmount:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
      /**  Display field for Fixed Amount in Report Currency 2.  */  
   Rpt2ScrFixedAmount:number,
   Rpt2ScrReportableAm:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
      /**  Display field for Fixed Amount in Report Currency 31.  */  
   Rpt3ScrFixedAmount:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   ScrDocDedTaxAmt:number,
      /**  Display field for Fixed amount in document currency  */  
   ScrDocFixedAmount:number,
   ScrDocReportableAmt:number,
   ScrDocTaxableAmt:number,
   ScrDocTaxAmt:number,
   ScrDocTaxAmtVar:number,
      /**  Display field for Fixed Amount  */  
   ScrFixedAmount:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
      /**  Flag to indicate if Manual field on tax record should be disabled  */  
   DisableManual:boolean,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
   VendorNumCountry:string,
   VendorNumZIP:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress2:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress1:string,
   VendorNumName:string,
   VendorNumTermsCode:string,
   VendorNumState:string,
   VendorNumAddress3:string,
   VendorNumVendorID:string,
   VendorNumCity:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LogInvAprvVoidTableset{
   LogAPInv:Erp_Tablesets_LogAPInvRow[],
   LogAPInvAttch:Erp_Tablesets_LogAPInvAttchRow[],
   LogAPInvTax:Erp_Tablesets_LogAPInvTaxRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   LegalNumberGenerate:Erp_Tablesets_LegalNumberGenerateRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtLogInvAprvVoidTableset{
   LogAPInv:Erp_Tablesets_LogAPInvRow[],
   LogAPInvAttch:Erp_Tablesets_LogAPInvAttchRow[],
   LogAPInvTax:Erp_Tablesets_LogAPInvTaxRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   LegalNumberGenerate:Erp_Tablesets_LegalNumberGenerateRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param vendorNum
      @param invoiceNum
   */  
export interface GetByID_input{
   vendorNum:number,
   invoiceNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_LogInvAprvVoidTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_LogInvAprvVoidTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_LogInvAprvVoidTableset[],
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
   returnObj:Erp_Tablesets_LogAPInvListTableset[],
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
   ds:Erp_Tablesets_LogInvAprvVoidTableset[],
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
   ds:Erp_Tablesets_LogInvAprvVoidTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewLegalNumberGenerate_input{
   ds:Erp_Tablesets_LogInvAprvVoidTableset[],
}

export interface GetNewLegalNumberGenerate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogInvAprvVoidTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param invoiceNum
   */  
export interface GetNewLogAPInvAttch_input{
   ds:Erp_Tablesets_LogInvAprvVoidTableset[],
   vendorNum:number,
   invoiceNum:string,
}

export interface GetNewLogAPInvAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogInvAprvVoidTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param invoiceNum
      @param taxCode
      @param rateCode
      @param ecAcquisitionSeq
   */  
export interface GetNewLogAPInvTax_input{
   ds:Erp_Tablesets_LogInvAprvVoidTableset[],
   vendorNum:number,
   invoiceNum:string,
   taxCode:string,
   rateCode:string,
   ecAcquisitionSeq:number,
}

export interface GetNewLogAPInvTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogInvAprvVoidTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewLogAPInv_input{
   ds:Erp_Tablesets_LogInvAprvVoidTableset[],
   vendorNum:number,
}

export interface GetNewLogAPInv_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogInvAprvVoidTableset,
}
}

   /** Required : 
      @param whereClauseLogAPInv
      @param whereClauseLogAPInvAttch
      @param whereClauseLogAPInvTax
      @param whereClauseEntityGLC
      @param whereClauseLegalNumberGenerate
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseLogAPInv:string,
   whereClauseLogAPInvAttch:string,
   whereClauseLogAPInvTax:string,
   whereClauseEntityGLC:string,
   whereClauseLegalNumberGenerate:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_LogInvAprvVoidTableset[],
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
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtLogInvAprvVoidTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtLogInvAprvVoidTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_LogInvAprvVoidTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogInvAprvVoidTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface VoidLoggedInvoice_input{
   ds:Erp_Tablesets_LogInvAprvVoidTableset[],
}

export interface VoidLoggedInvoice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogInvAprvVoidTableset,
}
}

