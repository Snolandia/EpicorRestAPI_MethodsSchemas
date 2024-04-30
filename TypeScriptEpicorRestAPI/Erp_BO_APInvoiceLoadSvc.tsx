import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.APInvoiceLoadSvc
// Description: A/P Open Invoice Load Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get APInvoiceLoads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APInvoiceLoads
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvoiceLoadRow
   */  
export function get_APInvoiceLoads(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceLoadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceLoadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APInvoiceLoads
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APInvoiceLoadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APInvoiceLoadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APInvoiceLoads(requestBody:Erp_Tablesets_APInvoiceLoadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the APInvoiceLoad item
   Description: Calls GetByID to retrieve the APInvoiceLoad item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APInvoiceLoad
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APInvoiceLoadRow
   */  
export function get_APInvoiceLoads_Company_VendorNum_InvoiceNum(Company:string, VendorNum:string, InvoiceNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APInvoiceLoadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads(" + Company + "," + VendorNum + "," + InvoiceNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_APInvoiceLoadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APInvoiceLoad for the service
   Description: Calls UpdateExt to update APInvoiceLoad. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APInvoiceLoad
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APInvoiceLoadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APInvoiceLoads_Company_VendorNum_InvoiceNum(Company:string, VendorNum:string, InvoiceNum:string, requestBody:Erp_Tablesets_APInvoiceLoadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads(" + Company + "," + VendorNum + "," + InvoiceNum + ")", {
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
   Summary: Call UpdateExt to delete APInvoiceLoad item
   Description: Call UpdateExt to delete APInvoiceLoad item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APInvoiceLoad
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APInvoiceLoads_Company_VendorNum_InvoiceNum(Company:string, VendorNum:string, InvoiceNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads(" + Company + "," + VendorNum + "," + InvoiceNum + ")", {
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
export function get_APInvoiceLoads_Company_VendorNum_InvoiceNum_EntityGLCs(Company:string, VendorNum:string, InvoiceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads(" + Company + "," + VendorNum + "," + InvoiceNum + ")/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_APInvoiceLoads_Company_VendorNum_InvoiceNum_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, VendorNum:string, InvoiceNum:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads(" + Company + "," + VendorNum + "," + InvoiceNum + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/EntityGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvoiceLoadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceLoadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceLoadListRow)
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
export function get_GetRows(whereClauseAPInvoiceLoad:string, whereClauseEntityGLC:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAPInvoiceLoad!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPInvoiceLoad=" + whereClauseAPInvoiceLoad
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method ChangeApplyDate
   Description: This method updates the A/P Apply Date
   OperationID: ChangeApplyDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeApplyDate(requestBody:ChangeApplyDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeApplyDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/ChangeApplyDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeApplyDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeInvoiceBalance
   Description: This method updates the A/P Invoice Amounts when the invoice balance changes or
the exchange rate changes.  Use the external fields APInvoiceLoad.DispInvoiceBal
and APInvoiceLoad.DocDispInvoiceBal to accept the user entered amount.  An input
parameter is expected to indicate if this method is called after changing the
Exchange Rate or the Base Invoice Balance or the Doc Invoice Balance.  When changing
the actual InvoiceBal and DocInvoiceBal fields instead of the Disp counterparts,
set the Change Type to be: 'B1' and 'D1' for base and doc fields.
   OperationID: ChangeInvoiceBalance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeInvoiceBalance(requestBody:ChangeInvoiceBalance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeInvoiceBalance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/ChangeInvoiceBalance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeInvoiceBalance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeInvoiceDate
   Description: This method updates the A/P Invoice Dates and Exchange Rates when the Invoice
Date changes and checks if the date is greater than the client today date.
This method will additionally return a message to present to the user if necessary.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/ChangeInvoiceDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method OnChangingInvoiceOrApplyDate
   Description: This method verifies the invoice date and/or apply date
   OperationID: OnChangingInvoiceOrApplyDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingInvoiceOrApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingInvoiceOrApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingInvoiceOrApplyDate(requestBody:OnChangingInvoiceOrApplyDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingInvoiceOrApplyDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/OnChangingInvoiceOrApplyDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingInvoiceOrApplyDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTerms
   Description: This method updates the A/P Invoice Due Date when the Terms Code changes.
   OperationID: ChangeTerms
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTerms_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTerms_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTerms(requestBody:ChangeTerms_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTerms_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/ChangeTerms", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTerms_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendorID
   Description: This method defaults the A/P Invoice Load details based on the proposed Vendor ID.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/ChangeVendorID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method Change1099Code
   OperationID: Change1099Code
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Change1099Code_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Change1099Code_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Change1099Code(requestBody:Change1099Code_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Change1099Code_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/Change1099Code", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Change1099Code_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFormType
   OperationID: ChangeFormType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFormType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFormType(requestBody:ChangeFormType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFormType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/ChangeFormType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeFormType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base CurrencyCode
   OperationID: GetCurrencyBase
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyBase(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCurrencyBase_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/GetCurrencyBase", {
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
         resolve(data as GetCurrencyBase_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCurrencyCodeOrRateGroup
   Description: This method is executed when changing the currency code or rate type, then calls the method GetExchangeRate to return the correct exchange rate.
   OperationID: OnChangeCurrencyCodeOrRateGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCurrencyCodeOrRateGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCurrencyCodeOrRateGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCurrencyCodeOrRateGroup(requestBody:OnChangeCurrencyCodeOrRateGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCurrencyCodeOrRateGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/OnChangeCurrencyCodeOrRateGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeCurrencyCodeOrRateGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPInvoiceLoad1
   Description: This method is to be used in place of GetNewAPInvoiceLoad.
   OperationID: GetNewAPInvoiceLoad1
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPInvoiceLoad1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPInvoiceLoad1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPInvoiceLoad1(requestBody:GetNewAPInvoiceLoad1_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPInvoiceLoad1_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/GetNewAPInvoiceLoad1", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAPInvoiceLoad1_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaxTypesList
   Description: Get where clause to select tax types, related to specified Tax Liability
   OperationID: GetTaxTypesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTaxTypesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxTypesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxTypesList(requestBody:GetTaxTypesList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTaxTypesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/GetTaxTypesList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTaxTypesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTotalBalance
   Description: This method returns the total unposted invoice load balance and the base
currency symbol.
   OperationID: GetTotalBalance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTotalBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTotalBalance(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTotalBalance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/GetTotalBalance", {
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
         resolve(data as GetTotalBalance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingTax
   Description: Called when the Tax Type or Tax Rate field changes.
   OperationID: OnChangingTax
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingTax(requestBody:OnChangingTax_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingTax_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/OnChangingTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingTax_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PostOpenInvLoad
   Description: This method performs the actual posting of open invoice loads. It is assumed
that the user already okayed to continue with the posting.
   OperationID: PostOpenInvLoad
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostOpenInvLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostOpenInvLoad(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PostOpenInvLoad_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/PostOpenInvLoad", {
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
         resolve(data as PostOpenInvLoad_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeVendBankID
   Description: Call this method when the user enters the ttApInv.BankID
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/OnChangeVendBankID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method ValidateVendorID
   Description: Validates the vendor ID
   OperationID: ValidateVendorID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateVendorID(requestBody:ValidateVendorID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateVendorID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/ValidateVendorID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateVendorID_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/ValidatePLInvoiceReference", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewAPInvoiceLoad
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPInvoiceLoad
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPInvoiceLoad_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPInvoiceLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPInvoiceLoad(requestBody:GetNewAPInvoiceLoad_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPInvoiceLoad_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/GetNewAPInvoiceLoad", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAPInvoiceLoad_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/GetNewEntityGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceLoadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APInvoiceLoadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceLoadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APInvoiceLoadRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow,
}

export interface Erp_Tablesets_APInvoiceLoadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this is an "open" Payable.  */  
   "OpenPayable":boolean,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "InvoiceNum":string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   "DebitMemo":boolean,
      /**  Invoice date.  */  
   "InvoiceDate":string,
      /**  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   "TermsCode":string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   "TaxAmt":number,
      /**  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  */  
   "DocTaxAmt":number,
      /**  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  */  
   "DiscountDate":string,
      /**  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   "DiscountAmt":number,
      /**  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   "DocDiscountAmt":number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   "DueDate":string,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   "PayDates":string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   "PayAmounts":string,
      /**  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   "DocPayAmounts":string,
      /**  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  */  
   "GLPosted":boolean,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   "Posted":boolean,
      /**  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  */  
   "FiscalYear":number,
      /**  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  */  
   "FiscalPeriod":number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   "StartUp":boolean,
      /**  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  */  
   "InvoiceRef":string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   "EntryPerson":string,
      /**  Used to establish invoice comments about the overall invoice.  */  
   "InvoiceComment":string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   "InvoiceAmt":number,
      /**  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   "DocInvoiceAmt":number,
      /**  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  */  
   "DocInvoiceVendorAmt":number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   "InvoiceBal":number,
      /**  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  */  
   "DocInvoiceBal":number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "UnpostedBal":number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "DocUnpostedBal":number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  */  
   "InvoiceHeld":boolean,
      /**  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  */  
   "PayHold":boolean,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   "Description":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  */  
   "REFPONum":number,
      /**  The Tax Region for this invoice.  */  
   "TaxRegionCode":string,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  Journal that invoice was posted to.  */  
   "JournalCode":string,
      /**  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  */  
   "UpdateTax":boolean,
      /**  For use by external G/L interfacing.  This field is sign flipped for debit memos.  */  
   "InvoiceVendorAmt":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  External Identification of the Invoice.  */  
   "ExternalID":string,
      /**  Allows user to control discount amount manually or automatically  */  
   "FixedAmt":boolean,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefInvoiceNum":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   "GlbVendorNum":number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   "GlbInvoiceNum":string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "DepGainLoss":number,
      /**  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  */  
   "CPay":boolean,
      /**  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  */  
   "CPayLinked":boolean,
      /**  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  */  
   "CPayLegalNumber":string,
      /**  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   "CPayCheckNum":number,
      /**  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   "CPayCheckDate":string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  */  
   "CPayInvoiceBal":number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  */  
   "CPayDocInvoiceBal":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  */  
   "GLControlType":string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "DocRounding":number,
      /**  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  */  
   "GLControlCode":string,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt2PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt3PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnpostedBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnpostedBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnpostedBal":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   "Rpt1CPayInvoiceBal":number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   "Rpt2CPayInvoiceBal":number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   "Rpt3CPayInvoiceBal":number,
      /**  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  */  
   "AllowOverrideLI":boolean,
      /**  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  */  
   "MatchedFromLI":boolean,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   "ApplyDate":string,
      /**  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   "PayDiscDays":string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   "PayDiscPer":string,
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
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   "PayDiscPartPay":boolean,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   "PIPayment":string,
      /**  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  */  
   "CorrectionInv":boolean,
      /**  Tax Rate Group Code  */  
   "TaxRateGrpCode":string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   "LockTaxRate":boolean,
      /**  Sweden and Finland Localization Field - Banking Reference  */  
   "SEBankRef":string,
      /**  Sweden and Finland Localization Field - Payment Code  */  
   "SEPayCode":string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   "GUIFormatCode":string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   "GUITaxTypeCode":string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   "GUIDeductCode":string,
      /**  Indicates that this is pre-payment invoice.  */  
   "PrePayment":boolean,
      /**  Letter of Credit ID.  */  
   "APLOCID":string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**   Taiwan Localization
Tax Amount Basis  */  
   "GUIImportTaxBasis":number,
      /**   Taiwan Localization
Tax Amount Basis in document currrency  */  
   "DocGUIImportTaxBasis":number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt1 currency  */  
   "Rpt1GUIImportTaxBasis":number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt2 currency  */  
   "Rpt2GUIImportTaxBasis":number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt3 currency  */  
   "Rpt3GUIImportTaxBasis":number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   "OvrDefTaxDate":boolean,
      /**  Linked flag  */  
   "Linked":boolean,
      /**  The claim reference from the expense group that generated the invoice.  */  
   "ClaimRef":string,
      /**  The employee from the group of expenses that created the invoice.  */  
   "EmpID":string,
      /**  Indicates that Invoice has been selected for payment in a bankfile  */  
   "InBankFile":boolean,
      /**  Credit Note Confirmation Date  */  
   "CNConfirmDate":string,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Legal Number for the self assessment.  */  
   "SelfLegalNumber":string,
      /**  Transaction Document Type for the self assessment.  */  
   "SelfTranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**   Denmark Localization
Card (payment) code  */  
   "CardCode":string,
      /**  Site Code  */  
   "SiteCode":string,
      /**   Denmark Localization
Account Number  */  
   "BankGiroAcctNbr":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Supplier Agent Name  */  
   "SupAgentName":string,
      /**  Supplier Agent Tax Region Number  */  
   "SupAgentTaxRegNo":string,
      /**  Non Deductable Code  */  
   "NonDeductCode":string,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Card ID  */  
   "CardID":string,
      /**  Card Holder Tax ID  */  
   "CardHolderTaxID":string,
      /**  Card Member Name  */  
   "CardMemberName":string,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  Non Deductable VAT Amount  */  
   "NonDeductVATAmt":number,
      /**  Non Deductable VAT Doc Amount  */  
   "NonDeductVATDocAmt":number,
      /**  Non Deductable VAT Rpt1 Amount  */  
   "NonDeductVATRpt1Amt":number,
      /**  Non Deductable VAT Rpt2 Amount  */  
   "NonDeductVATRpt2Amt":number,
      /**  Non Deductable VAT Rpt3 Amount  */  
   "NonDeductVATRpt3Amt":number,
      /**  Stores the number of the import document.  */  
   "ImportNum":string,
      /**  Country of Import  */  
   "ImportedFrom":string,
      /**  Date of import.  */  
   "ImportedDate":string,
      /**   Indicates that this is Advanced Tax invoice received from
supplier  */  
   "AdvTaxInv":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
      /**  Exchange Rate Label  */  
   "XRateLabel":string,
      /**  Display field for Invoice Balance  */  
   "DispInvoiceBal":number,
      /**  Display field for DocInvoiceBal  */  
   "DocDispInvoiceBal":number,
      /**  Flag to indicate if the Legal Number should be enabled.  */  
   "UseLegalNumber":boolean,
   "Rpt1DispInvoiceBal":number,
   "Rpt2DispInvoiceBal":number,
   "Rpt3DispInvoiceBal":number,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCurrDesc":string,
      /**  GL Control description.  */  
   "GLCntrlDescription":string,
      /**  GL Control Type description  */  
   "GLCntrlTypeDescription":string,
      /**  Description  */  
   "RateGrpCodeDescription":string,
      /**  Full description of terms....this is printed on purchase orders. Can't be blank.  */  
   "TermsDescription":string,
      /**  A unique code that identifies the currency.  */  
   "VendorCurrencyCode":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorZIP":string,
      /**  Can be blank.  */  
   "VendorState":string,
      /**  First address line of the Supplier  */  
   "VendorAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorAddress3":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APInvoiceLoadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this is an "open" Payable.  */  
   "OpenPayable":boolean,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "InvoiceNum":string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   "DebitMemo":boolean,
      /**  Invoice date.  */  
   "InvoiceDate":string,
      /**  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   "TermsCode":string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   "TaxAmt":number,
      /**  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  */  
   "DocTaxAmt":number,
      /**  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  */  
   "DiscountDate":string,
      /**  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   "DiscountAmt":number,
      /**  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   "DocDiscountAmt":number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   "DueDate":string,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   "PayDates":string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   "PayAmounts":string,
      /**  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   "DocPayAmounts":string,
      /**  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  */  
   "GLPosted":boolean,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   "Posted":boolean,
      /**  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  */  
   "FiscalYear":number,
      /**  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  */  
   "FiscalPeriod":number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   "StartUp":boolean,
      /**  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  */  
   "InvoiceRef":string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   "EntryPerson":string,
      /**  Used to establish invoice comments about the overall invoice.  */  
   "InvoiceComment":string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   "InvoiceAmt":number,
      /**  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   "DocInvoiceAmt":number,
      /**  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  */  
   "DocInvoiceVendorAmt":number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   "InvoiceBal":number,
      /**  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  */  
   "DocInvoiceBal":number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "UnpostedBal":number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "DocUnpostedBal":number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  */  
   "InvoiceHeld":boolean,
      /**  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  */  
   "PayHold":boolean,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   "Description":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  */  
   "REFPONum":number,
      /**  The Tax Region for this invoice.  */  
   "TaxRegionCode":string,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  Journal that invoice was posted to.  */  
   "JournalCode":string,
      /**  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  */  
   "UpdateTax":boolean,
      /**  For use by external G/L interfacing.  This field is sign flipped for debit memos.  */  
   "InvoiceVendorAmt":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  External Identification of the Invoice.  */  
   "ExternalID":string,
      /**  Allows user to control discount amount manually or automatically  */  
   "FixedAmt":boolean,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefInvoiceNum":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   "GlbVendorNum":number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   "GlbInvoiceNum":string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "DepGainLoss":number,
      /**  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  */  
   "CPay":boolean,
      /**  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  */  
   "CPayLinked":boolean,
      /**  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  */  
   "CPayLegalNumber":string,
      /**  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   "CPayCheckNum":number,
      /**  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   "CPayCheckDate":string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  */  
   "CPayInvoiceBal":number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  */  
   "CPayDocInvoiceBal":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  */  
   "GLControlType":string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "DocRounding":number,
      /**  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  */  
   "GLControlCode":string,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt2PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt3PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnpostedBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnpostedBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnpostedBal":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   "Rpt1CPayInvoiceBal":number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   "Rpt2CPayInvoiceBal":number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   "Rpt3CPayInvoiceBal":number,
      /**  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  */  
   "AllowOverrideLI":boolean,
      /**  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  */  
   "MatchedFromLI":boolean,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   "ApplyDate":string,
      /**  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   "PayDiscDays":string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   "PayDiscPer":string,
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
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   "PayDiscPartPay":boolean,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   "PIPayment":string,
      /**  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  */  
   "CorrectionInv":boolean,
      /**  Tax Rate Group Code  */  
   "TaxRateGrpCode":string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   "LockTaxRate":boolean,
      /**  Sweden and Finland Localization Field - Banking Reference  */  
   "SEBankRef":string,
      /**  Sweden and Finland Localization Field - Payment Code  */  
   "SEPayCode":string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   "GUIFormatCode":string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   "GUITaxTypeCode":string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   "GUIDeductCode":string,
      /**  Indicates that this is pre-payment invoice.  */  
   "PrePayment":boolean,
      /**  Letter of Credit ID.  */  
   "APLOCID":string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**   Taiwan Localization
Tax Amount Basis  */  
   "GUIImportTaxBasis":number,
      /**   Taiwan Localization
Tax Amount Basis in document currrency  */  
   "DocGUIImportTaxBasis":number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt1 currency  */  
   "Rpt1GUIImportTaxBasis":number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt2 currency  */  
   "Rpt2GUIImportTaxBasis":number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt3 currency  */  
   "Rpt3GUIImportTaxBasis":number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   "OvrDefTaxDate":boolean,
      /**  Linked flag  */  
   "Linked":boolean,
      /**  The claim reference from the expense group that generated the invoice.  */  
   "ClaimRef":string,
      /**  The employee from the group of expenses that created the invoice.  */  
   "EmpID":string,
      /**  Indicates that Invoice has been selected for payment in a bankfile  */  
   "InBankFile":boolean,
      /**  Credit Note Confirmation Date  */  
   "CNConfirmDate":string,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Legal Number for the self assessment.  */  
   "SelfLegalNumber":string,
      /**  Transaction Document Type for the self assessment.  */  
   "SelfTranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**   Denmark Localization
Card (payment) code  */  
   "CardCode":string,
      /**  Site Code  */  
   "SiteCode":string,
      /**   Denmark Localization
Account Number  */  
   "BankGiroAcctNbr":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Supplier Agent Name  */  
   "SupAgentName":string,
      /**  Supplier Agent Tax Region Number  */  
   "SupAgentTaxRegNo":string,
      /**  Non Deductable Code  */  
   "NonDeductCode":string,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Card ID  */  
   "CardID":string,
      /**  Card Holder Tax ID  */  
   "CardHolderTaxID":string,
      /**  Card Member Name  */  
   "CardMemberName":string,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  Non Deductable VAT Amount  */  
   "NonDeductVATAmt":number,
      /**  Non Deductable VAT Doc Amount  */  
   "NonDeductVATDocAmt":number,
      /**  Non Deductable VAT Rpt1 Amount  */  
   "NonDeductVATRpt1Amt":number,
      /**  Non Deductable VAT Rpt2 Amount  */  
   "NonDeductVATRpt2Amt":number,
      /**  Non Deductable VAT Rpt3 Amount  */  
   "NonDeductVATRpt3Amt":number,
      /**  Stores the number of the import document.  */  
   "ImportNum":string,
      /**  Country of Import  */  
   "ImportedFrom":string,
      /**  Date of import.  */  
   "ImportedDate":string,
      /**   Indicates that this is Advanced Tax invoice received from
supplier  */  
   "AdvTaxInv":boolean,
      /**   Indicates that the tax is included in the unit price
for this AP Invoice  */  
   "InPrice":boolean,
      /**  Transaction Document Type ID  */  
   "TranDocTypeID":string,
      /**  Reserved for Development - Integer  */  
   "DevInt1":number,
      /**  Reserved for Development - Integer  */  
   "DevInt2":number,
      /**  Reserved for development - decimal  */  
   "DevDec1":number,
      /**  Reserved for development - decimal  */  
   "DevDec2":number,
      /**  Reserved for development - decimal  */  
   "DevDec3":number,
      /**  Reserved for development - decimal  */  
   "DevDec4":number,
      /**  In case of Tax Inclusive Pricing if system-calculated Header related taxes are changed/deleted/added  by the user - this field is set to true by the system.  */  
   "DevLog1":boolean,
      /**  Reserved for development - logical  */  
   "DevLog2":boolean,
      /**  Assigned as "I" when Recurring Invoice has Inactive status.  */  
   "DevChar1":string,
      /**  Reserved for development - character  */  
   "DevChar2":string,
      /**  Reserved for development - date  */  
   "DevDate1":string,
      /**  Reserved for development - date  */  
   "DevDate2":string,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  CycleCode  */  
   "CycleCode":string,
      /**  Duration  */  
   "Duration":number,
      /**  EndDate  */  
   "EndDate":string,
      /**  MaxValueAmt  */  
   "MaxValueAmt":number,
      /**  DocMaxValueAmt  */  
   "DocMaxValueAmt":number,
      /**  Rpt1MaxValueAmt  */  
   "Rpt1MaxValueAmt":number,
      /**  Rpt2MaxValueAmt  */  
   "Rpt2MaxValueAmt":number,
      /**  Rpt3MaxValueAmt  */  
   "Rpt3MaxValueAmt":number,
      /**  HoldInvoice  */  
   "HoldInvoice":boolean,
      /**  CopyLatestInvoice  */  
   "CopyLatestInvoice":boolean,
      /**  OverrideEndDate  */  
   "OverrideEndDate":boolean,
      /**  CycleInactive  */  
   "CycleInactive":boolean,
      /**  RecurSource  */  
   "RecurSource":boolean,
      /**  InstanceNum  */  
   "InstanceNum":number,
      /**  RecurBalance  */  
   "RecurBalance":number,
      /**  DocRecurBalance  */  
   "DocRecurBalance":number,
      /**  Rpt1RecurBalance  */  
   "Rpt1RecurBalance":number,
      /**  Rpt2RecurBalance  */  
   "Rpt2RecurBalance":number,
      /**  Rpt3RecurBalance  */  
   "Rpt3RecurBalance":number,
      /**  LastDate  */  
   "LastDate":string,
      /**  IsRecurring  */  
   "IsRecurring":boolean,
      /**  InvoiceNumList  */  
   "InvoiceNumList":string,
      /**  IsMaxValue  */  
   "IsMaxValue":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CHISRCodeLine  */  
   "CHISRCodeLine":string,
      /**  DMReason  */  
   "DMReason":string,
      /**  UrgentPayment  */  
   "UrgentPayment":boolean,
      /**  AGDocPageNum  */  
   "AGDocPageNum":string,
      /**  AGCAICAEMark  */  
   "AGCAICAEMark":string,
      /**  AGCAICAENum  */  
   "AGCAICAENum":string,
      /**  AGCAICAEExpirationDate  */  
   "AGCAICAEExpirationDate":string,
      /**  AGAvTaxCreditFlag  */  
   "AGAvTaxCreditFlag":boolean,
      /**  AGUseGoodDefaultMark  */  
   "AGUseGoodDefaultMark":boolean,
      /**  AGCustomsClearanceNum  */  
   "AGCustomsClearanceNum":string,
      /**  AGCustomsCode  */  
   "AGCustomsCode":string,
      /**  AGDestinationCode  */  
   "AGDestinationCode":string,
      /**  Header Number  */  
   "HeadNum":number,
      /**  TranType  */  
   "TranType":string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   "TaxSvcID":string,
      /**  TWDeclareYear  */  
   "TWDeclareYear":number,
      /**  TWDeclarePeriod  */  
   "TWDeclarePeriod":number,
      /**  AP Checking Group ID  */  
   "APChkGrpID":string,
      /**  Invoice Type  */  
   "InvoiceType":string,
      /**  Indicates a computational cost for the invoice  */  
   "PEComputationalCost":string,
      /**  Referenced By BOE  */  
   "ReferencedByBOE":string,
      /**  DUA Reference Number used on Peru Localiation  */  
   "PEDUARefNum":string,
      /**  CustomsNumber  */  
   "CustomsNumber":string,
      /**  ReceivedDate  */  
   "ReceivedDate":string,
      /**  CustOverride  */  
   "CustOverride":number,
      /**  Invoice Number of Invoice Pre-Payment which should be automatically applied to this one during posting process.  */  
   "PrePaymentNum":string,
      /**  Pre-Payment amount in Base Currency.  */  
   "PrePaymentAmt":number,
      /**  Pre-Payment amount in Document Currency.  */  
   "DocPrePaymentAmt":number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   "Rpt1PrePaymentAmt":number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   "Rpt2PrePaymentAmt":number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   "Rpt3PrePaymentAmt":number,
      /**  CSF Peru - AP Payment Number  */  
   "PEAPPayNum":number,
      /**  SCF Peru - Detractions Tax Amount  */  
   "PEDetTaxAmt":number,
      /**  Peru Detraction Tax Currency Code  */  
   "PEDetTaxCurrencyCode":string,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   "PESUNATDepAmt":number,
      /**  Peru Document SUNAT Deposit Amount  */  
   "DocPESUNATDepAmt":number,
      /**  CSF Peru - SUNAT Deposit Date  */  
   "PESUNATDepDate":string,
      /**  CSF Peru -  SUNAT Deposit Number  */  
   "PESUNATDepNum":string,
      /**  SUNAT Reference Number. Once a payment is made, the SUNAT returns a reference number used as the receipt number for the payment.  */  
   "PESUNATNum":string,
      /**  Document Tax Amount used in Peru detractions  */  
   "DocPEDetTaxAmt":number,
      /**  MXFiscalFolio  */  
   "MXFiscalFolio":string,
      /**  PEBOEIsMultiGen  */  
   "PEBOEIsMultiGen":boolean,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  PrePayHeadNum  */  
   "PrePayHeadNum":number,
      /**  MXRetentionCode  */  
   "MXRetentionCode":string,
      /**  PE Reference Document ID  */  
   "PERefDocID":string,
      /**  PE Reason Code  */  
   "PEReasonCode":string,
      /**  PE Reason Description  */  
   "PEReasonDesc":string,
      /**  Malaysia Import Declaration Number  */  
   "MYImportNum":string,
      /**  TW GUI Code Seller  */  
   "TWGUIRegNumSeller":string,
      /**  TW GUI Code Buyer  */  
   "TWGUIRegNumBuyer":string,
      /**  MXTARCode  */  
   "MXTARCode":string,
      /**  Flag that indicates if the invoice is a GRNI document.  */  
   "GRNIClearing":boolean,
      /**  CSF Peru - Fiscal Credit Operation Status  */  
   "PEFiscalCreditOperStatus":number,
      /**  CSF Peru - International Tax agreement  */  
   "PEInternatTaxAgr":string,
      /**  CSF Peru - Rent type  */  
   "PERentType":string,
      /**  CSF Peru - Purchase  type  */  
   "PEPurchaseType":string,
      /**  TH Reference Invoice Num  */  
   "THRefInvoiceNum":string,
      /**  TH Reference Vendor Num  */  
   "THRefVendorNum":number,
      /**  Day when a company sums up accounts payable for supplier  */  
   "JPSummarizationDate":string,
      /**  Date of a Payment Statement  */  
   "JPBillingDate":string,
      /**  Legal Number of Payment Statement  */  
   "JPBillingNumber":string,
      /**  SelfInvoice  */  
   "SelfInvoice":boolean,
      /**  Printed  */  
   "Printed":boolean,
      /**  PurPoint  */  
   "PurPoint":string,
      /**  PLInvoiceReference  */  
   "PLInvoiceReference":string,
      /**  INPortCode  */  
   "INPortCode":string,
      /**  Indicates which invoice number has cancelled this invoice.  */  
   "RefCancelledby":string,
      /**  Indicates if this invoice is a cancellation invoice.  */  
   "CancellationInv":boolean,
      /**  Id of the netting transaction that generated this document.  */  
   "NettingID":number,
      /**  WithholdAcctToInterim  */  
   "WithholdAcctToInterim":boolean,
      /**  APTaxRoundOption  */  
   "APTaxRoundOption":number,
      /**  Source Plant used for multi site GL  */  
   "SourcePlant":string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   "ExtSysType":string,
      /**  URL for drill back to an integrated external system  */  
   "ExtSysURL":string,
      /**  CHQRIBAN  */  
   "CHQRIBAN":string,
      /**  CHQRReference  */  
   "CHQRReference":string,
      /**  Set to True for any invoice that is created via EDI  */  
   "EDIInvoice":boolean,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
      /**  1099 Code Description, defaults from Supplier  */  
   "Code1099Description":string,
      /**  1099 Code, defaults from Supplier  */  
   "Code1099ID":string,
      /**  Display field for Invoice Balance  */  
   "DispInvoiceBal":number,
      /**  Form Type Description  */  
   "FormTypeDescription":string,
      /**  Form Type ID  */  
   "FormTypeID":string,
      /**  Indicates whether created invoice should be paid.  */  
   "Paid":boolean,
      /**  CSF Poland. Vendor uses Invoice reference number  */  
   "PLVendorAutoInvoiceNum":boolean,
   "Print1099":boolean,
   "Rpt1DispInvoiceBal":number,
   "Rpt2DispInvoiceBal":number,
   "Rpt3DispInvoiceBal":number,
      /**  Taxable Value 1  */  
   "TaxableAmt1":number,
      /**  Taxable Value 2  */  
   "TaxableAmt2":number,
      /**  Taxable Value 3  */  
   "TaxableAmt3":number,
      /**  Taxable Value 4  */  
   "TaxableAmt4":number,
      /**  Tax Value 1  */  
   "TaxAmt1":number,
      /**  Tax Value 2  */  
   "TaxAmt2":number,
      /**  Tax Value 3  */  
   "TaxAmt3":number,
      /**  Tax Value 4  */  
   "TaxAmt4":number,
      /**  Tax Type 1  */  
   "TaxCode1":string,
   "TaxCode1Description":string,
      /**  Tax Type 2  */  
   "TaxCode2":string,
   "TaxCode2Description":string,
      /**  Tax Type 3  */  
   "TaxCode3":string,
   "TaxCode3Description":string,
      /**  Tax Type 4  */  
   "TaxCode4":string,
   "TaxCode4Description":string,
      /**  Tax Rate 1  */  
   "TaxRate1":string,
   "TaxRate1Description":string,
      /**  Tax Rate 2  */  
   "TaxRate2":string,
   "TaxRate2Description":string,
      /**  Tax Rate 3  */  
   "TaxRate3":string,
   "TaxRate3Description":string,
      /**  Tax Rate 4  */  
   "TaxRate4":string,
   "TaxRate4Description":string,
      /**  Flag to indicate if the Legal Number should be enabled.  */  
   "UseLegalNumber":boolean,
      /**  Exchange Rate Label  */  
   "XRateLabel":string,
   "BankName":string,
      /**  Display field for DocInvoiceBal  */  
   "DocDispInvoiceBal":number,
      /**  Site is a legal entity  */  
   "SiteIsLegalEntity":boolean,
   "BitFlag":number,
   "CurrencyCurrencyID":string,
   "CurrencyCurrDesc":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrName":string,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
   "RateGrpCodeDescription":string,
   "SourcePlantName":string,
   "TaxRgnDescription":string,
   "TermsDescription":string,
   "VendorName":string,
   "VendorZIP":string,
   "VendorCity":string,
   "VendorDefaultFOB":string,
   "VendorState":string,
   "VendorAddress1":string,
   "VendorAddress2":string,
   "VendorCountry":string,
   "VendorTermsCode":string,
   "VendorAddress3":string,
   "VendorCurrencyCode":string,
   "VendorVendorID":string,
   "XbSystIsDiscountforDebitM":boolean,
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




//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
      @param formTypeID
      @param proposedCode1099ID
      @param ds
   */  
export interface Change1099Code_input{
   formTypeID:string,
   proposedCode1099ID:string,
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
}

export interface Change1099Code_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeApplyDate_input{
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
}

export interface ChangeApplyDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
}
}

   /** Required : 
      @param formType
      @param ds
   */  
export interface ChangeFormType_input{
   formType:string,
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
}

export interface ChangeFormType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
}
}

   /** Required : 
      @param ds
      @param ipChangeType
   */  
export interface ChangeInvoiceBalance_input{
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
      /**  Valid values: 'E' = Exchange Rate; 'B' = DispInvoiceBal; 'D' = DocDispInvoiceBal
            'B1' = InvoiceBal; 'D1' = DocInvoiceBal  */  
   ipChangeType:string,
}

export interface ChangeInvoiceBalance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeInvoiceDate_input{
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
}

export interface ChangeInvoiceDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTerms_input{
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
}

export interface ChangeTerms_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
}
}

   /** Required : 
      @param ds
      @param ipProposedVendorID
   */  
export interface ChangeVendorID_input{
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
      /**  The proposed Vendor ID  */  
   ipProposedVendorID:string,
}

export interface ChangeVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
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

export interface Erp_Tablesets_APInvoiceLoadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this is an "open" Payable.  */  
   OpenPayable:boolean,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   InvoiceNum:string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   DebitMemo:boolean,
      /**  Invoice date.  */  
   InvoiceDate:string,
      /**  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   TaxAmt:number,
      /**  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  */  
   DocTaxAmt:number,
      /**  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  */  
   DiscountDate:string,
      /**  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   DiscountAmt:number,
      /**  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   DocDiscountAmt:number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDates:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   PayAmounts:string,
      /**  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   DocPayAmounts:string,
      /**  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  */  
   GLPosted:boolean,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  */  
   FiscalYear:number,
      /**  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  */  
   FiscalPeriod:number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   StartUp:boolean,
      /**  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  */  
   InvoiceRef:string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  Used to establish invoice comments about the overall invoice.  */  
   InvoiceComment:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  */  
   DocInvoiceVendorAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnpostedBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   DocUnpostedBal:number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  */  
   InvoiceHeld:boolean,
      /**  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  */  
   PayHold:boolean,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   Description:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  */  
   REFPONum:number,
      /**  The Tax Region for this invoice.  */  
   TaxRegionCode:string,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Journal that invoice was posted to.  */  
   JournalCode:string,
      /**  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  */  
   UpdateTax:boolean,
      /**  For use by external G/L interfacing.  This field is sign flipped for debit memos.  */  
   InvoiceVendorAmt:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  External Identification of the Invoice.  */  
   ExternalID:string,
      /**  Allows user to control discount amount manually or automatically  */  
   FixedAmt:boolean,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefInvoiceNum:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceNum:string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   DepGainLoss:number,
      /**  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  */  
   CPay:boolean,
      /**  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  */  
   CPayLinked:boolean,
      /**  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  */  
   CPayLegalNumber:string,
      /**  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   CPayCheckNum:number,
      /**  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   CPayCheckDate:string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  */  
   CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  */  
   CPayDocInvoiceBal:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  */  
   GLControlType:string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  */  
   GLControlCode:string,
      /**  Reporting currency value of this field  */  
   Rpt1DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscountAmt:number,
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
   Rpt1InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt2PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt3PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnpostedBal:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   Rpt1CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   Rpt2CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   Rpt3CPayInvoiceBal:number,
      /**  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  */  
   AllowOverrideLI:boolean,
      /**  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  */  
   MatchedFromLI:boolean,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDiscDays:string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   PayDiscPer:string,
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
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PayDiscPartPay:boolean,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   PIPayment:string,
      /**  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  */  
   CorrectionInv:boolean,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden and Finland Localization Field - Banking Reference  */  
   SEBankRef:string,
      /**  Sweden and Finland Localization Field - Payment Code  */  
   SEPayCode:string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Indicates that this is pre-payment invoice.  */  
   PrePayment:boolean,
      /**  Letter of Credit ID.  */  
   APLOCID:string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**   Taiwan Localization
Tax Amount Basis  */  
   GUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in document currrency  */  
   DocGUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt1 currency  */  
   Rpt1GUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt2 currency  */  
   Rpt2GUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt3 currency  */  
   Rpt3GUIImportTaxBasis:number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   OvrDefTaxDate:boolean,
      /**  Linked flag  */  
   Linked:boolean,
      /**  The claim reference from the expense group that generated the invoice.  */  
   ClaimRef:string,
      /**  The employee from the group of expenses that created the invoice.  */  
   EmpID:string,
      /**  Indicates that Invoice has been selected for payment in a bankfile  */  
   InBankFile:boolean,
      /**  Credit Note Confirmation Date  */  
   CNConfirmDate:string,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Legal Number for the self assessment.  */  
   SelfLegalNumber:string,
      /**  Transaction Document Type for the self assessment.  */  
   SelfTranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**   Denmark Localization
Card (payment) code  */  
   CardCode:string,
      /**  Site Code  */  
   SiteCode:string,
      /**   Denmark Localization
Account Number  */  
   BankGiroAcctNbr:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Supplier Agent Name  */  
   SupAgentName:string,
      /**  Supplier Agent Tax Region Number  */  
   SupAgentTaxRegNo:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Card ID  */  
   CardID:string,
      /**  Card Holder Tax ID  */  
   CardHolderTaxID:string,
      /**  Card Member Name  */  
   CardMemberName:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Non Deductable VAT Amount  */  
   NonDeductVATAmt:number,
      /**  Non Deductable VAT Doc Amount  */  
   NonDeductVATDocAmt:number,
      /**  Non Deductable VAT Rpt1 Amount  */  
   NonDeductVATRpt1Amt:number,
      /**  Non Deductable VAT Rpt2 Amount  */  
   NonDeductVATRpt2Amt:number,
      /**  Non Deductable VAT Rpt3 Amount  */  
   NonDeductVATRpt3Amt:number,
      /**  Stores the number of the import document.  */  
   ImportNum:string,
      /**  Country of Import  */  
   ImportedFrom:string,
      /**  Date of import.  */  
   ImportedDate:string,
      /**   Indicates that this is Advanced Tax invoice received from
supplier  */  
   AdvTaxInv:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  Exchange Rate Label  */  
   XRateLabel:string,
      /**  Display field for Invoice Balance  */  
   DispInvoiceBal:number,
      /**  Display field for DocInvoiceBal  */  
   DocDispInvoiceBal:number,
      /**  Flag to indicate if the Legal Number should be enabled.  */  
   UseLegalNumber:boolean,
   Rpt1DispInvoiceBal:number,
   Rpt2DispInvoiceBal:number,
   Rpt3DispInvoiceBal:number,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCurrName:string,
      /**  Description of the currency  */  
   CurrencyCurrDesc:string,
      /**  GL Control description.  */  
   GLCntrlDescription:string,
      /**  GL Control Type description  */  
   GLCntrlTypeDescription:string,
      /**  Description  */  
   RateGrpCodeDescription:string,
      /**  Full description of terms....this is printed on purchase orders. Can't be blank.  */  
   TermsDescription:string,
      /**  A unique code that identifies the currency.  */  
   VendorCurrencyCode:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorZIP:string,
      /**  Can be blank.  */  
   VendorState:string,
      /**  First address line of the Supplier  */  
   VendorAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorAddress3:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APInvoiceLoadListTableset{
   APInvoiceLoadList:Erp_Tablesets_APInvoiceLoadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APInvoiceLoadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this is an "open" Payable.  */  
   OpenPayable:boolean,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   InvoiceNum:string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   DebitMemo:boolean,
      /**  Invoice date.  */  
   InvoiceDate:string,
      /**  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   TaxAmt:number,
      /**  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  */  
   DocTaxAmt:number,
      /**  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  */  
   DiscountDate:string,
      /**  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   DiscountAmt:number,
      /**  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   DocDiscountAmt:number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDates:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   PayAmounts:string,
      /**  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   DocPayAmounts:string,
      /**  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  */  
   GLPosted:boolean,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  */  
   FiscalYear:number,
      /**  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  */  
   FiscalPeriod:number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   StartUp:boolean,
      /**  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  */  
   InvoiceRef:string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  Used to establish invoice comments about the overall invoice.  */  
   InvoiceComment:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  */  
   DocInvoiceVendorAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnpostedBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   DocUnpostedBal:number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  */  
   InvoiceHeld:boolean,
      /**  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  */  
   PayHold:boolean,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   Description:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  */  
   REFPONum:number,
      /**  The Tax Region for this invoice.  */  
   TaxRegionCode:string,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Journal that invoice was posted to.  */  
   JournalCode:string,
      /**  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  */  
   UpdateTax:boolean,
      /**  For use by external G/L interfacing.  This field is sign flipped for debit memos.  */  
   InvoiceVendorAmt:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  External Identification of the Invoice.  */  
   ExternalID:string,
      /**  Allows user to control discount amount manually or automatically  */  
   FixedAmt:boolean,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefInvoiceNum:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceNum:string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   DepGainLoss:number,
      /**  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  */  
   CPay:boolean,
      /**  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  */  
   CPayLinked:boolean,
      /**  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  */  
   CPayLegalNumber:string,
      /**  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   CPayCheckNum:number,
      /**  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   CPayCheckDate:string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  */  
   CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  */  
   CPayDocInvoiceBal:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  */  
   GLControlType:string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  */  
   GLControlCode:string,
      /**  Reporting currency value of this field  */  
   Rpt1DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscountAmt:number,
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
   Rpt1InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt2PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt3PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnpostedBal:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   Rpt1CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   Rpt2CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   Rpt3CPayInvoiceBal:number,
      /**  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  */  
   AllowOverrideLI:boolean,
      /**  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  */  
   MatchedFromLI:boolean,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDiscDays:string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   PayDiscPer:string,
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
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PayDiscPartPay:boolean,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   PIPayment:string,
      /**  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  */  
   CorrectionInv:boolean,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden and Finland Localization Field - Banking Reference  */  
   SEBankRef:string,
      /**  Sweden and Finland Localization Field - Payment Code  */  
   SEPayCode:string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Indicates that this is pre-payment invoice.  */  
   PrePayment:boolean,
      /**  Letter of Credit ID.  */  
   APLOCID:string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**   Taiwan Localization
Tax Amount Basis  */  
   GUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in document currrency  */  
   DocGUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt1 currency  */  
   Rpt1GUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt2 currency  */  
   Rpt2GUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt3 currency  */  
   Rpt3GUIImportTaxBasis:number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   OvrDefTaxDate:boolean,
      /**  Linked flag  */  
   Linked:boolean,
      /**  The claim reference from the expense group that generated the invoice.  */  
   ClaimRef:string,
      /**  The employee from the group of expenses that created the invoice.  */  
   EmpID:string,
      /**  Indicates that Invoice has been selected for payment in a bankfile  */  
   InBankFile:boolean,
      /**  Credit Note Confirmation Date  */  
   CNConfirmDate:string,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Legal Number for the self assessment.  */  
   SelfLegalNumber:string,
      /**  Transaction Document Type for the self assessment.  */  
   SelfTranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**   Denmark Localization
Card (payment) code  */  
   CardCode:string,
      /**  Site Code  */  
   SiteCode:string,
      /**   Denmark Localization
Account Number  */  
   BankGiroAcctNbr:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Supplier Agent Name  */  
   SupAgentName:string,
      /**  Supplier Agent Tax Region Number  */  
   SupAgentTaxRegNo:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Card ID  */  
   CardID:string,
      /**  Card Holder Tax ID  */  
   CardHolderTaxID:string,
      /**  Card Member Name  */  
   CardMemberName:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Non Deductable VAT Amount  */  
   NonDeductVATAmt:number,
      /**  Non Deductable VAT Doc Amount  */  
   NonDeductVATDocAmt:number,
      /**  Non Deductable VAT Rpt1 Amount  */  
   NonDeductVATRpt1Amt:number,
      /**  Non Deductable VAT Rpt2 Amount  */  
   NonDeductVATRpt2Amt:number,
      /**  Non Deductable VAT Rpt3 Amount  */  
   NonDeductVATRpt3Amt:number,
      /**  Stores the number of the import document.  */  
   ImportNum:string,
      /**  Country of Import  */  
   ImportedFrom:string,
      /**  Date of import.  */  
   ImportedDate:string,
      /**   Indicates that this is Advanced Tax invoice received from
supplier  */  
   AdvTaxInv:boolean,
      /**   Indicates that the tax is included in the unit price
for this AP Invoice  */  
   InPrice:boolean,
      /**  Transaction Document Type ID  */  
   TranDocTypeID:string,
      /**  Reserved for Development - Integer  */  
   DevInt1:number,
      /**  Reserved for Development - Integer  */  
   DevInt2:number,
      /**  Reserved for development - decimal  */  
   DevDec1:number,
      /**  Reserved for development - decimal  */  
   DevDec2:number,
      /**  Reserved for development - decimal  */  
   DevDec3:number,
      /**  Reserved for development - decimal  */  
   DevDec4:number,
      /**  In case of Tax Inclusive Pricing if system-calculated Header related taxes are changed/deleted/added  by the user - this field is set to true by the system.  */  
   DevLog1:boolean,
      /**  Reserved for development - logical  */  
   DevLog2:boolean,
      /**  Assigned as "I" when Recurring Invoice has Inactive status.  */  
   DevChar1:string,
      /**  Reserved for development - character  */  
   DevChar2:string,
      /**  Reserved for development - date  */  
   DevDate1:string,
      /**  Reserved for development - date  */  
   DevDate2:string,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  CycleCode  */  
   CycleCode:string,
      /**  Duration  */  
   Duration:number,
      /**  EndDate  */  
   EndDate:string,
      /**  MaxValueAmt  */  
   MaxValueAmt:number,
      /**  DocMaxValueAmt  */  
   DocMaxValueAmt:number,
      /**  Rpt1MaxValueAmt  */  
   Rpt1MaxValueAmt:number,
      /**  Rpt2MaxValueAmt  */  
   Rpt2MaxValueAmt:number,
      /**  Rpt3MaxValueAmt  */  
   Rpt3MaxValueAmt:number,
      /**  HoldInvoice  */  
   HoldInvoice:boolean,
      /**  CopyLatestInvoice  */  
   CopyLatestInvoice:boolean,
      /**  OverrideEndDate  */  
   OverrideEndDate:boolean,
      /**  CycleInactive  */  
   CycleInactive:boolean,
      /**  RecurSource  */  
   RecurSource:boolean,
      /**  InstanceNum  */  
   InstanceNum:number,
      /**  RecurBalance  */  
   RecurBalance:number,
      /**  DocRecurBalance  */  
   DocRecurBalance:number,
      /**  Rpt1RecurBalance  */  
   Rpt1RecurBalance:number,
      /**  Rpt2RecurBalance  */  
   Rpt2RecurBalance:number,
      /**  Rpt3RecurBalance  */  
   Rpt3RecurBalance:number,
      /**  LastDate  */  
   LastDate:string,
      /**  IsRecurring  */  
   IsRecurring:boolean,
      /**  InvoiceNumList  */  
   InvoiceNumList:string,
      /**  IsMaxValue  */  
   IsMaxValue:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHISRCodeLine  */  
   CHISRCodeLine:string,
      /**  DMReason  */  
   DMReason:string,
      /**  UrgentPayment  */  
   UrgentPayment:boolean,
      /**  AGDocPageNum  */  
   AGDocPageNum:string,
      /**  AGCAICAEMark  */  
   AGCAICAEMark:string,
      /**  AGCAICAENum  */  
   AGCAICAENum:string,
      /**  AGCAICAEExpirationDate  */  
   AGCAICAEExpirationDate:string,
      /**  AGAvTaxCreditFlag  */  
   AGAvTaxCreditFlag:boolean,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  AGCustomsClearanceNum  */  
   AGCustomsClearanceNum:string,
      /**  AGCustomsCode  */  
   AGCustomsCode:string,
      /**  AGDestinationCode  */  
   AGDestinationCode:string,
      /**  Header Number  */  
   HeadNum:number,
      /**  TranType  */  
   TranType:string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   TaxSvcID:string,
      /**  TWDeclareYear  */  
   TWDeclareYear:number,
      /**  TWDeclarePeriod  */  
   TWDeclarePeriod:number,
      /**  AP Checking Group ID  */  
   APChkGrpID:string,
      /**  Invoice Type  */  
   InvoiceType:string,
      /**  Indicates a computational cost for the invoice  */  
   PEComputationalCost:string,
      /**  Referenced By BOE  */  
   ReferencedByBOE:string,
      /**  DUA Reference Number used on Peru Localiation  */  
   PEDUARefNum:string,
      /**  CustomsNumber  */  
   CustomsNumber:string,
      /**  ReceivedDate  */  
   ReceivedDate:string,
      /**  CustOverride  */  
   CustOverride:number,
      /**  Invoice Number of Invoice Pre-Payment which should be automatically applied to this one during posting process.  */  
   PrePaymentNum:string,
      /**  Pre-Payment amount in Base Currency.  */  
   PrePaymentAmt:number,
      /**  Pre-Payment amount in Document Currency.  */  
   DocPrePaymentAmt:number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   Rpt1PrePaymentAmt:number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   Rpt2PrePaymentAmt:number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   Rpt3PrePaymentAmt:number,
      /**  CSF Peru - AP Payment Number  */  
   PEAPPayNum:number,
      /**  SCF Peru - Detractions Tax Amount  */  
   PEDetTaxAmt:number,
      /**  Peru Detraction Tax Currency Code  */  
   PEDetTaxCurrencyCode:string,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   PESUNATDepAmt:number,
      /**  Peru Document SUNAT Deposit Amount  */  
   DocPESUNATDepAmt:number,
      /**  CSF Peru - SUNAT Deposit Date  */  
   PESUNATDepDate:string,
      /**  CSF Peru -  SUNAT Deposit Number  */  
   PESUNATDepNum:string,
      /**  SUNAT Reference Number. Once a payment is made, the SUNAT returns a reference number used as the receipt number for the payment.  */  
   PESUNATNum:string,
      /**  Document Tax Amount used in Peru detractions  */  
   DocPEDetTaxAmt:number,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  PEBOEIsMultiGen  */  
   PEBOEIsMultiGen:boolean,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  PrePayHeadNum  */  
   PrePayHeadNum:number,
      /**  MXRetentionCode  */  
   MXRetentionCode:string,
      /**  PE Reference Document ID  */  
   PERefDocID:string,
      /**  PE Reason Code  */  
   PEReasonCode:string,
      /**  PE Reason Description  */  
   PEReasonDesc:string,
      /**  Malaysia Import Declaration Number  */  
   MYImportNum:string,
      /**  TW GUI Code Seller  */  
   TWGUIRegNumSeller:string,
      /**  TW GUI Code Buyer  */  
   TWGUIRegNumBuyer:string,
      /**  MXTARCode  */  
   MXTARCode:string,
      /**  Flag that indicates if the invoice is a GRNI document.  */  
   GRNIClearing:boolean,
      /**  CSF Peru - Fiscal Credit Operation Status  */  
   PEFiscalCreditOperStatus:number,
      /**  CSF Peru - International Tax agreement  */  
   PEInternatTaxAgr:string,
      /**  CSF Peru - Rent type  */  
   PERentType:string,
      /**  CSF Peru - Purchase  type  */  
   PEPurchaseType:string,
      /**  TH Reference Invoice Num  */  
   THRefInvoiceNum:string,
      /**  TH Reference Vendor Num  */  
   THRefVendorNum:number,
      /**  Day when a company sums up accounts payable for supplier  */  
   JPSummarizationDate:string,
      /**  Date of a Payment Statement  */  
   JPBillingDate:string,
      /**  Legal Number of Payment Statement  */  
   JPBillingNumber:string,
      /**  SelfInvoice  */  
   SelfInvoice:boolean,
      /**  Printed  */  
   Printed:boolean,
      /**  PurPoint  */  
   PurPoint:string,
      /**  PLInvoiceReference  */  
   PLInvoiceReference:string,
      /**  INPortCode  */  
   INPortCode:string,
      /**  Indicates which invoice number has cancelled this invoice.  */  
   RefCancelledby:string,
      /**  Indicates if this invoice is a cancellation invoice.  */  
   CancellationInv:boolean,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  WithholdAcctToInterim  */  
   WithholdAcctToInterim:boolean,
      /**  APTaxRoundOption  */  
   APTaxRoundOption:number,
      /**  Source Plant used for multi site GL  */  
   SourcePlant:string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   ExtSysType:string,
      /**  URL for drill back to an integrated external system  */  
   ExtSysURL:string,
      /**  CHQRIBAN  */  
   CHQRIBAN:string,
      /**  CHQRReference  */  
   CHQRReference:string,
      /**  Set to True for any invoice that is created via EDI  */  
   EDIInvoice:boolean,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  1099 Code Description, defaults from Supplier  */  
   Code1099Description:string,
      /**  1099 Code, defaults from Supplier  */  
   Code1099ID:string,
      /**  Display field for Invoice Balance  */  
   DispInvoiceBal:number,
      /**  Form Type Description  */  
   FormTypeDescription:string,
      /**  Form Type ID  */  
   FormTypeID:string,
      /**  Indicates whether created invoice should be paid.  */  
   Paid:boolean,
      /**  CSF Poland. Vendor uses Invoice reference number  */  
   PLVendorAutoInvoiceNum:boolean,
   Print1099:boolean,
   Rpt1DispInvoiceBal:number,
   Rpt2DispInvoiceBal:number,
   Rpt3DispInvoiceBal:number,
      /**  Taxable Value 1  */  
   TaxableAmt1:number,
      /**  Taxable Value 2  */  
   TaxableAmt2:number,
      /**  Taxable Value 3  */  
   TaxableAmt3:number,
      /**  Taxable Value 4  */  
   TaxableAmt4:number,
      /**  Tax Value 1  */  
   TaxAmt1:number,
      /**  Tax Value 2  */  
   TaxAmt2:number,
      /**  Tax Value 3  */  
   TaxAmt3:number,
      /**  Tax Value 4  */  
   TaxAmt4:number,
      /**  Tax Type 1  */  
   TaxCode1:string,
   TaxCode1Description:string,
      /**  Tax Type 2  */  
   TaxCode2:string,
   TaxCode2Description:string,
      /**  Tax Type 3  */  
   TaxCode3:string,
   TaxCode3Description:string,
      /**  Tax Type 4  */  
   TaxCode4:string,
   TaxCode4Description:string,
      /**  Tax Rate 1  */  
   TaxRate1:string,
   TaxRate1Description:string,
      /**  Tax Rate 2  */  
   TaxRate2:string,
   TaxRate2Description:string,
      /**  Tax Rate 3  */  
   TaxRate3:string,
   TaxRate3Description:string,
      /**  Tax Rate 4  */  
   TaxRate4:string,
   TaxRate4Description:string,
      /**  Flag to indicate if the Legal Number should be enabled.  */  
   UseLegalNumber:boolean,
      /**  Exchange Rate Label  */  
   XRateLabel:string,
   BankName:string,
      /**  Display field for DocInvoiceBal  */  
   DocDispInvoiceBal:number,
      /**  Site is a legal entity  */  
   SiteIsLegalEntity:boolean,
   BitFlag:number,
   CurrencyCurrencyID:string,
   CurrencyCurrDesc:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrSymbol:string,
   CurrencyCurrName:string,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
   RateGrpCodeDescription:string,
   SourcePlantName:string,
   TaxRgnDescription:string,
   TermsDescription:string,
   VendorName:string,
   VendorZIP:string,
   VendorCity:string,
   VendorDefaultFOB:string,
   VendorState:string,
   VendorAddress1:string,
   VendorAddress2:string,
   VendorCountry:string,
   VendorTermsCode:string,
   VendorAddress3:string,
   VendorCurrencyCode:string,
   VendorVendorID:string,
   XbSystIsDiscountforDebitM:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APInvoiceLoadTableset{
   APInvoiceLoad:Erp_Tablesets_APInvoiceLoadRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

export interface Erp_Tablesets_UpdExtAPInvoiceLoadTableset{
   APInvoiceLoad:Erp_Tablesets_APInvoiceLoadRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
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
   returnObj:Erp_Tablesets_APInvoiceLoadTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_APInvoiceLoadTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_APInvoiceLoadTableset[],
}

export interface GetCurrencyBase_output{
parameters : {
      /**  output parameters  */  
   opCurrencyBase:string,
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
   returnObj:Erp_Tablesets_APInvoiceLoadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewAPInvoiceLoad1_input{
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
}

export interface GetNewAPInvoiceLoad1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewAPInvoiceLoad_input{
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
   vendorNum:number,
}

export interface GetNewAPInvoiceLoad_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
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
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
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
   ds:Erp_Tablesets_APInvoiceLoadTableset,
}
}

   /** Required : 
      @param whereClauseAPInvoiceLoad
      @param whereClauseEntityGLC
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAPInvoiceLoad:string,
   whereClauseEntityGLC:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_APInvoiceLoadTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param sTaxLiability
   */  
export interface GetTaxTypesList_input{
      /**  Tax Liability.  */  
   sTaxLiability:string,
}

export interface GetTaxTypesList_output{
parameters : {
      /**  output parameters  */  
   sTaxTypesList:string,
}
}

export interface GetTotalBalance_output{
parameters : {
      /**  output parameters  */  
   opTotalInvBal:number,
   opBaseCurrSymbol:string,
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
export interface OnChangeCurrencyCodeOrRateGroup_input{
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
}

export interface OnChangeCurrencyCodeOrRateGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
}
}

   /** Required : 
      @param vendorNum
      @param vendorBankID
      @param ds
   */  
export interface OnChangeVendBankID_input{
      /**  Vendor Bank ID  */  
   vendorNum:number,
      /**  Vendor Bank ID  */  
   vendorBankID:string,
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
}

export interface OnChangeVendBankID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
}
}

   /** Required : 
      @param proposedDate
      @param dateField
   */  
export interface OnChangingInvoiceOrApplyDate_input{
      /**  The proposed date  */  
   proposedDate:string,
      /**  Pass "A' to check Apply Date or "I" for Invoice Date  */  
   dateField:string,
}

export interface OnChangingInvoiceOrApplyDate_output{
parameters : {
      /**  output parameters  */  
   dateMessage:string,
}
}

   /** Required : 
      @param iTaxNum
      @param sTaxCode
      @param sTaxRate
      @param bCheckCollectionMethod
      @param ds
   */  
export interface OnChangingTax_input{
      /**  Sequence number of tax (1 or 2 or 3)  */  
   iTaxNum:number,
      /**  Tax Code  */  
   sTaxCode:string,
      /**  Tax Rate  */  
   sTaxRate:string,
      /**  Check tax type's collection method  */  
   bCheckCollectionMethod:boolean,
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
}

export interface OnChangingTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
}
}

export interface PostOpenInvLoad_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAPInvoiceLoadTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAPInvoiceLoadTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_APInvoiceLoadTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceLoadTableset,
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
parameters : {
      /**  output parameters  */  
   isLogAPInvFound:boolean,
   logAPInvNum:string,
}
}

   /** Required : 
      @param vendorID
   */  
export interface ValidateVendorID_input{
   vendorID:string,
}

export interface ValidateVendorID_output{
parameters : {
      /**  output parameters  */  
   vendorNum:number,
}
}

