import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.RMAProcSvc
// Description: RMA Processing business object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/$metadata", {
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
   Description: Get RMAProcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMAProcs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMAHeadRow
   */  
export function get_RMAProcs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMAProcs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMAHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RMAHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RMAProcs(requestBody:Erp_Tablesets_RMAHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RMAProc item
   Description: Calls GetByID to retrieve the RMAProc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMAProc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RMAHeadRow
   */  
export function get_RMAProcs_Company_RMANum(Company:string, RMANum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RMAHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")", {
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
         resolve(data as Erp_Tablesets_RMAHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RMAProc for the service
   Description: Calls UpdateExt to update RMAProc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMAProc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMAHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RMAProcs_Company_RMANum(Company:string, RMANum:string, requestBody:Erp_Tablesets_RMAHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")", {
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
   Summary: Call UpdateExt to delete RMAProc item
   Description: Call UpdateExt to delete RMAProc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMAProc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RMAProcs_Company_RMANum(Company:string, RMANum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")", {
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
   Description: Get RMADtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RMADtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADtlRow
   */  
export function get_RMAProcs_Company_RMANum_RMADtls(Company:string, RMANum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")/RMADtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RMADtl item
   Description: Calls GetByID to retrieve the RMADtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMADtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RMADtlRow
   */  
export function get_RMAProcs_Company_RMANum_RMADtls_Company_RMANum_RMALine(Company:string, RMANum:string, RMALine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RMADtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")", {
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
         resolve(data as Erp_Tablesets_RMADtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RMAHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RMAHeadAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMAHeadAttchRow
   */  
export function get_RMAProcs_Company_RMANum_RMAHeadAttches(Company:string, RMANum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")/RMAHeadAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RMAHeadAttch item
   Description: Calls GetByID to retrieve the RMAHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMAHeadAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RMAHeadAttchRow
   */  
export function get_RMAProcs_Company_RMANum_RMAHeadAttches_Company_RMANum_DrawingSeq(Company:string, RMANum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RMAHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAProcs(" + Company + "," + RMANum + ")/RMAHeadAttches(" + Company + "," + RMANum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_RMAHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RMADtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMADtls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADtlRow
   */  
export function get_RMADtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMADtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMADtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RMADtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RMADtls(requestBody:Erp_Tablesets_RMADtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RMADtl item
   Description: Calls GetByID to retrieve the RMADtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMADtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RMADtlRow
   */  
export function get_RMADtls_Company_RMANum_RMALine(Company:string, RMANum:string, RMALine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RMADtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")", {
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
         resolve(data as Erp_Tablesets_RMADtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RMADtl for the service
   Description: Calls UpdateExt to update RMADtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMADtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMADtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RMADtls_Company_RMANum_RMALine(Company:string, RMANum:string, RMALine:string, requestBody:Erp_Tablesets_RMADtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")", {
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
   Summary: Call UpdateExt to delete RMADtl item
   Description: Call UpdateExt to delete RMADtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMADtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RMADtls_Company_RMANum_RMALine(Company:string, RMANum:string, RMALine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")", {
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
   Description: Get InvcDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InvcDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlRow
   */  
export function get_RMADtls_Company_RMANum_RMALine_InvcDtls(Company:string, RMANum:string, RMALine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")/InvcDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InvcDtl item
   Description: Calls GetByID to retrieve the InvcDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.InvcDtlRow
   */  
export function get_RMADtls_Company_RMANum_RMALine_InvcDtls_Company_InvoiceNum_InvoiceLine(Company:string, RMANum:string, RMALine:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InvcDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", {
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
         resolve(data as Erp_Tablesets_InvcDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RMARcpts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RMARcpts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMARcptRow
   */  
export function get_RMADtls_Company_RMANum_RMALine_RMARcpts(Company:string, RMANum:string, RMALine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMARcptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")/RMARcpts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMARcptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RMARcpt item
   Description: Calls GetByID to retrieve the RMARcpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMARcpt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param RMAReceipt Desc: RMAReceipt   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RMARcptRow
   */  
export function get_RMADtls_Company_RMANum_RMALine_RMARcpts_Company_RMANum_RMALine_RMAReceipt(Company:string, RMANum:string, RMALine:string, RMAReceipt:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RMARcptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")/RMARcpts(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")", {
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
         resolve(data as Erp_Tablesets_RMARcptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RMADtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RMADtlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADtlAttchRow
   */  
export function get_RMADtls_Company_RMANum_RMALine_RMADtlAttches(Company:string, RMANum:string, RMALine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")/RMADtlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RMADtlAttch item
   Description: Calls GetByID to retrieve the RMADtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMADtlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RMADtlAttchRow
   */  
export function get_RMADtls_Company_RMANum_RMALine_RMADtlAttches_Company_RMANum_RMALine_DrawingSeq(Company:string, RMANum:string, RMALine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RMADtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtls(" + Company + "," + RMANum + "," + RMALine + ")/RMADtlAttches(" + Company + "," + RMANum + "," + RMALine + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_RMADtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get InvcDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvcDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlRow
   */  
export function get_InvcDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/InvcDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InvcDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.InvcDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InvcDtls(requestBody:Erp_Tablesets_InvcDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/InvcDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the InvcDtl item
   Description: Calls GetByID to retrieve the InvcDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.InvcDtlRow
   */  
export function get_InvcDtls_Company_InvoiceNum_InvoiceLine(Company:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InvcDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", {
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
         resolve(data as Erp_Tablesets_InvcDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InvcDtl for the service
   Description: Calls UpdateExt to update InvcDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InvcDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InvcDtls_Company_InvoiceNum_InvoiceLine(Company:string, InvoiceNum:string, InvoiceLine:string, requestBody:Erp_Tablesets_InvcDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", {
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
   Summary: Call UpdateExt to delete InvcDtl item
   Description: Call UpdateExt to delete InvcDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InvcDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InvcDtls_Company_InvoiceNum_InvoiceLine(Company:string, InvoiceNum:string, InvoiceLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", {
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
   Description: Get RMARcpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMARcpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMARcptRow
   */  
export function get_RMARcpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMARcptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMARcpts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMARcptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMARcpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMARcptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RMARcptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RMARcpts(requestBody:Erp_Tablesets_RMARcptRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMARcpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RMARcpt item
   Description: Calls GetByID to retrieve the RMARcpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMARcpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param RMAReceipt Desc: RMAReceipt   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RMARcptRow
   */  
export function get_RMARcpts_Company_RMANum_RMALine_RMAReceipt(Company:string, RMANum:string, RMALine:string, RMAReceipt:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RMARcptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMARcpts(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")", {
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
         resolve(data as Erp_Tablesets_RMARcptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RMARcpt for the service
   Description: Calls UpdateExt to update RMARcpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMARcpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param RMAReceipt Desc: RMAReceipt   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMARcptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RMARcpts_Company_RMANum_RMALine_RMAReceipt(Company:string, RMANum:string, RMALine:string, RMAReceipt:string, requestBody:Erp_Tablesets_RMARcptRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMARcpts(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")", {
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
   Summary: Call UpdateExt to delete RMARcpt item
   Description: Call UpdateExt to delete RMARcpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMARcpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param RMAReceipt Desc: RMAReceipt   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RMARcpts_Company_RMANum_RMALine_RMAReceipt(Company:string, RMANum:string, RMALine:string, RMAReceipt:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMARcpts(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")", {
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
   Description: Get RMADtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMADtlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADtlAttchRow
   */  
export function get_RMADtlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMADtlAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMADtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RMADtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RMADtlAttches(requestBody:Erp_Tablesets_RMADtlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtlAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RMADtlAttch item
   Description: Calls GetByID to retrieve the RMADtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMADtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RMADtlAttchRow
   */  
export function get_RMADtlAttches_Company_RMANum_RMALine_DrawingSeq(Company:string, RMANum:string, RMALine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RMADtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtlAttches(" + Company + "," + RMANum + "," + RMALine + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_RMADtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RMADtlAttch for the service
   Description: Calls UpdateExt to update RMADtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMADtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMADtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RMADtlAttches_Company_RMANum_RMALine_DrawingSeq(Company:string, RMANum:string, RMALine:string, DrawingSeq:string, requestBody:Erp_Tablesets_RMADtlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtlAttches(" + Company + "," + RMANum + "," + RMALine + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete RMADtlAttch item
   Description: Call UpdateExt to delete RMADtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMADtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RMADtlAttches_Company_RMANum_RMALine_DrawingSeq(Company:string, RMANum:string, RMALine:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMADtlAttches(" + Company + "," + RMANum + "," + RMALine + "," + DrawingSeq + ")", {
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
   Description: Get RMAHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMAHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMAHeadAttchRow
   */  
export function get_RMAHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAHeadAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMAHeadAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMAHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RMAHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RMAHeadAttches(requestBody:Erp_Tablesets_RMAHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAHeadAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RMAHeadAttch item
   Description: Calls GetByID to retrieve the RMAHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMAHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RMAHeadAttchRow
   */  
export function get_RMAHeadAttches_Company_RMANum_DrawingSeq(Company:string, RMANum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RMAHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAHeadAttches(" + Company + "," + RMANum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_RMAHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RMAHeadAttch for the service
   Description: Calls UpdateExt to update RMAHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMAHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMAHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RMAHeadAttches_Company_RMANum_DrawingSeq(Company:string, RMANum:string, DrawingSeq:string, requestBody:Erp_Tablesets_RMAHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAHeadAttches(" + Company + "," + RMANum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete RMAHeadAttch item
   Description: Call UpdateExt to delete RMAHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMAHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RMAHeadAttches_Company_RMANum_DrawingSeq(Company:string, RMANum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMAHeadAttches(" + Company + "," + RMANum + "," + DrawingSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SelectedSerialNumbers", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectedSerialNumbers(requestBody:Erp_Tablesets_SelectedSerialNumbersRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SelectedSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
         resolve(data as Erp_Tablesets_SelectedSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, requestBody:Erp_Tablesets_SelectedSerialNumbersRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
   Description: Get SerialNumberSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SerialNumberSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNumberSearchRow
   */  
export function get_SerialNumberSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNumberSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SerialNumberSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNumberSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SerialNumberSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SerialNumberSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SerialNumberSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SerialNumberSearches(requestBody:Erp_Tablesets_SerialNumberSearchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SerialNumberSearches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the SerialNumberSearch item
   Description: Calls GetByID to retrieve the SerialNumberSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNumberSearch
      @param ProcessToken Desc: ProcessToken   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SerialNumberSearchRow
   */  
export function get_SerialNumberSearches_ProcessToken(ProcessToken:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SerialNumberSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SerialNumberSearches(" + ProcessToken + ")", {
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
         resolve(data as Erp_Tablesets_SerialNumberSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SerialNumberSearch for the service
   Description: Calls UpdateExt to update SerialNumberSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SerialNumberSearch
      @param ProcessToken Desc: ProcessToken   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SerialNumberSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SerialNumberSearches_ProcessToken(ProcessToken:string, requestBody:Erp_Tablesets_SerialNumberSearchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SerialNumberSearches(" + ProcessToken + ")", {
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
   Summary: Call UpdateExt to delete SerialNumberSearch item
   Description: Call UpdateExt to delete SerialNumberSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SerialNumberSearch
      @param ProcessToken Desc: ProcessToken   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SerialNumberSearches_ProcessToken(ProcessToken:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SerialNumberSearches(" + ProcessToken + ")", {
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
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SNFormats", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SNFormats(requestBody:Erp_Tablesets_SNFormatRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SNFormats", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
         resolve(data as Erp_Tablesets_SNFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, requestBody:Erp_Tablesets_SNFormatRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMAHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseRMAHead:string, whereClauseRMAHeadAttch:string, whereClauseRMADtl:string, whereClauseRMADtlAttch:string, whereClauseInvcDtl:string, whereClauseRMARcpt:string, whereClauseLegalNumGenOpts:string, whereClauseSelectedSerialNumbers:string, whereClauseSerialNumberSearch:string, whereClauseSNFormat:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRMAHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRMAHead=" + whereClauseRMAHead
   }
   if(typeof whereClauseRMAHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRMAHeadAttch=" + whereClauseRMAHeadAttch
   }
   if(typeof whereClauseRMADtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRMADtl=" + whereClauseRMADtl
   }
   if(typeof whereClauseRMADtlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRMADtlAttch=" + whereClauseRMADtlAttch
   }
   if(typeof whereClauseInvcDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInvcDtl=" + whereClauseInvcDtl
   }
   if(typeof whereClauseRMARcpt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRMARcpt=" + whereClauseRMARcpt
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
   if(typeof whereClauseSelectedSerialNumbers!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   }
   if(typeof whereClauseSerialNumberSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSerialNumberSearch=" + whereClauseSerialNumberSearch
   }
   if(typeof whereClauseSNFormat!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSNFormat=" + whereClauseSNFormat
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetRows" + params, {
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
export function get_GetByID(rmANum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rmANum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rmANum=" + rmANum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetList" + params, {
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
   Summary: Invoke method ChangeAttributeSetID
   Description: Call this method when the attribute set changes
   OperationID: ChangeAttributeSetID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAttributeSetID(requestBody:ChangeAttributeSetID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeAttributeSetID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeAttributeSetID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeAttributeSetID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeContact
   Description: Update RMA header contact information when the ConNum Contact is changed.
   OperationID: ChangeContact
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeContact(requestBody:ChangeContact_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeContact_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeContact", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeContact_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeContactRMADtl
   Description: Update RMA header contact information when the ConNum Contact is changed.
   OperationID: ChangeContactRMADtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeContactRMADtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeContactRMADtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeContactRMADtl(requestBody:ChangeContactRMADtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeContactRMADtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeContactRMADtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeContactRMADtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCustomer
   Description: This populates the customer information in the RMAHead datatable.
   OperationID: ChangeCustomer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustomer(requestBody:ChangeCustomer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCustomer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeCustomer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeCustomer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOrderLine
   Description: This method validates the order line and updates the RMADtl record with values
from the line.
   OperationID: ChangeOrderLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOrderLine(requestBody:ChangeOrderLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOrderLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeOrderLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeOrderLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOrderNumber
   Description: This method validates that the order number entered exists and the customer on
the order matches the customer on the RMAHead record.
   OperationID: ChangeOrderNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOrderNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOrderNumber(requestBody:ChangeOrderNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOrderNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeOrderNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeOrderNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOrderRelNum
   Description: This method validates the order release and updates the RMADtl record.
   OperationID: ChangeOrderRelNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOrderRelNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderRelNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOrderRelNum(requestBody:ChangeOrderRelNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOrderRelNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeOrderRelNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeOrderRelNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePartNum
   Description: This method validates the part number and updates the RMADtl record with values
from the part.
   OperationID: ChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePartNum(requestBody:ChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeReceivedQty
   Description: This method validates the ReceivedQty and ReceivedQtyUOM
and updates the RMARcpt record.
   OperationID: ChangeReceivedQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeReceivedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeReceivedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeReceivedQty(requestBody:ChangeReceivedQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeReceivedQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeReceivedQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeReceivedQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRevisionNum
   Description: Call this method when Revision changes to maintain inventory tracking
   OperationID: ChangeRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRevisionNum(requestBody:ChangeRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeRevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRMADtlInvoiceLine
   Description: Update RMA Header InvoiceLine it is changed.
   OperationID: ChangeRMADtlInvoiceLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRMADtlInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMADtlInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRMADtlInvoiceLine(requestBody:ChangeRMADtlInvoiceLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRMADtlInvoiceLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeRMADtlInvoiceLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRMADtlInvoiceLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRMADtlLegalNumber
   Description: Update RMA Header LegalNumber it is changed.
   OperationID: ChangeRMADtlLegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRMADtlLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMADtlLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRMADtlLegalNumber(requestBody:ChangeRMADtlLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRMADtlLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeRMADtlLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRMADtlLegalNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRMAHeadLegalNumber
   Description: Update RMA Header LegalNumber when it is changed.
   OperationID: ChangeRMAHeadLegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRMAHeadLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMAHeadLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRMAHeadLegalNumber(requestBody:ChangeRMAHeadLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRMAHeadLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeRMAHeadLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRMAHeadLegalNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipTo
   Description: This method validates the ShipToNum and updates the RMADtl record.
   OperationID: ChangeShipTo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipTo(requestBody:ChangeShipTo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeShipTo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeShipTo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeShipTo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipToCustID
   Description: This method validates the order release and updates the RMADtl record.
   OperationID: ChangeShipToCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipToCustID(requestBody:ChangeShipToCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeShipToCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeShipToCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeShipToCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeWarehouse
   Description: This method updates values in RMARcpt based on the new selling received quantity.
   OperationID: ChangeWarehouse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeWarehouse(requestBody:ChangeWarehouse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeWarehouse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ChangeWarehouse", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeWarehouse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCNCustomsDeclarationBillLine
   Description: Purpose:  Check Declaration Bill Line
Parameters:
<param name="bBeforeUpdate">if True - method is called before updating</param><param name="sMessage">Warning</param><param name="ds"></param>
   OperationID: CheckCNCustomsDeclarationBillLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCNCustomsDeclarationBillLine(requestBody:CheckCNCustomsDeclarationBillLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCNCustomsDeclarationBillLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/CheckCNCustomsDeclarationBillLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckCNCustomsDeclarationBillLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSerialNumbers
   Description: This method returns text of a message to be asked if the number of serial numbers
selected does not match the quantity entered for the RMARcpt or RMADtl record.
The user has the option of continuing with the mismatch quantities or canceling.
This method should be called before the update method and should be called only when
part is serial number tracked and the quantity is greater than zero.
If the user answers yes, the change can occur; otherwise the change shouldn't occur.
   OperationID: CheckSerialNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSerialNumbers(requestBody:CheckSerialNumbers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckSerialNumbers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/CheckSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckSerialNumbers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreditMemoExistsForRMA
   Description: Checks if Credit memo exists for specified RMA
   OperationID: CreditMemoExistsForRMA
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreditMemoExistsForRMA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreditMemoExistsForRMA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreditMemoExistsForRMA(requestBody:CreditMemoExistsForRMA_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreditMemoExistsForRMA_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/CreditMemoExistsForRMA", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreditMemoExistsForRMA_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDateUser
   Description: This method puts a date/time/user stamp in the Note box for the user
   OperationID: GetDateUser
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDateUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDateUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDateUser(requestBody:GetDateUser_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDateUser_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetDateUser", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDateUser_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method NoteUserAndDate
   Description: Add date/user stamp to note.
   OperationID: NoteUserAndDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/NoteUserAndDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NoteUserAndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NoteUserAndDate(requestBody:NoteUserAndDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<NoteUserAndDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/NoteUserAndDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as NoteUserAndDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRMAUseRefCosts
   Description: This method will return company parameter 'Use Referenced Invoice Costs'.
   OperationID: GetRMAUseRefCosts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRMAUseRefCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRMAUseRefCosts(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRMAUseRefCosts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetRMAUseRefCosts", {
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
         resolve(data as GetRMAUseRefCosts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSelectedSerialNumbers
   Description: This method will retrieve the serial numbers for an RMADtl or RMARcpt record and
update the SelectedSerialNumbers table with these records.
   OperationID: GetSelectedSerialNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectedSerialNumbers(requestBody:GetSelectedSerialNumbers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSelectedSerialNumbers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetSelectedSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetSelectedSerialNumbers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Get all the parameters needed for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectSerialNumbersParams(requestBody:GetSelectSerialNumbersParams_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSelectSerialNumbersParams_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetSelectSerialNumbersParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetSelectSerialNumbersParams_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/PreUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method RMACreditAdd
   Description: This method creates an RMA Credit record from the RMA Number and Line passed in.
The RMA Credit is stored in the InvcHead and InvcDtl tables.  Once the invoice is
created, the user has the option of updating the header and invoice line information.
It is expected that the A/R Invoice business object will be called to handle
the update of the header and/or line.
   OperationID: RMACreditAdd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RMACreditAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RMACreditAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RMACreditAdd(requestBody:RMACreditAdd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RMACreditAdd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/RMACreditAdd", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RMACreditAdd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckRMANum
   Description: Method to call when entering proposed RMA Number.  This method will return
two output variables.  One is a logical field to indicate if the RMA number
entered is existing or not.  The other variable is for the error message
in case the proposed RMA number is invalid.
   OperationID: CheckRMANum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckRMANum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRMANum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRMANum(requestBody:CheckRMANum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckRMANum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/CheckRMANum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckRMANum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSN(requestBody:ValidateSN_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSN_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/ValidateSN", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateSN_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailTranDocTypes
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetAvailTranDocTypes", {
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
   Summary: Invoke method BuildttSelectedSerialNumbersForHelpDeskRMA
   Description: Validates that a single serial number passed serial number is valid for an RMADtl line
   OperationID: BuildttSelectedSerialNumbersForHelpDeskRMA
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildttSelectedSerialNumbersForHelpDeskRMA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildttSelectedSerialNumbersForHelpDeskRMA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildttSelectedSerialNumbersForHelpDeskRMA(requestBody:BuildttSelectedSerialNumbersForHelpDeskRMA_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildttSelectedSerialNumbersForHelpDeskRMA_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/BuildttSelectedSerialNumbersForHelpDeskRMA", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildttSelectedSerialNumbersForHelpDeskRMA_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DisableIfPrinted
   Description: Logic if RMA is editable when RMA is printed
   OperationID: DisableIfPrinted
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DisableIfPrinted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisableIfPrinted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DisableIfPrinted(requestBody:DisableIfPrinted_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DisableIfPrinted_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/DisableIfPrinted", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DisableIfPrinted_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRMAHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMAHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRMAHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMAHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRMAHead(requestBody:GetNewRMAHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRMAHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetNewRMAHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRMAHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRMAHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMAHeadAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRMAHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMAHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRMAHeadAttch(requestBody:GetNewRMAHeadAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRMAHeadAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetNewRMAHeadAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRMAHeadAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRMADtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMADtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRMADtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMADtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRMADtl(requestBody:GetNewRMADtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRMADtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetNewRMADtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRMADtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRMADtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMADtlAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRMADtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMADtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRMADtlAttch(requestBody:GetNewRMADtlAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRMADtlAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetNewRMADtlAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRMADtlAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewInvcDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewInvcDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInvcDtl(requestBody:GetNewInvcDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewInvcDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetNewInvcDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewInvcDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRMARcpt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMARcpt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRMARcpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMARcpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRMARcpt(requestBody:GetNewRMARcpt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRMARcpt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetNewRMARcpt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRMARcpt_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMAProcSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RMADtlAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RMADtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RMAHeadAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RMAHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMAHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RMAHeadRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMARcptRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RMARcptRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNumberSearchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SerialNumberSearchRow,
}

export interface Erp_Tablesets_InvcDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Foreign key to the InvcHead.  */  
   "InvoiceNum":number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   "InvoiceLine":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  */  
   "LineType":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  */  
   "XRevisionNum":string,
      /**  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  */  
   "PartNum":string,
      /**  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  */  
   "LineDesc":string,
      /**  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  */  
   "IUM":string,
      /**  Our Current Revision Number for this Part.  */  
   "RevisionNum":string,
      /**  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  */  
   "POLine":string,
      /**  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  */  
   "TaxExempt":string,
      /**  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  */  
   "TaxCatID":string,
      /**   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  */  
   "Commissionable":boolean,
      /**   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  */  
   "DiscountPercent":number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "UnitPrice":number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "DocUnitPrice":number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  */  
   "OurOrderQty":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "ExtPrice":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "DocExtPrice":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "Discount":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "DocDiscount":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "TotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "DocTotalMiscChrg":number,
      /**  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  */  
   "ProdCode":string,
      /**  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  */  
   "OurShipQty":number,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  The packing slip line number that is being invoiced.  */  
   "PackLine":number,
      /**  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  */  
   "OrderNum":number,
      /**  The associated sales order line number.  */  
   "OrderLine":number,
      /**  Contains the release number of the order line item that is being invoiced.  */  
   "OrderRelNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  */  
   "ShipToNum":string,
      /**  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  */  
   "ShipDate":string,
      /**  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  */  
   "ShipViaCode":string,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   "AdvanceBillCredit":number,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   "DocAdvanceBillCredit":number,
      /**  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  */  
   "CustNum":number,
      /**  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  */  
   "InvoiceComment":string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  */  
   "ShpConNum":number,
      /**  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "MtlBurUnitCost":number,
      /**  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  */  
   "COSPostingReqd":boolean,
      /**   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   "COSPosted":boolean,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   "CallNum":number,
      /**  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  */  
   "CallCode":string,
      /**   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   "RMANum":number,
      /**   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  */  
   "RMALine":number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   "SalesCatID":string,
      /**   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  */  
   "JournalCode":string,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  */  
   "SellingOrderQty":number,
      /**  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  */  
   "SellingShipQty":number,
      /**  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Project Id that links the invoice detail  to the Project table.  */  
   "ProjectID":string,
      /**  Milestone id that links the invoice detail  to the ProjectMilestone.  */  
   "MilestoneID":string,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  */  
   "ListPrice":number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  */  
   "OrdBasedPrice":number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  */  
   "DocOrdBasedPrice":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "AdvGainLoss":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Sales representative commission rate.  */  
   "RepRate1":number,
      /**  Sales representative commission rate.  */  
   "RepRate2":number,
      /**  Sales representative commission rate.  */  
   "RepRate3":number,
      /**  Sales representative commission rate.  */  
   "RepRate4":number,
      /**  Sales representative commission rate.  */  
   "RepRate5":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit1":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit2":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit3":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit4":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit5":number,
      /**  Bill To Customer Number used for consolidated invoices  */  
   "BTCustNum":number,
      /**  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCMtlUnitCost":number,
      /**  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCLbrUnitCost":number,
      /**  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCBurUnitCost":number,
      /**  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCSubUnitCost":number,
      /**  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCMtlBurUnitCost":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  */  
   "RevChargeMethod":string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   "OverrideReverseCharge":boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   "RevChargeApplied":boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   "TaxConnectCalc":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AdvanceBillCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AdvanceBillCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AdvanceBillCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1OrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2OrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3OrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt1AdvGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt2AdvGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt3AdvGainLoss":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping adress country Number.  */  
   "OTSCountryNum":number,
      /**  Value is copied from PartTran for PE  */  
   "Plant":string,
      /**  value is copied from PartTran for PE  */  
   "WarehouseCode":string,
      /**  value is copied from PartTran for PE  */  
   "CallLine":number,
      /**  Drop Shipment Pack Line  */  
   "DropShipPackLine":number,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  FK to the Finance Charges table  */  
   "FinChargeCode":string,
      /**  Reference to the ABT, it is GUID, used in PostingEngine  */  
   "ABTUID":string,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "InUnitPrice":number,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "DocInUnitPrice":number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "InExtPrice":number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "DocInExtPrice":number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "InDiscount":number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "DocInDiscount":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   "InTotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   "DocInTotalMiscChrg":number,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  */  
   "InListPrice":number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  */  
   "DocInListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  */  
   "InOrdBasedPrice":number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  */  
   "DocInOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InUnitPrice":number,
      /**  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  */  
   "CorrectionDtl":boolean,
      /**  Asset number of the linked Asset Disposal transaction.  */  
   "AssetNum":string,
      /**  Unique number to identify the linked Asset Disposal transaction.  */  
   "DisposalNum":number,
      /**   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  */  
   "PBLineType":string,
      /**  Invoice line reference  */  
   "InvoiceLineRef":number,
      /**  Invoice Number Reference  */  
   "InvoiceRef":number,
      /**  Lot Number.  This field should be set according to the linked Shipment Line.  */  
   "LotNum":string,
      /**  Reference to the draft invoice line created in Invoice Preparation  */  
   "PBInvoiceLine":number,
      /**  Contains the value of the AC_RAHead.RAID client accommodation.  */  
   "RAID":number,
      /**  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  */  
   "RADtlID":number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   "DeferredRev":boolean,
      /**  Revenue Amortization Code.  */  
   "RACode":string,
      /**  Starting date the revenue is deferred.  */  
   "DefRevStart":string,
      /**  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  */  
   "ChargeDefRev":boolean,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  DefRevPosted  */  
   "DefRevPosted":boolean,
      /**  Unit price of Invoice linked to Bill of Exchange in original currency.  */  
   "LinkedInvcUnitPrice":number,
      /**  Withholding Tax Amount in reporting currency  */  
   "DspWithholdAmt":number,
      /**  Withholding Tax Amount in document currency  */  
   "DocDspWithholdAmt":number,
      /**  Withholding tax amount in reporting currency  */  
   "Rpt1DspWithholdAmt":number,
      /**  Withholding tax amount in reporting currency  */  
   "Rpt2DspWithholdAmt":number,
      /**  Withholding tax amount in reporting currency  */  
   "Rpt3DspWithholdAmt":number,
      /**  Currency code from linked Invoice Header  */  
   "LinkedCurrencyCode":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  PEBOEHeadNum  */  
   "PEBOEHeadNum":number,
      /**  MXSellingShipQty  */  
   "MXSellingShipQty":number,
      /**  MXUnitPrice  */  
   "MXUnitPrice":number,
      /**  DocMXUnitPrice  */  
   "DocMXUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1MXUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MXUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MXUnitPrice":number,
      /**  CustCostCenter  */  
   "CustCostCenter":string,
      /**  DEIsServices  */  
   "DEIsServices":boolean,
      /**  DEIsSecurityFinancialDerivative  */  
   "DEIsSecurityFinancialDerivative":boolean,
      /**  DEInternationalSecuritiesID  */  
   "DEInternationalSecuritiesID":string,
      /**  DEIsInvestment  */  
   "DEIsInvestment":boolean,
      /**  DEPayStatCode  */  
   "DEPayStatCode":string,
      /**  DefRevEndDate  */  
   "DefRevEndDate":string,
      /**  EntityUseCode  */  
   "EntityUseCode":string,
      /**  Indicates tha this invoice Line was reclassified.  */  
   "Reclassified":boolean,
      /**  Enables the user the ability to override the Percent or Amount of revenue to be deferred  */  
   "PartiallyDefer":boolean,
      /**  Percentage of revenue to be deferred for this line item  */  
   "DeferredPercent":number,
      /**  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  */  
   "Reclass":boolean,
      /**  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  */  
   "DeferredOnly":boolean,
      /**  Reclassification Code. This field will be required if Reclass is checked.  */  
   "ReclassCodeID":string,
      /**  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  */  
   "ReclassReasonCode":string,
      /**  Internal comments for reclassification entered by the user.  */  
   "ReclassComments":string,
      /**  Deferred Revenue Amount in base currency  */  
   "DeferredRevAmt":number,
      /**  Deferred Revenue Amount in document currency  */  
   "DocDeferredRevAmt":number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   "Rpt1DeferredRevAmt":number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   "Rpt2DeferredRevAmt":number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   "Rpt3DeferredRevAmt":number,
      /**  ChargeReclass  */  
   "ChargeReclass":boolean,
      /**  DEDenomination  */  
   "DEDenomination":string,
      /**  DropShipPONum  */  
   "DropShipPONum":number,
      /**  DocInAdvanceBillCredit  */  
   "DocInAdvanceBillCredit":number,
      /**  InAdvanceBillCredit  */  
   "InAdvanceBillCredit":number,
      /**  Rpt1InAdvanceBillCredit  */  
   "Rpt1InAdvanceBillCredit":number,
      /**  Rpt2InAdvanceBillCredit  */  
   "Rpt2InAdvanceBillCredit":number,
      /**  Rpt3InAdvanceBillCredit  */  
   "Rpt3InAdvanceBillCredit":number,
      /**  MYIndustryCode  */  
   "MYIndustryCode":string,
      /**  The dockingstation of the shipto address.  For future use.  */  
   "DockingStation":string,
      /**  ConsolidateLines  */  
   "ConsolidateLines":boolean,
      /**  MXCustomsDuty  */  
   "MXCustomsDuty":string,
      /**  CommodityCode  */  
   "CommodityCode":string,
      /**  MXProdServCode  */  
   "MXProdServCode":string,
      /**  Quote number to which this line item detail record is associated with.  */  
   "QuoteNum":number,
      /**  Quote Line number from which this invoice line was created from.  */  
   "QuoteLine":number,
      /**  True if transaction is related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  MXCustomsUMFrom  */  
   "MXCustomsUMFrom":string,
      /**  PE Detraction good or service code  */  
   "PEDetrGoodServiceCode":string,
      /**  PETaxExempt  */  
   "PETaxExempt":string,
      /**  Order number on the Invoicing Company.  */  
   "CColOrderNum":number,
      /**  Order number line the Invoicing Company.  */  
   "CColOrderLine":number,
      /**  Order number release the Invoicing Company.  */  
   "CColOrderRel":number,
      /**  Invoice Line reference on the Invoicing Company.  */  
   "CColInvoiceLineRef":number,
      /**  Packing slip number on the Invoicing Company.  */  
   "CColPackNum":number,
      /**  Packing slip line number on the Invoicing Company.  */  
   "CColPackLine":number,
      /**  Drop shipment packing slip number on the Invoicing Company.  */  
   "CColDropShipPackSlip":string,
      /**  Drop shipment packing slip line number on the Invoicing Company.  */  
   "CColDropShipPackSlipLine":number,
      /**  Ship To Customer ID from the Invoice Line in the subsidiary company.  */  
   "CColShipToCustID":string,
      /**  Ship To from the Invoice Line in the subsidiary company.  */  
   "CColShipToNum":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Exempt Reason Code  */  
   "ExemptReasonCode":string,
      /**  Associates the Call Line record back its linked jobnum  */  
   "JobNum":string,
      /**  Indicates where invoice detail was created from when created from a service call job. Not maintainable. “Summarized Labor”, “Summarized Material”, “Labor”, “Material”  */  
   "ServiceSource":string,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
      /**  AssemblySeq related to JobMtl or JobOper used to create invoice line from service call job  */  
   "AssemblySeq":number,
      /**  Job Mtl seq used to create invoice line from service call job  */  
   "MtlSeq":number,
      /**  Job subcontract oper seq used to create invoice line from service call job  */  
   "OprSeq":number,
      /**  Indicates the labor type of the LaborDtl used to create invoice from service call job.  */  
   "LaborType":string,
      /**  LaborDtl hours summed by labor rate. Used to create invoice line from labor related to service call job.  */  
   "BillableLaborHrs":number,
      /**  Billable rate used to create invoice line from labor related to service call job. In base currency.  */  
   "BillableLaborRate":number,
      /**  Indicates the type of service call transaction data used to create the invoice detail from a service call job. MT (material), LB (labor), SC (subcontract), MC (misc charge), SM (summarized material), SL (summarized labor), SS (summarized subcontract) No summarization for MC.  */  
   "ServiceSourceType":string,
      /**  TotalCovenantDiscount  */  
   "TotalCovenantDiscount":number,
      /**  DocCovenantDiscount  */  
   "DocCovenantDiscount":number,
      /**  Rpt1CovenantDiscount  */  
   "Rpt1CovenantDiscount":number,
      /**  Rpt2CovenantDiscount  */  
   "Rpt2CovenantDiscount":number,
      /**  Rpt3CovenantDiscount  */  
   "Rpt3CovenantDiscount":number,
      /**  TotalInCovenantDiscount  */  
   "TotalInCovenantDiscount":number,
      /**  DocInCovenantDiscount  */  
   "DocInCovenantDiscount":number,
      /**  Rpt1InCovenantDiscount  */  
   "Rpt1InCovenantDiscount":number,
      /**  Rpt2InCovenantDiscount  */  
   "Rpt2InCovenantDiscount":number,
      /**  Rpt3InCovenantDiscount  */  
   "Rpt3InCovenantDiscount":number,
      /**  Adv bill enabled flag  */  
   "AdvBillEnabled":boolean,
   "AllowTaxCodeUpd":boolean,
      /**  This flag not allow updating PartiallyDefer in 'Posted Invoice Update' if  AR Invoice Line was  marked as Partially Defer in AR Invoice Entry.  */  
   "AllowUpdPartDefer":boolean,
      /**  CustID associated with the InvcDtl.BTCustNum field.  */  
   "BillToCustID":string,
      /**  Customer Name associated with the InvcDtl.BTCustNum field.  */  
   "BTCustName":string,
      /**  The date and time that the record was last changed  */  
   "ChangeDateTime":string,
      /**  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  */  
   "CheckAmortAmounts":boolean,
   "CNGTIDescription1":string,
   "CNGTIDescription2":string,
   "CNGTIDescription3":string,
      /**  CSF China, discount tax amount  */  
   "CNGTIDiscountTaxAmount":number,
   "CNGTIIUM":string,
   "CNGTINetAmount":number,
   "CNGTIPartDescription":string,
   "CNGTISpecification":string,
   "CNGTITaxAmount":number,
   "CNGTITaxCode":string,
   "CNGTITaxPercent":number,
   "CNGTITotalAmount":number,
      /**  CSF China, Unit price = if InvcHead.InPrice then InvcDtl.InUnitPrice else InvcDtl.UnitPrice  */  
   "CNGTIUnitPrice":number,
   "ContractSuspended":boolean,
      /**  Currency code from InvcHead.  */  
   "CurrencyCode":string,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   "CurrencySwitch":boolean,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   "CustID":string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   "CustName":string,
      /**  Invoice Detail Customer Name  */  
   "CustomerName":string,
      /**  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  */  
   "DeleteRASchedule":boolean,
   "DispGLAcct":string,
      /**  Currency display symbol  */  
   "DisplaySymbol":string,
      /**  PO number for display.  */  
   "DispPONum":string,
      /**  Ship to display address  */  
   "DispShipToAddr":string,
      /**  Document display symbol.  */  
   "DocDisplaySymbol":string,
   "DocDspUnitPrice":number,
      /**  Document discount amount  */  
   "DocLessDiscount":number,
      /**  Doc line tax  */  
   "DocLineTax":number,
      /**  ExtPrice-disc+misc charges.  */  
   "DocLineTotal":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "DocPEDetAmt":number,
      /**  Drop Shipment  */  
   "DropShipment":boolean,
      /**  Display advance bill credit  */  
   "DspAdvanceBillCredit":number,
      /**  Display discount  */  
   "DspDiscount":number,
      /**  Display documents advance bill credit  */  
   "DspDocAdvanceBillCredit":number,
      /**  Display document discount  */  
   "DspDocDiscount":number,
      /**  Display document ext price  */  
   "DspDocExtPrice":number,
      /**  Display document less discount  */  
   "DspDocLessDiscount":number,
      /**  Display document line tax  */  
   "DspDocLineTax":number,
      /**  Display document line total  */  
   "DspDocLineTotal":number,
      /**  Display document total misc. charge  */  
   "DspDocTotalMiscChrg":number,
      /**  Display ext price  */  
   "DspExtPrice":number,
      /**  Display Invoice Reference  */  
   "DspInvoiceRef":number,
      /**  Display less discount  */  
   "DspLessDiscount":number,
      /**  Display line tax  */  
   "DspLineTax":number,
      /**  Display line total  */  
   "DspLineTotal":number,
      /**  Display our ship qty  */  
   "DspOurShipQty":number,
      /**  Display selling ship qty  */  
   "DspSellingShipQty":number,
   "DspTaxExempt":string,
      /**  Display total misc. charges  */  
   "DspTotalMiscChrg":number,
   "DspUnitPrice":number,
      /**  Invoice head due date.  */  
   "DueDate":string,
      /**  FSA Technician  */  
   "EmpID":string,
   "EnableDspWithholdAmt":boolean,
   "EnableRMADelete":boolean,
   "EnableRMAUpdate":boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   "FSAAction":string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "FSACallCode":string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "FSAContractCode":string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "FSAContractNum":number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   "FSAEmpID":string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   "FSAEquipmentInstallID":number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   "FSAEquipmentPartNum":string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   "FSAWarrantyCode":string,
      /**  GL Journal Source Transaction Amount  */  
   "GLTranAmt":number,
      /**  GL Journal Source Transaction Date  */  
   "GLTranDate":string,
      /**  Group associated to the invoice  */  
   "GroupID":string,
   "InPrice":boolean,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
      /**  Invoice Header Legal Number  */  
   "InvLegalNum":string,
      /**  Invoice Date from InvcHead.  */  
   "InvoiceDate":string,
      /**  Invoice header type  */  
   "InvoiceType":string,
      /**  Is commission button sensitive  */  
   "IsCommisBtnSensitive":boolean,
      /**  Set to true if intrastat is enabled.  */  
   "IsIntrastatSensitive":boolean,
      /**  Tax buton sensitive or not.  */  
   "IsTaxBtnSensitive":boolean,
      /**  display discount  */  
   "LessDiscount":number,
      /**  Line tax amount  */  
   "LineTax":number,
      /**  ExtPrice-disc+misc charges.  */  
   "LineTotal":number,
   "LinkedCurrencySymbol":string,
      /**  The flag based on the user responce to indicate if Ship To to be chnaged on Invoice detail record without tax information from Ship To because of the different tax pricing  */  
   "NoShipTaxRgnInfo":boolean,
      /**  Open invoice flag from InvcHead.  */  
   "OpenInvoice":boolean,
      /**  OrderUM display  */  
   "OrderUM":string,
      /**  original tax category  */  
   "OrigTaxCat":string,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "PEDetAmt":number,
      /**  PE Detraction good or service code description  */  
   "PEDetrGoodServiceCodeDesc":string,
   "PEDspCurrencySymbol":string,
      /**  PE VAT Exemption Reason  */  
   "PEVATExemptionReason":string,
      /**  Posted flag from the InvcHead.  */  
   "Posted":boolean,
   "RADesc":string,
      /**  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  */  
   "RASchedExists":boolean,
      /**  The internal flag to indicate if the logic is supposed to remove manual and/or manually added tax records per User request if the Line Tax Exempt field is populated  */  
   "RemoveManAdTax":boolean,
   "Rpt1DspAdvanceBillCredit":number,
   "Rpt1DspDiscount":number,
   "Rpt1DspExtPrice":number,
   "Rpt1DspLessDiscount":number,
   "Rpt1DspLineTax":number,
   "Rpt1DspLineTotal":number,
   "Rpt1DspTotalMiscChrg":number,
   "Rpt1DspUnitPrice":number,
   "Rpt1LineTax":number,
   "Rpt1LineTotal":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "Rpt1PEDetAmt":number,
   "Rpt2DspAdvanceBillCredit":number,
   "Rpt2DspDiscount":number,
   "Rpt2DspExtPrice":number,
   "Rpt2DspLessDiscount":number,
   "Rpt2DspLineTax":number,
   "Rpt2DspLineTotal":number,
   "Rpt2DspTotalMiscChrg":number,
   "Rpt2DspUnitPrice":number,
   "Rpt2LineTax":number,
   "Rpt2LineTotal":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "Rpt2PEDetAmt":number,
   "Rpt3DspAdvanceBillCredit":number,
   "Rpt3DspDiscount":number,
   "Rpt3DspExtPrice":number,
   "Rpt3DspLessDiscount":number,
   "Rpt3DspLineTax":number,
   "Rpt3DspLineTotal":number,
   "Rpt3DspTotalMiscChrg":number,
   "Rpt3DspUnitPrice":number,
   "Rpt3LineTax":number,
   "Rpt3LineTotal":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "Rpt3PEDetAmt":number,
      /**  1st sales rep of the invoice.  */  
   "SalesRepCode1":string,
      /**  2nd sales rep of the invoice header.  */  
   "SalesRepCode2":string,
      /**  3rd sales rep code of the invoice header.  */  
   "SalesRepCode3":string,
      /**  4th sales rep code of the invoice header.  */  
   "SalesRepCode4":string,
      /**  5th salesrep code of the invoice header.  */  
   "SalesRepCode5":string,
      /**  1st sales rep name  */  
   "SalesRepName1":string,
      /**  2nd sales rep name  */  
   "SalesRepName2":string,
      /**  3rd sales rep name  */  
   "SalesRepName3":string,
      /**  4th sales rep name  */  
   "SalesRepName4":string,
      /**  5th sales rep name  */  
   "SalesRepName5":string,
   "ShipToContactEMailAddress":string,
   "ShipToContactFaxNum":string,
   "ShipToContactName":string,
   "ShipToContactPhoneNum":string,
      /**  Ship Head Legal Number  */  
   "ShpLegalNum":string,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   "SoldToCustID":string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   "SoldToCustName":string,
      /**  Terms code from InvcHead.  */  
   "TermsCode":string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   "WarrantyCode":string,
      /**  This flag allow updating Reclassification data.  */  
   "AllowReclassify":boolean,
      /**  The flag to indicate if the amount  is re-calculated to doc/base/rpt currencies after entered and no need to re-calculate on save.  */  
   "LineAmtRecalcd":boolean,
      /**  Set to true if extra trade statistics is enabled.  */  
   "IsExtrastatSensitive":boolean,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   "TrackInventoryByRevision":boolean,
   "BitFlag":number,
   "CallCodeCallDescription":string,
   "CommodityCodeDescription":string,
   "ContractCodeContractDescription":string,
   "ContractNumSuspended":boolean,
   "CustCntName":string,
   "CustCntMiddleName":string,
   "CustCntFirstName":string,
   "CustCntFaxNum":string,
   "CustCntCorpName":string,
   "CustCntPhoneNum":string,
   "CustCntLastName":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumAllowShipTo3":boolean,
   "CustNumBTName":string,
   "InvoiceNumTermsCode":string,
   "InvoiceNumCardMemberName":string,
   "JournalCodeJrnlDescription":string,
   "MilestoneIDDescription":string,
   "MXProdServCodeDesc":string,
   "OrderLineLineDesc":string,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "OTSCntryEUMember":boolean,
   "OTSCntryISOCode":string,
   "OTSCntryDescription":string,
   "PackLineLineDesc":string,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "ProdCodeDescription":string,
   "ProjectIDDescription":string,
   "ReclassCodeDescription":string,
   "ReclassReasonDescription":string,
   "RMALineLineDesc":string,
   "SalesCatIDDescription":string,
   "ShipToCustCustID":string,
   "ShipToCustName":string,
   "ShipToCustBTName":string,
   "ShipToNumInactive":boolean,
   "ShipToNumName":string,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "TaxCatIDDescription":string,
   "TaxRegionDescription":string,
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

export interface Erp_Tablesets_RMADtlAttchRow{
   "Company":string,
   "RMANum":number,
   "RMALine":number,
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

export interface Erp_Tablesets_RMADtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Mirror image of RMAHead.OpenRMA.  */  
   "OpenRMA":boolean,
      /**  Indicates the Open/Closed status of the RMADtl.  This gets set to closed when there are no pending actions to be taken on related receipts.  */  
   "OpenDtl":boolean,
      /**  Return Authorization Number. Used to relate RMADtl to RMAHead.  */  
   "RMANum":number,
      /**  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  */  
   "RMALine":number,
      /**   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  */  
   "OrderNum":number,
      /**  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  */  
   "OrderLine":number,
      /**  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  */  
   "ReturnReasonCode":string,
      /**   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  */  
   "Note":string,
      /**  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  */  
   "PartNum":string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   "LineDesc":string,
      /**  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  */  
   "RevisionNum":string,
      /**  Quantity that is to be returned  */  
   "ReturnQty":number,
      /**  Unit Of Measure of the  ReturnQty.  */  
   "ReturnQtyUOM":string,
      /**  Reference Invoice number used for finding Tax Category  */  
   "RefInvoiceNum":number,
      /**  Reference invoice line - Used to obtain the correct tax category  */  
   "RefInvoiceLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  The Ship to number of the related header contact.  */  
   "ShipToNum":string,
      /**  The Contact Number of the related header contact  */  
   "ConNum":number,
      /**  Contains the system internal customer number used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  The order release number that the RMA line was created from.  */  
   "OrderRelNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Reference AR Invoice Number  */  
   "InvoiceNum":number,
      /**  Reference AR Invoice Line Number  */  
   "InvoiceLine":number,
      /**  Job Number.  */  
   "JobNum":string,
      /**  Assembly sequence number that this material is associated with.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   "MtlSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ECC RMA Comment  */  
   "ECCComment":string,
      /**  ECC RMA Num  */  
   "ECCRMANum":string,
      /**  ECC RMA Line  */  
   "ECCRMALine":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  CNDeclarationBillLine  */  
   "CNDeclarationBillLine":number,
      /**  Indicates that the line of the invoice has multiple packs consolidated. Details of the pack should be reviewied in InvcDtlPack table  */  
   "ConsolidateLines":boolean,
      /**  Indicates that the invoice line has consolidated shipment lines that are related to the same release of the sales order  */  
   "ConsolidateOneRelease":boolean,
   "CustomerContactEMailAddress":string,
      /**  The full customer's name.  */  
   "CustomerName":string,
      /**  The name for the ship to location.  */  
   "CustomerShipToName":string,
      /**  From RMAHead.DebitMemoRef, used by Customer Tracker  */  
   "DebitMemoRef":string,
      /**  If company parameter 'Allow Multiple Credit Invoices' is off and there is a least one credit memo then another credit memo adding is not allowed.  */  
   "EnableAddCreditMemo":boolean,
   "EnableDelete":boolean,
      /**  Flag to determine if Serial Numbers are required for this transaction.  */  
   "EnableSN":boolean,
   "EnableUpdate":boolean,
      /**  Determines if the RMA is synchronized with Epicor FSA application.  */  
   "EpicorFSA":boolean,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
      /**  Serivce Type  */  
   "FSAServiceType":string,
      /**  Technician  */  
   "FSATechnician":string,
      /**  From RMAHead.HDCaseNum, used by Customer Tracker  */  
   "HDCaseNum":number,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
   "LegalNumber":string,
   "LocalizationFlag":string,
      /**  Set from RMAHead.RMADate, used by Customer Tracker  */  
   "RMADate":string,
   "RMARcptExists":boolean,
      /**  Customer Id of the third-party Ship To  */  
   "ShipToCustID":string,
      /**  The name for the ship to location.  */  
   "ShipToName":string,
   "CustomerContactName":string,
      /**  The customer ID.  */  
   "CustomerCustID":string,
   "CNDeclarationBill":string,
   "BitFlag":number,
   "AttrValueSetDescription":string,
   "AttrValueSetShortDescription":string,
   "OrderNumCardMemberName":string,
   "OrderNumCurrencyCode":string,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumSellingFactor":number,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "ReasonDescription":string,
   "ReturnReasonCodeDescription":string,
   "ShipToNumInactive":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RMAHeadAttchRow{
   "Company":string,
   "RMANum":number,
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

export interface Erp_Tablesets_RMAHeadListRow{
      /**  Indicates if this RA is in an "open" status.  The user can toggle the setting of this field in header maintenance. It is also set automatically as the details are "Closed/Opened".  If there are no RMADtl records, then it is still considered as "open".  */  
   "OpenRMA":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  */  
   "RMANum":number,
      /**  Date of the Return Material Authorization.  Default as System date.  */  
   "RMADate":string,
      /**  Contains the system internal customer number used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  Reference to a customers accounts payable debit memo.  */  
   "DebitMemoRef":string,
      /**  The Clientele call number that is related to this RMA.  */  
   "CLCallNum":string,
      /**  The Legal Number of the record.  */  
   "LegalNumber":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Customer Name  */  
   "CustomerName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RMAHeadRow{
      /**  Indicates if this RA is in an "open" status.  The user can toggle the setting of this field in header maintenance. It is also set automatically as the details are "Closed/Opened".  If there are no RMADtl records, then it is still considered as "open".  */  
   "OpenRMA":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  */  
   "RMANum":number,
      /**  Date of the Return Material Authorization.  Default as System date.  */  
   "RMADate":string,
      /**  Contains the system internal customer number used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  Reference to a customers accounts payable debit memo.  */  
   "DebitMemoRef":string,
      /**  The Clientele call number that is related to this RMA.  */  
   "CLCallNum":string,
      /**  Cross reference RMA number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefRMANumber":string,
      /**  The help desk case that created this RMA.  */  
   "HDCaseNum":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  The Ship to number of the related header contact.  */  
   "ShipToNum":string,
      /**  The Contact Number of the related header contact  */  
   "ConNum":number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**   Indicates if the One Time Ship To info is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping Country Number  */  
   "OTSCountryNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Reference AR Invoice Number  */  
   "InvoiceNum":number,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Legal Number of the record.  */  
   "LegalNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The Return Invoice Number for the RMA (CSF - Turkey)  */  
   "RetInvoiceNum":string,
      /**  ECC RMA Number  */  
   "ECCRMANum":string,
      /**  Customer Web Reference to RMA.  */  
   "ECCCustRef":string,
      /**  DocumentPrinted  */  
   "DocumentPrinted":boolean,
      /**  Comments about the RMA overall  */  
   "RMAComment":string,
      /**  Web Comments about the RMA overall  */  
   "WebComment":string,
      /**  EpicorFSA  */  
   "EpicorFSA":boolean,
      /**  Declaration Bill  */  
   "CNDeclarationBill":string,
      /**  CNBonded  */  
   "CNBonded":boolean,
      /**  Bil to customer name  */  
   "BillToCustomerName":string,
      /**  Bill To Customer Name  */  
   "BTCustName":string,
   "CustomerContactEMailAddress":string,
   "CustomerContactName":string,
      /**  Column to indicate if the customer set for the RMA is sync'd to FSA.  */  
   "CustomerFSA":boolean,
   "EnableDelete":boolean,
   "EnableUpdate":boolean,
      /**  Column to indicate if the RMA was created on FSA.  */  
   "FromFSA":boolean,
      /**  Web address list for the contact who initiated the RMA.  */  
   "WebAddressList":string,
      /**  Delimited list of available bill to customers.  */  
   "AvailBTCustList":string,
   "BitFlag":number,
   "BTCustNumInactive":boolean,
   "CustomerName":string,
   "CustomerCustID":string,
   "CustomerBTName":string,
   "CustomerInactive":boolean,
   "HDCaseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RMARcptRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Return Authorization Number of related RMAHead.  */  
   "RMANum":number,
      /**  Line # of the related RMADtl record.  */  
   "RMALine":number,
      /**  RMA Receipt  */  
   "RMAReceipt":number,
      /**  Warehouse ID the item was received into.  Normally this would be a "Inspection" type of warehouse.  */  
   "WareHouseCode":string,
      /**  Warehouse Bin location in which the received item was placed.  */  
   "BinNum":string,
      /**  Receipt Date  */  
   "RcvDate":string,
      /**  Unique lot number for the part.  */  
   "LotNum":string,
      /**  This is set to NO when the entire quantity has been accounted for in RMADisp.  */  
   "OpenReceipt":boolean,
      /**  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost of Returned Item.  (See MtlUnitCost)  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost of Returned Item.  (See MtlUnitCost)  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost of Returned Item.  (See MtlUnitCost)  */  
   "SubUnitCost":number,
      /**  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  */  
   "MtlBurUnitCost":number,
      /**  The Site that this RMA receipt was received to.  This is set as from the "Current Site" at the time of receipt.  It will be used in the filtering of receipts in the Disposition process.  */  
   "Plant":string,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlMtlUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlLabUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlSubUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlBurdenUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlMtlBurUnitCost":number,
      /**  Quantity that has been received.  */  
   "ReceivedQty":number,
      /**  Quantity that has been dispositioned .  Cannot exceed ReceivedQty.  This is summation of the quantities from the supporting RMADisp records.  When DisposedQty = ReceivedQty the RMARcpt.OpenReceipt is set to NO.  */  
   "DisposedQty":number,
      /**  Unit of measure that qualifies the unit costs.  */  
   "CostUOM":string,
      /**  Received Quantity unit of measure.  */  
   "ReceivedQtyUOM":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Material Queue Records will only be updated if the "Request Move" box is checked  */  
   "RequestMove":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Part number of the RMA line  */  
   "PartNum":string,
   "EnableWarehouse":boolean,
   "EnableBin":boolean,
   "CustomerName":string,
   "PartRevisionNum":string,
   "EnableDelete":boolean,
   "EnableUpdate":boolean,
   "CustNum":number,
   "LegalNumberMessage":string,
      /**  PartPartDescription  */  
   "PartPartDescription":string,
      /**  PartTrackLots  */  
   "PartTrackLots":boolean,
      /**  PartTrackSerialNum  */  
   "PartTrackSerialNum":boolean,
      /**  The receipt quantity displayed in the RMADtl.ReturnQty.  */  
   "ThisRcptQty":number,
      /**  The UOM of the RMA Detail ( RMADtl.ReturnQtyUOM)  */  
   "ThisRcptQtyUOM":string,
      /**  Same value as ReceivedQtyUOM.  */  
   "DisposedQtyUOM":string,
      /**  Flag to determine if Serial Numbers are required for this transaction.  */  
   "EnableSN":boolean,
   "EnableInspection":boolean,
   "IsPartMaster":boolean,
      /**  Serial Number used only for FSA  */  
   "SerialNumber":string,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
   "PartTrackInventoryByRevision":boolean,
   "PartTrackInventoryAttributes":boolean,
   "BitFlag":number,
   "BinNumDescription":string,
   "WareHouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   "PartNum":string,
      /**  Number of digits in the serial number  */  
   "NumberOfDigits":number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   "SNMask":string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   "SNBaseDataType":string,
   "SNFormat1":string,
      /**  Whether or not to have leading zeroes  */  
   "LeadingZeroes":boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   "SNPrefix":string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   "SNLastUsedSeq":string,
   "HasSerialNumbers":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PartPricePerCode":string,
   "PartTrackLots":boolean,
   "PartTrackSerialNum":boolean,
   "PartTrackDimension":boolean,
   "PartSalesUM":string,
   "PartIUM":string,
   "PartSellingFactor":number,
   "PartPartDescription":string,
   "SerialMaskMaskType":number,
   "SerialMaskMask":string,
   "SerialMaskExample":string,
   "SerialMaskDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   "Company":string,
      /**  SerialNumber  */  
   "SerialNumber":string,
      /**  Scrapped flag  */  
   "Scrapped":boolean,
      /**  Scrapped reason code  */  
   "ScrappedReasonCode":string,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  Reference field  */  
   "Reference":string,
      /**  Reason code type = s  */  
   "ReasonCodeType":string,
      /**  Reason code description  */  
   "ReasonCodeDesc":string,
      /**  PartNumber  */  
   "PartNum":string,
      /**  Serial number prefix  */  
   "SNPrefix":string,
      /**  Base number used to create the serial number  */  
   "SNBaseNumber":string,
      /**  RowID of the source record for this serial number  */  
   "SourceRowID":string,
      /**  TransType of the record that created this serial number  */  
   "TransType":string,
      /**  True if this serial numbered part passed inspection  */  
   "PassedInspection":boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   "Deselected":boolean,
   "KitWhseList":string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   "RawSerialNum":string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   "KBLbrAction":number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   "KBLbrActionDesc":string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   "PreventDeselect":boolean,
      /**  Used only by SN Assignment  */  
   "XRefPartNum":string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   "XRefPartType":string,
   "PreDeselected":boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   "poLinkValues":string,
      /**  The mask the was used to generate the serial number  */  
   "SNMask":string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   "NotSavedToDB":boolean,
   "RowSelected":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SerialNumberSearchRow{
      /**  Token reserved for the process ID  */  
   "ProcessToken":string,
      /**  1st generic token.  */  
   "GenericToken1":string,
      /**  2nd generic token  */  
   "GenericToken2":string,
      /**  Returns where clause based on input tokens.  */  
   "WhereClause":string,
   "SysRowID":string,
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
      @param ds
      @param serialNumber
   */  
export interface BuildttSelectedSerialNumbersForHelpDeskRMA_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
}

export interface BuildttSelectedSerialNumbersForHelpDeskRMA_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
   snErrorMsg:string,
}
}

   /** Required : 
      @param ds
      @param attributeSetID
   */  
export interface ChangeAttributeSetID_input{
   ds:Erp_Tablesets_RMAProcTableset[],
   attributeSetID:number,
}

export interface ChangeAttributeSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param iConNum
   */  
export interface ChangeContactRMADtl_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed contact number  */  
   iConNum:number,
}

export interface ChangeContactRMADtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param iConNum
   */  
export interface ChangeContact_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed contact number  */  
   iConNum:number,
}

export interface ChangeContact_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param cCustID
   */  
export interface ChangeCustomer_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed customer id  */  
   cCustID:string,
}

export interface ChangeCustomer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param iOrderLine
   */  
export interface ChangeOrderLine_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed order line  */  
   iOrderLine:number,
}

export interface ChangeOrderLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param iOrderNum
   */  
export interface ChangeOrderNumber_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed order number  */  
   iOrderNum:number,
}

export interface ChangeOrderNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param iOrderRelNum
   */  
export interface ChangeOrderRelNum_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed order release number  */  
   iOrderRelNum:number,
}

export interface ChangeOrderRelNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param cPartNum
      @param SysRowID
      @param rowType
   */  
export interface ChangePartNum_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed part number  */  
   cPartNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface ChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
   cPartNum:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param ds
      @param ipInvoiceLine
   */  
export interface ChangeRMADtlInvoiceLine_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed InvoiceNum  */  
   ipInvoiceLine:number,
}

export interface ChangeRMADtlInvoiceLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param ipLegalNumber
   */  
export interface ChangeRMADtlLegalNumber_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed LegalNumber  */  
   ipLegalNumber:string,
}

export interface ChangeRMADtlLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param ipLegalNumber
   */  
export interface ChangeRMAHeadLegalNumber_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed LegalNumber  */  
   ipLegalNumber:string,
}

export interface ChangeRMAHeadLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param iReceivedQty
      @param iReceivedQtyUOM
   */  
export interface ChangeReceivedQty_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed received quantity  */  
   iReceivedQty:number,
      /**  The proposed received quantity UOM  */  
   iReceivedQtyUOM:string,
}

export interface ChangeReceivedQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param revisionNum
   */  
export interface ChangeRevisionNum_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The new Revision number  */  
   revisionNum:string,
}

export interface ChangeRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param ipShipToCustID
   */  
export interface ChangeShipToCustID_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed ShipToCustID.  */  
   ipShipToCustID:string,
}

export interface ChangeShipToCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param iShipTo
   */  
export interface ChangeShipTo_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The proposed ship to number  */  
   iShipTo:string,
}

export interface ChangeShipTo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeWarehouse_input{
   ds:Erp_Tablesets_RMAProcTableset[],
}

export interface ChangeWarehouse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
   cMessageText:string,
}
}

   /** Required : 
      @param bBeforeUpdate
      @param ds
   */  
export interface CheckCNCustomsDeclarationBillLine_input{
   bBeforeUpdate:boolean,
   ds:Erp_Tablesets_RMAProcTableset[],
}

export interface CheckCNCustomsDeclarationBillLine_output{
parameters : {
      /**  output parameters  */  
   sMessage:string,
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param proposedRMANum
   */  
export interface CheckRMANum_input{
      /**  The proposed RMA Number  */  
   proposedRMANum:number,
}

export interface CheckRMANum_output{
parameters : {
      /**  output parameters  */  
   opFoundRMA:boolean,
   opMessage:string,
}
}

   /** Required : 
      @param ds
      @param cTableName
   */  
export interface CheckSerialNumbers_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  The table name to check against; values are 'RMADtl' or 'RMARcpt'  */  
   cTableName:string,
}

export interface CheckSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
   cMessageText:string,
}
}

   /** Required : 
      @param rmaNum
   */  
export interface CreditMemoExistsForRMA_input{
      /**  Number of RMA to check.  */  
   rmaNum:number,
}

export interface CreditMemoExistsForRMA_output{
parameters : {
      /**  output parameters  */  
   rmaExists:boolean,
}
}

   /** Required : 
      @param rmANum
   */  
export interface DeleteByID_input{
   rmANum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param tranDocTypeID
      @param ramPrinted
   */  
export interface DisableIfPrinted_input{
   tranDocTypeID:string,
   ramPrinted:boolean,
}

export interface DisableIfPrinted_output{
   returnObj:boolean,
}

export interface Erp_Tablesets_InvcDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  */  
   LineType:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  */  
   XRevisionNum:string,
      /**  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  */  
   PartNum:string,
      /**  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  */  
   LineDesc:string,
      /**  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  */  
   IUM:string,
      /**  Our Current Revision Number for this Part.  */  
   RevisionNum:string,
      /**  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  */  
   POLine:string,
      /**  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  */  
   TaxExempt:string,
      /**  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  */  
   TaxCatID:string,
      /**   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  */  
   Commissionable:boolean,
      /**   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  */  
   DiscountPercent:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   UnitPrice:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocUnitPrice:number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  */  
   OurOrderQty:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   ExtPrice:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocExtPrice:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   Discount:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   TotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   DocTotalMiscChrg:number,
      /**  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  */  
   ProdCode:string,
      /**  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  */  
   OurShipQty:number,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  The packing slip line number that is being invoiced.  */  
   PackLine:number,
      /**  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  */  
   OrderNum:number,
      /**  The associated sales order line number.  */  
   OrderLine:number,
      /**  Contains the release number of the order line item that is being invoiced.  */  
   OrderRelNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  */  
   ShipToNum:string,
      /**  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  */  
   ShipDate:string,
      /**  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  */  
   ShipViaCode:string,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   AdvanceBillCredit:number,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   DocAdvanceBillCredit:number,
      /**  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  */  
   CustNum:number,
      /**  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  */  
   InvoiceComment:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  */  
   ShpConNum:number,
      /**  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   MtlBurUnitCost:number,
      /**  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  */  
   COSPostingReqd:boolean,
      /**   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   COSPosted:boolean,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   CallNum:number,
      /**  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  */  
   CallCode:string,
      /**   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  */  
   RMALine:number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   SalesCatID:string,
      /**   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  */  
   JournalCode:string,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  */  
   SellingOrderQty:number,
      /**  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  */  
   SellingShipQty:number,
      /**  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Project Id that links the invoice detail  to the Project table.  */  
   ProjectID:string,
      /**  Milestone id that links the invoice detail  to the ProjectMilestone.  */  
   MilestoneID:string,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  */  
   ListPrice:number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  */  
   OrdBasedPrice:number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  */  
   DocOrdBasedPrice:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   AdvGainLoss:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Sales representative commission rate.  */  
   RepRate1:number,
      /**  Sales representative commission rate.  */  
   RepRate2:number,
      /**  Sales representative commission rate.  */  
   RepRate3:number,
      /**  Sales representative commission rate.  */  
   RepRate4:number,
      /**  Sales representative commission rate.  */  
   RepRate5:number,
      /**  Sales representative commission percentage.  */  
   RepSplit1:number,
      /**  Sales representative commission percentage.  */  
   RepSplit2:number,
      /**  Sales representative commission percentage.  */  
   RepSplit3:number,
      /**  Sales representative commission percentage.  */  
   RepSplit4:number,
      /**  Sales representative commission percentage.  */  
   RepSplit5:number,
      /**  Bill To Customer Number used for consolidated invoices  */  
   BTCustNum:number,
      /**  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCMtlUnitCost:number,
      /**  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCLbrUnitCost:number,
      /**  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCBurUnitCost:number,
      /**  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCSubUnitCost:number,
      /**  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCMtlBurUnitCost:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  */  
   RevChargeMethod:string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   OverrideReverseCharge:boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   RevChargeApplied:boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3AdvGainLoss:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping adress country Number.  */  
   OTSCountryNum:number,
      /**  Value is copied from PartTran for PE  */  
   Plant:string,
      /**  value is copied from PartTran for PE  */  
   WarehouseCode:string,
      /**  value is copied from PartTran for PE  */  
   CallLine:number,
      /**  Drop Shipment Pack Line  */  
   DropShipPackLine:number,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  FK to the Finance Charges table  */  
   FinChargeCode:string,
      /**  Reference to the ABT, it is GUID, used in PostingEngine  */  
   ABTUID:string,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   InUnitPrice:number,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocInUnitPrice:number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   InExtPrice:number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocInExtPrice:number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   InDiscount:number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocInDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   InTotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   DocInTotalMiscChrg:number,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  */  
   InListPrice:number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  */  
   DocInListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  */  
   InOrdBasedPrice:number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  */  
   DocInOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt2InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt3InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InUnitPrice:number,
      /**  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  */  
   CorrectionDtl:boolean,
      /**  Asset number of the linked Asset Disposal transaction.  */  
   AssetNum:string,
      /**  Unique number to identify the linked Asset Disposal transaction.  */  
   DisposalNum:number,
      /**   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  */  
   PBLineType:string,
      /**  Invoice line reference  */  
   InvoiceLineRef:number,
      /**  Invoice Number Reference  */  
   InvoiceRef:number,
      /**  Lot Number.  This field should be set according to the linked Shipment Line.  */  
   LotNum:string,
      /**  Reference to the draft invoice line created in Invoice Preparation  */  
   PBInvoiceLine:number,
      /**  Contains the value of the AC_RAHead.RAID client accommodation.  */  
   RAID:number,
      /**  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  */  
   RADtlID:number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  */  
   ChargeDefRev:boolean,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  DefRevPosted  */  
   DefRevPosted:boolean,
      /**  Unit price of Invoice linked to Bill of Exchange in original currency.  */  
   LinkedInvcUnitPrice:number,
      /**  Withholding Tax Amount in reporting currency  */  
   DspWithholdAmt:number,
      /**  Withholding Tax Amount in document currency  */  
   DocDspWithholdAmt:number,
      /**  Withholding tax amount in reporting currency  */  
   Rpt1DspWithholdAmt:number,
      /**  Withholding tax amount in reporting currency  */  
   Rpt2DspWithholdAmt:number,
      /**  Withholding tax amount in reporting currency  */  
   Rpt3DspWithholdAmt:number,
      /**  Currency code from linked Invoice Header  */  
   LinkedCurrencyCode:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  PEBOEHeadNum  */  
   PEBOEHeadNum:number,
      /**  MXSellingShipQty  */  
   MXSellingShipQty:number,
      /**  MXUnitPrice  */  
   MXUnitPrice:number,
      /**  DocMXUnitPrice  */  
   DocMXUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1MXUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2MXUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3MXUnitPrice:number,
      /**  CustCostCenter  */  
   CustCostCenter:string,
      /**  DEIsServices  */  
   DEIsServices:boolean,
      /**  DEIsSecurityFinancialDerivative  */  
   DEIsSecurityFinancialDerivative:boolean,
      /**  DEInternationalSecuritiesID  */  
   DEInternationalSecuritiesID:string,
      /**  DEIsInvestment  */  
   DEIsInvestment:boolean,
      /**  DEPayStatCode  */  
   DEPayStatCode:string,
      /**  DefRevEndDate  */  
   DefRevEndDate:string,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  Indicates tha this invoice Line was reclassified.  */  
   Reclassified:boolean,
      /**  Enables the user the ability to override the Percent or Amount of revenue to be deferred  */  
   PartiallyDefer:boolean,
      /**  Percentage of revenue to be deferred for this line item  */  
   DeferredPercent:number,
      /**  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  */  
   Reclass:boolean,
      /**  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  */  
   DeferredOnly:boolean,
      /**  Reclassification Code. This field will be required if Reclass is checked.  */  
   ReclassCodeID:string,
      /**  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  */  
   ReclassReasonCode:string,
      /**  Internal comments for reclassification entered by the user.  */  
   ReclassComments:string,
      /**  Deferred Revenue Amount in base currency  */  
   DeferredRevAmt:number,
      /**  Deferred Revenue Amount in document currency  */  
   DocDeferredRevAmt:number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   Rpt1DeferredRevAmt:number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   Rpt2DeferredRevAmt:number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   Rpt3DeferredRevAmt:number,
      /**  ChargeReclass  */  
   ChargeReclass:boolean,
      /**  DEDenomination  */  
   DEDenomination:string,
      /**  DropShipPONum  */  
   DropShipPONum:number,
      /**  DocInAdvanceBillCredit  */  
   DocInAdvanceBillCredit:number,
      /**  InAdvanceBillCredit  */  
   InAdvanceBillCredit:number,
      /**  Rpt1InAdvanceBillCredit  */  
   Rpt1InAdvanceBillCredit:number,
      /**  Rpt2InAdvanceBillCredit  */  
   Rpt2InAdvanceBillCredit:number,
      /**  Rpt3InAdvanceBillCredit  */  
   Rpt3InAdvanceBillCredit:number,
      /**  MYIndustryCode  */  
   MYIndustryCode:string,
      /**  The dockingstation of the shipto address.  For future use.  */  
   DockingStation:string,
      /**  ConsolidateLines  */  
   ConsolidateLines:boolean,
      /**  MXCustomsDuty  */  
   MXCustomsDuty:string,
      /**  CommodityCode  */  
   CommodityCode:string,
      /**  MXProdServCode  */  
   MXProdServCode:string,
      /**  Quote number to which this line item detail record is associated with.  */  
   QuoteNum:number,
      /**  Quote Line number from which this invoice line was created from.  */  
   QuoteLine:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  MXCustomsUMFrom  */  
   MXCustomsUMFrom:string,
      /**  PE Detraction good or service code  */  
   PEDetrGoodServiceCode:string,
      /**  PETaxExempt  */  
   PETaxExempt:string,
      /**  Order number on the Invoicing Company.  */  
   CColOrderNum:number,
      /**  Order number line the Invoicing Company.  */  
   CColOrderLine:number,
      /**  Order number release the Invoicing Company.  */  
   CColOrderRel:number,
      /**  Invoice Line reference on the Invoicing Company.  */  
   CColInvoiceLineRef:number,
      /**  Packing slip number on the Invoicing Company.  */  
   CColPackNum:number,
      /**  Packing slip line number on the Invoicing Company.  */  
   CColPackLine:number,
      /**  Drop shipment packing slip number on the Invoicing Company.  */  
   CColDropShipPackSlip:string,
      /**  Drop shipment packing slip line number on the Invoicing Company.  */  
   CColDropShipPackSlipLine:number,
      /**  Ship To Customer ID from the Invoice Line in the subsidiary company.  */  
   CColShipToCustID:string,
      /**  Ship To from the Invoice Line in the subsidiary company.  */  
   CColShipToNum:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Exempt Reason Code  */  
   ExemptReasonCode:string,
      /**  Associates the Call Line record back its linked jobnum  */  
   JobNum:string,
      /**  Indicates where invoice detail was created from when created from a service call job. Not maintainable. “Summarized Labor”, “Summarized Material”, “Labor”, “Material”  */  
   ServiceSource:string,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  AssemblySeq related to JobMtl or JobOper used to create invoice line from service call job  */  
   AssemblySeq:number,
      /**  Job Mtl seq used to create invoice line from service call job  */  
   MtlSeq:number,
      /**  Job subcontract oper seq used to create invoice line from service call job  */  
   OprSeq:number,
      /**  Indicates the labor type of the LaborDtl used to create invoice from service call job.  */  
   LaborType:string,
      /**  LaborDtl hours summed by labor rate. Used to create invoice line from labor related to service call job.  */  
   BillableLaborHrs:number,
      /**  Billable rate used to create invoice line from labor related to service call job. In base currency.  */  
   BillableLaborRate:number,
      /**  Indicates the type of service call transaction data used to create the invoice detail from a service call job. MT (material), LB (labor), SC (subcontract), MC (misc charge), SM (summarized material), SL (summarized labor), SS (summarized subcontract) No summarization for MC.  */  
   ServiceSourceType:string,
      /**  TotalCovenantDiscount  */  
   TotalCovenantDiscount:number,
      /**  DocCovenantDiscount  */  
   DocCovenantDiscount:number,
      /**  Rpt1CovenantDiscount  */  
   Rpt1CovenantDiscount:number,
      /**  Rpt2CovenantDiscount  */  
   Rpt2CovenantDiscount:number,
      /**  Rpt3CovenantDiscount  */  
   Rpt3CovenantDiscount:number,
      /**  TotalInCovenantDiscount  */  
   TotalInCovenantDiscount:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
      /**  Adv bill enabled flag  */  
   AdvBillEnabled:boolean,
   AllowTaxCodeUpd:boolean,
      /**  This flag not allow updating PartiallyDefer in 'Posted Invoice Update' if  AR Invoice Line was  marked as Partially Defer in AR Invoice Entry.  */  
   AllowUpdPartDefer:boolean,
      /**  CustID associated with the InvcDtl.BTCustNum field.  */  
   BillToCustID:string,
      /**  Customer Name associated with the InvcDtl.BTCustNum field.  */  
   BTCustName:string,
      /**  The date and time that the record was last changed  */  
   ChangeDateTime:string,
      /**  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  */  
   CheckAmortAmounts:boolean,
   CNGTIDescription1:string,
   CNGTIDescription2:string,
   CNGTIDescription3:string,
      /**  CSF China, discount tax amount  */  
   CNGTIDiscountTaxAmount:number,
   CNGTIIUM:string,
   CNGTINetAmount:number,
   CNGTIPartDescription:string,
   CNGTISpecification:string,
   CNGTITaxAmount:number,
   CNGTITaxCode:string,
   CNGTITaxPercent:number,
   CNGTITotalAmount:number,
      /**  CSF China, Unit price = if InvcHead.InPrice then InvcDtl.InUnitPrice else InvcDtl.UnitPrice  */  
   CNGTIUnitPrice:number,
   ContractSuspended:boolean,
      /**  Currency code from InvcHead.  */  
   CurrencyCode:string,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   CurrencySwitch:boolean,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   CustID:string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   CustName:string,
      /**  Invoice Detail Customer Name  */  
   CustomerName:string,
      /**  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  */  
   DeleteRASchedule:boolean,
   DispGLAcct:string,
      /**  Currency display symbol  */  
   DisplaySymbol:string,
      /**  PO number for display.  */  
   DispPONum:string,
      /**  Ship to display address  */  
   DispShipToAddr:string,
      /**  Document display symbol.  */  
   DocDisplaySymbol:string,
   DocDspUnitPrice:number,
      /**  Document discount amount  */  
   DocLessDiscount:number,
      /**  Doc line tax  */  
   DocLineTax:number,
      /**  ExtPrice-disc+misc charges.  */  
   DocLineTotal:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   DocPEDetAmt:number,
      /**  Drop Shipment  */  
   DropShipment:boolean,
      /**  Display advance bill credit  */  
   DspAdvanceBillCredit:number,
      /**  Display discount  */  
   DspDiscount:number,
      /**  Display documents advance bill credit  */  
   DspDocAdvanceBillCredit:number,
      /**  Display document discount  */  
   DspDocDiscount:number,
      /**  Display document ext price  */  
   DspDocExtPrice:number,
      /**  Display document less discount  */  
   DspDocLessDiscount:number,
      /**  Display document line tax  */  
   DspDocLineTax:number,
      /**  Display document line total  */  
   DspDocLineTotal:number,
      /**  Display document total misc. charge  */  
   DspDocTotalMiscChrg:number,
      /**  Display ext price  */  
   DspExtPrice:number,
      /**  Display Invoice Reference  */  
   DspInvoiceRef:number,
      /**  Display less discount  */  
   DspLessDiscount:number,
      /**  Display line tax  */  
   DspLineTax:number,
      /**  Display line total  */  
   DspLineTotal:number,
      /**  Display our ship qty  */  
   DspOurShipQty:number,
      /**  Display selling ship qty  */  
   DspSellingShipQty:number,
   DspTaxExempt:string,
      /**  Display total misc. charges  */  
   DspTotalMiscChrg:number,
   DspUnitPrice:number,
      /**  Invoice head due date.  */  
   DueDate:string,
      /**  FSA Technician  */  
   EmpID:string,
   EnableDspWithholdAmt:boolean,
   EnableRMADelete:boolean,
   EnableRMAUpdate:boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   FSACallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   FSAContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   FSAContractNum:number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   FSAEmpID:string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   FSAWarrantyCode:string,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  Group associated to the invoice  */  
   GroupID:string,
   InPrice:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  Invoice Header Legal Number  */  
   InvLegalNum:string,
      /**  Invoice Date from InvcHead.  */  
   InvoiceDate:string,
      /**  Invoice header type  */  
   InvoiceType:string,
      /**  Is commission button sensitive  */  
   IsCommisBtnSensitive:boolean,
      /**  Set to true if intrastat is enabled.  */  
   IsIntrastatSensitive:boolean,
      /**  Tax buton sensitive or not.  */  
   IsTaxBtnSensitive:boolean,
      /**  display discount  */  
   LessDiscount:number,
      /**  Line tax amount  */  
   LineTax:number,
      /**  ExtPrice-disc+misc charges.  */  
   LineTotal:number,
   LinkedCurrencySymbol:string,
      /**  The flag based on the user responce to indicate if Ship To to be chnaged on Invoice detail record without tax information from Ship To because of the different tax pricing  */  
   NoShipTaxRgnInfo:boolean,
      /**  Open invoice flag from InvcHead.  */  
   OpenInvoice:boolean,
      /**  OrderUM display  */  
   OrderUM:string,
      /**  original tax category  */  
   OrigTaxCat:string,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   PEDetAmt:number,
      /**  PE Detraction good or service code description  */  
   PEDetrGoodServiceCodeDesc:string,
   PEDspCurrencySymbol:string,
      /**  PE VAT Exemption Reason  */  
   PEVATExemptionReason:string,
      /**  Posted flag from the InvcHead.  */  
   Posted:boolean,
   RADesc:string,
      /**  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  */  
   RASchedExists:boolean,
      /**  The internal flag to indicate if the logic is supposed to remove manual and/or manually added tax records per User request if the Line Tax Exempt field is populated  */  
   RemoveManAdTax:boolean,
   Rpt1DspAdvanceBillCredit:number,
   Rpt1DspDiscount:number,
   Rpt1DspExtPrice:number,
   Rpt1DspLessDiscount:number,
   Rpt1DspLineTax:number,
   Rpt1DspLineTotal:number,
   Rpt1DspTotalMiscChrg:number,
   Rpt1DspUnitPrice:number,
   Rpt1LineTax:number,
   Rpt1LineTotal:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   Rpt1PEDetAmt:number,
   Rpt2DspAdvanceBillCredit:number,
   Rpt2DspDiscount:number,
   Rpt2DspExtPrice:number,
   Rpt2DspLessDiscount:number,
   Rpt2DspLineTax:number,
   Rpt2DspLineTotal:number,
   Rpt2DspTotalMiscChrg:number,
   Rpt2DspUnitPrice:number,
   Rpt2LineTax:number,
   Rpt2LineTotal:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   Rpt2PEDetAmt:number,
   Rpt3DspAdvanceBillCredit:number,
   Rpt3DspDiscount:number,
   Rpt3DspExtPrice:number,
   Rpt3DspLessDiscount:number,
   Rpt3DspLineTax:number,
   Rpt3DspLineTotal:number,
   Rpt3DspTotalMiscChrg:number,
   Rpt3DspUnitPrice:number,
   Rpt3LineTax:number,
   Rpt3LineTotal:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   Rpt3PEDetAmt:number,
      /**  1st sales rep of the invoice.  */  
   SalesRepCode1:string,
      /**  2nd sales rep of the invoice header.  */  
   SalesRepCode2:string,
      /**  3rd sales rep code of the invoice header.  */  
   SalesRepCode3:string,
      /**  4th sales rep code of the invoice header.  */  
   SalesRepCode4:string,
      /**  5th salesrep code of the invoice header.  */  
   SalesRepCode5:string,
      /**  1st sales rep name  */  
   SalesRepName1:string,
      /**  2nd sales rep name  */  
   SalesRepName2:string,
      /**  3rd sales rep name  */  
   SalesRepName3:string,
      /**  4th sales rep name  */  
   SalesRepName4:string,
      /**  5th sales rep name  */  
   SalesRepName5:string,
   ShipToContactEMailAddress:string,
   ShipToContactFaxNum:string,
   ShipToContactName:string,
   ShipToContactPhoneNum:string,
      /**  Ship Head Legal Number  */  
   ShpLegalNum:string,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   SoldToCustID:string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   SoldToCustName:string,
      /**  Terms code from InvcHead.  */  
   TermsCode:string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   WarrantyCode:string,
      /**  This flag allow updating Reclassification data.  */  
   AllowReclassify:boolean,
      /**  The flag to indicate if the amount  is re-calculated to doc/base/rpt currencies after entered and no need to re-calculate on save.  */  
   LineAmtRecalcd:boolean,
      /**  Set to true if extra trade statistics is enabled.  */  
   IsExtrastatSensitive:boolean,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   TrackInventoryByRevision:boolean,
   BitFlag:number,
   CallCodeCallDescription:string,
   CommodityCodeDescription:string,
   ContractCodeContractDescription:string,
   ContractNumSuspended:boolean,
   CustCntName:string,
   CustCntMiddleName:string,
   CustCntFirstName:string,
   CustCntFaxNum:string,
   CustCntCorpName:string,
   CustCntPhoneNum:string,
   CustCntLastName:string,
   CustNumCustID:string,
   CustNumName:string,
   CustNumAllowShipTo3:boolean,
   CustNumBTName:string,
   InvoiceNumTermsCode:string,
   InvoiceNumCardMemberName:string,
   JournalCodeJrnlDescription:string,
   MilestoneIDDescription:string,
   MXProdServCodeDesc:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   OTSCntryEUMember:boolean,
   OTSCntryISOCode:string,
   OTSCntryDescription:string,
   PackLineLineDesc:string,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumAttrClassID:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackInventoryByRevision:boolean,
   ProdCodeDescription:string,
   ProjectIDDescription:string,
   ReclassCodeDescription:string,
   ReclassReasonDescription:string,
   RMALineLineDesc:string,
   SalesCatIDDescription:string,
   ShipToCustCustID:string,
   ShipToCustName:string,
   ShipToCustBTName:string,
   ShipToNumInactive:boolean,
   ShipToNumName:string,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   TaxCatIDDescription:string,
   TaxRegionDescription:string,
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

export interface Erp_Tablesets_RMADtlAttchRow{
   Company:string,
   RMANum:number,
   RMALine:number,
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

export interface Erp_Tablesets_RMADtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Mirror image of RMAHead.OpenRMA.  */  
   OpenRMA:boolean,
      /**  Indicates the Open/Closed status of the RMADtl.  This gets set to closed when there are no pending actions to be taken on related receipts.  */  
   OpenDtl:boolean,
      /**  Return Authorization Number. Used to relate RMADtl to RMAHead.  */  
   RMANum:number,
      /**  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  */  
   RMALine:number,
      /**   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  */  
   OrderNum:number,
      /**  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  */  
   OrderLine:number,
      /**  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  */  
   ReturnReasonCode:string,
      /**   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  */  
   Note:string,
      /**  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  */  
   PartNum:string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   LineDesc:string,
      /**  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  */  
   RevisionNum:string,
      /**  Quantity that is to be returned  */  
   ReturnQty:number,
      /**  Unit Of Measure of the  ReturnQty.  */  
   ReturnQtyUOM:string,
      /**  Reference Invoice number used for finding Tax Category  */  
   RefInvoiceNum:number,
      /**  Reference invoice line - Used to obtain the correct tax category  */  
   RefInvoiceLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  The Ship to number of the related header contact.  */  
   ShipToNum:string,
      /**  The Contact Number of the related header contact  */  
   ConNum:number,
      /**  Contains the system internal customer number used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The order release number that the RMA line was created from.  */  
   OrderRelNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Reference AR Invoice Number  */  
   InvoiceNum:number,
      /**  Reference AR Invoice Line Number  */  
   InvoiceLine:number,
      /**  Job Number.  */  
   JobNum:string,
      /**  Assembly sequence number that this material is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   MtlSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ECC RMA Comment  */  
   ECCComment:string,
      /**  ECC RMA Num  */  
   ECCRMANum:string,
      /**  ECC RMA Line  */  
   ECCRMALine:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  CNDeclarationBillLine  */  
   CNDeclarationBillLine:number,
      /**  Indicates that the line of the invoice has multiple packs consolidated. Details of the pack should be reviewied in InvcDtlPack table  */  
   ConsolidateLines:boolean,
      /**  Indicates that the invoice line has consolidated shipment lines that are related to the same release of the sales order  */  
   ConsolidateOneRelease:boolean,
   CustomerContactEMailAddress:string,
      /**  The full customer's name.  */  
   CustomerName:string,
      /**  The name for the ship to location.  */  
   CustomerShipToName:string,
      /**  From RMAHead.DebitMemoRef, used by Customer Tracker  */  
   DebitMemoRef:string,
      /**  If company parameter 'Allow Multiple Credit Invoices' is off and there is a least one credit memo then another credit memo adding is not allowed.  */  
   EnableAddCreditMemo:boolean,
   EnableDelete:boolean,
      /**  Flag to determine if Serial Numbers are required for this transaction.  */  
   EnableSN:boolean,
   EnableUpdate:boolean,
      /**  Determines if the RMA is synchronized with Epicor FSA application.  */  
   EpicorFSA:boolean,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Serivce Type  */  
   FSAServiceType:string,
      /**  Technician  */  
   FSATechnician:string,
      /**  From RMAHead.HDCaseNum, used by Customer Tracker  */  
   HDCaseNum:number,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
   LegalNumber:string,
   LocalizationFlag:string,
      /**  Set from RMAHead.RMADate, used by Customer Tracker  */  
   RMADate:string,
   RMARcptExists:boolean,
      /**  Customer Id of the third-party Ship To  */  
   ShipToCustID:string,
      /**  The name for the ship to location.  */  
   ShipToName:string,
   CustomerContactName:string,
      /**  The customer ID.  */  
   CustomerCustID:string,
   CNDeclarationBill:string,
   BitFlag:number,
   AttrValueSetDescription:string,
   AttrValueSetShortDescription:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PartNumAttrClassID:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumTrackInventoryAttributes:boolean,
   ReasonDescription:string,
   ReturnReasonCodeDescription:string,
   ShipToNumInactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RMAHeadAttchRow{
   Company:string,
   RMANum:number,
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

export interface Erp_Tablesets_RMAHeadListRow{
      /**  Indicates if this RA is in an "open" status.  The user can toggle the setting of this field in header maintenance. It is also set automatically as the details are "Closed/Opened".  If there are no RMADtl records, then it is still considered as "open".  */  
   OpenRMA:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  */  
   RMANum:number,
      /**  Date of the Return Material Authorization.  Default as System date.  */  
   RMADate:string,
      /**  Contains the system internal customer number used to relate this record to the customer master.  */  
   CustNum:number,
      /**  Reference to a customers accounts payable debit memo.  */  
   DebitMemoRef:string,
      /**  The Clientele call number that is related to this RMA.  */  
   CLCallNum:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Customer Name  */  
   CustomerName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RMAHeadListTableset{
   RMAHeadList:Erp_Tablesets_RMAHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RMAHeadRow{
      /**  Indicates if this RA is in an "open" status.  The user can toggle the setting of this field in header maintenance. It is also set automatically as the details are "Closed/Opened".  If there are no RMADtl records, then it is still considered as "open".  */  
   OpenRMA:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  */  
   RMANum:number,
      /**  Date of the Return Material Authorization.  Default as System date.  */  
   RMADate:string,
      /**  Contains the system internal customer number used to relate this record to the customer master.  */  
   CustNum:number,
      /**  Reference to a customers accounts payable debit memo.  */  
   DebitMemoRef:string,
      /**  The Clientele call number that is related to this RMA.  */  
   CLCallNum:string,
      /**  Cross reference RMA number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefRMANumber:string,
      /**  The help desk case that created this RMA.  */  
   HDCaseNum:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  The Ship to number of the related header contact.  */  
   ShipToNum:string,
      /**  The Contact Number of the related header contact  */  
   ConNum:number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**   Indicates if the One Time Ship To info is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping Country Number  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Reference AR Invoice Number  */  
   InvoiceNum:number,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The Return Invoice Number for the RMA (CSF - Turkey)  */  
   RetInvoiceNum:string,
      /**  ECC RMA Number  */  
   ECCRMANum:string,
      /**  Customer Web Reference to RMA.  */  
   ECCCustRef:string,
      /**  DocumentPrinted  */  
   DocumentPrinted:boolean,
      /**  Comments about the RMA overall  */  
   RMAComment:string,
      /**  Web Comments about the RMA overall  */  
   WebComment:string,
      /**  EpicorFSA  */  
   EpicorFSA:boolean,
      /**  Declaration Bill  */  
   CNDeclarationBill:string,
      /**  CNBonded  */  
   CNBonded:boolean,
      /**  Bil to customer name  */  
   BillToCustomerName:string,
      /**  Bill To Customer Name  */  
   BTCustName:string,
   CustomerContactEMailAddress:string,
   CustomerContactName:string,
      /**  Column to indicate if the customer set for the RMA is sync'd to FSA.  */  
   CustomerFSA:boolean,
   EnableDelete:boolean,
   EnableUpdate:boolean,
      /**  Column to indicate if the RMA was created on FSA.  */  
   FromFSA:boolean,
      /**  Web address list for the contact who initiated the RMA.  */  
   WebAddressList:string,
      /**  Delimited list of available bill to customers.  */  
   AvailBTCustList:string,
   BitFlag:number,
   BTCustNumInactive:boolean,
   CustomerName:string,
   CustomerCustID:string,
   CustomerBTName:string,
   CustomerInactive:boolean,
   HDCaseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RMAProcTableset{
   RMAHead:Erp_Tablesets_RMAHeadRow[],
   RMAHeadAttch:Erp_Tablesets_RMAHeadAttchRow[],
   RMADtl:Erp_Tablesets_RMADtlRow[],
   RMADtlAttch:Erp_Tablesets_RMADtlAttchRow[],
   InvcDtl:Erp_Tablesets_InvcDtlRow[],
   RMARcpt:Erp_Tablesets_RMARcptRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SerialNumberSearch:Erp_Tablesets_SerialNumberSearchRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RMARcptRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Return Authorization Number of related RMAHead.  */  
   RMANum:number,
      /**  Line # of the related RMADtl record.  */  
   RMALine:number,
      /**  RMA Receipt  */  
   RMAReceipt:number,
      /**  Warehouse ID the item was received into.  Normally this would be a "Inspection" type of warehouse.  */  
   WareHouseCode:string,
      /**  Warehouse Bin location in which the received item was placed.  */  
   BinNum:string,
      /**  Receipt Date  */  
   RcvDate:string,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  This is set to NO when the entire quantity has been accounted for in RMADisp.  */  
   OpenReceipt:boolean,
      /**  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost of Returned Item.  (See MtlUnitCost)  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost of Returned Item.  (See MtlUnitCost)  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost of Returned Item.  (See MtlUnitCost)  */  
   SubUnitCost:number,
      /**  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  */  
   MtlBurUnitCost:number,
      /**  The Site that this RMA receipt was received to.  This is set as from the "Current Site" at the time of receipt.  It will be used in the filtering of receipts in the Disposition process.  */  
   Plant:string,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlMtlBurUnitCost:number,
      /**  Quantity that has been received.  */  
   ReceivedQty:number,
      /**  Quantity that has been dispositioned .  Cannot exceed ReceivedQty.  This is summation of the quantities from the supporting RMADisp records.  When DisposedQty = ReceivedQty the RMARcpt.OpenReceipt is set to NO.  */  
   DisposedQty:number,
      /**  Unit of measure that qualifies the unit costs.  */  
   CostUOM:string,
      /**  Received Quantity unit of measure.  */  
   ReceivedQtyUOM:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Material Queue Records will only be updated if the "Request Move" box is checked  */  
   RequestMove:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Part number of the RMA line  */  
   PartNum:string,
   EnableWarehouse:boolean,
   EnableBin:boolean,
   CustomerName:string,
   PartRevisionNum:string,
   EnableDelete:boolean,
   EnableUpdate:boolean,
   CustNum:number,
   LegalNumberMessage:string,
      /**  PartPartDescription  */  
   PartPartDescription:string,
      /**  PartTrackLots  */  
   PartTrackLots:boolean,
      /**  PartTrackSerialNum  */  
   PartTrackSerialNum:boolean,
      /**  The receipt quantity displayed in the RMADtl.ReturnQty.  */  
   ThisRcptQty:number,
      /**  The UOM of the RMA Detail ( RMADtl.ReturnQtyUOM)  */  
   ThisRcptQtyUOM:string,
      /**  Same value as ReceivedQtyUOM.  */  
   DisposedQtyUOM:string,
      /**  Flag to determine if Serial Numbers are required for this transaction.  */  
   EnableSN:boolean,
   EnableInspection:boolean,
   IsPartMaster:boolean,
      /**  Serial Number used only for FSA  */  
   SerialNumber:string,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   PartTrackInventoryByRevision:boolean,
   PartTrackInventoryAttributes:boolean,
   BitFlag:number,
   BinNumDescription:string,
   WareHouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
   HasSerialNumbers:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartPartDescription:string,
   SerialMaskMaskType:number,
   SerialMaskMask:string,
   SerialMaskExample:string,
   SerialMaskDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsRow{
      /**  The part number to which the serial numbers have been assigned.  */  
   partNum:string,
      /**  The quantity of serial numbers that need to be selected.  */  
   quantity:number,
      /**  whereClause for filtering available serial numbers  */  
   whereClause:string,
      /**  transType of this transaction  */  
   transType:string,
      /**  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  */  
   sourceRowID:string,
      /**  Determines if serial numbers can be created.  */  
   enableCreate:boolean,
      /**  Determines if serial numbers can be selected.  */  
   enableSelect:boolean,
      /**  Determines if serial numbers can be retrieved.  */  
   enableRetrieve:boolean,
      /**  Specifies whether Voided serial numbers can be manually selected.  */  
   allowVoided:boolean,
      /**  The Plant associated with this transaction  */  
   plant:string,
   xrefPartNum:string,
   xrefPartType:string,
   xrefCustNum:number,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   attributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   attributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   revisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsTableset{
   SelectSerialNumbersParams:Erp_Tablesets_SelectSerialNumbersParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Reference field  */  
   Reference:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  PartNumber  */  
   PartNum:string,
      /**  Serial number prefix  */  
   SNPrefix:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  Used only by SN Assignment  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask the was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
   RowSelected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SerialNumberSearchRow{
      /**  Token reserved for the process ID  */  
   ProcessToken:string,
      /**  1st generic token.  */  
   GenericToken1:string,
      /**  2nd generic token  */  
   GenericToken2:string,
      /**  Returns where clause based on input tokens.  */  
   WhereClause:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtRMAProcTableset{
   RMAHead:Erp_Tablesets_RMAHeadRow[],
   RMAHeadAttch:Erp_Tablesets_RMAHeadAttchRow[],
   RMADtl:Erp_Tablesets_RMADtlRow[],
   RMADtlAttch:Erp_Tablesets_RMADtlAttchRow[],
   InvcDtl:Erp_Tablesets_InvcDtlRow[],
   RMARcpt:Erp_Tablesets_RMARcptRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SerialNumberSearch:Erp_Tablesets_SerialNumberSearchRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   listAvailTranDocTypes:string,
}
}

   /** Required : 
      @param rmANum
   */  
export interface GetByID_input{
   rmANum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_RMAProcTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_RMAProcTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_RMAProcTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetDateUser_input{
   ds:Erp_Tablesets_RMAProcTableset[],
}

export interface GetDateUser_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
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
   returnObj:Erp_Tablesets_RMAHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param invoiceNum
   */  
export interface GetNewInvcDtl_input{
   ds:Erp_Tablesets_RMAProcTableset[],
   invoiceNum:number,
}

export interface GetNewInvcDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param rmANum
      @param rmALine
   */  
export interface GetNewRMADtlAttch_input{
   ds:Erp_Tablesets_RMAProcTableset[],
   rmANum:number,
   rmALine:number,
}

export interface GetNewRMADtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param rmANum
   */  
export interface GetNewRMADtl_input{
   ds:Erp_Tablesets_RMAProcTableset[],
   rmANum:number,
}

export interface GetNewRMADtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param rmANum
   */  
export interface GetNewRMAHeadAttch_input{
   ds:Erp_Tablesets_RMAProcTableset[],
   rmANum:number,
}

export interface GetNewRMAHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewRMAHead_input{
   ds:Erp_Tablesets_RMAProcTableset[],
}

export interface GetNewRMAHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param rmANum
      @param rmALine
   */  
export interface GetNewRMARcpt_input{
   ds:Erp_Tablesets_RMAProcTableset[],
   rmANum:number,
   rmALine:number,
}

export interface GetNewRMARcpt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

export interface GetRMAUseRefCosts_output{
      /**  Company parameter 'Use Referenced Invoice Costs' value.  */  
   returnObj:boolean,
}

   /** Required : 
      @param whereClauseRMAHead
      @param whereClauseRMAHeadAttch
      @param whereClauseRMADtl
      @param whereClauseRMADtlAttch
      @param whereClauseInvcDtl
      @param whereClauseRMARcpt
      @param whereClauseLegalNumGenOpts
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSerialNumberSearch
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRMAHead:string,
   whereClauseRMAHeadAttch:string,
   whereClauseRMADtl:string,
   whereClauseRMADtlAttch:string,
   whereClauseInvcDtl:string,
   whereClauseRMARcpt:string,
   whereClauseLegalNumGenOpts:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSerialNumberSearch:string,
   whereClauseSNFormat:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_RMAProcTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param ipTableName
   */  
export interface GetSelectSerialNumbersParams_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  Table Name RMADtl or RMARcpt  */  
   ipTableName:string,
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param cTableName
      @param iRMANum
      @param iRMALine
      @param iRMAReceipt
      @param ds
   */  
export interface GetSelectedSerialNumbers_input{
      /**  The table to retrieve the serial numbers for. Valid values are:
            RMADtl or RMARcpt  */  
   cTableName:string,
      /**  The RMA Number  */  
   iRMANum:number,
      /**  The RMA Detail line number  */  
   iRMALine:number,
      /**  The RMA Receipt number; will be 0 when cTableName = RMADtl  */  
   iRMAReceipt:number,
   ds:Erp_Tablesets_RMAProcTableset[],
}

export interface GetSelectedSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
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
      @param currentNote
   */  
export interface NoteUserAndDate_input{
   currentNote:string,
}

export interface NoteUserAndDate_output{
parameters : {
      /**  output parameters  */  
   updatedNote:string,
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_RMAProcTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
   RequiresUserInput:boolean,
}
}

   /** Required : 
      @param iRMANum
      @param iRMALine
      @param iCorrection
      @param ds
   */  
export interface RMACreditAdd_input{
      /**  The RMA Number to create the invoice from  */  
   iRMANum:number,
      /**  The RMA Line to create the invoice line from  */  
   iRMALine:number,
      /**  True will create a correction invoice, false will create a credit memo  */  
   iCorrection:boolean,
   ds:Erp_Tablesets_RMAProcTableset[],
}

export interface RMACreditAdd_output{
parameters : {
      /**  output parameters  */  
   iInvoiceNum:number,
   iInvoiceLine:number,
   opErrMsg:string,
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtRMAProcTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtRMAProcTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_RMAProcTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
}
}

   /** Required : 
      @param ds
      @param serialNumber
      @param ipTableName
   */  
export interface ValidateSN_input{
   ds:Erp_Tablesets_RMAProcTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
      /**  RMA TableName  */  
   ipTableName:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMAProcTableset,
   isVoided:boolean,
   warningMsg:string,
}
}

