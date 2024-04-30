import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.LogAPInvSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get LogAPInvs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LogAPInvs
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
export function get_LogAPInvs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   OperationID: NewUpdateExt_LogAPInvs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LogAPInvRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LogAPInvRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LogAPInvs(requestBody:Erp_Tablesets_LogAPInvRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LogAPInv item
   Description: Calls GetByID to retrieve the LogAPInv item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LogAPInv
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
export function get_LogAPInvs_Company_VendorNum_InvoiceNum(Company:string, VendorNum:string, InvoiceNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LogAPInvRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvs(" + Company + "," + VendorNum + "," + InvoiceNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Calls UpdateExt to update LogAPInv for the service
   Description: Calls UpdateExt to update LogAPInv. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LogAPInv
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
export function patch_LogAPInvs_Company_VendorNum_InvoiceNum(Company:string, VendorNum:string, InvoiceNum:string, requestBody:Erp_Tablesets_LogAPInvRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvs(" + Company + "," + VendorNum + "," + InvoiceNum + ")", {
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
   Summary: Call UpdateExt to delete LogAPInv item
   Description: Call UpdateExt to delete LogAPInv item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LogAPInv
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LogAPInvs_Company_VendorNum_InvoiceNum(Company:string, VendorNum:string, InvoiceNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvs(" + Company + "," + VendorNum + "," + InvoiceNum + ")", {
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
export function get_LogAPInvs_Company_VendorNum_InvoiceNum_LogAPInvTaxes(Company:string, VendorNum:string, InvoiceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvs(" + Company + "," + VendorNum + "," + InvoiceNum + ")/LogAPInvTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_LogAPInvs_Company_VendorNum_InvoiceNum_LogAPInvTaxes_Company_VendorNum_InvoiceNum_TaxCode_RateCode_ECAcquisitionSeq_Void(Company:string, VendorNum:string, InvoiceNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, Void:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LogAPInvTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvs(" + Company + "," + VendorNum + "," + InvoiceNum + ")/LogAPInvTaxes(" + Company + "," + VendorNum + "," + InvoiceNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + "," + Void + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_LogAPInvs_Company_VendorNum_InvoiceNum_EntityGLCs(Company:string, VendorNum:string, InvoiceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvs(" + Company + "," + VendorNum + "," + InvoiceNum + ")/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_LogAPInvs_Company_VendorNum_InvoiceNum_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, VendorNum:string, InvoiceNum:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvs(" + Company + "," + VendorNum + "," + InvoiceNum + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_LogAPInvs_Company_VendorNum_InvoiceNum_LogAPInvAttches(Company:string, VendorNum:string, InvoiceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvs(" + Company + "," + VendorNum + "," + InvoiceNum + ")/LogAPInvAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_LogAPInvs_Company_VendorNum_InvoiceNum_LogAPInvAttches_Company_VendorNum_InvoiceNum_DrawingSeq(Company:string, VendorNum:string, InvoiceNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LogAPInvAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvs(" + Company + "," + VendorNum + "," + InvoiceNum + ")/LogAPInvAttches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvTaxes(" + Company + "," + VendorNum + "," + InvoiceNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + "," + Void + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvTaxes(" + Company + "," + VendorNum + "," + InvoiceNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + "," + Void + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvTaxes(" + Company + "," + VendorNum + "," + InvoiceNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + "," + Void + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/EntityGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvAttches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvAttches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + DrawingSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LogAPInvAttches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + DrawingSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LegalNumGenOpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetRows(whereClauseLogAPInv:string, whereClauseLogAPInvAttch:string, whereClauseLogAPInvTax:string, whereClauseEntityGLC:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method ChangeCurrency
   Description: Method to call when changing the currency on the invoice.  Validates the currency code and
updates APInvHed with default values based on the currency.
   OperationID: ChangeCurrency
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrency(requestBody:ChangeCurrency_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCurrency_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeCurrency", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeCurrency_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFixedAmount
   Description: Method to call when changing the fixed amount on a tax record.  Updates LogAPInvTax
tax amounts based on the new fixed amount.
   OperationID: ChangeFixedAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFixedAmount(requestBody:ChangeFixedAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFixedAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeFixedAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeFixedAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeGLCntrlType
   Description: Return if GL Control Type have GL Control Code
   OperationID: ChangeGLCntrlType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeGLCntrlType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLCntrlType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGLCntrlType(requestBody:ChangeGLCntrlType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeGLCntrlType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeGLCntrlType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeGLCntrlType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeInvoiceDate
   Description: Method to call when changing the invoice date on the invoice.  Updates APInvHed
with default values based on the new date.
   OperationID: ChangeInvoiceDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeInvoiceDate(requestBody:ChangeInvoiceDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeInvoiceDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeInvoiceDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeInvoiceDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeInvoiceDateEx
   Description: Method to call when changing the invoice date on the invoice.  Updates APInvHed
with default values based on the new date.
This method will additionally return a message to present to the user if the date is greater than
the client today date.
   OperationID: ChangeInvoiceDateEx
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceDateEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceDateEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeInvoiceDateEx(requestBody:ChangeInvoiceDateEx_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeInvoiceDateEx_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeInvoiceDateEx", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeInvoiceDateEx_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeInvoiceNum
   Description: Method to call when changing the invoice num.
   OperationID: ChangeInvoiceNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeInvoiceNum(requestBody:ChangeInvoiceNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeInvoiceNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeInvoiceNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeInvoiceNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeInvoiceRef
   Description: Method to call when changing the invoice reference on the debit memo.  Validates the
invoice reference number id and updates APInvHed with values from the new invoice reference.
   OperationID: ChangeInvoiceRef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeInvoiceRef(requestBody:ChangeInvoiceRef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeInvoiceRef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeInvoiceRef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeInvoiceRef_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeInvoiceVendorAmt
   Description: Method to call when changing the invoice vendor amount on an invoice record.  Updates APInvHed
amounts based on the new invoice vendor amount.
   OperationID: ChangeInvoiceVendorAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceVendorAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceVendorAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeInvoiceVendorAmt(requestBody:ChangeInvoiceVendorAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeInvoiceVendorAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeInvoiceVendorAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeInvoiceVendorAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLockRate
   Description: Method to call when changing the lock rate flag on the invoice.  Updates
LogAPInv.EnableExchangeRate field.
   OperationID: ChangeLockRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLockRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLockRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLockRate(requestBody:ChangeLockRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLockRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeLockRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeLockRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeManualTaxCalculation
   Description: Method to call when changing the manual tax calculation value on a tax record.  Updates APInvTax
tax amounts based on the new value of the flag.
   OperationID: ChangeManualTaxCalculation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeManualTaxCalculation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeManualTaxCalculation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeManualTaxCalculation(requestBody:ChangeManualTaxCalculation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeManualTaxCalculation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeManualTaxCalculation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeManualTaxCalculation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRateCode
   Description: Method to call when changing the tax percent on a tax record.  Updates LogAPInvTax
tax amounts based on the new tax percent.
   OperationID: ChangeRateCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRateCode(requestBody:ChangeRateCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRateCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeRateCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRateCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePurPointInfo
   Description: This method returns default information for the Vendor Purchase Point.
   OperationID: ChangePurPointInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePurPointInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePurPointInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePurPointInfo(requestBody:ChangePurPointInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePurPointInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangePurPointInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangePurPointInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRefPONum
   Description: Method to call when changing the po number reference on the invoice.  Validates the
po number reference and updates APInvHed with default values based on the po number.
   OperationID: ChangeRefPONum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRefPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRefPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRefPONum(requestBody:ChangeRefPONum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRefPONum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeRefPONum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRefPONum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeReportableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates APInvTax
tax amounts based on the new taxable amount.
   OperationID: ChangeReportableAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeReportableAmt(requestBody:ChangeReportableAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeReportableAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeReportableAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeReportableAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSEPMUID
   Description: Method to call when changing the Payment Method.
   OperationID: ChangeSEPMUID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSEPMUID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSEPMUID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSEPMUID(requestBody:ChangeSEPMUID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSEPMUID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeSEPMUID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeSEPMUID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaxableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates APInvTax
tax amounts based on the new taxable amount.
   OperationID: ChangeTaxableAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxableAmt(requestBody:ChangeTaxableAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTaxableAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeTaxableAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTaxableAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaxAmt
   Description: Method to call when changing the tax amount on a tax record.  Updates APInvTax
tax amounts based on the new tax amount.
   OperationID: ChangeTaxAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxAmt(requestBody:ChangeTaxAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTaxAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeTaxAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTaxAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaxCode
   Description: Method to call when changing the tax code on a tax record.  Validates the tax code and
updates APInvTax tax amounts based on the new tax code.
   OperationID: ChangeTaxCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxCode(requestBody:ChangeTaxCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTaxCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeTaxCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTaxCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaxDeductable
   Description: Method to call when changing the tax deductable on a tax record.  Updates APInvTax
tax amounts based on the new tax percent.
   OperationID: ChangeTaxDeductable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxDeductable(requestBody:ChangeTaxDeductable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTaxDeductable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeTaxDeductable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTaxDeductable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaxLock
   Description: Method to call when changing the tax lock rate flag on the invoice.  Updates
LogAPInv.EnableTaxExRate field.
   OperationID: ChangeTaxLock
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTaxLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxLock(requestBody:ChangeTaxLock_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTaxLock_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeTaxLock", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTaxLock_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaxPercent
   Description: Method to call when changing the tax percent on a tax record.  Updates LogAPInvTax
tax amounts based on the new tax percent.
   OperationID: ChangeTaxPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxPercent(requestBody:ChangeTaxPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTaxPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeTaxPercent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTaxPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaxRegion
   Description: Method to call when changing the vendor id on the invoice.  Validates the vendor id and
updates LogAPInv with values from the new vendor.
updates LogAPInv with values from the new vendor.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeTaxRegion", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method ChangeTermsCode
   Description: Method to call when changing the terms code on the invoice.  Validates the terms code and
updates LogAPInv with default values based on the new code.
   OperationID: ChangeTermsCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTermsCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTermsCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTermsCode(requestBody:ChangeTermsCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTermsCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeTermsCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTermsCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendorID
   Description: Method to call when changing the vendor id on the invoice.  Validates the vendor id and
updates LogAPInv with values from the new vendor.
updates LogAPInv with values from the new vendor.
   OperationID: ChangeVendorID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendorID(requestBody:ChangeVendorID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendorID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeVendorID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendorID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBankRef
   Description: Before updating the LogAPInv record, CheckBankRef will be called to check if the
bank reference conforms to format standards.  If not, the user will be
presented with a warning message and allowed to continue with the save.
At this time this method is specific to Finland/Sweden localization
   OperationID: CheckBankRef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckBankRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBankRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBankRef(requestBody:CheckBankRef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckBankRef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/CheckBankRef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckBankRef_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/CheckDocumentIsLocked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method CheckRateGrpCode
   Description: Update APInvoice Detail information when the RateGrp is changed.
   OperationID: CheckRateGrpCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRateGrpCode(requestBody:CheckRateGrpCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckRateGrpCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/CheckRateGrpCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckRateGrpCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTaxRateGrpCode
   Description: Update APInvoice Detail information when the TaxRateGrp is changed.
   OperationID: CheckTaxRateGrpCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckTaxRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTaxRateGrpCode(requestBody:CheckTaxRateGrpCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckTaxRateGrpCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/CheckTaxRateGrpCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckTaxRateGrpCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Method to call to get available tran doc types.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetAvailTranDocTypes", {
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
   Summary: Invoke method GetNewLogAPInvDebitMemo
   Description: Method to call when adding a new Logged Debit Memo AP Invoice record
   OperationID: GetNewLogAPInvDebitMemo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLogAPInvDebitMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLogAPInvDebitMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLogAPInvDebitMemo(requestBody:GetNewLogAPInvDebitMemo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLogAPInvDebitMemo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetNewLogAPInvDebitMemo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLogAPInvDebitMemo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLogAPInvInvoice
   Description: Method to call when adding a new logged AP Invoice record
   OperationID: GetNewLogAPInvInvoice
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLogAPInvInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLogAPInvInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLogAPInvInvoice(requestBody:GetNewLogAPInvInvoice_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLogAPInvInvoice_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetNewLogAPInvInvoice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLogAPInvInvoice_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPercentFixedAmt
   Description: Purpose:
Parameters:
<param name="ipInvDate">Invoice date to use</param>
Notes:
   OperationID: GetPercentFixedAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPercentFixedAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPercentFixedAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPercentFixedAmt(requestBody:GetPercentFixedAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPercentFixedAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetPercentFixedAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPercentFixedAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetvalidEAD
   OperationID: GetvalidEAD
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetvalidEAD_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetvalidEAD_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetvalidEAD(requestBody:GetvalidEAD_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetvalidEAD_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetvalidEAD", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetvalidEAD_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetValueExchageRate
   Description: This method returns the Exchange Rate information for the selected Currency.  The system
may not have an exchange rate between the APInvoice and Base so it may use an middle Currency
so that it will go APInvoice Currency -> Ref Currency -> Base Currency
   OperationID: GetValueExchageRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetValueExchageRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValueExchageRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetValueExchageRate(requestBody:GetValueExchageRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetValueExchageRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetValueExchageRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetValueExchageRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDueDate
   Description: Method to call when changing the Due date on the invoice.
   OperationID: ChangeDueDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDueDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDueDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDueDate(requestBody:ChangeDueDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDueDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ChangeDueDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDueDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofApplyDate
   Description: This method should be called to validate the new apply date entered by the user.
   OperationID: OnChangeofApplyDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofApplyDate(requestBody:OnChangeofApplyDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofApplyDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/OnChangeofApplyDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeofApplyDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofApplyDateEx
   Description: This method should be called to validate the new apply date entered by the user.
This method will additionally return a message to present to the user if the date is greater than
the client today date.
   OperationID: OnChangeofApplyDateEx
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofApplyDateEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofApplyDateEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofApplyDateEx(requestBody:OnChangeofApplyDateEx_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofApplyDateEx_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/OnChangeofApplyDateEx", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeofApplyDateEx_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofTaxPoint
   Description: This method should be called to validate the new tax rate date entered by the user.
   OperationID: OnChangeofTaxPoint
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofTaxPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofTaxPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofTaxPoint(requestBody:OnChangeofTaxPoint_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofTaxPoint_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/OnChangeofTaxPoint", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeofTaxPoint_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofTaxRateDate
   Description: This method should be called to validate the new apply date entered by the user.
   OperationID: OnChangeofTaxRateDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofTaxRateDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofTaxRateDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofTaxRateDate(requestBody:OnChangeofTaxRateDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofTaxRateDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/OnChangeofTaxRateDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeofTaxRateDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes
   OperationID: OnChangeTranDocTypeID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTranDocTypeID(requestBody:OnChangeTranDocTypeID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTranDocTypeID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/OnChangeTranDocTypeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeTranDocTypeID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfTransApplyDate
   Description: This method should be called to validate the new apply date entered for the transferred invoice.
   OperationID: OnChangeOfTransApplyDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfTransApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfTransApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfTransApplyDate(requestBody:OnChangeOfTransApplyDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfTransApplyDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/OnChangeOfTransApplyDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfTransApplyDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeVendBankID
   Description: Call this method when the user enters the ttLogApInv.BankID
   OperationID: OnChangeVendBankID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeVendBankID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendBankID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendBankID(requestBody:OnChangeVendBankID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeVendBankID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/OnChangeVendBankID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeVendBankID_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/PreUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method SetReadyToCalc
   Description: Purpose: create tax records according Tax Liability, Calculate Tax Amount only for the first tax line
Parameters:  none
Notes:
<param name="ipGroupID">ipGroupID </param><param name="ipInvoiceNum">ipInvoiceNum </param><param name="ipVendorNum">ipVendorNum </param><param name="ipCalcAll">ipCalcAll</param><param name="ds">The Log AP Invoice data set</param>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/SetReadyToCalc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method TransferInvoiceToGroup
   Description: Method to call when transfering an invoice to a different group.
   OperationID: TransferInvoiceToGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/TransferInvoiceToGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TransferInvoiceToGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TransferInvoiceToGroup(requestBody:TransferInvoiceToGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<TransferInvoiceToGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/TransferInvoiceToGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as TransferInvoiceToGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateBankRefs
   Description: Validate Banking References
   OperationID: ValidateBankRefs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateBankRefs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBankRefs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBankRefs(requestBody:ValidateBankRefs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateBankRefs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ValidateBankRefs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateBankRefs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateRateCode
   Description: Purpose:     Validate the RateCode on the LogAPInvTax
Parameters:
<param name="ipRateCode"> proposed rate code </param><param name="ipTaxCode">Tax code associated with the rate</param><param name="ipInvDate">invoice date</param><param name="ds">The Logged AP Invoice data set</param>
Notes:
   OperationID: ValidateRateCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRateCode(requestBody:ValidateRateCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateRateCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ValidateRateCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateRateCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the LogAPInv.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/AssignLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/VoidLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetLegalNumGenOpts
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetLegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method DecodeISRCodeLine
   Description: Decode ISR Code Line and return data for filling Invoice Header
At this time this method is specific to Switzerland localization
   OperationID: DecodeISRCodeLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DecodeISRCodeLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DecodeISRCodeLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DecodeISRCodeLine(requestBody:DecodeISRCodeLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DecodeISRCodeLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/DecodeISRCodeLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DecodeISRCodeLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePLInvoiceReference
   Description: CSF Poland. Validate unique of PLInvoiceReference for selected supplier
   OperationID: ValidatePLInvoiceReference
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePLInvoiceReference_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePLInvoiceReference_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePLInvoiceReference(requestBody:ValidatePLInvoiceReference_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePLInvoiceReference_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/ValidatePLInvoiceReference", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidatePLInvoiceReference_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetNewLogAPInv", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetNewLogAPInvAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetNewLogAPInvTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetNewEntityGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LogAPInvSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
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
      @param VendorNum
      @param InvoiceNum
      @param ds
   */  
export interface AssignLegalNumber_input{
      /**  The vendor number.  */  
   VendorNum:number,
      /**  The invoice number.  */  
   InvoiceNum:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface AssignLegalNumber_output{
parameters : {
      /**  output parameters  */  
   LegalNumberMessage:string,
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedCurrencyCode
      @param ds
   */  
export interface ChangeCurrency_input{
      /**  The proposed currency code  */  
   ProposedCurrencyCode:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeCurrency_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedDueDate
      @param ds
   */  
export interface ChangeDueDate_input{
      /**  The proposed invoice date  */  
   ProposedDueDate:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeDueDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param proposedFixedAmt
      @param ds
   */  
export interface ChangeFixedAmount_input{
      /**  The proposed fixed amount  */  
   proposedFixedAmt:number,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeFixedAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param vGLControlType
   */  
export interface ChangeGLCntrlType_input{
      /**  GL Control Type selected for the Invoice  */  
   vGLControlType:string,
}

export interface ChangeGLCntrlType_output{
parameters : {
      /**  output parameters  */  
   opGLControlCode:string,
   opDescription:string,
}
}

   /** Required : 
      @param ProposedInvoiceDate
      @param ds
   */  
export interface ChangeInvoiceDateEx_input{
      /**  The proposed invoice date  */  
   ProposedInvoiceDate:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeInvoiceDateEx_output{
parameters : {
      /**  output parameters  */  
   cMessageText:string,
   DateMessage:string,
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedInvoiceDate
      @param ds
   */  
export interface ChangeInvoiceDate_input{
      /**  The proposed invoice date  */  
   ProposedInvoiceDate:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeInvoiceDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ipInvoiceNum
      @param ipVendorNum
   */  
export interface ChangeInvoiceNum_input{
      /**  The proposed invoice Number  */  
   ipInvoiceNum:string,
      /**  The vendor Num (ID)  */  
   ipVendorNum:number,
}

export interface ChangeInvoiceNum_output{
}

   /** Required : 
      @param ProposedInvoiceRef
      @param ds
   */  
export interface ChangeInvoiceRef_input{
      /**  The proposed invoice reference number  */  
   ProposedInvoiceRef:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeInvoiceRef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedInvoiceVendorAmt
      @param ds
   */  
export interface ChangeInvoiceVendorAmt_input{
      /**  The proposed tax amount  */  
   ProposedInvoiceVendorAmt:number,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeInvoiceVendorAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeLockRate_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeLockRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeManualTaxCalculation_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeManualTaxCalculation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ds
      @param purPoint
   */  
export interface ChangePurPointInfo_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
      /**  Proposed Purchase Point value  */  
   purPoint:string,
}

export interface ChangePurPointInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeRateCode_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeRateCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedRefPONum
      @param confirmCheck
      @param ds
   */  
export interface ChangeRefPONum_input{
      /**  The proposed po number reference  */  
   ProposedRefPONum:number,
      /**  Confirm Check  */  
   confirmCheck:boolean,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeRefPONum_output{
parameters : {
      /**  output parameters  */  
   confirmMsg:string,
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedReportableAmt
      @param ds
   */  
export interface ChangeReportableAmt_input{
      /**  The proposed reportable amount  */  
   ProposedReportableAmt:number,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeReportableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeSEPMUID_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeSEPMUID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedTaxAmt
      @param ds
   */  
export interface ChangeTaxAmt_input{
      /**  The proposed tax amount  */  
   ProposedTaxAmt:number,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeTaxAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedTaxCode
      @param ds
   */  
export interface ChangeTaxCode_input{
      /**  The proposed tax code  */  
   ProposedTaxCode:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeTaxCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param proposedTaxDeductable
      @param ds
   */  
export interface ChangeTaxDeductable_input{
      /**  The proposed tax deductable  */  
   proposedTaxDeductable:number,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeTaxDeductable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTaxLock_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeTaxLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedTaxPercent
      @param ds
   */  
export interface ChangeTaxPercent_input{
      /**  The proposed tax percent  */  
   ProposedTaxPercent:number,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeTaxPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedTaxRegion
      @param ds
   */  
export interface ChangeTaxRegion_input{
      /**  The proposed tax region  */  
   ProposedTaxRegion:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeTaxRegion_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedTaxableAmt
      @param ds
   */  
export interface ChangeTaxableAmt_input{
      /**  The proposed taxable amount  */  
   ProposedTaxableAmt:number,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeTaxableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedTermsCode
      @param ds
   */  
export interface ChangeTermsCode_input{
      /**  The proposed terms code  */  
   ProposedTermsCode:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeTermsCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ProposedVendorID
      @param confirmCheck
      @param ds
   */  
export interface ChangeVendorID_input{
      /**  The proposed vendor id  */  
   ProposedVendorID:string,
      /**  Confirm Check  */  
   confirmCheck:boolean,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ChangeVendorID_output{
parameters : {
      /**  output parameters  */  
   confirmMsg:string,
   OutInPrice:string,
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckBankRef_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface CheckBankRef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
   OpMessage:string,
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
      @param ipRateGrpCode
      @param ds
   */  
export interface CheckRateGrpCode_input{
      /**  Currency Rate Group Code  */  
   ipRateGrpCode:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface CheckRateGrpCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ipRateGrpCode
      @param ds
   */  
export interface CheckTaxRateGrpCode_input{
      /**  Currency Rate Group Code  */  
   ipRateGrpCode:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface CheckTaxRateGrpCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ipISRCodeLine
   */  
export interface DecodeISRCodeLine_input{
      /**  ISR Code Line for decoding  */  
   ipISRCodeLine:string,
}

export interface DecodeISRCodeLine_output{
parameters : {
      /**  output parameters  */  
   opSlipType:string,
   opSlipCode:string,
   opAmount:number,
   opCurrencyCode:string,
   opISRRefNum:string,
   opVendorNum:number,
   opVendorID:string,
   opVendorName:string,
}
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

export interface Erp_Tablesets_LogAPInvTableset{
   LogAPInv:Erp_Tablesets_LogAPInvRow[],
   LogAPInvAttch:Erp_Tablesets_LogAPInvAttchRow[],
   LogAPInvTax:Erp_Tablesets_LogAPInvTaxRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

export interface Erp_Tablesets_UpdExtLogAPInvTableset{
   LogAPInv:Erp_Tablesets_LogAPInvRow[],
   LogAPInvAttch:Erp_Tablesets_LogAPInvAttchRow[],
   LogAPInvTax:Erp_Tablesets_LogAPInvTaxRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   AvailTypes:string,
}
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
   returnObj:Erp_Tablesets_LogAPInvTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_LogAPInvTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_LogAPInvTableset[],
}

   /** Required : 
      @param ds
      @param VendorNum
      @param InvoiceNum
      @param Voided
   */  
export interface GetLegalNumGenOpts_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
      /**  Vendor Number  */  
   VendorNum:number,
      /**  Invoice Number  */  
   InvoiceNum:string,
      /**  LotAPInv Voided  */  
   Voided:boolean,
}

export interface GetLegalNumGenOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
   RequiresUserInput:boolean,
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
   ds:Erp_Tablesets_LogAPInvTableset[],
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
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param invoiceNum
   */  
export interface GetNewLogAPInvAttch_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
   vendorNum:number,
   invoiceNum:string,
}

export interface GetNewLogAPInvAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ds
      @param cGroupID
   */  
export interface GetNewLogAPInvDebitMemo_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
      /**  The group id to add the invoice to  */  
   cGroupID:string,
}

export interface GetNewLogAPInvDebitMemo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ds
      @param cGroupID
   */  
export interface GetNewLogAPInvInvoice_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
      /**  The group id to add the invoice to  */  
   cGroupID:string,
}

export interface GetNewLogAPInvInvoice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
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
   ds:Erp_Tablesets_LogAPInvTableset[],
   vendorNum:number,
   invoiceNum:string,
   taxCode:string,
   rateCode:string,
   ecAcquisitionSeq:number,
}

export interface GetNewLogAPInvTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewLogAPInv_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
   vendorNum:number,
}

export interface GetNewLogAPInv_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ipInvDate
   */  
export interface GetPercentFixedAmt_input{
   ipInvDate:string,
}

export interface GetPercentFixedAmt_output{
}

   /** Required : 
      @param whereClauseLogAPInv
      @param whereClauseLogAPInvAttch
      @param whereClauseLogAPInvTax
      @param whereClauseEntityGLC
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseLogAPInv:string,
   whereClauseLogAPInvAttch:string,
   whereClauseLogAPInvTax:string,
   whereClauseEntityGLC:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_LogAPInvTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param vCurrencyCode
      @param vRateGrpCode
   */  
export interface GetValueExchageRate_input{
      /**  Currency selected for the Logged APInvoice  */  
   vCurrencyCode:string,
      /**  Currency Rate Group selected for the Logged APInvoice  */  
   vRateGrpCode:string,
}

export interface GetValueExchageRate_output{
parameters : {
      /**  output parameters  */  
   vExchangeRate:number,
   vXRateLabel:string,
}
}

   /** Required : 
      @param inTransType
      @param inDateLabel
      @param proposedDate
   */  
export interface GetvalidEAD_input{
   inTransType:string,
   inDateLabel:string,
   proposedDate:string,
}

export interface GetvalidEAD_output{
parameters : {
      /**  output parameters  */  
   proposedDate:string,
   cMessageText:string,
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
      @param vendorNum
      @param invoiceNum
      @param newTransApplyDate
      @param ds
   */  
export interface OnChangeOfTransApplyDate_input{
      /**  Vendor Number.  */  
   vendorNum:number,
      /**  Invoice Number.  */  
   invoiceNum:string,
      /**  New Apply Date.  */  
   newTransApplyDate:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface OnChangeOfTransApplyDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ipTranDocTypeID
      @param ds
   */  
export interface OnChangeTranDocTypeID_input{
      /**  TranDocTypeID supplied  */  
   ipTranDocTypeID:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface OnChangeTranDocTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param pcVendBankID
      @param ds
   */  
export interface OnChangeVendBankID_input{
      /**  Vendor Bank ID  */  
   pcVendBankID:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface OnChangeVendBankID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param VendorNum
      @param InvoiceNum
      @param NewApplyDate
      @param ds
   */  
export interface OnChangeofApplyDateEx_input{
      /**  Vendor Number.  */  
   VendorNum:number,
      /**  Invoice Number.  */  
   InvoiceNum:string,
      /**  New Apply Date.  */  
   NewApplyDate:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface OnChangeofApplyDateEx_output{
parameters : {
      /**  output parameters  */  
   DateMessage:string,
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param VendorNum
      @param InvoiceNum
      @param NewApplyDate
      @param ds
   */  
export interface OnChangeofApplyDate_input{
      /**  Vendor Number.  */  
   VendorNum:number,
      /**  Invoice Number.  */  
   InvoiceNum:string,
      /**  New Apply Date.  */  
   NewApplyDate:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface OnChangeofApplyDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param VendorNum
      @param InvoiceNum
      @param newTaxPoint
      @param ds
   */  
export interface OnChangeofTaxPoint_input{
      /**  Vendor Number.  */  
   VendorNum:number,
      /**  Invoice Number.  */  
   InvoiceNum:string,
      /**  New Tax Point.  */  
   newTaxPoint:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface OnChangeofTaxPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param VendorNum
      @param InvoiceNum
      @param newTaxDate
      @param ds
   */  
export interface OnChangeofTaxRateDate_input{
      /**  Vendor Number.  */  
   VendorNum:number,
      /**  Invoice Number.  */  
   InvoiceNum:string,
      /**  New Tax Date.  */  
   newTaxDate:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface OnChangeofTaxRateDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ipGroupID
      @param ipInvoiceNum
      @param ipVendorNum
      @param ipCalcAll
      @param ds
   */  
export interface SetReadyToCalc_input{
   ipGroupID:string,
   ipInvoiceNum:string,
   ipVendorNum:number,
   ipCalcAll:boolean,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface SetReadyToCalc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param TransferToGroupID
      @param XferInvVendorNum
      @param XferInvInvoiceNum
   */  
export interface TransferInvoiceToGroup_input{
      /**  The group id to transfer the invoice to  */  
   TransferToGroupID:string,
      /**  The vendor number on the invoice to transfer  */  
   XferInvVendorNum:number,
      /**  The invoice number of the invoice to transfer  */  
   XferInvInvoiceNum:string,
}

export interface TransferInvoiceToGroup_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtLogAPInvTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtLogAPInvTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param ipGroupID
   */  
export interface ValidateBankRefs_input{
      /**  Group ID  */  
   ipGroupID:string,
}

export interface ValidateBankRefs_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   cErrorMsg:string,
}
}

   /** Required : 
      @param intVendorNum
      @param txtInvoiceNum
      @param txtPLInvoiceReference
   */  
export interface ValidatePLInvoiceReference_input{
   intVendorNum:number,
   txtInvoiceNum:string,
   txtPLInvoiceReference:string,
}

export interface ValidatePLInvoiceReference_output{
}

   /** Required : 
      @param ipRateCode
      @param ipTaxCode
      @param ipInvDate
      @param ds
   */  
export interface ValidateRateCode_input{
   ipRateCode:string,
   ipTaxCode:string,
   ipInvDate:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface ValidateRateCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

   /** Required : 
      @param VendorNum
      @param InvoiceNum
      @param VoidedReason
      @param ds
   */  
export interface VoidLegalNumber_input{
      /**  The vendor number.  */  
   VendorNum:number,
      /**  The invoice number.  */  
   InvoiceNum:string,
      /**  Reason for the void  */  
   VoidedReason:string,
   ds:Erp_Tablesets_LogAPInvTableset[],
}

export interface VoidLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LogAPInvTableset,
}
}

