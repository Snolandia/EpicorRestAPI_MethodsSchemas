import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.QuoteAsmSvc
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteAsms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteAsms
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmRow
   */  
export function get_QuoteAsms(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteAsms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteAsmRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteAsmRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteAsms(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteAsm item
   Description: Calls GetByID to retrieve the QuoteAsm item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsm
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmRow
   */  
export function get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteAsmRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteAsmRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteAsm for the service
   Description: Calls UpdateExt to update QuoteAsm. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteAsm
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteAsmRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteAsm item
   Description: Call UpdateExt to delete QuoteAsm item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteAsm
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteAsmInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteAsmInsps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmInspRow
   */  
export function get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteAsmInsps(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteAsmInsps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteAsmInsp item
   Description: Calls GetByID to retrieve the QuoteAsmInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsmInsp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmInspRow
   */  
export function get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteAsmInsps_Company_QuoteNum_QuoteLine_AssemblySeq_PlanSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteAsmInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteAsmInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + PlanSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteAsmInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteMtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteMtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlRow
   */  
export function get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteMtls(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteMtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteMtl item
   Description: Calls GetByID to retrieve the QuoteMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlRow
   */  
export function get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteOprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOprs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprRow
   */  
export function get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteOprs(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteOprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOpr item
   Description: Calls GetByID to retrieve the QuoteOpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOpr1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprRow
   */  
export function get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteAsmRefDes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteAsmRefDes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmRefDesRow
   */  
export function get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteAsmRefDes(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmRefDesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteAsmRefDes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmRefDesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteAsmRefDe item
   Description: Calls GetByID to retrieve the QuoteAsmRefDe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsmRefDe1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RefDesSeq Desc: RefDesSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmRefDesRow
   */  
export function get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteAsmRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, RefDesSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteAsmRefDesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteAsmRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteAsmRefDesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteAsmAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteAsmAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmAttchRow
   */  
export function get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteAsmAttches(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteAsmAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteAsmAttch item
   Description: Calls GetByID to retrieve the QuoteAsmAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsmAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmAttchRow
   */  
export function get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteAsmAttches_Company_QuoteNum_QuoteLine_AssemblySeq_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteAsmAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteAsmAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteAsmAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteAsmInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteAsmInsps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmInspRow
   */  
export function get_QuoteAsmInsps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmInsps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteAsmInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteAsmInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteAsmInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteAsmInsps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmInsps", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteAsmInsp item
   Description: Calls GetByID to retrieve the QuoteAsmInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsmInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmInspRow
   */  
export function get_QuoteAsmInsps_Company_QuoteNum_QuoteLine_AssemblySeq_PlanSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteAsmInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + PlanSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteAsmInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteAsmInsp for the service
   Description: Calls UpdateExt to update QuoteAsmInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteAsmInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteAsmInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteAsmInsps_Company_QuoteNum_QuoteLine_AssemblySeq_PlanSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, PlanSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + PlanSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteAsmInsp item
   Description: Call UpdateExt to delete QuoteAsmInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteAsmInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteAsmInsps_Company_QuoteNum_QuoteLine_AssemblySeq_PlanSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, PlanSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + PlanSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteMtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteMtls
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlRow
   */  
export function get_QuoteMtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteMtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteMtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteMtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteMtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteMtl item
   Description: Calls GetByID to retrieve the QuoteMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlRow
   */  
export function get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteMtl for the service
   Description: Calls UpdateExt to update QuoteMtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteMtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteMtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteMtl item
   Description: Call UpdateExt to delete QuoteMtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteMtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteMtlInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteMtlInsps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlInspRow
   */  
export function get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_QuoteMtlInsps(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")/QuoteMtlInsps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteMtlInsp item
   Description: Calls GetByID to retrieve the QuoteMtlInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtlInsp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlInspRow
   */  
export function get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_QuoteMtlInsps_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_PlanSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteMtlInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")/QuoteMtlInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + PlanSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteMtlInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteMtlRefDes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteMtlRefDes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlRefDesRow
   */  
export function get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_QuoteMtlRefDes(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlRefDesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")/QuoteMtlRefDes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlRefDesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteMtlRefDe item
   Description: Calls GetByID to retrieve the QuoteMtlRefDe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtlRefDe1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RefDesSeq Desc: RefDesSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlRefDesRow
   */  
export function get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_QuoteMtlRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, RefDesSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteMtlRefDesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")/QuoteMtlRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteMtlRefDesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteMtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteMtlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlAttchRow
   */  
export function get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_QuoteMtlAttches(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")/QuoteMtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteMtlAttch item
   Description: Calls GetByID to retrieve the QuoteMtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlAttchRow
   */  
export function get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_QuoteMtlAttches_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteMtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")/QuoteMtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteMtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteMtlInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteMtlInsps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlInspRow
   */  
export function get_QuoteMtlInsps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlInsps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteMtlInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteMtlInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteMtlInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteMtlInsps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlInsps", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteMtlInsp item
   Description: Calls GetByID to retrieve the QuoteMtlInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtlInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlInspRow
   */  
export function get_QuoteMtlInsps_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_PlanSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteMtlInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + PlanSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteMtlInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteMtlInsp for the service
   Description: Calls UpdateExt to update QuoteMtlInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteMtlInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteMtlInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteMtlInsps_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_PlanSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, PlanSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + PlanSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteMtlInsp item
   Description: Call UpdateExt to delete QuoteMtlInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteMtlInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteMtlInsps_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_PlanSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, PlanSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + PlanSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteMtlRefDes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteMtlRefDes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlRefDesRow
   */  
export function get_QuoteMtlRefDes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlRefDesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlRefDes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlRefDesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteMtlRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteMtlRefDesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteMtlRefDesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteMtlRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlRefDes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteMtlRefDe item
   Description: Calls GetByID to retrieve the QuoteMtlRefDe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtlRefDe
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RefDesSeq Desc: RefDesSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlRefDesRow
   */  
export function get_QuoteMtlRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, RefDesSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteMtlRefDesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteMtlRefDesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteMtlRefDe for the service
   Description: Calls UpdateExt to update QuoteMtlRefDe. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteMtlRefDe
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RefDesSeq Desc: RefDesSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteMtlRefDesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteMtlRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, RefDesSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteMtlRefDe item
   Description: Call UpdateExt to delete QuoteMtlRefDe item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteMtlRefDe
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RefDesSeq Desc: RefDesSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteMtlRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, RefDesSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteMtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteMtlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlAttchRow
   */  
export function get_QuoteMtlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteMtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteMtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteMtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteMtlAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteMtlAttch item
   Description: Calls GetByID to retrieve the QuoteMtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlAttchRow
   */  
export function get_QuoteMtlAttches_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteMtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteMtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteMtlAttch for the service
   Description: Calls UpdateExt to update QuoteMtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteMtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteMtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteMtlAttches_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + DrawingSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteMtlAttch item
   Description: Call UpdateExt to delete QuoteMtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteMtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteMtlAttches_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + DrawingSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteOprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOprs
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprRow
   */  
export function get_QuoteOprs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteOprs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOpr item
   Description: Calls GetByID to retrieve the QuoteOpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprRow
   */  
export function get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteOpr for the service
   Description: Calls UpdateExt to update QuoteOpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteOpr item
   Description: Call UpdateExt to delete QuoteOpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteOprActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOprActions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprActionRow
   */  
export function get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprActions(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprActions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOprAction item
   Description: Calls GetByID to retrieve the QuoteOprAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprAction1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprActionRow
   */  
export function get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprActions_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, ActionSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOprActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprActions(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOprActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteOprInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOprInsps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprInspRow
   */  
export function get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprInsps(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprInsps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOprInsp item
   Description: Calls GetByID to retrieve the QuoteOprInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprInsp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprInspRow
   */  
export function get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprInsps_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_PlanSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOprInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + PlanSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOprInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteOpDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOpDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOpDtlRow
   */  
export function get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOpDtls(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOpDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOpDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOpDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOpDtl item
   Description: Calls GetByID to retrieve the QuoteOpDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOpDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param OpDtlSeq Desc: OpDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOpDtlRow
   */  
export function get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOpDtls_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_OpDtlSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, OpDtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOpDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOpDtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + OpDtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOpDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteOprMachParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOprMachParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprMachParamRow
   */  
export function get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprMachParams(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprMachParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprMachParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprMachParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOprMachParam item
   Description: Calls GetByID to retrieve the QuoteOprMachParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprMachParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param MachParamSeq Desc: MachParamSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprMachParamRow
   */  
export function get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprMachParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_MachParamSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, MachParamSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOprMachParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprMachParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + MachParamSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOprMachParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteOprAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOprAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprAttchRow
   */  
export function get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprAttches(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOprAttch item
   Description: Calls GetByID to retrieve the QuoteOprAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprAttchRow
   */  
export function get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprAttches_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOprAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOprAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteOprActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOprActions
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprActionRow
   */  
export function get_QuoteOprActions(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOprActions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOprActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOprActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteOprActions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOprAction item
   Description: Calls GetByID to retrieve the QuoteOprAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprActionRow
   */  
export function get_QuoteOprActions_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, ActionSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOprActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOprActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteOprAction for the service
   Description: Calls UpdateExt to update QuoteOprAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOprAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOprActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteOprActions_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, ActionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteOprAction item
   Description: Call UpdateExt to delete QuoteOprAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOprAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteOprActions_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, ActionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteOprActionParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOprActionParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprActionParamRow
   */  
export function get_QuoteOprActions_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq_QuoteOprActionParams(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, ActionSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprActionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + ")/QuoteOprActionParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprActionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOprActionParam item
   Description: Calls GetByID to retrieve the QuoteOprActionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprActionParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param ActionParamSeq Desc: ActionParamSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprActionParamRow
   */  
export function get_QuoteOprActions_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq_QuoteOprActionParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq_ActionParamSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, ActionSeq:string, ActionParamSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOprActionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + ")/QuoteOprActionParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOprActionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteOprActionParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOprActionParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprActionParamRow
   */  
export function get_QuoteOprActionParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprActionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActionParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprActionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOprActionParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOprActionParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOprActionParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteOprActionParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActionParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOprActionParam item
   Description: Calls GetByID to retrieve the QuoteOprActionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprActionParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param ActionParamSeq Desc: ActionParamSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprActionParamRow
   */  
export function get_QuoteOprActionParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq_ActionParamSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, ActionSeq:string, ActionParamSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOprActionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActionParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOprActionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteOprActionParam for the service
   Description: Calls UpdateExt to update QuoteOprActionParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOprActionParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param ActionParamSeq Desc: ActionParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOprActionParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteOprActionParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq_ActionParamSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, ActionSeq:string, ActionParamSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActionParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteOprActionParam item
   Description: Call UpdateExt to delete QuoteOprActionParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOprActionParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param ActionParamSeq Desc: ActionParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteOprActionParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq_ActionParamSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, ActionSeq:string, ActionParamSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActionParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteOprInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOprInsps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprInspRow
   */  
export function get_QuoteOprInsps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprInsps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOprInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOprInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOprInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteOprInsps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprInsps", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOprInsp item
   Description: Calls GetByID to retrieve the QuoteOprInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprInspRow
   */  
export function get_QuoteOprInsps_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_PlanSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOprInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + PlanSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOprInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteOprInsp for the service
   Description: Calls UpdateExt to update QuoteOprInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOprInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOprInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteOprInsps_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_PlanSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, PlanSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + PlanSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteOprInsp item
   Description: Call UpdateExt to delete QuoteOprInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOprInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteOprInsps_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_PlanSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, PlanSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + PlanSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteOpDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOpDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOpDtlRow
   */  
export function get_QuoteOpDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOpDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOpDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOpDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOpDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOpDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOpDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteOpDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOpDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOpDtl item
   Description: Calls GetByID to retrieve the QuoteOpDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOpDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param OpDtlSeq Desc: OpDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOpDtlRow
   */  
export function get_QuoteOpDtls_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_OpDtlSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, OpDtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOpDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOpDtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + OpDtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOpDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteOpDtl for the service
   Description: Calls UpdateExt to update QuoteOpDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOpDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param OpDtlSeq Desc: OpDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOpDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteOpDtls_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_OpDtlSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, OpDtlSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOpDtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + OpDtlSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteOpDtl item
   Description: Call UpdateExt to delete QuoteOpDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOpDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param OpDtlSeq Desc: OpDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteOpDtls_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_OpDtlSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, OpDtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOpDtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + OpDtlSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteOprMachParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOprMachParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprMachParamRow
   */  
export function get_QuoteOprMachParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprMachParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprMachParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprMachParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOprMachParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOprMachParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOprMachParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteOprMachParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprMachParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOprMachParam item
   Description: Calls GetByID to retrieve the QuoteOprMachParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprMachParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param MachParamSeq Desc: MachParamSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprMachParamRow
   */  
export function get_QuoteOprMachParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_MachParamSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, MachParamSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOprMachParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprMachParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + MachParamSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOprMachParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteOprMachParam for the service
   Description: Calls UpdateExt to update QuoteOprMachParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOprMachParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param MachParamSeq Desc: MachParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOprMachParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteOprMachParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_MachParamSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, MachParamSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprMachParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + MachParamSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteOprMachParam item
   Description: Call UpdateExt to delete QuoteOprMachParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOprMachParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param MachParamSeq Desc: MachParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteOprMachParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_MachParamSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, MachParamSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprMachParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + MachParamSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteOprAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOprAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprAttchRow
   */  
export function get_QuoteOprAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOprAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOprAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOprAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteOprAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteOprAttch item
   Description: Calls GetByID to retrieve the QuoteOprAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprAttchRow
   */  
export function get_QuoteOprAttches_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteOprAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteOprAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteOprAttch for the service
   Description: Calls UpdateExt to update QuoteOprAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOprAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOprAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteOprAttches_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + DrawingSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteOprAttch item
   Description: Call UpdateExt to delete QuoteOprAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOprAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteOprAttches_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, OprSeq:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + DrawingSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteAsmRefDes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteAsmRefDes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmRefDesRow
   */  
export function get_QuoteAsmRefDes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmRefDesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmRefDes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmRefDesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteAsmRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteAsmRefDesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteAsmRefDesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteAsmRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmRefDes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteAsmRefDe item
   Description: Calls GetByID to retrieve the QuoteAsmRefDe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsmRefDe
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RefDesSeq Desc: RefDesSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmRefDesRow
   */  
export function get_QuoteAsmRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, RefDesSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteAsmRefDesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteAsmRefDesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteAsmRefDe for the service
   Description: Calls UpdateExt to update QuoteAsmRefDe. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteAsmRefDe
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RefDesSeq Desc: RefDesSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteAsmRefDesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteAsmRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, RefDesSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteAsmRefDe item
   Description: Call UpdateExt to delete QuoteAsmRefDe item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteAsmRefDe
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RefDesSeq Desc: RefDesSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteAsmRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, MtlSeq:string, RefDesSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteAsmAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteAsmAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmAttchRow
   */  
export function get_QuoteAsmAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteAsmAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteAsmAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteAsmAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteAsmAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteAsmAttch item
   Description: Calls GetByID to retrieve the QuoteAsmAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsmAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmAttchRow
   */  
export function get_QuoteAsmAttches_Company_QuoteNum_QuoteLine_AssemblySeq_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteAsmAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteAsmAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteAsmAttch for the service
   Description: Calls UpdateExt to update QuoteAsmAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteAsmAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteAsmAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteAsmAttches_Company_QuoteNum_QuoteLine_AssemblySeq_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + DrawingSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteAsmAttch item
   Description: Call UpdateExt to delete QuoteAsmAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteAsmAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteAsmAttches_Company_QuoteNum_QuoteLine_AssemblySeq_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + DrawingSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get QuoteStages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteStages
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteStageRow
   */  
export function get_QuoteStages(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteStageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteStages", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteStageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteStages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteStageRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteStageRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteStages(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteStages", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteStage item
   Description: Calls GetByID to retrieve the QuoteStage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteStage
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param StageSeq Desc: StageSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteStageRow
   */  
export function get_QuoteStages_Company_QuoteNum_QuoteLine_AssemblySeq_StageSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, StageSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteStageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteStages(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + StageSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteStageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteStage for the service
   Description: Calls UpdateExt to update QuoteStage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteStage
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param StageSeq Desc: StageSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteStageRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteStages_Company_QuoteNum_QuoteLine_AssemblySeq_StageSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, StageSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteStages(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + StageSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteStage item
   Description: Call UpdateExt to delete QuoteStage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteStage
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param StageSeq Desc: StageSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteStages_Company_QuoteNum_QuoteLine_AssemblySeq_StageSeq(Company:string, QuoteNum:string, QuoteLine:string, AssemblySeq:string, StageSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteStages(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + StageSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseQuoteAsm:string, whereClauseQuoteAsmAttch:string, whereClauseQuoteAsmInsp:string, whereClauseQuoteMtl:string, whereClauseQuoteMtlAttch:string, whereClauseQuoteMtlInsp:string, whereClauseQuoteMtlRefDes:string, whereClauseQuoteOpr:string, whereClauseQuoteOprAttch:string, whereClauseQuoteOprAction:string, whereClauseQuoteOprActionParam:string, whereClauseQuoteOprInsp:string, whereClauseQuoteOpDtl:string, whereClauseQuoteOprMachParam:string, whereClauseQuoteAsmRefDes:string, whereClauseQuoteStage:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseQuoteAsm!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteAsm=" + whereClauseQuoteAsm
   }
   if(typeof whereClauseQuoteAsmAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteAsmAttch=" + whereClauseQuoteAsmAttch
   }
   if(typeof whereClauseQuoteAsmInsp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteAsmInsp=" + whereClauseQuoteAsmInsp
   }
   if(typeof whereClauseQuoteMtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteMtl=" + whereClauseQuoteMtl
   }
   if(typeof whereClauseQuoteMtlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteMtlAttch=" + whereClauseQuoteMtlAttch
   }
   if(typeof whereClauseQuoteMtlInsp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteMtlInsp=" + whereClauseQuoteMtlInsp
   }
   if(typeof whereClauseQuoteMtlRefDes!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteMtlRefDes=" + whereClauseQuoteMtlRefDes
   }
   if(typeof whereClauseQuoteOpr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteOpr=" + whereClauseQuoteOpr
   }
   if(typeof whereClauseQuoteOprAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteOprAttch=" + whereClauseQuoteOprAttch
   }
   if(typeof whereClauseQuoteOprAction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteOprAction=" + whereClauseQuoteOprAction
   }
   if(typeof whereClauseQuoteOprActionParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteOprActionParam=" + whereClauseQuoteOprActionParam
   }
   if(typeof whereClauseQuoteOprInsp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteOprInsp=" + whereClauseQuoteOprInsp
   }
   if(typeof whereClauseQuoteOpDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteOpDtl=" + whereClauseQuoteOpDtl
   }
   if(typeof whereClauseQuoteOprMachParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteOprMachParam=" + whereClauseQuoteOprMachParam
   }
   if(typeof whereClauseQuoteAsmRefDes!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteAsmRefDes=" + whereClauseQuoteAsmRefDes
   }
   if(typeof whereClauseQuoteStage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteStage=" + whereClauseQuoteStage
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(quoteNum:string, quoteLine:string, assemblySeq:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof quoteNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "quoteNum=" + quoteNum
   }
   if(typeof quoteLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "quoteLine=" + quoteLine
   }
   if(typeof assemblySeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "assemblySeq=" + assemblySeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddRefDesRange
   Description: Creates new QuoteMtlRefDes records based on the QuoteMtl dataset fields.
   OperationID: AddRefDesRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRefDesRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRefDesRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddRefDesRange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/AddRefDesRange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AppendDetails
   Description: This method takes the records built in BuildAppendDetails that are marked as append
and writes them to the database.  It will return the updated dataset.
   OperationID: AppendDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AppendDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AppendDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AppendDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/AppendDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildAppendDetails
   Description: This method returns the information that can be appended for approval
   OperationID: BuildAppendDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAppendDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAppendDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildAppendDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/BuildAppendDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOpDtlCapability
   Description: Method to call when changing the Capability ID.  This method will update QuoteOpDtl
to see if the labor and burden rates need to be reset.  Blank is a valid entry for
Capability ID.
   OperationID: ChangeOpDtlCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpDtlCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpDtlCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOpDtlCapability(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeOpDtlCapability", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOperAutoReceive
   Description: Verification when changing the AutoReceive field
   OperationID: ChangeOperAutoReceive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperAutoReceive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperAutoReceive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOperAutoReceive(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeOperAutoReceive", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOperLaborEntryMethod
   Description: Verification when changing the LaborEntryMethod field
   OperationID: ChangeOperLaborEntryMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperLaborEntryMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperLaborEntryMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOperLaborEntryMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeOperLaborEntryMethod", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOpDtlOverrideRates
   Description: Method to call when changing the Override Rates Flag.  This method will update
QuoteOpDtl with the default labor and burden rates from the appropriate resource
or resource group if the QuoteOpDtl.OverrideRates is set to false.
   OperationID: ChangeOpDtlOverrideRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpDtlOverrideRates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpDtlOverrideRates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOpDtlOverrideRates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeOpDtlOverrideRates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOpDtlResourceGrpID
   Description: Method to call when changing the Resource Group ID.  This method will update QuoteOpDtl
with the default labor and burden rates from the new resource group.  Blank is a valid
entry for Resource Group ID.
   OperationID: ChangeOpDtlResourceGrpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpDtlResourceGrpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpDtlResourceGrpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOpDtlResourceGrpID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeOpDtlResourceGrpID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOpDtlResourceID
   Description: Method to call when changing the Resource ID.  This method will update QuoteOpDtl
with the default labor and burden rates from the new resource.  Blank is a valid
entry for Resource ID.
   OperationID: ChangeOpDtlResourceID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpDtlResourceID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpDtlResourceID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOpDtlResourceID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeOpDtlResourceID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOperPrimaryProdOpDtl
   Description: This method defaults/resets the production standards when selecting Primary
Production Operation Detail.
This method should run when the QuoteOpr.PrimaryProdOpDtl field changes.
   OperationID: ChangeOperPrimaryProdOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperPrimaryProdOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperPrimaryProdOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOperPrimaryProdOpDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeOperPrimaryProdOpDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOperPrimarySetupOpDtl
   Description: This method defaults/resets the setup values when selecting Primary
Setup Operation Detail.
This method should run when the QuoteOpr.PrimarySetupOpDtl field changes.
   OperationID: ChangeOperPrimarySetupOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperPrimarySetupOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperPrimarySetupOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOperPrimarySetupOpDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeOperPrimarySetupOpDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMtlPurPoint
   Description: This method updates the vendor related information when the Vendor/Purchase Point
field changes.  It updates the vendor price breaks as well.  This method should run when
the field ttQuoteMtl.PurPoint changes.
   OperationID: ChangeMtlPurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlPurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlPurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMtlPurPoint(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeMtlPurPoint", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOperPurPoint
   Description: This method updates the vendor related information when the Vendor/Purchase Point
field changes.  It updates the vendor price breaks as well.  This method should run when
the field ttQuoteOpr.PurPoint changes.
   OperationID: ChangeOperPurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperPurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperPurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOperPurPoint(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeOperPurPoint", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOperVendorID
   Description: This method updates the vendor related information when the Vendor/Purchase Point
field changes.  It updates the vendor price breaks as well.  This method should run when
the field ttQuoteOpr.VendorNumVendorID changes.
   OperationID: ChangeOperVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOperVendorID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeOperVendorID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOpMtlReqQty
   Description: Method to call when changing the OpMtlReqQty.
   OperationID: ChangeOpMtlReqQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpMtlReqQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpMtlReqQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOpMtlReqQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeOpMtlReqQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOpMtlSalvageReqQty
   Description: Method to call when changing the QuoteMtl.SalvageQtyPer.
   OperationID: ChangeOpMtlSalvageReqQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpMtlSalvageReqQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpMtlSalvageReqQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOpMtlSalvageReqQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeOpMtlSalvageReqQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteAsmblQtyPer
   Description: This methods updates the QuoteAsmbl Required Quantity.
This method should run when the QuoteAsmbl.QtyPer field changes.
   OperationID: ChangeQuoteAsmblQtyPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteAsmblQtyPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteAsmblQtyPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteAsmblQtyPer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteAsmblQtyPer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteAsmblValRefDes
   Description: Verify that there are no other QuoteMtlRefDes records in the assembly having
the same RefDes value if the QuoteAsmbl.ValRefDes = true. This method should
run before changing the QuoteAsmbl.ValRefDes.
   OperationID: ChangeQuoteAsmblValRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteAsmblValRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteAsmblValRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteAsmblValRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteAsmblValRefDes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteAsmReqRefDes
   Description: This methods assigns QuoteAsm.RDEndNum field when QuoteAsm.ReqRefDes changes.
This method should run when the QuoteAsm.ReqRefDes changes.
   OperationID: ChangeQuoteAsmReqRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteAsmReqRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteAsmReqRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteAsmReqRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteAsmReqRefDes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteMtlEstUnitCost
   Description: This methods recalculates the Est Mtl Burden Unit Cost when the
Est Unit Cost value changes.
This method should run when the QuoteMtl.EstUnitCost changes.
   OperationID: ChangeQuoteMtlEstUnitCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlEstUnitCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlEstUnitCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteMtlEstUnitCost(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteMtlEstUnitCost", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteMtlLinkToContract
   Description: This method should run when the JobMtl.LinkToContract changes.
   OperationID: ChangeQuoteMtlLinkToContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlLinkToContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlLinkToContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteMtlLinkToContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteMtlLinkToContract", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteMtlMtlBurRate
   Description: This methods recalculates the Est Mtl Burden Unit Cost when the
Mtl Burden Rate value changes.
This method should run when the QuoteMtl.MtlBurRate changes.
   OperationID: ChangeQuoteMtlMtlBurRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlMtlBurRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlMtlBurRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteMtlMtlBurRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteMtlMtlBurRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteMtlMiscCharge
   Description: This method validates if transaction exists and updates fields based on value of Misc. Charge flag.
This method should run when the QuoteMtl.MiscCharge field changes.
   OperationID: ChangeQuoteMtlMiscCharge
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlMiscCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlMiscCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteMtlMiscCharge(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteMtlMiscCharge", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteMtlReqRefDes
   Description: This methods assigns QuoteMtl.RDEndNum field when QuoteMtl.ReqRefDes changes.
This method should run when the QuoteMtl.ReqRefDes changes.
   OperationID: ChangeQuoteMtlReqRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlReqRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlReqRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteMtlReqRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteMtlReqRefDes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteMtlSalvageMtlBurUnitRate
   Description: This methods recalculates the Salvage Mtl Burden Unit Cost when the
Salvage Mtl Burden Rate value changes.
This method should run when the ECOMtl.SalvageMtlBurRate changes.
   OperationID: ChangeQuoteMtlSalvageMtlBurUnitRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlSalvageMtlBurUnitRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlSalvageMtlBurUnitRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteMtlSalvageMtlBurUnitRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteMtlSalvageMtlBurUnitRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteMtlSalvagePartNum
   Description: This methods assigns associated fields when ECOMtl.SalvagePartNum changes.
This method should run when the ECOMtl.SalvagePartNum changes.
   OperationID: ChangeQuoteMtlSalvagePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlSalvagePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlSalvagePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteMtlSalvagePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteMtlSalvagePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteMtlSalvageUnitCredit
   Description: This methods recalculates the Salvage Mtl Burden Unit Cost when the
Salvage Unit Credit value changes.
This method should run when the ECOMtl.SalvageUnitCredit changes.
   OperationID: ChangeQuoteMtlSalvageUnitCredit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlSalvageUnitCredit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlSalvageUnitCredit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteMtlSalvageUnitCredit(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteMtlSalvageUnitCredit", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteOprOprSeq
   Description: This method will update all of the associated records to the QuoteOpr if the
OprSeq field is changing.
This method should run before changing the QuoteOpr.OprSeq and not when a new record.
   OperationID: ChangeQuoteOprOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteOprOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteOprOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteOprOprSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteOprOprSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckConfigurationAndGetConfigType
   Description: This method checks if a part must be configured prior to a GetDetails.
   OperationID: CheckConfigurationAndGetConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConfigurationAndGetConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConfigurationAndGetConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckConfigurationAndGetConfigType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/CheckConfigurationAndGetConfigType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method checkQuotePartConfiguration
   Description: Checks if the Part of the Quote Line needs configuration and return information needed for the configuration call.
   OperationID: checkQuotePartConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/checkQuotePartConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/checkQuotePartConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_checkQuotePartConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/checkQuotePartConfiguration", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckConfiguration
   Description: This method checks if a part must be configured prior to a GetDetails.
   OperationID: CheckConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/CheckConfiguration", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckConfigurationAndGetConfigInfo
   Description: This method checks if a part must be configured prior to a GetDetails and retrieves information related to the configuration.
   OperationID: CheckConfigurationAndGetConfigInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConfigurationAndGetConfigInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConfigurationAndGetConfigInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckConfigurationAndGetConfigInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/CheckConfigurationAndGetConfigInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckOperPrimaryProdOpDtl
   Description: This method validated the value of Primary Production Operation Detail.
This method should run when the QuoteOpr.PrimaryProdOpDtl is changing.
   OperationID: CheckOperPrimaryProdOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOperPrimaryProdOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOperPrimaryProdOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOperPrimaryProdOpDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/CheckOperPrimaryProdOpDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckOperPrimarySetupOpDtl
   Description: This method validated the value of Primary Setup Operation Detail.
This method should run when the QuoteOpr.PrimarySetupOpDtl is changing.
   OperationID: CheckOperPrimarySetupOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOperPrimarySetupOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOperPrimarySetupOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOperPrimarySetupOpDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/CheckOperPrimarySetupOpDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPartErrors
   Description: This method runs through a quote's BOM and returns a list of assembly and/or
materials that are on hold or inactive.  Quote cannot be engineered or Quoted
until these errors are taken care of
   OperationID: CheckPartErrors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPartErrors_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartErrors_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPartErrors(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/CheckPartErrors", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPrePartInfo
   Description: The method is to be run on leave of the PartNum, Revision fields before the
GetPartInfo or Update methods are run.  This returns all the questions that
need to be asked before a part can be changed.
   OperationID: CheckPrePartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrePartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrePartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPrePartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/CheckPrePartInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CollapseAssembly
   Description: Collapses any single Quote Assembly except Assembly 0
   OperationID: CollapseAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CollapseAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CollapseAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CollapseAssembly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/CollapseAssembly", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteAsmChildDelete
   Description: Deletes the QuoteAsm child records
   OperationID: QuoteAsmChildDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteAsmChildDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteAsmChildDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteAsmChildDelete(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmChildDelete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteAllAssembly
   Description: The method deletes all assemblies and their subassemblies, materials and operations
while leaving the base assembly sequence alone.
   OperationID: DeleteAllAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteAllAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAllAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteAllAssembly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/DeleteAllAssembly", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteRefDesRange
   Description: Deletes QuoteMtlRefDes records based on the QuoteMtl dataset fields.
   OperationID: DeleteRefDesRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRefDesRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRefDesRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRefDesRange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/DeleteRefDesRange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EnableSupplierPriceList
   Description: This method returns whether or not the supplier price list option
is enabled.  This is based on security rights for the user.
   OperationID: EnableSupplierPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableSupplierPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnableSupplierPriceList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/EnableSupplierPriceList", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindAsm
   OperationID: FindAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindAsm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/FindAsm", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAsmOprInfo
   Description: This method updates the related operation description when the RelatedOperation field
changes. To be run before update.
   OperationID: GetAsmOprInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAsmOprInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAsmOprInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAsmOprInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetAsmOprInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAsmPartInfo
   Description: This method updates the dataset with Part Defaults when the PartNum or Revision field
changes. To be run before update. CheckPrePartInfo should be run first
   OperationID: GetAsmPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAsmPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAsmPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAsmPartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetAsmPartInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBasePartAndConfigType
   Description: Retrieve the based configured part and config type
   OperationID: GetBasePartAndConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartAndConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartAndConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBasePartAndConfigType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetBasePartAndConfigType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBasePartForConfig
   Description: This method will retrieve the base configured part number to be passed
to configuration entry
   OperationID: GetBasePartForConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartForConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartForConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBasePartForConfig(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetBasePartForConfig", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMtlConfigPartRev
   OperationID: GetMtlConfigPartRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlConfigPartRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlConfigPartRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlConfigPartRev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetMtlConfigPartRev", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMtlConfigPartRevAndConfigType
   OperationID: GetMtlConfigPartRevAndConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlConfigPartRevAndConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlConfigPartRevAndConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlConfigPartRevAndConfigType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetMtlConfigPartRevAndConfigType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDatasetForTreeByRef
   Description: Same as GetDataSetForTree but expects ref QuoteAsmTableset to improve performance within kinetic when merging large volumes of data.
            
This methods will return the dataset for QuoteAsm.  The method will return the
records related to the assembly provided and the first child level assemblies related to
the input inputted assembly.
   OperationID: GetDatasetForTreeByRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTreeByRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTreeByRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDatasetForTreeByRef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetDatasetForTreeByRef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDatasetForTree
   Description: This methods will return the dataset for QuoteAsm.  The method will return the
records related to the assembly provided and the first child level assemblies related to
the input inputted assembly.
   OperationID: GetDatasetForTree
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDatasetForTree(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetDatasetForTree", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDatasetForTreeRefresh
   Description: This methods will return the dataset for QuoteAsm.  The method will return the
records related to all the assemblies specified in assemblySeqList
   OperationID: GetDatasetForTreeRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTreeRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTreeRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDatasetForTreeRefresh(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetDatasetForTreeRefresh", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDetails
   Description: This method retrieves the manufacturing details from a source file.  The source file
will either be a Quote, a Job, or a Method (Part).  The assembly records will
be created regardless if the part is in error or not.  If there are errors, the
quote cannot be "quoted" unless all parts are fixed.  To find the parts in error
run CheckPartErrors
   OperationID: GetDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMtlBuyItInfo
   Description: This method updates Vendor and LeadTime when BuyIt is checked
   OperationID: GetMtlBuyItInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlBuyItInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlBuyItInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlBuyItInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetMtlBuyItInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMtlDirectInfo
   Description: This method updates Vendor and LeadTime when BuyIt is checked
   OperationID: GetMtlDirectInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlDirectInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlDirectInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlDirectInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetMtlDirectInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMtlOprInfo
   Description: This method defaults the EstScrap fields when the QuoteMtl.RelatedOperation changes
   OperationID: GetMtlOprInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlOprInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlOprInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlOprInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetMtlOprInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckQuoteMtlPartNum
   OperationID: CheckQuoteMtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckQuoteMtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckQuoteMtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckQuoteMtlPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/CheckQuoteMtlPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMtlPartInfo
   Description: This method updates the dataset with Part Defaults when the PartNum field changes.
To be run after partNum changes but before update. CheckPrePartInfo should be run first
   OperationID: GetMtlPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlPartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetMtlPartInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMtlVendorInfo
   Description: This method defaults the Vendor fields when the VendorNumVendorID field is changed
   OperationID: GetMtlVendorInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlVendorInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlVendorInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlVendorInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetMtlVendorInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAssembly
   Description: This method creates a new Assembly after prompting for the AsemblySeq and BOMLevel
as well as the QuoteLine and QuoteNum fields. This is to replace the standard GetNewQuoteAsm
   OperationID: GetNewAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAssembly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewAssembly", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOperation
   Description: This method creates a new Operation after prompting for the SubConType as well as the
AssemblySeq, QuoteLine and QuoteNum fields. This is to replace the standard GetNewQuoteOpr
   OperationID: GetNewOperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOperation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewOperation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOprOpCodeInfo
   Description: This method defaults the OpStd information when the OpCode field changes.
Updates the burden rates as well.
   OperationID: GetOprOpCodeInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOprOpCodeInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOprOpCodeInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOprOpCodeInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetOprOpCodeInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOprOpStdInfo
   Description: This method defaults Operation Standard information when OpStdId changes
   OperationID: GetOprOpStdInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOprOpStdInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOprOpStdInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOprOpStdInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetOprOpStdInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOprPartInfo
   Description: This method updates the dataset with Part Defaults when the PartNum field changes.
To be run after partNum changes but before update. CheckPrePartInfo should be run first
   OperationID: GetOprPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOprPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOprPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOprPartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetOprPartInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOprStdFormatInfo
   Description: This method updates the dataset after the StdFormat field changes.  Can be run on the ColumnChanged event
   OperationID: GetOprStdFormatInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOprStdFormatInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOprStdFormatInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOprStdFormatInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetOprStdFormatInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQuoteEngUIDefaults
   Description: Return separated list of values for use in QuoteEng:
AllowPurchasingInfo = Security.CheckSecurityAccess("bo.Part.AllowPurchasingInfo")
PreventQQChange = EQSyst.PreventQQChange
SiteExternalMES = PlantConfCtrl.ExternalMES
   OperationID: GetQuoteEngUIDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteEngUIDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQuoteEngUIDefaults(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetQuoteEngUIDefaults", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertBOMAsm
   Description: This methods allows for the insertion of an engineering assembly for drag/drop functionality,
validates a QuoteAsm record exists for the parent
   OperationID: InsertBOMAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertBOMAsm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertBOMAsm", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertBOMMtl
   Description: This methods allows for the insertion of an engineering material for drag/drop functionality,
validates a JobAsmbl record exists for the parent
   OperationID: InsertBOMMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertBOMMtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertBOMMtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertBOMOper
   Description: This methods allows for the insertion of an engineering operation for drag/drop functionality,
validates a JobAsmbl record exists for the parent
   OperationID: InsertBOMOper
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMOper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMOper_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertBOMOper(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertBOMOper", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertMaterial
   Description: This methods allows for the insertion on a material for drag/drop functionality,
validates a QuoteAsm record exists and the part is valid.
   OperationID: InsertMaterial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertMaterial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertMaterial_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertMaterial(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertMaterial", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertOpDtlCapability
   Description: This method allows for the insertion of Capability on an operation to create
operation detail for drag/drop functionality.
   OperationID: InsertOpDtlCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOpDtlCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOpDtlCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOpDtlCapability(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertOpDtlCapability", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertOpDtlResource
   Description: This method allows for the insertion of Resource on an operation to create
operation detail for drag/drop functionality.
   OperationID: InsertOpDtlResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOpDtlResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOpDtlResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOpDtlResource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertOpDtlResource", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertOpDtlResourceGrp
   Description: This method allows for the insertion of Resource Group on an operation to create
operation detail for drag/drop functionality.
   OperationID: InsertOpDtlResourceGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOpDtlResourceGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOpDtlResourceGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOpDtlResourceGrp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertOpDtlResourceGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertOperationOP
   Description: This methods allows for the insertion of an operation for drag/drop functionality
using operation code as input.  This would eventually replace the original InsertOperation
method where work center code is the input.
   OperationID: InsertOperationOP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOperationOP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOperationOP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOperationOP(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertOperationOP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertOperCapability
   Description: This method allows for the insertion of Capability on an assembly to create
QuoteOpr/QuoteOpDtl for drag/drop functionality.
   OperationID: InsertOperCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOperCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOperCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOperCapability(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertOperCapability", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertOperResGroup
   Description: This method allows for the insertion of ResourceGroup on an assembly to create
QuoteOpr/QuoteOpDtl for drag/drop functionality.
   OperationID: InsertOperResGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOperResGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOperResGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOperResGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertOperResGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertOperResource
   Description: This method allows for the insertion of Resource on an assembly to create
QuoteOpr/QuoteOpDtl for drag/drop functionality.
   OperationID: InsertOperResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOperResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOperResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOperResource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertOperResource", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertSubAssembly
   Description: This methods allows for the insertion of a subassembly for drag/drop functionality,
validates a QuoteAsm record exists and the part is valid.
   OperationID: InsertSubAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertSubAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertSubAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertSubAssembly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertSubAssembly", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertNewSubAssembly
   Description: This methods allows for the insertion of a subassembly for drag/drop functionality,
validates a QuoteAsm record exists and the part is valid.
   OperationID: InsertNewSubAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertNewSubAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertNewSubAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertNewSubAssembly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/InsertNewSubAssembly", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateLinkToContractData
   Description: Validate Parts allowed for Planning Contracts.
   OperationID: ValidateLinkToContractData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateLinkToContractData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLinkToContractData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateLinkToContractData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ValidateLinkToContractData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckChangeJobAsmblParent
   Description: This method validates validates the new Parent field
   OperationID: CheckChangeJobAsmblParent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckChangeJobAsmblParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckChangeJobAsmblParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckChangeJobAsmblParent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/CheckChangeJobAsmblParent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeJobAsmblParent
   Description: This method validates the new Parent field and populates defaults associated with the Parent.
This method should run when the JobAsmbl.Parent field changes.
   OperationID: ChangeJobAsmblParent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobAsmblParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobAsmblParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJobAsmblParent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeJobAsmblParent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteOprInitSNReqSubCon
   Description: Method required to set the initial value of QuoteOpr.SNRequiredSubConShip
   OperationID: QuoteOprInitSNReqSubCon
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteOprInitSNReqSubCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteOprInitSNReqSubCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteOprInitSNReqSubCon(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprInitSNReqSubCon", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSNReqValues
   Description: This method updates the columns SNRequiredOpr and SNRequiredSubConShip when the main Part
changes. If the new part number is not serial tracked and those fields were set as true previuosly, they must be set to false.
   OperationID: ValidateSNReqValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSNReqValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSNReqValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSNReqValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ValidateSNReqValues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateInspection
   Description: Method to validate the Inspection control fields. (EQM)
   OperationID: ValidateInspection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateInspection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInspection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateInspection(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ValidateInspection", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePartToLinkToContract
   Description: Validate Parts allowed for Planning Contracts.
   OperationID: ValidatePartToLinkToContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePartToLinkToContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartToLinkToContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePartToLinkToContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ValidatePartToLinkToContract", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshMtlPriceBreak
   Description: This method refreshes the QuoteMtl PBrkQty and PBrkCost fields after
VendPart and VendPBrk tables have been updated. It will also update the
LeadTime and Unit Cost fields as well.
   OperationID: RefreshMtlPriceBreak
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshMtlPriceBreak_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshMtlPriceBreak_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshMtlPriceBreak(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/RefreshMtlPriceBreak", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshOprPriceBreak
   Description: This method refreshes the QuoteOpr PBrkQty and PBrkCost fields after
VendPart and VendPBrk tables have been updated. It will also update the
LeadTime and Unit Cost fields as well.
   OperationID: RefreshOprPriceBreak
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshOprPriceBreak_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshOprPriceBreak_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshOprPriceBreak(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/RefreshOprPriceBreak", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResequenceMaterial
   Description: This method resequences Material for an assembly by sequence, part or bubble
   OperationID: ResequenceMaterial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResequenceMaterial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResequenceMaterial_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResequenceMaterial(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ResequenceMaterial", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResequenceOperations
   Description: This method resequences the operations of an assembly by 10's
   OperationID: ResequenceOperations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResequenceOperations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResequenceOperations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResequenceOperations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ResequenceOperations", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteOprIUM
   Description: procedure for changing QuoteOpr.IUM field
   OperationID: ChangeQuoteOprIUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteOprIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteOprIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteOprIUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteOprIUM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteOprQtyPer
   Description: procedure for changing QuoteOpr.QtyPer field
   OperationID: ChangeQuoteOprQtyPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteOprQtyPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteOprQtyPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteOprQtyPer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteOprQtyPer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteMtlIUM
   Description: procedure for changing QuoteMtl.IUM field
   OperationID: ChangeQuoteMtlIUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteMtlIUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteMtlIUM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteMtlSalvageUM
   Description: procedure for changing QuoteMtl.SalvageUM field
   OperationID: ChangeQuoteMtlSalvageUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlSalvageUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlSalvageUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteMtlSalvageUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteMtlSalvageUM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteOprSNRequiredOpr
   Description: Validates SNRequiredOpr flag to avoid to set it false if the prior operation has the flag set to true
The flag cannot be set to true if the part is not serial tracked also.
   OperationID: ChangeQuoteOprSNRequiredOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteOprSNRequiredOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteOprSNRequiredOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteOprSNRequiredOpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeQuoteOprSNRequiredOpr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSubcontractPartNum
   Description: Check if SNRequiredOpr column is enabled/disabled on Subcontract Detail panel on UI
   OperationID: ChangeSubcontractPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubcontractPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubcontractPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSubcontractPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/ChangeSubcontractPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method JobPartBeforeGetNew
   Description: Validates if JobHead.PartNum is serial tracked, additional JobParts cannot be added.
   OperationID: JobPartBeforeGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/JobPartBeforeGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JobPartBeforeGetNew(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/JobPartBeforeGetNew", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetProjectRoles
   Description: Returns list of Project Roles
   OperationID: GetProjectRoles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProjectRoles_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetProjectRoles(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetProjectRoles", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQuoteMtlIsMtlConfigurationOn
   Description: After Material was configured we need to check if was success to display the correct Materials Tree Context Menu option (Configure or Configuration)
   OperationID: GetQuoteMtlIsMtlConfigurationOn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuoteMtlIsMtlConfigurationOn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteMtlIsMtlConfigurationOn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQuoteMtlIsMtlConfigurationOn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetQuoteMtlIsMtlConfigurationOn", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreGetDetails
   Description: This method should be called right before the GetDetails method.  It necessary,
it'll return a question on resequencing assembly's while getting details.
The answer will be sent as a parameter to the GetDetails method.
This method will also return a BasePartNum and BaseRevisionNum.  If the BasePartNum
isn't null then use this as the default part number for GetDetails.
This is called from GetDetailsEntry
   OperationID: PreGetDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGetDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGetDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreGetDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/PreGetDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindQuoteMtlByPLMMtlSeq
   Description: Allows PLM Users to get QuoteMtl's AsmSeq and MtlSeq by sending the unique-per-line value PLMMtlSeq
   OperationID: FindQuoteMtlByPLMMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindQuoteMtlByPLMMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindQuoteMtlByPLMMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindQuoteMtlByPLMMtlSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/FindQuoteMtlByPLMMtlSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeSetQuoteAsm
   Description: Call this method when the QuoteAsm attribute set changes
   OperationID: OnChangingAttributeSetQuoteAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSetQuoteAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSetQuoteAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSetQuoteAsm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/OnChangingAttributeSetQuoteAsm", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeSetQuoteMtl
   Description: Call this method when the QuoteMtl attribute set changes
   OperationID: OnChangingAttributeSetQuoteMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSetQuoteMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSetQuoteMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSetQuoteMtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/OnChangingAttributeSetQuoteMtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeSetQuoteOpr
   Description: Call this method when the QuoteOpr attribute set changes
   OperationID: OnChangingAttributeSetQuoteOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSetQuoteOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSetQuoteOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSetQuoteOpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/OnChangingAttributeSetQuoteOpr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPiecesQuoteMtl
   Description: Call this method when the QuoteMtl Number Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPiecesQuoteMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPiecesQuoteMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPiecesQuoteMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPiecesQuoteMtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/OnChangingNumberOfPiecesQuoteMtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPiecesQuoteOpr
   Description: Call this method when the QuoteOpr Number Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPiecesQuoteOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPiecesQuoteOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPiecesQuoteOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPiecesQuoteOpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/OnChangingNumberOfPiecesQuoteOpr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingMtlRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingMtlRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingMtlRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingMtlRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingMtlRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/OnChangingMtlRevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingQuoteOprRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingQuoteOprRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingQuoteOprRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingQuoteOprRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingQuoteOprRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/OnChangingQuoteOprRevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingSalvageRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingSalvageRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSalvageRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSalvageRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingSalvageRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/OnChangingSalvageRevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteAsm
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteAsm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteAsm", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteAsmAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteAsmAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteAsmAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteAsmAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteAsmAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteAsmAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteAsmInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteAsmInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteAsmInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteAsmInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteAsmInsp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteAsmInsp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteMtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteMtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteMtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteMtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteMtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteMtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteMtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteMtlAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteMtlAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteMtlInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteMtlInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteMtlInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteMtlInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteMtlInsp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteMtlInsp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteMtlRefDes
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteMtlRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteMtlRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteMtlRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteMtlRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteMtlRefDes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteOpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteOpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteOpr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteOprAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOprAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOprAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOprAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteOprAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteOprAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteOprAction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOprAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOprAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOprAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteOprAction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteOprAction", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteOprActionParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOprActionParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOprActionParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOprActionParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteOprActionParam(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteOprActionParam", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteOprInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOprInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOprInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOprInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteOprInsp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteOprInsp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteOpDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteOpDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteOpDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteOprMachParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOprMachParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOprMachParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOprMachParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteOprMachParam(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteOprMachParam", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteAsmRefDes
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteAsmRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteAsmRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteAsmRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteAsmRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteAsmRefDes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteStage
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteStage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteStage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteStage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteStage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/GetNewQuoteStage", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteAsmAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmInspRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteAsmInspRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteAsmListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmRefDesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteAsmRefDesRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteAsmRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteMtlAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlInspRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteMtlInspRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlRefDesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteMtlRefDesRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteMtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOpDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteOpDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprActionParamRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteOprActionParamRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprActionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteOprActionRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteOprAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprInspRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteOprInspRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprMachParamRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteOprMachParamRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteOprRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteStageRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteStageRow[],
}

export interface Erp_Tablesets_QuoteAsmAttchRow{
   "Company":string,
   "QuoteNum":number,
   "QuoteLine":number,
   "AssemblySeq":number,
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

export interface Erp_Tablesets_QuoteAsmInspRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with.  */  
   "QuoteNum":number,
      /**  The QuoteLine that record is related to.  */  
   "QuoteLine":number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely identifies the QuoteAsmInsp record within the QuoteNum/QuoteLine/AssemblySeq  */  
   "PlanSeq":number,
      /**  The inspection plan part number (configurator part number).  */  
   "InspPlanPartNum":string,
      /**  The inspection plan revision number (configurator revision number).  */  
   "InspPlanRevNum":string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   "SpecID":string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   "SpecRevNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "SpecHedDescription":string,
   "BitFlag":number,
   "InspPlanDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteAsmListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the last QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  An integer that uniquely identifies the Assembly record within the Quote/Line.  Assigned by the system one greater than the last QuoteAsm record on file for the given quote/line.  */  
   "AssemblySeq":number,
      /**  Part number for this assembly.  Cannot be blank.  It does not have to be valid in the Part master file.  */  
   "PartNum":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description if valid Part record.  */  
   "Description":string,
      /**  The revision number for the assembly. An optional field. Use the Part.RevisionNum as a default.  */  
   "RevisionNum":string,
      /**  The production Quantity required for this assembly per one of it's Parent Part.  */  
   "QtyPer":number,
      /**  The unit of measure for this assembly. Use the Part.IUM as a default.  */  
   "IUM":string,
      /**  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse  */  
   "Direct":boolean,
      /**  Sequence number of the Parent Assembly.  0 means no parent assembly (i.e. this is the final assembly).  Cannot be negative like the other pointers because this one shows up in a browser.  */  
   "Parent":number,
      /**   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find the last assembly (i.e. where the Parent is the same and the NextPeer is -1). Then NextPeer of that assembly gets updated with this assembly's sequence number and this assembly gets its PriorPeer field updated with the sequence number from that assembly which was found.  -1 means that there is no prior assembly (i.e. it is the first assembly of its peers).  */  
   "PriorPeer":number,
      /**   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find the first assembly (i.e. where the Parent is the same and the PriorPeer is -1).  Then the PriorPeer of that assembly is updated with this assembly's sequence number and then this assembly's NextPeer gets updated with the sequence number from the assembly that was found.   -1 means that the assembly is the last assembly of its peers.  */  
   "NextPeer":number,
      /**  Seq # of this assembly's very first subassembly. This is known as the Child assembly. Automatically maintained by the maintenance programs. The logic is to find the Parent assembly record and if its child is -1, update it with this assembly's seq #.  */  
   "Child":number,
      /**  Optional field for Engineering Drawing Number. Defaulted from BomHead.DrawNum during methods pull functions.  */  
   "DrawNum":string,
      /**  Editor widget for Job Assembly comments.  */  
   "CommentText":string,
      /**  An internally system assigned integer which is used as part of an index to organize the QuoteAsm records into a Bill of Material fashion sequence.  */  
   "BomSequence":number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the QuoteAsm in reference to the Bill of Material structure.  */  
   "BomLevel":number,
      /**   A system maintained field. This is how many of the assemblies are required to produce ONE of the END ITEM.  This is a calculated field.  Calculated as the
 ( Parents RequiredQty  X QtyPer).
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer. The refresh may also occur if the structure of the assemblies is changed.  */  
   "RequiredQty":number,
      /**  Indicates if this quote assembly is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   "Template":boolean,
      /**   The operation number (Quote.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   "AutoRecOpr":number,
      /**  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  */  
   "FindNum":string,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   "FinalOpr":number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   "WIStartDate":string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   "WIStartHour":number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueDate":string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueHour":number,
      /**   An assembly record can be related to a specific operation.  This field contains the QuoteOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  */  
   "RelatedOperation":number,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   "EstScrapType":string,
   "OrigMtlSeq":number,
   "OrigRuleTag":string,
      /**  Validate Reference Designators.  */  
   "ValRefDes":boolean,
      /**  The part number used to identify the configured part number initially entered on the assembly.  */  
   "BasePartNum":string,
      /**  The revision number used to identify the configured part/revision number initially entered on the material.  */  
   "BaseRevisionNum":string,
      /**  Required number of designators  */  
   "ReqRefDes":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "RelatedOperationDescription":string,
      /**  QutoeAsm.PartNum of the Parent Assembly  */  
   "ParentPartNum":string,
      /**  QuoteAsm.RevisionNum of the Parent Assembly  */  
   "ParentRevisionNum":string,
      /**  QuoteAsm.Description of Parent assmebly  */  
   "ParentDescription":string,
      /**  Boolean to indicate GetDetails has started  */  
   "ProcessingDetails":boolean,
      /**  Clone of the Parent field (.Net keyword issue)  */  
   "ParentAssemblySeq":number,
      /**  Clone of the Child field (.Net keyword issue)  */  
   "ChildAssemblySeq":number,
      /**  Add assembly as "Sub"assembly or "Asm"bly  */  
   "AddAsmAs":string,
      /**  If this field is true, then the current value of ttQuoteAsm.AssemblySeq will be used when creating new QuoteAsm records. This allows processes, like PLM, to create new QuoteAsm records with a specific AssemblySeq.  */  
   "OverrideNextAsmSeq":boolean,
      /**  The prefix will be defaulted from the reference category defined for the assemblies. The value on this field will be used to create reference designators.  */  
   "RDPrefix":string,
      /**  The suffix will be defaulted from the reference category defined for the assemblie. The value on this field will be used to create reference designators.  */  
   "RDSuffix":string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   "RDStartNum":number,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   "RDEndNum":number,
      /**  Description  */  
   "AnalysisCdDescription":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "QuoteLineLineDesc":string,
      /**  A unique code that identifies the currency.  */  
   "QuoteNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteAsmRefDesRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  The QuoteLine that record is related to.  */  
   "QuoteLine":number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  */  
   "MtlSeq":number,
      /**  Identifier of Reference Designator  */  
   "RefDes":string,
      /**  Unique identifies the reference designator with the material sequence.  */  
   "RefDesSeq":number,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   "MtlPartNum":string,
      /**  Free form side location. (Top, Bottom, Both, Level, etc)  */  
   "Side":string,
      /**  X Coordinate of the reference designator  */  
   "XLocation":number,
      /**  Y Coordinate of the reference designator  */  
   "YLocation":number,
      /**  Z Coordinate of the reference designator  */  
   "ZLocation":number,
      /**  Rotation of the reference designator. Max value = 360.000  */  
   "Rotation":number,
      /**  Designator Description  */  
   "Description":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteAsmRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the last QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  An integer that uniquely identifies the Assembly record within the Quote/Line.  Assigned by the system one greater than the last QuoteAsm record on file for the given quote/line.  */  
   "AssemblySeq":number,
      /**  Part number for this assembly.  Cannot be blank.  It does not have to be valid in the Part master file.  */  
   "PartNum":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description if valid Part record.  */  
   "Description":string,
      /**  The revision number for the assembly. An optional field. Use the Part.RevisionNum as a default.  */  
   "RevisionNum":string,
      /**  The production Quantity required for this assembly per one of it's Parent Part.  */  
   "QtyPer":number,
      /**  The unit of measure for this assembly. Use the Part.IUM as a default.  */  
   "IUM":string,
      /**  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse  */  
   "Direct":boolean,
      /**  Sequence number of the Parent Assembly.  0 means no parent assembly (i.e. this is the final assembly).  Cannot be negative like the other pointers because this one shows up in a browser.  */  
   "Parent":number,
      /**   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find the last assembly (i.e. where the Parent is the same and the NextPeer is -1). Then NextPeer of that assembly gets updated with this assembly's sequence number and this assembly gets its PriorPeer field updated with the sequence number from that assembly which was found.  -1 means that there is no prior assembly (i.e. it is the first assembly of its peers).  */  
   "PriorPeer":number,
      /**   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find the first assembly (i.e. where the Parent is the same and the PriorPeer is -1).  Then the PriorPeer of that assembly is updated with this assembly's sequence number and then this assembly's NextPeer gets updated with the sequence number from the assembly that was found.   -1 means that the assembly is the last assembly of its peers.  */  
   "NextPeer":number,
      /**  Seq # of this assembly's very first subassembly. This is known as the Child assembly. Automatically maintained by the maintenance programs. The logic is to find the Parent assembly record and if its child is -1, update it with this assembly's seq #.  */  
   "Child":number,
      /**  Optional field for Engineering Drawing Number. Defaulted from BomHead.DrawNum during methods pull functions.  */  
   "DrawNum":string,
      /**  Editor widget for Job Assembly comments.  */  
   "CommentText":string,
      /**  An internally system assigned integer which is used as part of an index to organize the QuoteAsm records into a Bill of Material fashion sequence.  */  
   "BomSequence":number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the QuoteAsm in reference to the Bill of Material structure.  */  
   "BomLevel":number,
      /**   A system maintained field. This is how many of the assemblies are required to produce ONE of the END ITEM.  This is a calculated field.  Calculated as the
 ( Parents RequiredQty  X QtyPer).
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer. The refresh may also occur if the structure of the assemblies is changed.  */  
   "RequiredQty":number,
      /**  Indicates if this quote assembly is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   "Template":boolean,
      /**   The operation number (Quote.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   "AutoRecOpr":number,
      /**  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  */  
   "FindNum":string,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   "FinalOpr":number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   "WIStartDate":string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   "WIStartHour":number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueDate":string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueHour":number,
      /**   An assembly record can be related to a specific operation.  This field contains the QuoteOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  */  
   "RelatedOperation":number,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   "EstScrapType":string,
   "OrigMtlSeq":number,
   "OrigRuleTag":string,
      /**  Validate Reference Designators.  */  
   "ValRefDes":boolean,
      /**  The part number used to identify the configured part number initially entered on the assembly.  */  
   "BasePartNum":string,
      /**  The revision number used to identify the configured part/revision number initially entered on the material.  */  
   "BaseRevisionNum":string,
      /**  Required number of designators  */  
   "ReqRefDes":number,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   "OrigStructTag":string,
      /**  LinkToContract  */  
   "LinkToContract":boolean,
      /**  ContractID  */  
   "ContractID":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   "KBConfigProdID":number,
      /**  Clone of the Child field (.Net keyword issue)  */  
   "ChildAssemblySeq":number,
      /**  External field to hold JCSyst.GetCostsFromTemplate value  */  
   "GetCostsFromTemplate":boolean,
      /**  If this field is true, then the current value of ttQuoteAsm.AssemblySeq will be used when creating new QuoteAsm records. This allows processes, like PLM, to create new QuoteAsm records with a specific AssemblySeq.  */  
   "OverrideNextAsmSeq":boolean,
      /**  Clone of the Parent field (.Net keyword issue)  */  
   "ParentAssemblySeq":number,
      /**  QuoteAsm.Description of Parent assmebly  */  
   "ParentDescription":string,
      /**  QutoeAsm.PartNum of the Parent Assembly  */  
   "ParentPartNum":string,
      /**  QuoteAsm.RevisionNum of the Parent Assembly  */  
   "ParentRevisionNum":string,
      /**  Internal flag to identify if current Part is an Inventory Part  */  
   "PartExists":boolean,
      /**  Boolean to indicate GetDetails has started  */  
   "ProcessingDetails":boolean,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   "RDEndNum":number,
      /**  The prefix will be defaulted from the reference category defined for the assemblies. The value on this field will be used to create reference designators.  */  
   "RDPrefix":string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   "RDStartNum":number,
      /**  The suffix will be defaulted from the reference category defined for the assemblie. The value on this field will be used to create reference designators.  */  
   "RDSuffix":string,
   "RelatedOperationDescription":string,
      /**  Add assembly as "Sub"assembly or "Asm"bly  */  
   "AddAsmAs":string,
      /**  External field for EQSyst GetCostsFromInventory  */  
   "GetCostsFromInventory":boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   "EnableInventoryAttributes":boolean,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumAttrClassID":string,
   "PartNumIUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumSalesUM":string,
   "PartNumSellingFactor":number,
   "PartNumTrackLots":boolean,
   "PartNumPricePerCode":string,
   "PartNumPartDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "QuoteLineSmartString":string,
   "QuoteLineGroupSeq":number,
   "QuoteLineLineDesc":string,
   "QuoteLineSysRowID":string,
   "QuoteLineSmartStringProcessed":boolean,
   "QuoteLineReadyToQuote":boolean,
   "QuoteLineContractID":string,
   "QuoteLineKitFlag":string,
   "QuoteLineExternalMES":boolean,
   "QuoteNumQuoted":boolean,
   "QuoteNumQuoteClosed":boolean,
   "QuoteNumCurrencyCode":string,
   "QuoteNumCustNum":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteMtlAttchRow{
   "Company":string,
   "QuoteNum":number,
   "QuoteLine":number,
   "AssemblySeq":number,
   "MtlSeq":number,
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

export interface Erp_Tablesets_QuoteMtlInspRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with.  */  
   "QuoteNum":number,
      /**  The QuoteLine that record is related to.  */  
   "QuoteLine":number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  */  
   "MtlSeq":number,
      /**  A sequence number that uniquely identifies the QuoteMtlInsp record within the QuoteNum/QuoteLine/AssemblySeq/MtlSeq  */  
   "PlanSeq":number,
      /**  The inspection plan part number (configurator part number).  */  
   "InspPlanPartNum":string,
      /**  The inspection plan revision number (configurator revision number).  */  
   "InspPlanRevNum":string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   "SpecID":string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   "SpecRevNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "SpecHedDescription":string,
   "BitFlag":number,
   "InspPlanDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteMtlRefDesRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  The QuoteLine that record is related to.  */  
   "QuoteLine":number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  */  
   "MtlSeq":number,
      /**  Identifier of Reference Designator  */  
   "RefDes":string,
      /**  Unique identifies the reference designator with the material sequence.  */  
   "RefDesSeq":number,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   "MtlPartNum":string,
      /**  Free form side location. (Top, Bottom, Both, Level, etc)  */  
   "Side":string,
      /**  X Coordinate of the reference designator  */  
   "XLocation":number,
      /**  Y Coordinate of the reference designator  */  
   "YLocation":number,
      /**  Z Coordinate of the reference designator  */  
   "ZLocation":number,
      /**  Rotation of the reference designator. Max value = 360.000  */  
   "Rotation":number,
      /**  Designator Description  */  
   "Description":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteMtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  The QuoteLine that record is related to.  */  
   "QuoteLine":number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  */  
   "MtlSeq":number,
      /**  Part number of required material. Does not have to be valid in Part master file, but must not be blank.  */  
   "PartNum":string,
      /**  Description of the material. Cannot be blank  */  
   "Description":string,
      /**  Quantity required per one of the Parent item. This is a factor used in calculating the total material requirement.  */  
   "QtyPer":number,
      /**  The issue/usage unit of measure for this material.  */  
   "IUM":string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  */  
   "Direct":boolean,
      /**  Expected Purchasing lead time (in days) for the material. This is passed along to the job if the item gets manufactured.  */  
   "LeadTime":number,
      /**   A material record can be related to a specific operation. This field contains the QuoteOpr.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  */  
   "RelatedOperation":number,
      /**  Part number for Salvaged scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  */  
   "SalvagePartNum":string,
      /**  Description of Salvaged material. Use Part.Description for a default.  */  
   "SalvageDescription":string,
      /**  A factor that multiplied by the RequiredQty for the material results in the expected total salvage quantity.  */  
   "SalvageQtyPer":number,
      /**  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  */  
   "SalvageUM":string,
      /**  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  */  
   "SalvageUnitCredit":number,
      /**  The salvage material burden rate for this Quote Material.  */  
   "SalvageMtlBurRate":number,
      /**  Estimated salvage Mtl Burden Unit Credit. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   "SalvageEstMtlBurUnitCredit":number,
      /**   Comments for manufacturing about this material record. These comments are printed on manufacturing reports,  such as the router. For valid Parts use the Part.MfgComment as a default.
View as Editor widget.  */  
   "MfgComment":string,
      /**  Used to identify a default vendor. Use the Part.VendorNum as a default. This will be used as a default for purchasing and miscellaneous receipts. This field is not directly maintainable; instead it's assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  An optional field, but if entered must be valid.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   "PurPoint":string,
      /**  Indicates if this material is to be Purchased for the Job. If this is a non inventory part then this is "Yes" and can't be changed. If this is a valid Part then set it to "NO" but the user can override it.  */  
   "BuyIt":boolean,
      /**   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.

View as Editor widget.  */  
   "PurComment":string,
      /**  Minimum Cost that will be used for this material. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the material cost for the quote.  */  
   "MinimumCost":number,
      /**  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   "EstUnitCost":number,
      /**  The material burden rate for this Quote Material.  */  
   "MtlBurRate":number,
      /**  Estimated Mtl Burden Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   "EstMtlBurUnitCost":number,
      /**  Required Qty per ONE of the  END ITEM.  This is a system calculated field.  Calculated as (Parent Required Qty X QtyPer). The parent qty is one if assemblySeq zero else  (QuoteAsmbl.RequireQty) if AssemblySeq > 0.  */  
   "RequiredQty":number,
      /**  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   "EstScrapType":string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   "FixedQty":boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   "FindNum":string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
CLasses could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  */  
   "Class":string,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   "APSAddResType":string,
      /**  A flag to indicate that this quote material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   "RFQNeeded":boolean,
      /**  The number of vendor quotes that are required for this quote material.  Can be zero if RFQ(s) are not required.  */  
   "RFQVendQuotes":number,
      /**  RFQ number that the item is linked to.  */  
   "RFQNum":number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   "RFQStat":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   "GlbRFQ":boolean,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   "PBrkCost02":number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   "PBrkCost03":number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   "PBrkCost04":number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   "PBrkCost05":number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   "PBrkCost06":number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   "PBrkCost07":number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   "PBrkCost08":number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   "PBrkCost09":number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   "PBrkCost10":number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   "PBrkQty01":number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   "PBrkQty02":number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   "PBrkQty03":number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   "PBrkQty04":number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   "PBrkQty05":number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   "PBrkQty06":number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   "PBrkQty07":number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   "PBrkQty08":number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   "PBrkQty09":number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   "PBrkQty10":number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   "PBrkCost01":number,
      /**  Required number of designators  */  
   "ReqRefDes":number,
      /**  The part number used to identify the configured part number initially entered on the assembly.  */  
   "BasePartNum":string,
      /**  The revision number used to identify the configured part/revision number initially entered on the material.  */  
   "BaseRevisionNum":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   "OrigStructTag":string,
      /**  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   "OrigGroupSeq":number,
      /**  Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:  */  
   "EstMtlUnitCost":number,
      /**  LinkToContract  */  
   "LinkToContract":boolean,
      /**  ContractID  */  
   "ContractID":string,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   "MiscCode":string,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   "MiscCharge":boolean,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  Unique identifier per Quote Line that allows PLM Integration to find QuoteMtl record.  */  
   "PLMMtlSeq":number,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   "LocationView":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "SalvageAttributeSetID":number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   "SalvagePlanningNumberOfPieces":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "SalvagePlanningAttributeSetID":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "SalvageRevisionNum":string,
      /**  Delimited list of Address fields in Company format  */  
   "AddrList":string,
      /**  This field will tell if the Direct checkbox will be automatically set. If using a NonPartMaster then this field will be set to FALSE. Otherwise if QtyBearing is Yes then this field will be set to TRUE.  */  
   "AutoSetChkDirect":boolean,
      /**  Base Unit of Measure  */  
   "BaseUOM":string,
      /**  This field is used as and internal flag on BO to enable/disable FixedQty column on UI form.  */  
   "EnableFixedQty":boolean,
   "IsMtlConfigurationOn":boolean,
   "IsMtlConfigureOn":boolean,
   "IsMtlExtConfig":boolean,
      /**  IsMtlRevisionApproved  */  
   "IsMtlRevisionApproved":boolean,
      /**  Internal flag to identify if the Part is an Inventory Part.  */  
   "PartExists":boolean,
      /**  Indicates if theres a price break available and if its expired  */  
   "PBImage":string,
   "QtyBearing":boolean,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   "RDEndNum":number,
      /**  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   "RDPrefix":string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   "RDStartNum":number,
      /**  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   "RDSuffix":string,
      /**  Description from OpMaster of the QuoteOpr.OpCode  */  
   "RelatedOperationDescription":string,
      /**  Salvage Part Base UOM  */  
   "SalvageBaseUOM":string,
      /**  Salvage Part Track Dimension Setting  */  
   "SalvagePartTrackMulti":boolean,
      /**  Scrap Unit of Measure  */  
   "ScrapUOM":string,
      /**  Vendor address formatted  */  
   "VendorAddress":string,
      /**  Planning number of pieces for this attribute set.  */  
   "DispPlanningNumberOfPieces":number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   "DispSalvagePlanningNumberOfPieces":number,
      /**  ID of related Attribute Class.  */  
   "SalvageAttrClassID":string,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   "SalvageTrackInventoryAttributes":boolean,
      /**  Indicates if inventory for this part is tracked by revision.  */  
   "SalvageTrackInventoryByRevision":boolean,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "AssemblySeqDescription":string,
   "ClassDescription":string,
   "ClassInactive":boolean,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumSalesUM":string,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumAttrClassID":string,
   "PurMiscDescription":string,
   "PurPointCountry":string,
   "PurPointName":string,
   "PurPointState":string,
   "PurPointAddress2":string,
   "PurPointZip":string,
   "PurPointPrimPCon":number,
   "PurPointAddress3":string,
   "PurPointCity":string,
   "PurPointAddress1":string,
   "QuoteLineLineDesc":string,
   "QuoteNumCurrencyCode":string,
   "RFQLineLineDesc":string,
   "VendorNumAddress1":string,
   "VendorNumZIP":string,
   "VendorNumName":string,
   "VendorNumTermsCode":string,
   "VendorNumVendorID":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCountry":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress2":string,
   "VendorNumAddress3":string,
   "VendorNumState":string,
   "VendorNumCity":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteOpDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with.   System assigned.  */  
   "QuoteNum":number,
      /**  Used to link back to the QuoteLine.   System assigned.  */  
   "QuoteLine":number,
      /**  Used to link back to the QuoteAsmbl record.  System assigned.  */  
   "AssemblySeq":number,
      /**  Used to link back to the QuoteOpr record.  System assigned.  */  
   "OprSeq":number,
      /**  Uniquely identifies the QuoteOpDtl.  System assigned.  */  
   "OpDtlSeq":number,
      /**  The user can select the capability the operation is to perform.  The system will select the resource.  */  
   "CapabilityID":string,
      /**  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  */  
   "ResourceGrpID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  */  
   "ResourceID":string,
      /**  The standard setup hours for the operation.   This is the setup time required for each machine.  */  
   "SetupHours":number,
      /**  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  */  
   "ProdHours":number,
      /**  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  */  
   "NumResources":number,
      /**  The burden rate used for setup time.  Used as a default in Job and Quote entry.  */  
   "SetupBurRate":number,
      /**  Burden rate used for production time on an operation. Job and Quoting use it as a default when entering operation details.  */  
   "ProdBurRate":number,
      /**  The labor rate used for setup time.  Used as a default in Job and Quote entry.  */  
   "SetupLabRate":number,
      /**  Labor rate used for production time on an operation. Job and Quoting use it as a default when entering operation details.  */  
   "ProdLabRate":number,
      /**  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  */  
   "SetupOrProd":string,
      /**  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   "OpDtlDesc":string,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   "ProdStandard":number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   "StdFormat":string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   "StdBasis":string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   "OpsPerPart":number,
      /**  If yes then the user has overridden the rates that were on the  record when it was inititally created.  The initial rates came from the master files.  */  
   "OverrideRates":boolean,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   "ConcurrentCapacity":number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   "DailyProdRate":number,
      /**  Duplicated from QuoteOper.SetupCrewSize.   It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   "SetUpCrewSize":number,
      /**  Duplicated from QuoteOper.ProdCrewSize.  The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  */  
   "ProdCrewSize":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   "QtyPerCycle":number,
   "CapabilityDesc":string,
      /**  The Operation Standard ID stored in QuoteOpr.  */  
   "OperOpStdID":string,
      /**  Indicates if primary production operation.  */  
   "PrimaryProd":boolean,
      /**  Indicates if primary setup operation.  */  
   "PrimarySetup":boolean,
   "ResourceDesc":string,
   "ResourceGrpDesc":string,
      /**  Flag for sub contract  */  
   "SubContract":boolean,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "CapabilityIDDescription":string,
   "QuoteLineLineDesc":string,
   "QuoteNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteOprActionParamRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this record is associated with.  */  
   "QuoteNum":number,
      /**  The Quote Line that record is related to.  */  
   "QuoteLine":number,
      /**  A sequence number which uniquely identifies the assembly record within the method.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the operation record within the method.  */  
   "OprSeq":number,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   "ActionSeq":number,
      /**  A sequence number which uniquely identifies parameter within the Operation/Action set.  */  
   "ActionParamSeq":number,
      /**  Data type of Action Parameter.  */  
   "ActionParamFieldDataType":string,
      /**  Value of Action Parameter.  */  
   "ActionParamValueCharacter":string,
      /**  Value of Action Parameter.  */  
   "ActionParamValueDate":string,
      /**  Value of Action Parameter.  */  
   "ActionParamValueDecimal":number,
      /**  Value of Action Parameter.  */  
   "ActionParamValueInteger":number,
      /**  Value of Action Parameter.  */  
   "ActionParamValueLogical":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteOprActionRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this record is associated with.  */  
   "QuoteNum":number,
      /**  The Quote Line that record is related to.  */  
   "QuoteLine":number,
      /**  A sequence number which uniquely identifies the assembly record within the method.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the operation record within the method.  */  
   "OprSeq":number,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   "ActionSeq":number,
      /**  Description of Action.  */  
   "ActionDesc":string,
      /**  Indicated if this action must be completed before Operation can be completed.  */  
   "Required":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteOprAttchRow{
   "Company":string,
   "QuoteNum":number,
   "QuoteLine":number,
   "AssemblySeq":number,
   "OprSeq":number,
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

export interface Erp_Tablesets_QuoteOprInspRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with.  */  
   "QuoteNum":number,
      /**  The QuoteLine that record is related to.  */  
   "QuoteLine":number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the operation record within the Quote/Line/Assembly. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last QuoteOpr for the QuoteLine/Asm and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**  A sequence number that uniquely identifies the QuoteOprInsp record within the QuoteNum/QuoteLine/AssemblySeq/OprSeq  */  
   "PlanSeq":number,
      /**  The inspection plan part number (configurator part number).  */  
   "InspPlanPartNum":string,
      /**  The inspection plan revision number (configurator revision number).  */  
   "InspPlanRevNum":string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   "SpecID":string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   "SpecRevNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "SpecHedDescription":string,
   "BitFlag":number,
   "InspPlanDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteOprMachParamRow{
      /**  Company  */  
   "Company":string,
      /**  QuoteNum  */  
   "QuoteNum":number,
      /**  QuoteLine  */  
   "QuoteLine":number,
      /**  AssemblySeq  */  
   "AssemblySeq":number,
      /**  OprSeq  */  
   "OprSeq":number,
      /**  MachParamSeq  */  
   "MachParamSeq":number,
      /**  RequestCode  */  
   "RequestCode":string,
      /**  MachineNum  */  
   "MachineNum":string,
      /**  ToolNum  */  
   "ToolNum":string,
      /**  PartNum  */  
   "PartNum":string,
      /**  ParamNum  */  
   "ParamNum":number,
      /**  ParamUpperLimit  */  
   "ParamUpperLimit":number,
      /**  ParamNominalValue  */  
   "ParamNominalValue":number,
      /**  ParamLowerLimit  */  
   "ParamLowerLimit":number,
      /**  ParamDelayValue  */  
   "ParamDelayValue":number,
      /**  SpecEnable  */  
   "SpecEnable":boolean,
      /**  SpecControlAlarm  */  
   "SpecControlAlarm":boolean,
      /**  SpecRunAlarm  */  
   "SpecRunAlarm":boolean,
      /**  ProcSpecAlarm  */  
   "ProcSpecAlarm":boolean,
      /**  ProcControlAlarm  */  
   "ProcControlAlarm":boolean,
      /**  PartQualSpecEnable  */  
   "PartQualSpecEnable":boolean,
      /**  PartQualControlEnable  */  
   "PartQualControlEnable":boolean,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteOprRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  The QuoteLine that record is related to.  */  
   "QuoteLine":number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the operation record within the Quote/Line/Assembly. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last QuoteOpr for the QuoteLine/Asm and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**   Operation Master Code - Links the QuoteOpr  record with a OpMaster record.  Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  */  
   "OpCode":string,
      /**   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.

Valid for "inside operations" only.  */  
   "OpStdID":string,
      /**  The TOTAL estimated set up hours FOR ALL MACHINES. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours * Machines.  */  
   "EstSetHours":number,
      /**   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.

NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   "ProdStandard":number,
      /**   Qualifier for the Production Standard field.  The valid qualifiers are:

"HP" - Hours/Piece, "MP" - Minutes/Piece, "PH" - Pieces/Hour,

"PM" - Pieces/Minute, "OH" - Operations/Hour,

"OM"  - Operations/Minute, HR - Fixed Hours.  */  
   "StdFormat":string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor to the number of pieces. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.

This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   "StdBasis":string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   "OpsPerPart":number,
      /**  Production Quantity per one of the Parent Item.  */  
   "QtyPer":number,
      /**  Labor rate used for estimated production labor costs. Default from the OpMaster.QProdLRate if not zero, else OpMaster.ProdLRate.  */  
   "ProdLabRate":number,
      /**  Labor rate for estimated setup labor costs. Default from the OpMaster.QSetupLRate if not zero, else OpMaster.SetupLabRate.  */  
   "SetupLabRate":number,
      /**  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.QProdBurRate if not zero, else WrkCenter.ProdBurRate.  */  
   "ProdBurRate":number,
      /**  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.QSetUpBurRate if not zero, else WrkCenter.SetupBurRate.  */  
   "SetupBurRate":number,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is, the more machines the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, NOT SETUP.  The stored setup hours is a total for all machines.  This stored number is divided by the number of machines when it is displayed on the screen during operation maintenance.  */  
   "Machines":number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field.  It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   "SetUpCrewSize":number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  */  
   "ProdCrewSize":number,
      /**  Estimated Scrap (fallout) that is expected to occur on this operation. The scrap increase the Run quantity. Example; need 1000 pieces scrap of 10 % will show a operation run quantity of 1100.  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   "EstScrapType":string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   "SubContract":boolean,
      /**  Issue Unit of Measure. Applicable only when SubContract = Yes  */  
   "IUM":string,
      /**  Hours required is calculated as days * 8. Only Applicable when SubContract = Yes.  */  
   "DaysOut":number,
      /**  The PartNum to be shipped to the subcontract. Applicable only when SubContract = Yes.  Default the QuoteDtl.PartNum or QuoteAsm.PartNum depending on the QuoteOpr.AssemblySeq.  */  
   "PartNum":string,
      /**  Description of item to be sent to subcontractor.  */  
   "Description":string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   "PurPoint":string,
      /**  Editor widget for quote operation comments.  */  
   "CommentText":string,
      /**   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   "SchedRelation":string,
      /**  Minimum Cost that will be used for subcontract costs. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the subcontract cost for the quote.  */  
   "MinimumCost":number,
      /**  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   "EstUnitCost":number,
      /**  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calcs are rounded up to the next whole number before multiplying by the AddlSetUpHours..  */  
   "AddlSetupHours":number,
      /**  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  */  
   "AddlSetUpQty":number,
      /**  Specifies the total production quantity for this operation. This is an application calculated field used for display purposes only. If no quantity is calculated, the default quantity displays the value of one. The value that displays in this field calculates as follows: Run Quantity = Scrap Quantity + Production Quantity. Note: The Run Qty value refreshes when maintenance is performed on the operation record or the assemblies production quantity is changed.  */  
   "RunQty":number,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   "MiscAmt":number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   "WIQueStartDate":string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   "WIQueStartHour":number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   "WIStartDate":string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   "WIStartHour":number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueDate":string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueHour":number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIMoveDueDate":string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIMoveDueHour":number,
      /**  The Number of Hours per machine per day that this operations "actual" schedule is based on.  Used in logic of quote scheduling.  */  
   "WIHoursPerMachine":number,
      /**  A flag to indicate that this quote operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   "RFQNeeded":boolean,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   "LaborEntryMethod":string,
      /**  The number of vendor quotes that are required for this quote subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   "RFQVendQuotes":number,
      /**  The quantity requested for first article inspection.  */  
   "FAQty":number,
      /**  RFQ number that the item is linked to.  */  
   "RFQNum":number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   "RFQStat":string,
      /**  Used to group operation to save on setups.  */  
   "SetupGroup":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**   Identifies the primary QuoteOpDtl to be used for setup.  The setup time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = S or B.  */  
   "PrimarySetupOpDtl":number,
      /**   Identifies the primary QuoteOpDtl to be used for production.  The production run time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = P or B.  */  
   "PrimaryProdOpDtl":number,
      /**  Operation Description.  */  
   "OpDesc":string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   "GlbRFQ":boolean,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty07":number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty08":number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty09":number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty10":number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   "PBrkCost01":number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   "PBrkCost02":number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   "PBrkCost03":number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   "PBrkCost04":number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   "PBrkCost05":number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   "PBrkCost06":number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   "PBrkCost07":number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   "PBrkCost08":number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   "PBrkCost09":number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   "PBrkCost10":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   "PBrkStdRate01":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   "PBrkStdRate02":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   "PBrkStdRate03":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   "PBrkStdRate04":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   "PBrkStdRate05":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   "PBrkStdRate06":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   "PBrkStdRate07":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   "PBrkStdRate08":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   "PBrkStdRate09":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   "PBrkStdRate10":number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty01":number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty02":number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty03":number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty04":number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty05":number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty06":number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   "SNRequiredOpr":boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   "SNRequiredSubConShip":boolean,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   "SendAheadType":string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   "SendAheadOffset":number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   "PrjRoleList":string,
      /**  Allow use all Roles  */  
   "UseAllRoles":boolean,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  PctReg  */  
   "PctReg":number,
      /**  SetupMaterial  */  
   "SetupMaterial":number,
      /**  MaterialColorRating  */  
   "MaterialColorRating":number,
      /**  MiscInfo1  */  
   "MiscInfo1":string,
      /**  MiscInfo2  */  
   "MiscInfo2":string,
      /**  SetupURL  */  
   "SetupURL":string,
      /**  ExpPctUp  */  
   "ExpPctUp":number,
      /**  ExpCycTm  */  
   "ExpCycTm":number,
      /**  ExpGood  */  
   "ExpGood":number,
      /**  NonProdLimit  */  
   "NonProdLimit":number,
      /**  AutoSpcEnable  */  
   "AutoSpcEnable":boolean,
      /**  AutoSpcPeriod  */  
   "AutoSpcPeriod":number,
      /**  PartQualEnable  */  
   "PartQualEnable":boolean,
      /**  AutoSpcSubgroup  */  
   "AutoSpcSubgroup":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   "QtyPerCycle":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  TemplateID  */  
   "TemplateID":string,
      /**  StageNumber  */  
   "StageNumber":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Indicates if the scheduling resources should be refreshed when the op code changes.  */  
   "RefreshResources":boolean,
      /**  Vendor Address  */  
   "AddrList":string,
   "APSAltOpDesc":string,
   "APSNextOpDesc":string,
   "APSPrepOpDesc":string,
   "AutoReceive":boolean,
      /**  Used to display selected UOM next to unit cost field  */  
   "DspQtyIUM":string,
      /**  Indicates whether to enable the AutoReceive field  */  
   "EnableAutoRec":boolean,
      /**  This field is used as a flag to enable/disable the controls binded to SNRequiredOpr column in UI forms.  */  
   "EnableSNRequiredOpr":boolean,
      /**  This field is used as a flag for SNRequiredSubConShip column to determine when to enable/disable it on UI form.  */  
   "EnableSNSubConShip":boolean,
   "FinalOpr":boolean,
   "HoursPerMachine":number,
   "OpStdDescription":string,
   "PBImage":string,
      /**  Primary Resource Group Description  */  
   "PrimaryResourceGrpDesc":string,
      /**  The Resource Group ID of the primary production operation detail.  */  
   "PrimaryResourceGrpID":string,
      /**  Vendor address formatted  */  
   "VendorAddress":string,
      /**  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   "PrimaryProdOpDtlDesc":string,
      /**  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   "PrimarySetupOpDtlDesc":string,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "AssemblySeqDescription":string,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "OpCodeOpDesc":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumSellingFactor":number,
   "PartNumPricePerCode":string,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PurPointCity":string,
   "PurPointState":string,
   "PurPointZip":string,
   "PurPointCountry":string,
   "PurPointAddress1":string,
   "PurPointName":string,
   "PurPointAddress3":string,
   "PurPointAddress2":string,
   "PurPointPrimPCon":number,
   "QuoteLineLineDesc":string,
   "QuoteNumCurrencyCode":string,
   "RFQLineLineDesc":string,
   "SetupGroupDescription":string,
   "VendorNumAddress2":string,
   "VendorNumAddress1":string,
   "VendorNumCountry":string,
   "VendorNumCity":string,
   "VendorNumCurrencyCode":string,
   "VendorNumVendorID":string,
   "VendorNumName":string,
   "VendorNumZIP":string,
   "VendorNumState":string,
   "VendorNumAddress3":string,
   "VendorNumTermsCode":string,
   "VendorNumDefaultFOB":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteStageRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this record is associated with.  */  
   "QuoteNum":number,
      /**  The Quote Line that record is related to.  */  
   "QuoteLine":number,
      /**  Assembly Sequence # that this Stage is associated with.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies stage record within the stage set.  */  
   "StageSeq":number,
      /**  The identification of related StageNo.  */  
   "StageNumber":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
   "StageNumberDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipQuoteNum
      @param ipQuoteLine
      @param ipAsmSeq
      @param ipMtlSeq
      @param ipPrefix
      @param ipStartNum
      @param ipEndNum
      @param ipSuffix
      @param ds
   */  
export interface AddRefDesRange_input{
      /**  The Quote Number  */  
   ipQuoteNum:number,
      /**  The Quote Line Number  */  
   ipQuoteLine:number,
      /**  The Quote Assembly  */  
   ipAsmSeq:number,
      /**  The Quote Material Seq  */  
   ipMtlSeq:number,
      /**  The Prefix to be used to delete Reference Designators  */  
   ipPrefix:string,
      /**  The Starting Number to delete Reference Designators  */  
   ipStartNum:number,
      /**  The Ending Number to delete Reference Designators  */  
   ipEndNum:number,
      /**  The Suffix to be used to delete Reference Designators  */  
   ipSuffix:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface AddRefDesRange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param targetQuote
      @param targetLine
      @param targetAsm
      @param sourceFile
      @param keyOne
      @param keyTwo
      @param keyThree
      @param ipCompleteTree
   */  
export interface AppendDetails_input{
   ds:Erp_Tablesets_QtAppendTableset[],
      /**  Target Quote  */  
   targetQuote:number,
      /**  Target QuoteLine  */  
   targetLine:number,
      /**  Target Quote AssemblySeq  */  
   targetAsm:number,
      /**  Indicates where the details are being appended from.  Either Quote,
           Job or Method  */  
   sourceFile:string,
      /**  Unique key field one for Job or Method source  */  
   keyOne:string,
      /**  Unique key field two for Method source  */  
   keyTwo:string,
      /**  Unique key field two for Method source  */  
   keyThree:string,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface AppendDetails_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
parameters : {
      /**  output parameters  */  
   errorList:string,
}
}

   /** Required : 
      @param sourceFile
      @param keyOne
      @param keyTwo
      @param keyThree
      @param targetQuote
      @param targetLine
      @param targetAsm
      @param vShipByDate
   */  
export interface BuildAppendDetails_input{
      /**  Source of the append details, Quote, Job or Method  */  
   sourceFile:string,
      /**  First key field of source  */  
   keyOne:string,
      /**  Second key field of source  */  
   keyTwo:string,
      /**  Third key field of source  */  
   keyThree:string,
      /**  Target Quote Num  */  
   targetQuote:number,
      /**  Target Line Number  */  
   targetLine:number,
      /**  Target Assembly  */  
   targetAsm:number,
      /**  used to correctly calculate Revision for Pahntom Mtls on Append Details.  */  
   vShipByDate:string,
}

export interface BuildAppendDetails_output{
   returnObj:Erp_Tablesets_QtAppendTableset[],
}

   /** Required : 
      @param ds
   */  
export interface ChangeJobAsmblParent_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeJobAsmblParent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ProposedPurPoint
      @param ds
   */  
export interface ChangeMtlPurPoint_input{
      /**  The proposed Purchase Point  */  
   ProposedPurPoint:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeMtlPurPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ProposedCapID
      @param ds
   */  
export interface ChangeOpDtlCapability_input{
      /**  The proposed Capability ID  */  
   ProposedCapID:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeOpDtlCapability_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeOpDtlOverrideRates_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeOpDtlOverrideRates_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ProposedResGrpID
      @param ds
   */  
export interface ChangeOpDtlResourceGrpID_input{
      /**  The proposed Resource Group ID  */  
   ProposedResGrpID:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeOpDtlResourceGrpID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ProposedResourceID
      @param ds
   */  
export interface ChangeOpDtlResourceID_input{
      /**  The proposed Resource ID  */  
   ProposedResourceID:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeOpDtlResourceID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeOpMtlReqQty_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeOpMtlReqQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeOpMtlSalvageReqQty_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeOpMtlSalvageReqQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param iAutoReceive
      @param ds
   */  
export interface ChangeOperAutoReceive_input{
      /**  Proposed value for AutoReceive field  */  
   iAutoReceive:boolean,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeOperAutoReceive_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param iLaborEntryMethod
      @param ds
   */  
export interface ChangeOperLaborEntryMethod_input{
      /**  Proposed value for LaborEntryMethod field  */  
   iLaborEntryMethod:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeOperLaborEntryMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeOperPrimaryProdOpDtl_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeOperPrimaryProdOpDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeOperPrimarySetupOpDtl_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeOperPrimarySetupOpDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ProposedPurPoint
      @param ds
   */  
export interface ChangeOperPurPoint_input{
      /**  The proposed Purchase Point  */  
   ProposedPurPoint:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeOperPurPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ProposedVendorID
      @param ds
   */  
export interface ChangeOperVendorID_input{
      /**  The proposed Vendor ID  */  
   ProposedVendorID:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeOperVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuoteAsmReqRefDes_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteAsmReqRefDes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuoteAsmblQtyPer_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteAsmblQtyPer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ipProposedValResDes
      @param ds
   */  
export interface ChangeQuoteAsmblValRefDes_input{
      /**  The new proposed QuoteAsmbl.ValRefDes value  */  
   ipProposedValResDes:boolean,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteAsmblValRefDes_output{
}

   /** Required : 
      @param ipProposedEstUnitCost
      @param ds
   */  
export interface ChangeQuoteMtlEstUnitCost_input{
      /**  The new proposed QuoteMtl.MtlBurRate value  */  
   ipProposedEstUnitCost:number,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteMtlEstUnitCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuoteMtlIUM_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteMtlIUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuoteMtlLinkToContract_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteMtlLinkToContract_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuoteMtlMiscCharge_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteMtlMiscCharge_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ipProposedMtlBurRate
      @param ds
   */  
export interface ChangeQuoteMtlMtlBurRate_input{
      /**  The new proposed QuoteMtl.MtlBurRate value  */  
   ipProposedMtlBurRate:number,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteMtlMtlBurRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuoteMtlReqRefDes_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteMtlReqRefDes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ipProposedSalvageMtlBurRate
      @param ds
   */  
export interface ChangeQuoteMtlSalvageMtlBurUnitRate_input{
      /**  The new proposed ECOMtl.SalvageMtlBurRate value  */  
   ipProposedSalvageMtlBurRate:number,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteMtlSalvageMtlBurUnitRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ipProposedSalvagePartNum
      @param ds
   */  
export interface ChangeQuoteMtlSalvagePartNum_input{
      /**  The new proposed ECOMtl.SalvagePartNum value  */  
   ipProposedSalvagePartNum:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteMtlSalvagePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuoteMtlSalvageUM_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteMtlSalvageUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ipProposedSalvageUnitCredit
      @param ds
   */  
export interface ChangeQuoteMtlSalvageUnitCredit_input{
      /**  The new proposed ECOMtl.SalvageUnitCredit value  */  
   ipProposedSalvageUnitCredit:number,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteMtlSalvageUnitCredit_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuoteOprIUM_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteOprIUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ipProposedOprSeq
      @param ds
   */  
export interface ChangeQuoteOprOprSeq_input{
      /**  The new proposed QuoteOpr.OprSeq value  */  
   ipProposedOprSeq:number,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteOprOprSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuoteOprQtyPer_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteOprQtyPer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ipProposedSNRequired
      @param ds
   */  
export interface ChangeQuoteOprSNRequiredOpr_input{
      /**  The new proposed QuoteAsm.SNRequiredOpr value  */  
   ipProposedSNRequired:boolean,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeQuoteOprSNRequiredOpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ipProposedPartNum
      @param ds
   */  
export interface ChangeSubcontractPartNum_input{
      /**  The new proposed QuoteOpr.PartNum value  */  
   ipProposedPartNum:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ChangeSubcontractPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ipNewParent
      @param ds
   */  
export interface CheckChangeJobAsmblParent_input{
      /**  New Parent value to check against  */  
   ipNewParent:number,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface CheckChangeJobAsmblParent_output{
}

   /** Required : 
      @param relatedToTable
      @param relatedToSysRowID
      @param sourcePart
      @param sourceRevision
      @param findRevision
      @param foreignTable
      @param foreignSysRowID
   */  
export interface CheckConfigurationAndGetConfigInfo_input{
      /**  Related To File  */  
   relatedToTable:string,
      /**  The job on which the configuration should be saved.  */  
   relatedToSysRowID:string,
      /**  Part Num to get details from (populated when sourceFile = "Method")  */  
   sourcePart:string,
      /**  Revision number to get details from (populated when sourceFile = "Method")  */  
   sourceRevision:string,
      /**  Foreign row  */  
   findRevision:boolean,
      /**  Foreign row  */  
   foreignTable:string,
      /**  Foreign row SysRowID  */  
   foreignSysRowID:string,
}

export interface CheckConfigurationAndGetConfigInfo_output{
parameters : {
      /**  output parameters  */  
   foreignTable:string,
   foreignSysRowID:string,
   configurationExists:boolean,
   canGetDetails:boolean,
   needsConfiguration:boolean,
   configureRevision:string,
   reasonMessage:string,
   warningMsg:boolean,
   isNIC:boolean,
   structTag:string,
   ruleTag:string,
   configType:string,
   configURL:string,
   configID:string,
   kbConfigProdID:number,
}
}

   /** Required : 
      @param relatedToTable
      @param relatedToSysRowID
      @param sourcePart
      @param sourceRevision
      @param findRevision
      @param foreignTable
      @param foreignSysRowID
   */  
export interface CheckConfigurationAndGetConfigType_input{
      /**  Related To File  */  
   relatedToTable:string,
      /**  The job on which the configuration should be saved.  */  
   relatedToSysRowID:string,
      /**  Part Num to get details from (populated when sourceFile = "Method")  */  
   sourcePart:string,
      /**  Revision number to get details from (populated when sourceFile = "Method")  */  
   sourceRevision:string,
      /**  Foreign row  */  
   findRevision:boolean,
      /**  Foreign row  */  
   foreignTable:string,
      /**  Foreign row SysRowID  */  
   foreignSysRowID:string,
}

export interface CheckConfigurationAndGetConfigType_output{
parameters : {
      /**  output parameters  */  
   foreignTable:string,
   foreignSysRowID:string,
   configurationExists:boolean,
   canGetDetails:boolean,
   needsConfiguration:boolean,
   configureRevision:string,
   reasonMessage:string,
   warningMsg:boolean,
   isNIC:boolean,
   structTag:string,
   ruleTag:string,
   configType:string,
   configURL:string,
   configID:string,
}
}

   /** Required : 
      @param relatedToTable
      @param relatedToSysRowID
      @param sourcePart
      @param sourceRevision
      @param findRevision
      @param foreignTable
      @param foreignSysRowID
   */  
export interface CheckConfiguration_input{
      /**  Related To File  */  
   relatedToTable:string,
      /**  The job on which the configuration should be saved.  */  
   relatedToSysRowID:string,
      /**  Part Num to get details from (populated when sourceFile = "Method")  */  
   sourcePart:string,
      /**  Revision number to get details from (populated when sourceFile = "Method")  */  
   sourceRevision:string,
   findRevision:boolean,
      /**  Foreign row  */  
   foreignTable:string,
      /**  Foreign row SysRowID  */  
   foreignSysRowID:string,
}

export interface CheckConfiguration_output{
parameters : {
      /**  output parameters  */  
   foreignTable:string,
   foreignSysRowID:string,
   configurationExists:boolean,
   canGetDetails:boolean,
   needsConfiguration:boolean,
   configureRevision:string,
   reasonMessage:string,
   warningMsg:boolean,
   isNIC:boolean,
   structTag:string,
   ruleTag:string,
}
}

   /** Required : 
      @param ds
      @param ipPrimaryProdOpDtl
   */  
export interface CheckOperPrimaryProdOpDtl_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  The new PrimaryProdOpDtl value to change to  */  
   ipPrimaryProdOpDtl:number,
}

export interface CheckOperPrimaryProdOpDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param ipPrimarySetupOpDtl
   */  
export interface CheckOperPrimarySetupOpDtl_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  The new PrimarySetupOpDtl value to change to  */  
   ipPrimarySetupOpDtl:number,
}

export interface CheckOperPrimarySetupOpDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
   */  
export interface CheckPartErrors_input{
      /**  Quote Number  */  
   quoteNum:number,
      /**  QuoteLine, 0 for all lines, otherwise only looks a specific line  */  
   quoteLine:number,
}

export interface CheckPartErrors_output{
parameters : {
      /**  output parameters  */  
   runOutWarnings:string,
}
}

   /** Required : 
      @param partNum
      @param sourceTable
      @param sourceSysRowID
   */  
export interface CheckPrePartInfo_input{
      /**  The new PartNum if a substitute part is found, partNum will be the substitute part  */  
   partNum:string,
      /**  The table that caused this method to be called  */  
   sourceTable:string,
      /**  sys row DI of the source table - this is needed for the product configurator logic  */  
   sourceSysRowID:string,
}

export interface CheckPrePartInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   vMessage:string,
   vSubAvail:boolean,
   vMsgType:string,
   productConfiguratorMessage:string,
}
}

   /** Required : 
      @param ds
      @param ipProposedPartNum
   */  
export interface CheckQuoteMtlPartNum_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  Identifies the PartNum to validate  */  
   ipProposedPartNum:string,
}

export interface CheckQuoteMtlPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ipQuoteNum
      @param ipQuoteLine
      @param ipAsmSeq
   */  
export interface CollapseAssembly_input{
   ipQuoteNum:number,
   ipQuoteLine:number,
   ipAsmSeq:number,
}

export interface CollapseAssembly_output{
}

   /** Required : 
      @param quoteNum
      @param quoteLine
   */  
export interface DeleteAllAssembly_input{
      /**  Quote Number of the assemblies  */  
   quoteNum:number,
      /**  Quote Assembly Line Number  */  
   quoteLine:number,
}

export interface DeleteAllAssembly_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param assemblySeq
   */  
export interface DeleteByID_input{
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ipQuoteNum
      @param ipQuoteLine
      @param ipAsmSeq
      @param ipMtlSeq
      @param ipPrefix
      @param ipStartNum
      @param ipEndNum
      @param ipSuffix
      @param ds
   */  
export interface DeleteRefDesRange_input{
      /**  The Quote Number  */  
   ipQuoteNum:number,
      /**  The Quote Line Number  */  
   ipQuoteLine:number,
      /**  The Quote Assembly  */  
   ipAsmSeq:number,
      /**  The Quote Material Seq  */  
   ipMtlSeq:number,
      /**  The Prefix to be used to delete Reference Designators  */  
   ipPrefix:string,
      /**  The Starting Number to delete Reference Designators  */  
   ipStartNum:number,
      /**  The Ending Number to delete Reference Designators  */  
   ipEndNum:number,
      /**  The Suffix to be used to delete Reference Designators  */  
   ipSuffix:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface DeleteRefDesRange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

export interface EnableSupplierPriceList_output{
parameters : {
      /**  output parameters  */  
   lEnableSupplierPriceList:boolean,
}
}

export interface Erp_Tablesets_QtAppendTableset{
   QtMtlApp:Erp_Tablesets_QtMtlAppRow[],
   QtOprApp:Erp_Tablesets_QtOprAppRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_QtMtlAppRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  */  
   MtlSeq:number,
      /**  Part number of required material. Does not have to be valid in Part master file, but must not be blank.  */  
   PartNum:string,
      /**  Description of the material. Cannot be blank  */  
   Description:string,
      /**  Quantity required per one of the Parent item. This is a factor used in calculating the total material requirement.  */  
   QtyPer:number,
      /**  The issue/usage unit of measure for this material.  */  
   IUM:string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  */  
   Direct:boolean,
      /**  Expected Purchasing lead time (in days) for the material. This is passed along to the job if the item gets manufactured.  */  
   LeadTime:number,
      /**   A material record can be related to a specific operation. This field contains the QuoteOpr.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  */  
   RelatedOperation:number,
      /**  Part number for Salvaged scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  */  
   SalvagePartNum:string,
      /**  Description of Salvaged material. Use Part.Description for a default.  */  
   SalvageDescription:string,
      /**  A factor that multiplied by the RequiredQty for the material results in the expected total salvage quantity.  */  
   SalvageQtyPer:number,
      /**  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  */  
   SalvageUM:string,
      /**  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  */  
   SalvageUnitCredit:number,
      /**  The salvage material burden rate for this Quote Material.  */  
   SalvageMtlBurRate:number,
      /**  Estimated salvage Mtl Burden Unit Credit. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   SalvageEstMtlBurUnitCredit:number,
      /**   Comments for manufacturing about this material record. These comments are printed on manufacturing reports,  such as the router. For valid Parts use the Part.MfgComment as a default.
View as Editor widget.  */  
   MfgComment:string,
      /**  Used to identify a default vendor. Use the Part.VendorNum as a default. This will be used as a default for purchasing and miscellaneous receipts. This field is not directly maintainable; instead it's assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  An optional field, but if entered must be valid.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Indicates if this material is to be Purchased for the Job. If this is a non inventory part then this is "Yes" and can't be changed. If this is a valid Part then set it to "NO" but the user can override it.  */  
   BuyIt:boolean,
      /**   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.

View as Editor widget.  */  
   PurComment:string,
      /**  Minimum Cost that will be used for this material. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the material cost for the quote.  */  
   MinimumCost:number,
      /**  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   EstUnitCost:number,
      /**  The material burden rate for this Quote Material.  */  
   MtlBurRate:number,
      /**  Estimated Mtl Burden Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   EstMtlBurUnitCost:number,
      /**  Required Qty per ONE of the  END ITEM.  This is a system calculated field.  Calculated as (Parent Required Qty X QtyPer). The parent qty is one if assemblySeq zero else  (QuoteAsmbl.RequireQty) if AssemblySeq > 0.  */  
   RequiredQty:number,
      /**  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   FixedQty:boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   FindNum:string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
CLasses could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  */  
   Class:string,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   APSAddResType:string,
      /**  A flag to indicate that this quote material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this quote material.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost02:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost03:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost04:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost05:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost06:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost07:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost08:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost09:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost10:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty01:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty02:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty03:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty04:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty05:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty06:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty07:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty08:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty09:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty10:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost01:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Indicates whether to append QuoteMtl record or not  */  
   Append:boolean,
   MtlPartNum:string,
      /**  The alternate method for the material.  */  
   AltMethod:string,
      /**  Original Material Sequence  */  
   OrigMtlSeq:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QtOprAppRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Quote/Line/Assembly. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last QuoteOpr for the QuoteLine/Asm and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**   Operation Master Code - Links the QuoteOpr  record with a OpMaster record.  Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.

Valid for "inside operations" only.  */  
   OpStdID:string,
      /**  The TOTAL estimated set up hours FOR ALL MACHINES. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours * Machines.  */  
   EstSetHours:number,
      /**   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.

NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**   Qualifier for the Production Standard field.  The valid qualifiers are:

"HP" - Hours/Piece, "MP" - Minutes/Piece, "PH" - Pieces/Hour,

"PM" - Pieces/Minute, "OH" - Operations/Hour,

"OM"  - Operations/Minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor to the number of pieces. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.

This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  Production Quantity per one of the Parent Item.  */  
   QtyPer:number,
      /**  Labor rate used for estimated production labor costs. Default from the OpMaster.QProdLRate if not zero, else OpMaster.ProdLRate.  */  
   ProdLabRate:number,
      /**  Labor rate for estimated setup labor costs. Default from the OpMaster.QSetupLRate if not zero, else OpMaster.SetupLabRate.  */  
   SetupLabRate:number,
      /**  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.QProdBurRate if not zero, else WrkCenter.ProdBurRate.  */  
   ProdBurRate:number,
      /**  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.QSetUpBurRate if not zero, else WrkCenter.SetupBurRate.  */  
   SetupBurRate:number,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is, the more machines the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, NOT SETUP.  The stored setup hours is a total for all machines.  This stored number is divided by the number of machines when it is displayed on the screen during operation maintenance.  */  
   Machines:number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field.  It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  */  
   ProdCrewSize:number,
      /**  Estimated Scrap (fallout) that is expected to occur on this operation. The scrap increase the Run quantity. Example; need 1000 pieces scrap of 10 % will show a operation run quantity of 1100.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  Issue Unit of Measure. Applicable only when SubContract = Yes  */  
   IUM:string,
      /**  Hours required is calculated as days * 8. Only Applicable when SubContract = Yes.  */  
   DaysOut:number,
      /**  The PartNum to be shipped to the subcontract. Applicable only when SubContract = Yes.  Default the QuoteDtl.PartNum or QuoteAsm.PartNum depending on the QuoteOpr.AssemblySeq.  */  
   PartNum:string,
      /**  Description of item to be sent to subcontractor.  */  
   Description:string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Editor widget for quote operation comments.  */  
   CommentText:string,
      /**   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   SchedRelation:string,
      /**  Minimum Cost that will be used for subcontract costs. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the subcontract cost for the quote.  */  
   MinimumCost:number,
      /**  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   EstUnitCost:number,
      /**  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calcs are rounded up to the next whole number before multiplying by the AddlSetUpHours..  */  
   AddlSetupHours:number,
      /**  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  */  
   AddlSetUpQty:number,
      /**  Specifies the total production quantity for this operation. This is an application calculated field used for display purposes only. If no quantity is calculated, the default quantity displays the value of one. The value that displays in this field calculates as follows: Run Quantity = Scrap Quantity + Production Quantity. Note: The Run Qty value refreshes when maintenance is performed on the operation record or the assemblies production quantity is changed.  */  
   RunQty:number,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   MiscAmt:number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIQueStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIQueStartHour:number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIStartHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIMoveDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIMoveDueHour:number,
      /**  The Number of Hours per machine per day that this operations "actual" schedule is based on.  Used in logic of quote scheduling.  */  
   WIHoursPerMachine:number,
      /**  A flag to indicate that this quote operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   RFQNeeded:boolean,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  The number of vendor quotes that are required for this quote subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  The quantity requested for first article inspection.  */  
   FAQty:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**   Identifies the primary QuoteOpDtl to be used for setup.  The setup time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = S or B.  */  
   PrimarySetupOpDtl:number,
      /**   Identifies the primary QuoteOpDtl to be used for production.  The production run time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = P or B.  */  
   PrimaryProdOpDtl:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty07:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty08:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty09:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty10:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost01:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost02:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost03:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost04:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost05:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost06:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost07:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost08:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost09:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost10:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate01:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate02:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate03:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate04:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate05:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate06:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate07:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate08:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate09:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate10:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty01:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty02:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty03:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty04:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty05:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty06:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   APSPrepOp:number,
   APSNextOp:number,
   APSAltOp:number,
   APSSpecificResource:string,
   APSCycleTime:number,
   APSConstantTime:number,
   APSSetupGroup:number,
   APSMakeFactor:number,
   APSContainerSize:number,
   APSSchedulerName:string,
   APSMaxLength:number,
   APSTransferTime:number,
   APSEffectiveness:number,
   APSOperationClass:string,
   APSAuxResource:string,
   APSAddResource:string,
      /**  Indicates whether to append details or not  */  
   Append:boolean,
      /**  Holds new Seq for search of QuoteMtl.RelatedOperation  */  
   AppendedOprSeq:number,
   FinalOperation:boolean,
   AutoReceive:boolean,
      /**  ResourceGrpID  */  
   ResourceGrpID:string,
      /**  Job Oper Alternate Method.  */  
   AltMethod:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteAsmAttchRow{
   Company:string,
   QuoteNum:number,
   QuoteLine:number,
   AssemblySeq:number,
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

export interface Erp_Tablesets_QuoteAsmInspRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely identifies the QuoteAsmInsp record within the QuoteNum/QuoteLine/AssemblySeq  */  
   PlanSeq:number,
      /**  The inspection plan part number (configurator part number).  */  
   InspPlanPartNum:string,
      /**  The inspection plan revision number (configurator revision number).  */  
   InspPlanRevNum:string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   SpecID:string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   SpecRevNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   SpecHedDescription:string,
   BitFlag:number,
   InspPlanDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteAsmListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the last QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  An integer that uniquely identifies the Assembly record within the Quote/Line.  Assigned by the system one greater than the last QuoteAsm record on file for the given quote/line.  */  
   AssemblySeq:number,
      /**  Part number for this assembly.  Cannot be blank.  It does not have to be valid in the Part master file.  */  
   PartNum:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description if valid Part record.  */  
   Description:string,
      /**  The revision number for the assembly. An optional field. Use the Part.RevisionNum as a default.  */  
   RevisionNum:string,
      /**  The production Quantity required for this assembly per one of it's Parent Part.  */  
   QtyPer:number,
      /**  The unit of measure for this assembly. Use the Part.IUM as a default.  */  
   IUM:string,
      /**  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse  */  
   Direct:boolean,
      /**  Sequence number of the Parent Assembly.  0 means no parent assembly (i.e. this is the final assembly).  Cannot be negative like the other pointers because this one shows up in a browser.  */  
   Parent:number,
      /**   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find the last assembly (i.e. where the Parent is the same and the NextPeer is -1). Then NextPeer of that assembly gets updated with this assembly's sequence number and this assembly gets its PriorPeer field updated with the sequence number from that assembly which was found.  -1 means that there is no prior assembly (i.e. it is the first assembly of its peers).  */  
   PriorPeer:number,
      /**   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find the first assembly (i.e. where the Parent is the same and the PriorPeer is -1).  Then the PriorPeer of that assembly is updated with this assembly's sequence number and then this assembly's NextPeer gets updated with the sequence number from the assembly that was found.   -1 means that the assembly is the last assembly of its peers.  */  
   NextPeer:number,
      /**  Seq # of this assembly's very first subassembly. This is known as the Child assembly. Automatically maintained by the maintenance programs. The logic is to find the Parent assembly record and if its child is -1, update it with this assembly's seq #.  */  
   Child:number,
      /**  Optional field for Engineering Drawing Number. Defaulted from BomHead.DrawNum during methods pull functions.  */  
   DrawNum:string,
      /**  Editor widget for Job Assembly comments.  */  
   CommentText:string,
      /**  An internally system assigned integer which is used as part of an index to organize the QuoteAsm records into a Bill of Material fashion sequence.  */  
   BomSequence:number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the QuoteAsm in reference to the Bill of Material structure.  */  
   BomLevel:number,
      /**   A system maintained field. This is how many of the assemblies are required to produce ONE of the END ITEM.  This is a calculated field.  Calculated as the
 ( Parents RequiredQty  X QtyPer).
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer. The refresh may also occur if the structure of the assemblies is changed.  */  
   RequiredQty:number,
      /**  Indicates if this quote assembly is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   Template:boolean,
      /**   The operation number (Quote.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  */  
   FindNum:string,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIStartHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueHour:number,
      /**   An assembly record can be related to a specific operation.  This field contains the QuoteOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  */  
   RelatedOperation:number,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
   OrigMtlSeq:number,
   OrigRuleTag:string,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  The part number used to identify the configured part number initially entered on the assembly.  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part/revision number initially entered on the material.  */  
   BaseRevisionNum:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   RelatedOperationDescription:string,
      /**  QutoeAsm.PartNum of the Parent Assembly  */  
   ParentPartNum:string,
      /**  QuoteAsm.RevisionNum of the Parent Assembly  */  
   ParentRevisionNum:string,
      /**  QuoteAsm.Description of Parent assmebly  */  
   ParentDescription:string,
      /**  Boolean to indicate GetDetails has started  */  
   ProcessingDetails:boolean,
      /**  Clone of the Parent field (.Net keyword issue)  */  
   ParentAssemblySeq:number,
      /**  Clone of the Child field (.Net keyword issue)  */  
   ChildAssemblySeq:number,
      /**  Add assembly as "Sub"assembly or "Asm"bly  */  
   AddAsmAs:string,
      /**  If this field is true, then the current value of ttQuoteAsm.AssemblySeq will be used when creating new QuoteAsm records. This allows processes, like PLM, to create new QuoteAsm records with a specific AssemblySeq.  */  
   OverrideNextAsmSeq:boolean,
      /**  The prefix will be defaulted from the reference category defined for the assemblies. The value on this field will be used to create reference designators.  */  
   RDPrefix:string,
      /**  The suffix will be defaulted from the reference category defined for the assemblie. The value on this field will be used to create reference designators.  */  
   RDSuffix:string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   RDStartNum:number,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   RDEndNum:number,
      /**  Description  */  
   AnalysisCdDescription:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   QuoteLineLineDesc:string,
      /**  A unique code that identifies the currency.  */  
   QuoteNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteAsmListTableset{
   QuoteAsmList:Erp_Tablesets_QuoteAsmListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_QuoteAsmRefDesRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  */  
   MtlSeq:number,
      /**  Identifier of Reference Designator  */  
   RefDes:string,
      /**  Unique identifies the reference designator with the material sequence.  */  
   RefDesSeq:number,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   MtlPartNum:string,
      /**  Free form side location. (Top, Bottom, Both, Level, etc)  */  
   Side:string,
      /**  X Coordinate of the reference designator  */  
   XLocation:number,
      /**  Y Coordinate of the reference designator  */  
   YLocation:number,
      /**  Z Coordinate of the reference designator  */  
   ZLocation:number,
      /**  Rotation of the reference designator. Max value = 360.000  */  
   Rotation:number,
      /**  Designator Description  */  
   Description:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteAsmRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the last QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  An integer that uniquely identifies the Assembly record within the Quote/Line.  Assigned by the system one greater than the last QuoteAsm record on file for the given quote/line.  */  
   AssemblySeq:number,
      /**  Part number for this assembly.  Cannot be blank.  It does not have to be valid in the Part master file.  */  
   PartNum:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description if valid Part record.  */  
   Description:string,
      /**  The revision number for the assembly. An optional field. Use the Part.RevisionNum as a default.  */  
   RevisionNum:string,
      /**  The production Quantity required for this assembly per one of it's Parent Part.  */  
   QtyPer:number,
      /**  The unit of measure for this assembly. Use the Part.IUM as a default.  */  
   IUM:string,
      /**  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse  */  
   Direct:boolean,
      /**  Sequence number of the Parent Assembly.  0 means no parent assembly (i.e. this is the final assembly).  Cannot be negative like the other pointers because this one shows up in a browser.  */  
   Parent:number,
      /**   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find the last assembly (i.e. where the Parent is the same and the NextPeer is -1). Then NextPeer of that assembly gets updated with this assembly's sequence number and this assembly gets its PriorPeer field updated with the sequence number from that assembly which was found.  -1 means that there is no prior assembly (i.e. it is the first assembly of its peers).  */  
   PriorPeer:number,
      /**   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find the first assembly (i.e. where the Parent is the same and the PriorPeer is -1).  Then the PriorPeer of that assembly is updated with this assembly's sequence number and then this assembly's NextPeer gets updated with the sequence number from the assembly that was found.   -1 means that the assembly is the last assembly of its peers.  */  
   NextPeer:number,
      /**  Seq # of this assembly's very first subassembly. This is known as the Child assembly. Automatically maintained by the maintenance programs. The logic is to find the Parent assembly record and if its child is -1, update it with this assembly's seq #.  */  
   Child:number,
      /**  Optional field for Engineering Drawing Number. Defaulted from BomHead.DrawNum during methods pull functions.  */  
   DrawNum:string,
      /**  Editor widget for Job Assembly comments.  */  
   CommentText:string,
      /**  An internally system assigned integer which is used as part of an index to organize the QuoteAsm records into a Bill of Material fashion sequence.  */  
   BomSequence:number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the QuoteAsm in reference to the Bill of Material structure.  */  
   BomLevel:number,
      /**   A system maintained field. This is how many of the assemblies are required to produce ONE of the END ITEM.  This is a calculated field.  Calculated as the
 ( Parents RequiredQty  X QtyPer).
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer. The refresh may also occur if the structure of the assemblies is changed.  */  
   RequiredQty:number,
      /**  Indicates if this quote assembly is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   Template:boolean,
      /**   The operation number (Quote.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  */  
   FindNum:string,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIStartHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueHour:number,
      /**   An assembly record can be related to a specific operation.  This field contains the QuoteOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  */  
   RelatedOperation:number,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
   OrigMtlSeq:number,
   OrigRuleTag:string,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  The part number used to identify the configured part number initially entered on the assembly.  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part/revision number initially entered on the material.  */  
   BaseRevisionNum:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigStructTag:string,
      /**  LinkToContract  */  
   LinkToContract:boolean,
      /**  ContractID  */  
   ContractID:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  Clone of the Child field (.Net keyword issue)  */  
   ChildAssemblySeq:number,
      /**  External field to hold JCSyst.GetCostsFromTemplate value  */  
   GetCostsFromTemplate:boolean,
      /**  If this field is true, then the current value of ttQuoteAsm.AssemblySeq will be used when creating new QuoteAsm records. This allows processes, like PLM, to create new QuoteAsm records with a specific AssemblySeq.  */  
   OverrideNextAsmSeq:boolean,
      /**  Clone of the Parent field (.Net keyword issue)  */  
   ParentAssemblySeq:number,
      /**  QuoteAsm.Description of Parent assmebly  */  
   ParentDescription:string,
      /**  QutoeAsm.PartNum of the Parent Assembly  */  
   ParentPartNum:string,
      /**  QuoteAsm.RevisionNum of the Parent Assembly  */  
   ParentRevisionNum:string,
      /**  Internal flag to identify if current Part is an Inventory Part  */  
   PartExists:boolean,
      /**  Boolean to indicate GetDetails has started  */  
   ProcessingDetails:boolean,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   RDEndNum:number,
      /**  The prefix will be defaulted from the reference category defined for the assemblies. The value on this field will be used to create reference designators.  */  
   RDPrefix:string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   RDStartNum:number,
      /**  The suffix will be defaulted from the reference category defined for the assemblie. The value on this field will be used to create reference designators.  */  
   RDSuffix:string,
   RelatedOperationDescription:string,
      /**  Add assembly as "Sub"assembly or "Asm"bly  */  
   AddAsmAs:string,
      /**  External field for EQSyst GetCostsFromInventory  */  
   GetCostsFromInventory:boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   EnableInventoryAttributes:boolean,
   BitFlag:number,
   AnalysisCdDescription:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackInventoryByRevision:boolean,
   QuoteLineSmartString:string,
   QuoteLineGroupSeq:number,
   QuoteLineLineDesc:string,
   QuoteLineSysRowID:string,
   QuoteLineSmartStringProcessed:boolean,
   QuoteLineReadyToQuote:boolean,
   QuoteLineContractID:string,
   QuoteLineKitFlag:string,
   QuoteLineExternalMES:boolean,
   QuoteNumQuoted:boolean,
   QuoteNumQuoteClosed:boolean,
   QuoteNumCurrencyCode:string,
   QuoteNumCustNum:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteAsmTableset{
   QuoteAsm:Erp_Tablesets_QuoteAsmRow[],
   QuoteAsmAttch:Erp_Tablesets_QuoteAsmAttchRow[],
   QuoteAsmInsp:Erp_Tablesets_QuoteAsmInspRow[],
   QuoteMtl:Erp_Tablesets_QuoteMtlRow[],
   QuoteMtlAttch:Erp_Tablesets_QuoteMtlAttchRow[],
   QuoteMtlInsp:Erp_Tablesets_QuoteMtlInspRow[],
   QuoteMtlRefDes:Erp_Tablesets_QuoteMtlRefDesRow[],
   QuoteOpr:Erp_Tablesets_QuoteOprRow[],
   QuoteOprAttch:Erp_Tablesets_QuoteOprAttchRow[],
   QuoteOprAction:Erp_Tablesets_QuoteOprActionRow[],
   QuoteOprActionParam:Erp_Tablesets_QuoteOprActionParamRow[],
   QuoteOprInsp:Erp_Tablesets_QuoteOprInspRow[],
   QuoteOpDtl:Erp_Tablesets_QuoteOpDtlRow[],
   QuoteOprMachParam:Erp_Tablesets_QuoteOprMachParamRow[],
   QuoteAsmRefDes:Erp_Tablesets_QuoteAsmRefDesRow[],
   QuoteStage:Erp_Tablesets_QuoteStageRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_QuoteMtlAttchRow{
   Company:string,
   QuoteNum:number,
   QuoteLine:number,
   AssemblySeq:number,
   MtlSeq:number,
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

export interface Erp_Tablesets_QuoteMtlInspRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  */  
   MtlSeq:number,
      /**  A sequence number that uniquely identifies the QuoteMtlInsp record within the QuoteNum/QuoteLine/AssemblySeq/MtlSeq  */  
   PlanSeq:number,
      /**  The inspection plan part number (configurator part number).  */  
   InspPlanPartNum:string,
      /**  The inspection plan revision number (configurator revision number).  */  
   InspPlanRevNum:string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   SpecID:string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   SpecRevNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   SpecHedDescription:string,
   BitFlag:number,
   InspPlanDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteMtlRefDesRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  */  
   MtlSeq:number,
      /**  Identifier of Reference Designator  */  
   RefDes:string,
      /**  Unique identifies the reference designator with the material sequence.  */  
   RefDesSeq:number,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   MtlPartNum:string,
      /**  Free form side location. (Top, Bottom, Both, Level, etc)  */  
   Side:string,
      /**  X Coordinate of the reference designator  */  
   XLocation:number,
      /**  Y Coordinate of the reference designator  */  
   YLocation:number,
      /**  Z Coordinate of the reference designator  */  
   ZLocation:number,
      /**  Rotation of the reference designator. Max value = 360.000  */  
   Rotation:number,
      /**  Designator Description  */  
   Description:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteMtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  */  
   MtlSeq:number,
      /**  Part number of required material. Does not have to be valid in Part master file, but must not be blank.  */  
   PartNum:string,
      /**  Description of the material. Cannot be blank  */  
   Description:string,
      /**  Quantity required per one of the Parent item. This is a factor used in calculating the total material requirement.  */  
   QtyPer:number,
      /**  The issue/usage unit of measure for this material.  */  
   IUM:string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  */  
   Direct:boolean,
      /**  Expected Purchasing lead time (in days) for the material. This is passed along to the job if the item gets manufactured.  */  
   LeadTime:number,
      /**   A material record can be related to a specific operation. This field contains the QuoteOpr.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  */  
   RelatedOperation:number,
      /**  Part number for Salvaged scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  */  
   SalvagePartNum:string,
      /**  Description of Salvaged material. Use Part.Description for a default.  */  
   SalvageDescription:string,
      /**  A factor that multiplied by the RequiredQty for the material results in the expected total salvage quantity.  */  
   SalvageQtyPer:number,
      /**  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  */  
   SalvageUM:string,
      /**  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  */  
   SalvageUnitCredit:number,
      /**  The salvage material burden rate for this Quote Material.  */  
   SalvageMtlBurRate:number,
      /**  Estimated salvage Mtl Burden Unit Credit. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   SalvageEstMtlBurUnitCredit:number,
      /**   Comments for manufacturing about this material record. These comments are printed on manufacturing reports,  such as the router. For valid Parts use the Part.MfgComment as a default.
View as Editor widget.  */  
   MfgComment:string,
      /**  Used to identify a default vendor. Use the Part.VendorNum as a default. This will be used as a default for purchasing and miscellaneous receipts. This field is not directly maintainable; instead it's assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  An optional field, but if entered must be valid.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Indicates if this material is to be Purchased for the Job. If this is a non inventory part then this is "Yes" and can't be changed. If this is a valid Part then set it to "NO" but the user can override it.  */  
   BuyIt:boolean,
      /**   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.

View as Editor widget.  */  
   PurComment:string,
      /**  Minimum Cost that will be used for this material. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the material cost for the quote.  */  
   MinimumCost:number,
      /**  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   EstUnitCost:number,
      /**  The material burden rate for this Quote Material.  */  
   MtlBurRate:number,
      /**  Estimated Mtl Burden Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   EstMtlBurUnitCost:number,
      /**  Required Qty per ONE of the  END ITEM.  This is a system calculated field.  Calculated as (Parent Required Qty X QtyPer). The parent qty is one if assemblySeq zero else  (QuoteAsmbl.RequireQty) if AssemblySeq > 0.  */  
   RequiredQty:number,
      /**  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   FixedQty:boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   FindNum:string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
CLasses could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  */  
   Class:string,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   APSAddResType:string,
      /**  A flag to indicate that this quote material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this quote material.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost02:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost03:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost04:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost05:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost06:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost07:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost08:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost09:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost10:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty01:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty02:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty03:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty04:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty05:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty06:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty07:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty08:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty09:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty10:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost01:number,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  The part number used to identify the configured part number initially entered on the assembly.  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part/revision number initially entered on the material.  */  
   BaseRevisionNum:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigStructTag:string,
      /**  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigGroupSeq:number,
      /**  Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:  */  
   EstMtlUnitCost:number,
      /**  LinkToContract  */  
   LinkToContract:boolean,
      /**  ContractID  */  
   ContractID:string,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   MiscCode:string,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   MiscCharge:boolean,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  Unique identifier per Quote Line that allows PLM Integration to find QuoteMtl record.  */  
   PLMMtlSeq:number,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   LocationView:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvageAttributeSetID:number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   SalvagePlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvagePlanningAttributeSetID:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   SalvageRevisionNum:string,
      /**  Delimited list of Address fields in Company format  */  
   AddrList:string,
      /**  This field will tell if the Direct checkbox will be automatically set. If using a NonPartMaster then this field will be set to FALSE. Otherwise if QtyBearing is Yes then this field will be set to TRUE.  */  
   AutoSetChkDirect:boolean,
      /**  Base Unit of Measure  */  
   BaseUOM:string,
      /**  This field is used as and internal flag on BO to enable/disable FixedQty column on UI form.  */  
   EnableFixedQty:boolean,
   IsMtlConfigurationOn:boolean,
   IsMtlConfigureOn:boolean,
   IsMtlExtConfig:boolean,
      /**  IsMtlRevisionApproved  */  
   IsMtlRevisionApproved:boolean,
      /**  Internal flag to identify if the Part is an Inventory Part.  */  
   PartExists:boolean,
      /**  Indicates if theres a price break available and if its expired  */  
   PBImage:string,
   QtyBearing:boolean,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   RDEndNum:number,
      /**  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDPrefix:string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   RDStartNum:number,
      /**  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDSuffix:string,
      /**  Description from OpMaster of the QuoteOpr.OpCode  */  
   RelatedOperationDescription:string,
      /**  Salvage Part Base UOM  */  
   SalvageBaseUOM:string,
      /**  Salvage Part Track Dimension Setting  */  
   SalvagePartTrackMulti:boolean,
      /**  Scrap Unit of Measure  */  
   ScrapUOM:string,
      /**  Vendor address formatted  */  
   VendorAddress:string,
      /**  Planning number of pieces for this attribute set.  */  
   DispPlanningNumberOfPieces:number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   DispSalvagePlanningNumberOfPieces:number,
      /**  ID of related Attribute Class.  */  
   SalvageAttrClassID:string,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   SalvageTrackInventoryAttributes:boolean,
      /**  Indicates if inventory for this part is tracked by revision.  */  
   SalvageTrackInventoryByRevision:boolean,
   BitFlag:number,
   AnalysisCdDescription:string,
   AssemblySeqDescription:string,
   ClassDescription:string,
   ClassInactive:boolean,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumAttrClassID:string,
   PurMiscDescription:string,
   PurPointCountry:string,
   PurPointName:string,
   PurPointState:string,
   PurPointAddress2:string,
   PurPointZip:string,
   PurPointPrimPCon:number,
   PurPointAddress3:string,
   PurPointCity:string,
   PurPointAddress1:string,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
   RFQLineLineDesc:string,
   VendorNumAddress1:string,
   VendorNumZIP:string,
   VendorNumName:string,
   VendorNumTermsCode:string,
   VendorNumVendorID:string,
   VendorNumDefaultFOB:string,
   VendorNumCountry:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress2:string,
   VendorNumAddress3:string,
   VendorNumState:string,
   VendorNumCity:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteOpDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.   System assigned.  */  
   QuoteNum:number,
      /**  Used to link back to the QuoteLine.   System assigned.  */  
   QuoteLine:number,
      /**  Used to link back to the QuoteAsmbl record.  System assigned.  */  
   AssemblySeq:number,
      /**  Used to link back to the QuoteOpr record.  System assigned.  */  
   OprSeq:number,
      /**  Uniquely identifies the QuoteOpDtl.  System assigned.  */  
   OpDtlSeq:number,
      /**  The user can select the capability the operation is to perform.  The system will select the resource.  */  
   CapabilityID:string,
      /**  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  */  
   ResourceID:string,
      /**  The standard setup hours for the operation.   This is the setup time required for each machine.  */  
   SetupHours:number,
      /**  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  */  
   ProdHours:number,
      /**  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  */  
   NumResources:number,
      /**  The burden rate used for setup time.  Used as a default in Job and Quote entry.  */  
   SetupBurRate:number,
      /**  Burden rate used for production time on an operation. Job and Quoting use it as a default when entering operation details.  */  
   ProdBurRate:number,
      /**  The labor rate used for setup time.  Used as a default in Job and Quote entry.  */  
   SetupLabRate:number,
      /**  Labor rate used for production time on an operation. Job and Quoting use it as a default when entering operation details.  */  
   ProdLabRate:number,
      /**  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  */  
   SetupOrProd:string,
      /**  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   OpDtlDesc:string,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  If yes then the user has overridden the rates that were on the  record when it was inititally created.  The initial rates came from the master files.  */  
   OverrideRates:boolean,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   ConcurrentCapacity:number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   DailyProdRate:number,
      /**  Duplicated from QuoteOper.SetupCrewSize.   It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Duplicated from QuoteOper.ProdCrewSize.  The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  */  
   ProdCrewSize:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
   CapabilityDesc:string,
      /**  The Operation Standard ID stored in QuoteOpr.  */  
   OperOpStdID:string,
      /**  Indicates if primary production operation.  */  
   PrimaryProd:boolean,
      /**  Indicates if primary setup operation.  */  
   PrimarySetup:boolean,
   ResourceDesc:string,
   ResourceGrpDesc:string,
      /**  Flag for sub contract  */  
   SubContract:boolean,
   BitFlag:number,
   AssemblySeqDescription:string,
   CapabilityIDDescription:string,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteOprActionParamRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this record is associated with.  */  
   QuoteNum:number,
      /**  The Quote Line that record is related to.  */  
   QuoteLine:number,
      /**  A sequence number which uniquely identifies the assembly record within the method.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the method.  */  
   OprSeq:number,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   ActionSeq:number,
      /**  A sequence number which uniquely identifies parameter within the Operation/Action set.  */  
   ActionParamSeq:number,
      /**  Data type of Action Parameter.  */  
   ActionParamFieldDataType:string,
      /**  Value of Action Parameter.  */  
   ActionParamValueCharacter:string,
      /**  Value of Action Parameter.  */  
   ActionParamValueDate:string,
      /**  Value of Action Parameter.  */  
   ActionParamValueDecimal:number,
      /**  Value of Action Parameter.  */  
   ActionParamValueInteger:number,
      /**  Value of Action Parameter.  */  
   ActionParamValueLogical:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteOprActionRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this record is associated with.  */  
   QuoteNum:number,
      /**  The Quote Line that record is related to.  */  
   QuoteLine:number,
      /**  A sequence number which uniquely identifies the assembly record within the method.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the method.  */  
   OprSeq:number,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   ActionSeq:number,
      /**  Description of Action.  */  
   ActionDesc:string,
      /**  Indicated if this action must be completed before Operation can be completed.  */  
   Required:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteOprAttchRow{
   Company:string,
   QuoteNum:number,
   QuoteLine:number,
   AssemblySeq:number,
   OprSeq:number,
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

export interface Erp_Tablesets_QuoteOprInspRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Quote/Line/Assembly. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last QuoteOpr for the QuoteLine/Asm and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  A sequence number that uniquely identifies the QuoteOprInsp record within the QuoteNum/QuoteLine/AssemblySeq/OprSeq  */  
   PlanSeq:number,
      /**  The inspection plan part number (configurator part number).  */  
   InspPlanPartNum:string,
      /**  The inspection plan revision number (configurator revision number).  */  
   InspPlanRevNum:string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   SpecID:string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   SpecRevNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   SpecHedDescription:string,
   BitFlag:number,
   InspPlanDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteOprMachParamRow{
      /**  Company  */  
   Company:string,
      /**  QuoteNum  */  
   QuoteNum:number,
      /**  QuoteLine  */  
   QuoteLine:number,
      /**  AssemblySeq  */  
   AssemblySeq:number,
      /**  OprSeq  */  
   OprSeq:number,
      /**  MachParamSeq  */  
   MachParamSeq:number,
      /**  RequestCode  */  
   RequestCode:string,
      /**  MachineNum  */  
   MachineNum:string,
      /**  ToolNum  */  
   ToolNum:string,
      /**  PartNum  */  
   PartNum:string,
      /**  ParamNum  */  
   ParamNum:number,
      /**  ParamUpperLimit  */  
   ParamUpperLimit:number,
      /**  ParamNominalValue  */  
   ParamNominalValue:number,
      /**  ParamLowerLimit  */  
   ParamLowerLimit:number,
      /**  ParamDelayValue  */  
   ParamDelayValue:number,
      /**  SpecEnable  */  
   SpecEnable:boolean,
      /**  SpecControlAlarm  */  
   SpecControlAlarm:boolean,
      /**  SpecRunAlarm  */  
   SpecRunAlarm:boolean,
      /**  ProcSpecAlarm  */  
   ProcSpecAlarm:boolean,
      /**  ProcControlAlarm  */  
   ProcControlAlarm:boolean,
      /**  PartQualSpecEnable  */  
   PartQualSpecEnable:boolean,
      /**  PartQualControlEnable  */  
   PartQualControlEnable:boolean,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteOprRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Quote/Line/Assembly. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last QuoteOpr for the QuoteLine/Asm and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**   Operation Master Code - Links the QuoteOpr  record with a OpMaster record.  Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.

Valid for "inside operations" only.  */  
   OpStdID:string,
      /**  The TOTAL estimated set up hours FOR ALL MACHINES. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours * Machines.  */  
   EstSetHours:number,
      /**   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.

NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**   Qualifier for the Production Standard field.  The valid qualifiers are:

"HP" - Hours/Piece, "MP" - Minutes/Piece, "PH" - Pieces/Hour,

"PM" - Pieces/Minute, "OH" - Operations/Hour,

"OM"  - Operations/Minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor to the number of pieces. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.

This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  Production Quantity per one of the Parent Item.  */  
   QtyPer:number,
      /**  Labor rate used for estimated production labor costs. Default from the OpMaster.QProdLRate if not zero, else OpMaster.ProdLRate.  */  
   ProdLabRate:number,
      /**  Labor rate for estimated setup labor costs. Default from the OpMaster.QSetupLRate if not zero, else OpMaster.SetupLabRate.  */  
   SetupLabRate:number,
      /**  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.QProdBurRate if not zero, else WrkCenter.ProdBurRate.  */  
   ProdBurRate:number,
      /**  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.QSetUpBurRate if not zero, else WrkCenter.SetupBurRate.  */  
   SetupBurRate:number,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is, the more machines the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, NOT SETUP.  The stored setup hours is a total for all machines.  This stored number is divided by the number of machines when it is displayed on the screen during operation maintenance.  */  
   Machines:number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field.  It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  */  
   ProdCrewSize:number,
      /**  Estimated Scrap (fallout) that is expected to occur on this operation. The scrap increase the Run quantity. Example; need 1000 pieces scrap of 10 % will show a operation run quantity of 1100.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  Issue Unit of Measure. Applicable only when SubContract = Yes  */  
   IUM:string,
      /**  Hours required is calculated as days * 8. Only Applicable when SubContract = Yes.  */  
   DaysOut:number,
      /**  The PartNum to be shipped to the subcontract. Applicable only when SubContract = Yes.  Default the QuoteDtl.PartNum or QuoteAsm.PartNum depending on the QuoteOpr.AssemblySeq.  */  
   PartNum:string,
      /**  Description of item to be sent to subcontractor.  */  
   Description:string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Editor widget for quote operation comments.  */  
   CommentText:string,
      /**   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   SchedRelation:string,
      /**  Minimum Cost that will be used for subcontract costs. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the subcontract cost for the quote.  */  
   MinimumCost:number,
      /**  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   EstUnitCost:number,
      /**  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calcs are rounded up to the next whole number before multiplying by the AddlSetUpHours..  */  
   AddlSetupHours:number,
      /**  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  */  
   AddlSetUpQty:number,
      /**  Specifies the total production quantity for this operation. This is an application calculated field used for display purposes only. If no quantity is calculated, the default quantity displays the value of one. The value that displays in this field calculates as follows: Run Quantity = Scrap Quantity + Production Quantity. Note: The Run Qty value refreshes when maintenance is performed on the operation record or the assemblies production quantity is changed.  */  
   RunQty:number,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   MiscAmt:number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIQueStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIQueStartHour:number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIStartHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIMoveDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIMoveDueHour:number,
      /**  The Number of Hours per machine per day that this operations "actual" schedule is based on.  Used in logic of quote scheduling.  */  
   WIHoursPerMachine:number,
      /**  A flag to indicate that this quote operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   RFQNeeded:boolean,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  The number of vendor quotes that are required for this quote subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  The quantity requested for first article inspection.  */  
   FAQty:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**   Identifies the primary QuoteOpDtl to be used for setup.  The setup time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = S or B.  */  
   PrimarySetupOpDtl:number,
      /**   Identifies the primary QuoteOpDtl to be used for production.  The production run time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = P or B.  */  
   PrimaryProdOpDtl:number,
      /**  Operation Description.  */  
   OpDesc:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty07:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty08:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty09:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty10:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost01:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost02:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost03:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost04:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost05:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost06:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost07:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost08:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost09:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost10:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate01:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate02:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate03:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate04:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate05:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate06:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate07:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate08:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate09:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate10:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty01:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty02:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty03:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty04:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty05:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty06:number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   SNRequiredOpr:boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   SNRequiredSubConShip:boolean,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   SendAheadType:string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   SendAheadOffset:number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   PrjRoleList:string,
      /**  Allow use all Roles  */  
   UseAllRoles:boolean,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  PctReg  */  
   PctReg:number,
      /**  SetupMaterial  */  
   SetupMaterial:number,
      /**  MaterialColorRating  */  
   MaterialColorRating:number,
      /**  MiscInfo1  */  
   MiscInfo1:string,
      /**  MiscInfo2  */  
   MiscInfo2:string,
      /**  SetupURL  */  
   SetupURL:string,
      /**  ExpPctUp  */  
   ExpPctUp:number,
      /**  ExpCycTm  */  
   ExpCycTm:number,
      /**  ExpGood  */  
   ExpGood:number,
      /**  NonProdLimit  */  
   NonProdLimit:number,
      /**  AutoSpcEnable  */  
   AutoSpcEnable:boolean,
      /**  AutoSpcPeriod  */  
   AutoSpcPeriod:number,
      /**  PartQualEnable  */  
   PartQualEnable:boolean,
      /**  AutoSpcSubgroup  */  
   AutoSpcSubgroup:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  TemplateID  */  
   TemplateID:string,
      /**  StageNumber  */  
   StageNumber:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Indicates if the scheduling resources should be refreshed when the op code changes.  */  
   RefreshResources:boolean,
      /**  Vendor Address  */  
   AddrList:string,
   APSAltOpDesc:string,
   APSNextOpDesc:string,
   APSPrepOpDesc:string,
   AutoReceive:boolean,
      /**  Used to display selected UOM next to unit cost field  */  
   DspQtyIUM:string,
      /**  Indicates whether to enable the AutoReceive field  */  
   EnableAutoRec:boolean,
      /**  This field is used as a flag to enable/disable the controls binded to SNRequiredOpr column in UI forms.  */  
   EnableSNRequiredOpr:boolean,
      /**  This field is used as a flag for SNRequiredSubConShip column to determine when to enable/disable it on UI form.  */  
   EnableSNSubConShip:boolean,
   FinalOpr:boolean,
   HoursPerMachine:number,
   OpStdDescription:string,
   PBImage:string,
      /**  Primary Resource Group Description  */  
   PrimaryResourceGrpDesc:string,
      /**  The Resource Group ID of the primary production operation detail.  */  
   PrimaryResourceGrpID:string,
      /**  Vendor address formatted  */  
   VendorAddress:string,
      /**  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   PrimaryProdOpDtlDesc:string,
      /**  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   PrimarySetupOpDtlDesc:string,
   BitFlag:number,
   AnalysisCdDescription:string,
   AssemblySeqDescription:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   OpCodeOpDesc:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumIUM:string,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumAttrClassID:string,
   PartNumTrackInventoryByRevision:boolean,
   PurPointCity:string,
   PurPointState:string,
   PurPointZip:string,
   PurPointCountry:string,
   PurPointAddress1:string,
   PurPointName:string,
   PurPointAddress3:string,
   PurPointAddress2:string,
   PurPointPrimPCon:number,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
   RFQLineLineDesc:string,
   SetupGroupDescription:string,
   VendorNumAddress2:string,
   VendorNumAddress1:string,
   VendorNumCountry:string,
   VendorNumCity:string,
   VendorNumCurrencyCode:string,
   VendorNumVendorID:string,
   VendorNumName:string,
   VendorNumZIP:string,
   VendorNumState:string,
   VendorNumAddress3:string,
   VendorNumTermsCode:string,
   VendorNumDefaultFOB:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteStageRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this record is associated with.  */  
   QuoteNum:number,
      /**  The Quote Line that record is related to.  */  
   QuoteLine:number,
      /**  Assembly Sequence # that this Stage is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies stage record within the stage set.  */  
   StageSeq:number,
      /**  The identification of related StageNo.  */  
   StageNumber:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
   StageNumberDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtQuoteAsmTableset{
   QuoteAsm:Erp_Tablesets_QuoteAsmRow[],
   QuoteAsmAttch:Erp_Tablesets_QuoteAsmAttchRow[],
   QuoteAsmInsp:Erp_Tablesets_QuoteAsmInspRow[],
   QuoteMtl:Erp_Tablesets_QuoteMtlRow[],
   QuoteMtlAttch:Erp_Tablesets_QuoteMtlAttchRow[],
   QuoteMtlInsp:Erp_Tablesets_QuoteMtlInspRow[],
   QuoteMtlRefDes:Erp_Tablesets_QuoteMtlRefDesRow[],
   QuoteOpr:Erp_Tablesets_QuoteOprRow[],
   QuoteOprAttch:Erp_Tablesets_QuoteOprAttchRow[],
   QuoteOprAction:Erp_Tablesets_QuoteOprActionRow[],
   QuoteOprActionParam:Erp_Tablesets_QuoteOprActionParamRow[],
   QuoteOprInsp:Erp_Tablesets_QuoteOprInspRow[],
   QuoteOpDtl:Erp_Tablesets_QuoteOpDtlRow[],
   QuoteOprMachParam:Erp_Tablesets_QuoteOprMachParamRow[],
   QuoteAsmRefDes:Erp_Tablesets_QuoteAsmRefDesRow[],
   QuoteStage:Erp_Tablesets_QuoteStageRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipQuoteNum
      @param ipQuoteLine
      @param ipStartAssemblySeq
      @param ipPartNum
   */  
export interface FindAsm_input{
   ipQuoteNum:number,
   ipQuoteLine:number,
   ipStartAssemblySeq:number,
   ipPartNum:string,
}

export interface FindAsm_output{
parameters : {
      /**  output parameters  */  
   opAssemblySeq:number,
   opRowID:string,
}
}

   /** Required : 
      @param company
      @param quoteNum
      @param quoteLine
      @param PLMMtlSeq
   */  
export interface FindQuoteMtlByPLMMtlSeq_input{
   company:string,
   quoteNum:number,
   quoteLine:number,
   PLMMtlSeq:number,
}

export interface FindQuoteMtlByPLMMtlSeq_output{
parameters : {
      /**  output parameters  */  
   asmSeq:number,
   mtlSeq:number,
}
}

   /** Required : 
      @param ds
      @param relatedOperation
   */  
export interface GetAsmOprInfo_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  Value of the RelatedOperation that is being tested  */  
   relatedOperation:number,
}

export interface GetAsmOprInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param defaultRev
   */  
export interface GetAsmPartInfo_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  Indicates if the system should try and find the correct RevisionNum
            (yes) or use the value in the dataset (no)  */  
   defaultRev:boolean,
}

export interface GetAsmPartInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param sourceSysRowID
   */  
export interface GetBasePartAndConfigType_input{
      /**  QuoteDtl sysrowid  */  
   sourceSysRowID:string,
}

export interface GetBasePartAndConfigType_output{
parameters : {
      /**  output parameters  */  
   cfgPartNum:string,
   cfgRevisionNum:string,
   configType:string,
   configURL:string,
   configID:string,
}
}

   /** Required : 
      @param sourceSysRowID
   */  
export interface GetBasePartForConfig_input{
      /**  QuoteDtl SysRowID  */  
   sourceSysRowID:string,
}

export interface GetBasePartForConfig_output{
parameters : {
      /**  output parameters  */  
   cfgPartNum:string,
   cfgRevisionNum:string,
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param assemblySeq
   */  
export interface GetByID_input{
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
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
      @param ds
      @param ipQuoteNum
      @param ipQuoteLine
      @param ipStartAssemblySeq
      @param ipCurrentAssemblySeq
      @param ipCompleteTree
   */  
export interface GetDatasetForTreeByRef_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  The Quote Number to return data for.  */  
   ipQuoteNum:number,
      /**  The Quote Line Number to return data for.  */  
   ipQuoteLine:number,
      /**  The Assembly Sequence to return data for.  */  
   ipStartAssemblySeq:number,
      /**  The Assembly Sequence to return data for.  */  
   ipCurrentAssemblySeq:number,
      /**  Would you like to retun a complete dataset for this job number?  */  
   ipCompleteTree:boolean,
}

export interface GetDatasetForTreeByRef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ipQuoteNum
      @param ipQuoteLine
      @param assemblySeqList
   */  
export interface GetDatasetForTreeRefresh_input{
      /**  The Quote Number to return data for.  */  
   ipQuoteNum:number,
      /**  The Quote Line Number to return data for.  */  
   ipQuoteLine:number,
      /**  Tilde separated list of assembly sequences to refresh  */  
   assemblySeqList:string,
}

export interface GetDatasetForTreeRefresh_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param ipQuoteNum
      @param ipQuoteLine
      @param ipStartAssemblySeq
      @param ipCurrentAssemblySeq
      @param ipCompleteTree
   */  
export interface GetDatasetForTree_input{
      /**  The Quote Number to return data for.  */  
   ipQuoteNum:number,
      /**  The Quote Line Number to return data for.  */  
   ipQuoteLine:number,
      /**  The Assembly Sequence to return data for.  */  
   ipStartAssemblySeq:number,
      /**  The Assembly Sequence to return data for.  */  
   ipCurrentAssemblySeq:number,
      /**  Would you like to retun a complete dataset for this job number?  */  
   ipCompleteTree:boolean,
}

export interface GetDatasetForTree_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param targetAsm
      @param sourceFile
      @param sourceQuote
      @param sourceLine
      @param sourceJob
      @param sourceAsm
      @param sourcePart
      @param sourceRev
      @param sourceAltMethod
      @param useMethodForParts
      @param ipCompleteTree
      @param getCostsFromTemp
   */  
export interface GetDetails_input{
      /**  Quote Number of the target Assembly  */  
   quoteNum:number,
      /**  Quote Line of the target Assembly  */  
   quoteLine:number,
      /**  Sequence of the target Assembly  */  
   targetAsm:number,
      /**  Source (Quote, Job, or Method) of the details to copy  */  
   sourceFile:string,
      /**  Quote Number to get details from (populated when sourceFile = "Quote")  */  
   sourceQuote:number,
      /**  Quote Line to get details from (populated when sourceFile = "Quote")  */  
   sourceLine:number,
      /**  Job Number to get details from (populated when sourceFile = "Job")  */  
   sourceJob:string,
      /**  Quote Assembly to get details from (populated when sourceFile = "Quote" or "Job")  */  
   sourceAsm:number,
      /**  Part Num to get details from (populated when sourceFile = "Method")  */  
   sourcePart:string,
      /**  Revision number to get details from (populated when sourceFile = "Method")  */  
   sourceRev:string,
      /**  Alternate Method to get details from (populated when sourceFile = "Method")  */  
   sourceAltMethod:string,
      /**  If true use the method passed in for all parts in assemblies, if false
            use the assembly part's default method.  */  
   useMethodForParts:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
      /**  Would you like get an exact copy of materials costs?  */  
   getCostsFromTemp:boolean,
}

export interface GetDetails_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
parameters : {
      /**  output parameters  */  
   partErrors:string,
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
   returnObj:Erp_Tablesets_QuoteAsmListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetMtlBuyItInfo_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface GetMtlBuyItInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param sysRowID
      @param revisionNum
   */  
export interface GetMtlConfigPartRevAndConfigType_input{
   sysRowID:string,
   revisionNum:string,
}

export interface GetMtlConfigPartRevAndConfigType_output{
parameters : {
      /**  output parameters  */  
   cfgPartNum:string,
   cfgRevisionNum:string,
   configType:string,
   configURL:string,
   configID:string,
}
}

   /** Required : 
      @param sysRowID
      @param revisionNum
   */  
export interface GetMtlConfigPartRev_input{
   sysRowID:string,
   revisionNum:string,
}

export interface GetMtlConfigPartRev_output{
parameters : {
      /**  output parameters  */  
   cfgPartNum:string,
   cfgRevisionNum:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetMtlDirectInfo_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface GetMtlDirectInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param relatedOperation
      @param ds
   */  
export interface GetMtlOprInfo_input{
      /**  Value of the RelatedOperation that is being tested  */  
   relatedOperation:number,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface GetMtlOprInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param partName
   */  
export interface GetMtlPartInfo_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  Identifies the PartNum field to validate either PartNum or SalvagePartNum  */  
   partName:string,
}

export interface GetMtlPartInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param vendorID
   */  
export interface GetMtlVendorInfo_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  Proposed Vendor ID  */  
   vendorID:string,
}

export interface GetMtlVendorInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param bomLevel
      @param priorAssemblySeq
   */  
export interface GetNewAssembly_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  Assembly's parent Quote  */  
   quoteNum:number,
      /**  Assembly's parent Quote detail Line  */  
   quoteLine:number,
      /**  Assembly's parent assembly Seq  */  
   assemblySeq:number,
      /**  Assembly's parent BOMLevel  */  
   bomLevel:number,
      /**  If adding a sub-assembly record, this value is 0.  If
            inserting after a specific assembly then use that record's assembly seq (must be different
            from the parent assembly seq)  */  
   priorAssemblySeq:number,
}

export interface GetNewAssembly_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param subContract
   */  
export interface GetNewOperation_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  Operations's parent Quote  */  
   quoteNum:number,
      /**  Operations's parent Quote detail Line  */  
   quoteLine:number,
      /**  Operations's parent assembly Seq  */  
   assemblySeq:number,
      /**  Operations's sub contract type  */  
   subContract:boolean,
}

export interface GetNewOperation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
   */  
export interface GetNewQuoteAsmAttch_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
}

export interface GetNewQuoteAsmAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
   */  
export interface GetNewQuoteAsmInsp_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
}

export interface GetNewQuoteAsmInsp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param mtlSeq
   */  
export interface GetNewQuoteAsmRefDes_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
   mtlSeq:number,
}

export interface GetNewQuoteAsmRefDes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
   */  
export interface GetNewQuoteAsm_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
}

export interface GetNewQuoteAsm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param mtlSeq
   */  
export interface GetNewQuoteMtlAttch_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
   mtlSeq:number,
}

export interface GetNewQuoteMtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param mtlSeq
   */  
export interface GetNewQuoteMtlInsp_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
   mtlSeq:number,
}

export interface GetNewQuoteMtlInsp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param mtlSeq
   */  
export interface GetNewQuoteMtlRefDes_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
   mtlSeq:number,
}

export interface GetNewQuoteMtlRefDes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
   */  
export interface GetNewQuoteMtl_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
}

export interface GetNewQuoteMtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param oprSeq
   */  
export interface GetNewQuoteOpDtl_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
   oprSeq:number,
}

export interface GetNewQuoteOpDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param oprSeq
      @param actionSeq
   */  
export interface GetNewQuoteOprActionParam_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
   oprSeq:number,
   actionSeq:number,
}

export interface GetNewQuoteOprActionParam_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param oprSeq
   */  
export interface GetNewQuoteOprAction_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
   oprSeq:number,
}

export interface GetNewQuoteOprAction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param oprSeq
   */  
export interface GetNewQuoteOprAttch_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
   oprSeq:number,
}

export interface GetNewQuoteOprAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param oprSeq
   */  
export interface GetNewQuoteOprInsp_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
   oprSeq:number,
}

export interface GetNewQuoteOprInsp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param oprSeq
   */  
export interface GetNewQuoteOprMachParam_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
   oprSeq:number,
}

export interface GetNewQuoteOprMachParam_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
   */  
export interface GetNewQuoteOpr_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
}

export interface GetNewQuoteOpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
   */  
export interface GetNewQuoteStage_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
}

export interface GetNewQuoteStage_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ProposedOpCode
      @param ds
   */  
export interface GetOprOpCodeInfo_input{
      /**  The proposed Operation Code  */  
   ProposedOpCode:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface GetOprOpCodeInfo_output{
parameters : {
      /**  output parameters  */  
   RefreshMessage:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetOprOpStdInfo_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface GetOprOpStdInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param partName
   */  
export interface GetOprPartInfo_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  Identifies the PartNum field to validate either PartNum or SalvagePartNum  */  
   partName:string,
}

export interface GetOprPartInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetOprStdFormatInfo_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface GetOprStdFormatInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

export interface GetProjectRoles_output{
   returnObj:any,      //schema had no properties on an object.
}

export interface GetQuoteEngUIDefaults_output{
parameters : {
      /**  output parameters  */  
   defaultValues:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetQuoteMtlIsMtlConfigurationOn_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface GetQuoteMtlIsMtlConfigurationOn_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param whereClauseQuoteAsm
      @param whereClauseQuoteAsmAttch
      @param whereClauseQuoteAsmInsp
      @param whereClauseQuoteMtl
      @param whereClauseQuoteMtlAttch
      @param whereClauseQuoteMtlInsp
      @param whereClauseQuoteMtlRefDes
      @param whereClauseQuoteOpr
      @param whereClauseQuoteOprAttch
      @param whereClauseQuoteOprAction
      @param whereClauseQuoteOprActionParam
      @param whereClauseQuoteOprInsp
      @param whereClauseQuoteOpDtl
      @param whereClauseQuoteOprMachParam
      @param whereClauseQuoteAsmRefDes
      @param whereClauseQuoteStage
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseQuoteAsm:string,
   whereClauseQuoteAsmAttch:string,
   whereClauseQuoteAsmInsp:string,
   whereClauseQuoteMtl:string,
   whereClauseQuoteMtlAttch:string,
   whereClauseQuoteMtlInsp:string,
   whereClauseQuoteMtlRefDes:string,
   whereClauseQuoteOpr:string,
   whereClauseQuoteOprAttch:string,
   whereClauseQuoteOprAction:string,
   whereClauseQuoteOprActionParam:string,
   whereClauseQuoteOprInsp:string,
   whereClauseQuoteOpDtl:string,
   whereClauseQuoteOprMachParam:string,
   whereClauseQuoteAsmRefDes:string,
   whereClauseQuoteStage:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
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
      @param ipParentQuoteAsmRowid
      @param ipSourceRowid
      @param ipOperSeq
      @param ipDroppedAs
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertBOMAsm_input{
      /**  The rowid of the parent quoteasm to add to  */  
   ipParentQuoteAsmRowid:string,
      /**  The rowid of source record could be jobasmbl or quoteasm to be added to the parent quoteasm  */  
   ipSourceRowid:string,
      /**  The related operation seq (or 0 if unrelated)  */  
   ipOperSeq:number,
      /**  The character value to determine where to drop and to drop as what. valid values: JobAsmbl, JobAsmbl-AsMtl, QuoteAsm, QuoteAsm-AsMtl  */  
   ipDroppedAs:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertBOMAsm_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param ipParentQuoteAsmRowid
      @param ipSourceRowid
      @param ipOperSeq
      @param ipMtlSeq
      @param ipBeforeMtlRowid
      @param ipDroppedAs
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertBOMMtl_input{
      /**  The rowid of the quoteasm record to add the material to  */  
   ipParentQuoteAsmRowid:string,
      /**  The rowid of source record could be partmtl, jobmtl, or
            quotemtl to be added to the parent quoteasm  */  
   ipSourceRowid:string,
      /**  The related operation seq (or 0 if unrelated)  */  
   ipOperSeq:number,
      /**  The material seq to use  */  
   ipMtlSeq:number,
      /**  The material rowid to insert material before  */  
   ipBeforeMtlRowid:string,
      /**  The character value to determine where to drop and to drop as what.
            valid values: PartMtl, PartMtl-AsAsm, JobMtl-AsAsm, JobMtl, QuoteMtl-AsAsm, QuoteMtl  */  
   ipDroppedAs:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertBOMMtl_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param ipParentQuoteAsmRowid
      @param ipSourceRowid
      @param ipNewOperSeq
      @param ipBeforeOperRowid
      @param ipDroppedAs
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertBOMOper_input{
      /**  The rowid of the parent jobasmbl to add to  */  
   ipParentQuoteAsmRowid:string,
      /**  The rowid of source record could be joboper, partopr, or
            quoteopr to be added to the parent jobasmbl  */  
   ipSourceRowid:string,
      /**  The new operation seq  */  
   ipNewOperSeq:number,
      /**  The operation rowid to insert operation before  */  
   ipBeforeOperRowid:string,
      /**  The character value to determine where to drop and to drop as what.
            valid values: PartOpr, JobOper, QuoteOpr  */  
   ipDroppedAs:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertBOMOper_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param ipQuoteAsmRowID
      @param ipPartNum
      @param ipOperSeq
      @param ipMtlSeq
      @param ipBeforeMtlRowid
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertMaterial_input{
      /**  The rowid of the QuoteAsm record to add the material to  */  
   ipQuoteAsmRowID:string,
      /**  The part number being added  */  
   ipPartNum:string,
      /**  The related operation seq (or 0 if unrelated)  */  
   ipOperSeq:number,
      /**  The material seq to use  */  
   ipMtlSeq:number,
      /**  The material rowid to insert material before  */  
   ipBeforeMtlRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertMaterial_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param ipQuoteAsmRowID
      @param ipPartNum
      @param ipOperSeq
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertNewSubAssembly_input{
      /**  The rowid of the QuoteAsm record to add the material to  */  
   ipQuoteAsmRowID:string,
      /**  The part number being added  */  
   ipPartNum:string,
      /**  The related operation seq (or 0 if unrelated)  */  
   ipOperSeq:number,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertNewSubAssembly_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
parameters : {
      /**  output parameters  */  
   revisionNum:string,
   newQuoteAsmSeq:number,
   newQuoteAsmSysRowID:string,
}
}

   /** Required : 
      @param ipQuoteOprRowID
      @param ipCapabilityID
      @param ipNewOpDtlSeq
      @param ipBeforeOpDtlRowid
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertOpDtlCapability_input{
      /**  The rowid of the QuoteOpr record to add the operation detail to  */  
   ipQuoteOprRowID:string,
      /**  The Capability ID being added  */  
   ipCapabilityID:string,
      /**  The new operation detail seq  */  
   ipNewOpDtlSeq:number,
      /**  The operation detail rowid to insert operation detail before  */  
   ipBeforeOpDtlRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertOpDtlCapability_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param ipQuoteOprRowID
      @param ipResourceGrpID
      @param ipNewOpDtlSeq
      @param ipBeforeOpDtlRowid
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertOpDtlResourceGrp_input{
      /**  The rowid of the QuoteOpr record to add the operation detail to  */  
   ipQuoteOprRowID:string,
      /**  The Resource Group ID being added  */  
   ipResourceGrpID:string,
      /**  The new operation detail seq  */  
   ipNewOpDtlSeq:number,
      /**  The operation detail rowid to insert operation detail before  */  
   ipBeforeOpDtlRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertOpDtlResourceGrp_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param ipQuoteOprRowID
      @param ipResourceID
      @param ipNewOpDtlSeq
      @param ipBeforeOpDtlRowid
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertOpDtlResource_input{
      /**  The rowid of the QuoteOpr record to add the operation detail to  */  
   ipQuoteOprRowID:string,
      /**  The Resource ID being added  */  
   ipResourceID:string,
      /**  The new operation detail seq  */  
   ipNewOpDtlSeq:number,
      /**  The operation detail rowid to insert operation detail before  */  
   ipBeforeOpDtlRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertOpDtlResource_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param ipQuoteAsmRowID
      @param ipCapabilityID
      @param ipNewOprSeq
      @param ipBeforeOprRowid
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertOperCapability_input{
      /**  The rowid of the QuoteAsm record to add the operation detail to  */  
   ipQuoteAsmRowID:string,
      /**  The Capability ID being added  */  
   ipCapabilityID:string,
      /**  The new operation seq  */  
   ipNewOprSeq:number,
      /**  The operation rowid to insert operation before  */  
   ipBeforeOprRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertOperCapability_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipQuoteAsmRowID
      @param ipResourceGrpID
      @param ipNewOprSeq
      @param ipBeforeOprRowid
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertOperResGroup_input{
      /**  The rowid of the QuoteAsm record to add the operation detail to  */  
   ipQuoteAsmRowID:string,
      /**  The Resource Group ID being added  */  
   ipResourceGrpID:string,
      /**  The new operation seq  */  
   ipNewOprSeq:number,
      /**  The operation rowid to insert operation before  */  
   ipBeforeOprRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertOperResGroup_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipQuoteAsmRowID
      @param ipResourceID
      @param ipNewOprSeq
      @param ipBeforeOprRowid
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertOperResource_input{
      /**  The rowid of the QuoteAsm record to add the operation detail to  */  
   ipQuoteAsmRowID:string,
      /**  The Resource ID being added  */  
   ipResourceID:string,
      /**  The new operation seq  */  
   ipNewOprSeq:number,
      /**  The operation rowid to insert operation before  */  
   ipBeforeOprRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertOperResource_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipQuoteAsmRowID
      @param ipOpCode
      @param ipNewOprSeq
      @param ipBeforeOperRowid
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertOperationOP_input{
      /**  The rowid of the QuoteAsm record to add the operation to  */  
   ipQuoteAsmRowID:string,
      /**  The operation code being added  */  
   ipOpCode:string,
      /**  The new operation seq  */  
   ipNewOprSeq:number,
      /**  The operation rowid to insert operation before  */  
   ipBeforeOperRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertOperationOP_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipQuoteAsmRowID
      @param ipPartNum
      @param ipOperSeq
      @param ipReturn
      @param ipCompleteTree
   */  
export interface InsertSubAssembly_input{
      /**  The rowid of the QuoteAsm record to add the material to  */  
   ipQuoteAsmRowID:string,
      /**  The part number being added  */  
   ipPartNum:string,
      /**  The related operation seq (or 0 if unrelated)  */  
   ipOperSeq:number,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface InsertSubAssembly_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

export interface JobPartBeforeGetNew_output{
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSetQuoteAsm_input{
   attributeSetID:number,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface OnChangingAttributeSetQuoteAsm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSetQuoteMtl_input{
   attributeSetID:number,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface OnChangingAttributeSetQuoteMtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSetQuoteOpr_input{
   attributeSetID:number,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface OnChangingAttributeSetQuoteOpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingMtlRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface OnChangingMtlRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param relatedColumn
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPiecesQuoteMtl_input{
   relatedColumn:string,
   numberOfPieces:number,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface OnChangingNumberOfPiecesQuoteMtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param relatedColumn
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPiecesQuoteOpr_input{
   relatedColumn:string,
   numberOfPieces:number,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface OnChangingNumberOfPiecesQuoteOpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingQuoteOprRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface OnChangingQuoteOprRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingSalvageRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface OnChangingSalvageRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param sourcePartNum
      @param sourceRevisionNum
      @param sourceFile
      @param targetJobNum
      @param targetAsm
      @param sourceSysRowID
   */  
export interface PreGetDetails_input{
      /**  Indicates the source part number to get details from  */  
   sourcePartNum:string,
      /**  Indicates the source revision number to get details from  */  
   sourceRevisionNum:string,
      /**  Indicates where the details are being appended from.  Either Quote,
            Job or Method  */  
   sourceFile:string,
      /**  Target Job Number  */  
   targetJobNum:string,
      /**  Sequence of the target Assembly  */  
   targetAsm:number,
   sourceSysRowID:string,
}

export interface PreGetDetails_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
   BasePartNum:string,
   BaseRevisionNum:string,
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param assemblySeq
   */  
export interface QuoteAsmChildDelete_input{
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
}

export interface QuoteAsmChildDelete_output{
}

   /** Required : 
      @param ds
   */  
export interface QuoteOprInitSNReqSubCon_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface QuoteOprInitSNReqSubCon_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param mtlSeq
      @param vendorNum
      @param pum
      @param effectiveDate
   */  
export interface RefreshMtlPriceBreak_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  Material Quote  */  
   quoteNum:number,
      /**  Material Quote Line  */  
   quoteLine:number,
      /**  Material Assembly  */  
   assemblySeq:number,
      /**  Material Sequence  */  
   mtlSeq:number,
      /**  Vendor Number from vendor price break  */  
   vendorNum:number,
      /**  Purchasing Unit of measure for the Part  */  
   pum:string,
      /**  Effective date from vendor price break  */  
   effectiveDate:string,
}

export interface RefreshMtlPriceBreak_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param oprSeq
      @param vendorNum
      @param pum
      @param effectiveDate
   */  
export interface RefreshOprPriceBreak_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
      /**  Operation Quote  */  
   quoteNum:number,
      /**  Operation Quote Line  */  
   quoteLine:number,
      /**  Operation Assembly  */  
   assemblySeq:number,
      /**  Operation Sequence  */  
   oprSeq:number,
      /**  Vendor Number from vendor price break  */  
   vendorNum:number,
   pum:string,
      /**  Effective date from vendor price break  */  
   effectiveDate:string,
}

export interface RefreshOprPriceBreak_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param reseqOption
      @param ipCompleteTree
   */  
export interface ResequenceMaterial_input{
      /**  Quote Number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Assembly Sequences  */  
   assemblySeq:number,
      /**  "M" for Material, "P" for Part, or "B" for Bubble  */  
   reseqOption:string,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface ResequenceMaterial_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param ipCompleteTree
   */  
export interface ResequenceOperations_input{
      /**  Quote Number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Assembly Sequence  */  
   assemblySeq:number,
      /**  Would you like to return a complete dataset for this QuoteAsm?  */  
   ipCompleteTree:boolean,
}

export interface ResequenceOperations_output{
   returnObj:Erp_Tablesets_QuoteAsmTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtQuoteAsmTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtQuoteAsmTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param ipProposedInspPlan
      @param ipProposedSpecId
      @param iptable
      @param setRev
      @param ds
   */  
export interface ValidateInspection_input{
      /**  The new proposed InspPlanPartNum value  */  
   ipProposedInspPlan:string,
      /**  The new proposed SpecID value  */  
   ipProposedSpecId:string,
      /**  table name  */  
   iptable:string,
      /**  if set default revision  */  
   setRev:boolean,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ValidateInspection_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param bLinkToContract
      @param iQuoteNum
      @param iQuoteLine
      @param sPartNum
      @param sTablename
   */  
export interface ValidateLinkToContractData_input{
   bLinkToContract:boolean,
   iQuoteNum:number,
   iQuoteLine:number,
   sPartNum:string,
   sTablename:string,
}

export interface ValidateLinkToContractData_output{
}

   /** Required : 
      @param bLinkToContract
      @param iQuoteNum
      @param iQuoteLine
      @param partNum
      @param tableName
   */  
export interface ValidatePartToLinkToContract_input{
   bLinkToContract:boolean,
   iQuoteNum:number,
   iQuoteLine:number,
   partNum:string,
   tableName:string,
}

export interface ValidatePartToLinkToContract_output{
}

   /** Required : 
      @param ipQuoteNum
      @param ipQuoteLine
      @param ipQuoteAsmSeq
      @param ipPartNum
      @param ds
   */  
export interface ValidateSNReqValues_input{
      /**  Quote Number  */  
   ipQuoteNum:number,
      /**  Quote Line  */  
   ipQuoteLine:number,
      /**  Assembly Seq  */  
   ipQuoteAsmSeq:number,
      /**  Part Number  */  
   ipPartNum:string,
   ds:Erp_Tablesets_QuoteAsmTableset[],
}

export interface ValidateSNReqValues_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteAsmTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
   */  
export interface checkQuotePartConfiguration_input{
      /**  Quote number for which we are checking  */  
   quoteNum:number,
      /**  Quote number Line for which we are checking  */  
   quoteLine:number,
}

export interface checkQuotePartConfiguration_output{
parameters : {
      /**  output parameters  */  
   canGetDetails:boolean,
   needsConfiguration:boolean,
   isNIC:boolean,
   reasonMessage:string,
   configType:string,
   configURL:string,
   configID:string,
   targetSysRowID:string,
   partNum:string,
   revisionNum:string,
   kitFlag:string,
   kitsLoaded:boolean,
   smartStringProcessed:boolean,
   smartString:string,
}
}

