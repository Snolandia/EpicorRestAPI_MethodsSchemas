import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.MobileLaborSvc
// Description: MobileLaborSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/$metadata", {
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
   Description: Get MobileLabors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileLabors
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborHedRow
   */  
export function get_MobileLabors(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileLabors
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileLaborHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MobileLaborHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileLabors(requestBody:Erp_Tablesets_MobileLaborHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the MobileLabor item
   Description: Calls GetByID to retrieve the MobileLabor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLabor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileLaborHedRow
   */  
export function get_MobileLabors_Company_LaborHedSeq(Company:string, LaborHedSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileLaborHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors(" + Company + "," + LaborHedSeq + ")", {
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
         resolve(data as Erp_Tablesets_MobileLaborHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MobileLabor for the service
   Description: Calls UpdateExt to update MobileLabor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileLabor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileLaborHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MobileLabors_Company_LaborHedSeq(Company:string, LaborHedSeq:string, requestBody:Erp_Tablesets_MobileLaborHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors(" + Company + "," + LaborHedSeq + ")", {
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
   Summary: Call UpdateExt to delete MobileLabor item
   Description: Call UpdateExt to delete MobileLabor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileLabor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MobileLabors_Company_LaborHedSeq(Company:string, LaborHedSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors(" + Company + "," + LaborHedSeq + ")", {
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
   Description: Get MobileLaborDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MobileLaborDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborDtlRow
   */  
export function get_MobileLabors_Company_LaborHedSeq_MobileLaborDtls(Company:string, LaborHedSeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors(" + Company + "," + LaborHedSeq + ")/MobileLaborDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MobileLaborDtl item
   Description: Calls GetByID to retrieve the MobileLaborDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLaborDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileLaborDtlRow
   */  
export function get_MobileLabors_Company_LaborHedSeq_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileLaborDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors(" + Company + "," + LaborHedSeq + ")/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
         resolve(data as Erp_Tablesets_MobileLaborDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get MobileLaborDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileLaborDtls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborDtlRow
   */  
export function get_MobileLaborDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileLaborDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MobileLaborDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileLaborDtls(requestBody:Erp_Tablesets_MobileLaborDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the MobileLaborDtl item
   Description: Calls GetByID to retrieve the MobileLaborDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLaborDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileLaborDtlRow
   */  
export function get_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileLaborDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
         resolve(data as Erp_Tablesets_MobileLaborDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MobileLaborDtl for the service
   Description: Calls UpdateExt to update MobileLaborDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileLaborDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, requestBody:Erp_Tablesets_MobileLaborDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
   Summary: Call UpdateExt to delete MobileLaborDtl item
   Description: Call UpdateExt to delete MobileLaborDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileLaborDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
   Description: Get MobileLaborDtlComments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MobileLaborDtlComments1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborDtlCommentRow
   */  
export function get_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq_MobileLaborDtlComments(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/MobileLaborDtlComments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MobileLaborDtlComment item
   Description: Calls GetByID to retrieve the MobileLaborDtlComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLaborDtlComment1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileLaborDtlCommentRow
   */  
export function get_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq_MobileLaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company:string, LaborHedSeq:string, LaborDtlSeq:string, CommentNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileLaborDtlCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/MobileLaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")", {
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
         resolve(data as Erp_Tablesets_MobileLaborDtlCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MobileLaborDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MobileLaborDtlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborDtlAttchRow
   */  
export function get_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq_MobileLaborDtlAttches(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/MobileLaborDtlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MobileLaborDtlAttch item
   Description: Calls GetByID to retrieve the MobileLaborDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLaborDtlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileLaborDtlAttchRow
   */  
export function get_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq_MobileLaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileLaborDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/MobileLaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_MobileLaborDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get MobileLaborDtlComments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileLaborDtlComments
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborDtlCommentRow
   */  
export function get_MobileLaborDtlComments(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlComments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileLaborDtlComments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlCommentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MobileLaborDtlCommentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileLaborDtlComments(requestBody:Erp_Tablesets_MobileLaborDtlCommentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlComments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the MobileLaborDtlComment item
   Description: Calls GetByID to retrieve the MobileLaborDtlComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLaborDtlComment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileLaborDtlCommentRow
   */  
export function get_MobileLaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company:string, LaborHedSeq:string, LaborDtlSeq:string, CommentNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileLaborDtlCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")", {
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
         resolve(data as Erp_Tablesets_MobileLaborDtlCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MobileLaborDtlComment for the service
   Description: Calls UpdateExt to update MobileLaborDtlComment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileLaborDtlComment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlCommentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MobileLaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company:string, LaborHedSeq:string, LaborDtlSeq:string, CommentNum:string, requestBody:Erp_Tablesets_MobileLaborDtlCommentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")", {
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
   Summary: Call UpdateExt to delete MobileLaborDtlComment item
   Description: Call UpdateExt to delete MobileLaborDtlComment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileLaborDtlComment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MobileLaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company:string, LaborHedSeq:string, LaborDtlSeq:string, CommentNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")", {
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
   Description: Get MobileLaborDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileLaborDtlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborDtlAttchRow
   */  
export function get_MobileLaborDtlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileLaborDtlAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MobileLaborDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileLaborDtlAttches(requestBody:Erp_Tablesets_MobileLaborDtlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the MobileLaborDtlAttch item
   Description: Calls GetByID to retrieve the MobileLaborDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLaborDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileLaborDtlAttchRow
   */  
export function get_MobileLaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileLaborDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_MobileLaborDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MobileLaborDtlAttch for the service
   Description: Calls UpdateExt to update MobileLaborDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileLaborDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MobileLaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, DrawingSeq:string, requestBody:Erp_Tablesets_MobileLaborDtlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete MobileLaborDtlAttch item
   Description: Call UpdateExt to delete MobileLaborDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileLaborDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MobileLaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")", {
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
   Description: Get MobileApproverLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileApproverLists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileApproverListRow
   */  
export function get_MobileApproverLists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileApproverListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileApproverLists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileApproverListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileApproverLists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileApproverListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MobileApproverListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileApproverLists(requestBody:Erp_Tablesets_MobileApproverListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileApproverLists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the MobileApproverList item
   Description: Calls GetByID to retrieve the MobileApproverList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileApproverList
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileApproverListRow
   */  
export function get_MobileApproverLists_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileApproverListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileApproverLists(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_MobileApproverListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MobileApproverList for the service
   Description: Calls UpdateExt to update MobileApproverList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileApproverList
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileApproverListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MobileApproverLists_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_MobileApproverListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileApproverLists(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete MobileApproverList item
   Description: Call UpdateExt to delete MobileApproverList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileApproverList
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MobileApproverLists_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileApproverLists(" + SysRowID + ")", {
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
   Description: Get MobileQuickEntryViews items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileQuickEntryViews
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileQuickEntryViewRow
   */  
export function get_MobileQuickEntryViews(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileQuickEntryViewRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileQuickEntryViews", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileQuickEntryViewRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileQuickEntryViews
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileQuickEntryViewRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MobileQuickEntryViewRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileQuickEntryViews(requestBody:Erp_Tablesets_MobileQuickEntryViewRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileQuickEntryViews", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the MobileQuickEntryView item
   Description: Calls GetByID to retrieve the MobileQuickEntryView item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileQuickEntryView
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileQuickEntryViewRow
   */  
export function get_MobileQuickEntryViews_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileQuickEntryViewRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileQuickEntryViews(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_MobileQuickEntryViewRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MobileQuickEntryView for the service
   Description: Calls UpdateExt to update MobileQuickEntryView. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileQuickEntryView
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileQuickEntryViewRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MobileQuickEntryViews_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_MobileQuickEntryViewRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileQuickEntryViews(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete MobileQuickEntryView item
   Description: Call UpdateExt to delete MobileQuickEntryView item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileQuickEntryView
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MobileQuickEntryViews_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileQuickEntryViews(" + SysRowID + ")", {
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
   Description: Get MobileTimeWeeklyViews items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileTimeWeeklyViews
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileTimeWeeklyViewRow
   */  
export function get_MobileTimeWeeklyViews(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileTimeWeeklyViewRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileTimeWeeklyViews", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileTimeWeeklyViewRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileTimeWeeklyViews
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileTimeWeeklyViewRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MobileTimeWeeklyViewRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileTimeWeeklyViews(requestBody:Erp_Tablesets_MobileTimeWeeklyViewRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileTimeWeeklyViews", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the MobileTimeWeeklyView item
   Description: Calls GetByID to retrieve the MobileTimeWeeklyView item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileTimeWeeklyView
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileTimeWeeklyViewRow
   */  
export function get_MobileTimeWeeklyViews_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileTimeWeeklyViewRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileTimeWeeklyViews(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_MobileTimeWeeklyViewRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MobileTimeWeeklyView for the service
   Description: Calls UpdateExt to update MobileTimeWeeklyView. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileTimeWeeklyView
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileTimeWeeklyViewRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MobileTimeWeeklyViews_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_MobileTimeWeeklyViewRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileTimeWeeklyViews(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete MobileTimeWeeklyView item
   Description: Call UpdateExt to delete MobileTimeWeeklyView item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileTimeWeeklyView
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MobileTimeWeeklyViews_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileTimeWeeklyViews(" + SysRowID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseMobileLaborHed:string, whereClauseMobileLaborDtl:string, whereClauseMobileLaborDtlAttch:string, whereClauseMobileLaborDtlComment:string, whereClauseMobileApproverList:string, whereClauseMobileQuickEntryView:string, whereClauseMobileTimeWeeklyView:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseMobileLaborHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMobileLaborHed=" + whereClauseMobileLaborHed
   }
   if(typeof whereClauseMobileLaborDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMobileLaborDtl=" + whereClauseMobileLaborDtl
   }
   if(typeof whereClauseMobileLaborDtlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMobileLaborDtlAttch=" + whereClauseMobileLaborDtlAttch
   }
   if(typeof whereClauseMobileLaborDtlComment!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMobileLaborDtlComment=" + whereClauseMobileLaborDtlComment
   }
   if(typeof whereClauseMobileApproverList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMobileApproverList=" + whereClauseMobileApproverList
   }
   if(typeof whereClauseMobileQuickEntryView!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMobileQuickEntryView=" + whereClauseMobileQuickEntryView
   }
   if(typeof whereClauseMobileTimeWeeklyView!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMobileTimeWeeklyView=" + whereClauseMobileTimeWeeklyView
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/GetRows" + params, {
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
export function get_GetByID(laborHedSeq:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof laborHedSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "laborHedSeq=" + laborHedSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/GetList" + params, {
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
   Summary: Invoke method MobileGetApprovalStatus
   Description: Populates the MobileApproverList Temp Table with the current expense's approver data.
   OperationID: MobileGetApprovalStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetApprovalStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetApprovalStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetApprovalStatus(requestBody:MobileGetApprovalStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetApprovalStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetApprovalStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetApprovalStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetQuickEntry
   Description: Populates the MobileQuickEntryView Temp Table with the current employee QuickEntry data.
   OperationID: MobileGetQuickEntry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetQuickEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetQuickEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetQuickEntry(requestBody:MobileGetQuickEntry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetQuickEntry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetQuickEntry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetQuickEntry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: MobileGetRows
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetRows(requestBody:MobileGetRows_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetRowsWithFilter
   Description: Returns a dataset containing all rows that satisfy the where clauses and filters.
   OperationID: MobileGetRowsWithFilter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetRowsWithFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRowsWithFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetRowsWithFilter(requestBody:MobileGetRowsWithFilter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetRowsWithFilter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetRowsWithFilter", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetRowsWithFilter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetByID
   Description: Returns a DataSet given the primary key.
   OperationID: MobileGetByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetByID(requestBody:MobileGetByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileLaborGetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: MobileLaborGetList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileLaborGetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileLaborGetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileLaborGetList(requestBody:MobileLaborGetList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileLaborGetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborGetList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileLaborGetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMobileLaborDtlAttchs
   Description: Custom Method to retrieve only the MobileLaborDtlAttch records for the current labor
   OperationID: GetMobileLaborDtlAttchs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMobileLaborDtlAttchs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMobileLaborDtlAttchs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMobileLaborDtlAttchs(requestBody:GetMobileLaborDtlAttchs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMobileLaborDtlAttchs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/GetMobileLaborDtlAttchs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetMobileLaborDtlAttchs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMobileLaborDtlComments
   Description: Custom Method to retrieve only the MobileLaborDtlComment records for the current labor
   OperationID: GetMobileLaborDtlComments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMobileLaborDtlComments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMobileLaborDtlComments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMobileLaborDtlComments(requestBody:GetMobileLaborDtlComments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMobileLaborDtlComments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/GetMobileLaborDtlComments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetMobileLaborDtlComments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetNewLaborHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: MobileGetNewLaborHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetNewLaborHed(requestBody:MobileGetNewLaborHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetNewLaborHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetNewLaborHed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetNewLaborHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetNewLaborDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: MobileGetNewLaborDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetNewLaborDtl(requestBody:MobileGetNewLaborDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetNewLaborDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetNewLaborDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetNewLaborDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetNewLaborDtlComment
   Description: Calls GetNewLaborDtlComment base method then assign selected and default values.
   OperationID: MobileGetNewLaborDtlComment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborDtlComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborDtlComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetNewLaborDtlComment(requestBody:MobileGetNewLaborDtlComment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetNewLaborDtlComment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetNewLaborDtlComment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetNewLaborDtlComment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetNewLaborDtlAttch
   Description: Calls GetNewLaborDtlAttch base method then assign selected and default values.
   OperationID: MobileGetNewLaborDtlAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetNewLaborDtlAttch(requestBody:MobileGetNewLaborDtlAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetNewLaborDtlAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetNewLaborDtlAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetNewLaborDtlAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetNewLaborDtlOnSelectForWork
   Description: Call GetNewLaborDtl base method then assign selected values and default values
   OperationID: MobileGetNewLaborDtlOnSelectForWork
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborDtlOnSelectForWork_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborDtlOnSelectForWork_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetNewLaborDtlOnSelectForWork(requestBody:MobileGetNewLaborDtlOnSelectForWork_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetNewLaborDtlOnSelectForWork_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetNewLaborDtlOnSelectForWork", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetNewLaborDtlOnSelectForWork_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetNewLaborDtlNoHdr
   Description: This method is called to add a new labor detail without having a labor header
   OperationID: MobileGetNewLaborDtlNoHdr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborDtlNoHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborDtlNoHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetNewLaborDtlNoHdr(requestBody:MobileGetNewLaborDtlNoHdr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetNewLaborDtlNoHdr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetNewLaborDtlNoHdr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetNewLaborDtlNoHdr_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetNewLaborDtlWithHdr
   Description: This method is called to add a new labor detail without having a labor header record available
   OperationID: MobileGetNewLaborDtlWithHdr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborDtlWithHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborDtlWithHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetNewLaborDtlWithHdr(requestBody:MobileGetNewLaborDtlWithHdr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetNewLaborDtlWithHdr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetNewLaborDtlWithHdr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetNewLaborDtlWithHdr_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetNewTimeWeeklyView
   Description: Gets a new TimeWeeklyView record for the current week
   OperationID: MobileGetNewTimeWeeklyView
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetNewTimeWeeklyView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewTimeWeeklyView_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetNewTimeWeeklyView(requestBody:MobileGetNewTimeWeeklyView_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetNewTimeWeeklyView_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetNewTimeWeeklyView", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetNewTimeWeeklyView_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileDeleteLaborDtl
   Description: This method delete records related to HCM PTO.
   OperationID: MobileDeleteLaborDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileDeleteLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDeleteLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileDeleteLaborDtl(requestBody:MobileDeleteLaborDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileDeleteLaborDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileDeleteLaborDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileDeleteLaborDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileDelete
   Description: Method to call to delete expense records
   OperationID: MobileDelete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileDelete(requestBody:MobileDelete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileDelete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileDelete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileDelete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileLaborUpdate
   Description: Commits the DataSet changes to the data store.
   OperationID: MobileLaborUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileLaborUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileLaborUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileLaborUpdate(requestBody:MobileLaborUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileLaborUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileLaborUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileChangeEquipID
   Description: This method should call when EquipID is changed
   OperationID: MobileChangeEquipID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileChangeEquipID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileChangeEquipID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileChangeEquipID(requestBody:MobileChangeEquipID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileChangeEquipID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileChangeEquipID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileChangeEquipID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileChangeIndirectCode
   Description: This method should call when IndirectCode is changed
   OperationID: MobileChangeIndirectCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileChangeIndirectCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileChangeIndirectCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileChangeIndirectCode(requestBody:MobileChangeIndirectCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileChangeIndirectCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileChangeIndirectCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileChangeIndirectCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileChangeLaborType
   Description: This method should call when LaborType is changed
   OperationID: MobileChangeLaborType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileChangeLaborType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileChangeLaborType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileChangeLaborType(requestBody:MobileChangeLaborType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileChangeLaborType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileChangeLaborType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileChangeLaborType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileChangeResourceId
   Description: This method should call when ResourceID is changed
   OperationID: MobileChangeResourceId
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileChangeResourceId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileChangeResourceId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileChangeResourceId(requestBody:MobileChangeResourceId_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileChangeResourceId_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileChangeResourceId", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileChangeResourceId_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileCheckResourceGroup
   Description: This method should call when ResourceGroup is changed
   OperationID: MobileCheckResourceGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileCheckResourceGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileCheckResourceGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileCheckResourceGroup(requestBody:MobileCheckResourceGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileCheckResourceGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileCheckResourceGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileCheckResourceGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileCheckWarnings
   Description: This method runs the labor warning routine and returns any warnings the user
needs to be aware of. This needs to be run right before the update method. If
the user answers okay to all of the questions, then the update method can be
run. Otherwise the labor record needs to be corrected
   OperationID: MobileCheckWarnings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileCheckWarnings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileCheckWarnings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileCheckWarnings(requestBody:MobileCheckWarnings_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileCheckWarnings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileCheckWarnings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileCheckWarnings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileDefaultDtlTime
   Description: Sets Default DtlTime
   OperationID: MobileDefaultDtlTime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileDefaultDtlTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultDtlTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileDefaultDtlTime(requestBody:MobileDefaultDtlTime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileDefaultDtlTime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileDefaultDtlTime", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileDefaultDtlTime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileDefaultIndirect
   Description: Sets Default Indirect
   OperationID: MobileDefaultIndirect
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileDefaultIndirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultIndirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileDefaultIndirect(requestBody:MobileDefaultIndirect_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileDefaultIndirect_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileDefaultIndirect", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileDefaultIndirect_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileDefaultJobNum
   Description: Sets Default JobNum
   OperationID: MobileDefaultJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileDefaultJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileDefaultJobNum(requestBody:MobileDefaultJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileDefaultJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileDefaultJobNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileDefaultJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileDefaultLaborHrs
   Description: Sets Default LaborHrs
   OperationID: MobileDefaultLaborHrs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileDefaultLaborHrs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultLaborHrs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileDefaultLaborHrs(requestBody:MobileDefaultLaborHrs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileDefaultLaborHrs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileDefaultLaborHrs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileDefaultLaborHrs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileDefaultLaborQty
   Description: Sets Default LaborQty
   OperationID: MobileDefaultLaborQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileDefaultLaborQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultLaborQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileDefaultLaborQty(requestBody:MobileDefaultLaborQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileDefaultLaborQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileDefaultLaborQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileDefaultLaborQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileDefaultPhaseOprSeq
   Description: Sets Default PhaseOprSeq
   OperationID: MobileDefaultPhaseOprSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileDefaultPhaseOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultPhaseOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileDefaultPhaseOprSeq(requestBody:MobileDefaultPhaseOprSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileDefaultPhaseOprSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileDefaultPhaseOprSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileDefaultPhaseOprSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileDefaultOprSeq
   Description: Sets Default OprSeq
   OperationID: MobileDefaultOprSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileDefaultOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileDefaultOprSeq(requestBody:MobileDefaultOprSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileDefaultOprSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileDefaultOprSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileDefaultOprSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileVerifyScrapQty
   Description: This method defaults fields when the scrap qty field changes. Also checks for any labor warnings the user needs to be aware of
   OperationID: MobileVerifyScrapQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileVerifyScrapQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileVerifyScrapQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileVerifyScrapQty(requestBody:MobileVerifyScrapQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileVerifyScrapQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileVerifyScrapQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileVerifyScrapQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileDefaultLaborType
   Description: Sets Default LaborType
   OperationID: MobileDefaultLaborType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileDefaultLaborType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultLaborType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileDefaultLaborType(requestBody:MobileDefaultLaborType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileDefaultLaborType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileDefaultLaborType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileDefaultLaborType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckRecall
   Description: The procedure is called prior to performing a recall.  It will check
if subsequent approvals have occurred.  If they have the user
will have the opportunity to cancel the recall.
   OperationID: CheckRecall
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckRecall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRecall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRecall(requestBody:CheckRecall_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckRecall_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/CheckRecall", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckRecall_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecallTrans
   Description: Method to call when recalling from approval entry
   OperationID: RecallTrans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RecallTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecallTrans(requestBody:RecallTrans_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RecallTrans_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/RecallTrans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RecallTrans_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyLaborDetail
   Description: Method to copy the values from one LaborDtl record to a new LaborDtl record.
   OperationID: CopyLaborDetail
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyLaborDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyLaborDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyLaborDetail(requestBody:CopyLaborDetail_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyLaborDetail_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/CopyLaborDetail", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CopyLaborDetail_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileSync
   Description: Method to call to synchronize draft records to the database
   OperationID: MobileSync
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileSync_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileSync_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileSync(requestBody:MobileSync_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileSync_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileSync", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileSync_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileSyncSuccessful
   Description: Receives the fields needed to find and delete the validation record created when synchronization is successful
   OperationID: MobileSyncSuccessful
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileSyncSuccessful_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileSyncSuccessful_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileSyncSuccessful(requestBody:MobileSyncSuccessful_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileSyncSuccessful_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileSyncSuccessful", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileSyncSuccessful_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileAttachmentUpdate
   Description: Method to call to update attachment record and upload file to the storage defined by document type (or default company storage)
   OperationID: MobileAttachmentUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileAttachmentUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileAttachmentUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileAttachmentUpdate(requestBody:MobileAttachmentUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileAttachmentUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileAttachmentUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileAttachmentUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetHomePageData
   OperationID: MobileGetHomePageData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetHomePageData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetHomePageData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetHomePageData(requestBody:MobileGetHomePageData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetHomePageData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetHomePageData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetHomePageData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileOverrides
   Description: Method to be called by Mobile Time entry. Overrides the Resource Group and Operation Code in a job.
   OperationID: MobileOverrides
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileOverrides_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileOverrides_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileOverrides(requestBody:MobileOverrides_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileOverrides_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileOverrides", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileOverrides_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileDefaultPhaseID
   Description: This method to be called by Mobile Time entry. Defaults dataset fields when the PhaseID field changes.
   OperationID: MobileDefaultPhaseID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileDefaultPhaseID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultPhaseID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileDefaultPhaseID(requestBody:MobileDefaultPhaseID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileDefaultPhaseID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileDefaultPhaseID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileDefaultPhaseID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileRecallFromApproval
   Description: Method to recall Labor for Approval.
   OperationID: MobileRecallFromApproval
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileRecallFromApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileRecallFromApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileRecallFromApproval(requestBody:MobileRecallFromApproval_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileRecallFromApproval_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileRecallFromApproval", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileRecallFromApproval_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVersion
   Description: Returns BO Version
   OperationID: GetVersion
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVersion(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVersion_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/GetVersion", {
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
         resolve(data as GetVersion_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SubmitSelected
   Description: Method to call to submit selected time
   OperationID: SubmitSelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SubmitSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitSelected(requestBody:SubmitSelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SubmitSelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/SubmitSelected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SubmitSelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ApproveReject
   Description: The procedure is called when the user selects EmpExpense records for reject or approve
   OperationID: ApproveReject
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ApproveReject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveReject_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApproveReject(requestBody:ApproveReject_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ApproveReject_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/ApproveReject", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ApproveReject_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetRowsPendingApproval
   OperationID: MobileGetRowsPendingApproval
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetRowsPendingApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRowsPendingApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetRowsPendingApproval(requestBody:MobileGetRowsPendingApproval_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetRowsPendingApproval_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetRowsPendingApproval", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetRowsPendingApproval_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetRowsPendingApprovalWithFilter
   OperationID: MobileGetRowsPendingApprovalWithFilter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetRowsPendingApprovalWithFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRowsPendingApprovalWithFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetRowsPendingApprovalWithFilter(requestBody:MobileGetRowsPendingApprovalWithFilter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetRowsPendingApprovalWithFilter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileGetRowsPendingApprovalWithFilter", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MobileGetRowsPendingApprovalWithFilter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMobileLaborHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileLaborHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMobileLaborHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileLaborHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMobileLaborHed(requestBody:GetNewMobileLaborHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMobileLaborHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/GetNewMobileLaborHed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewMobileLaborHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMobileLaborDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileLaborDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMobileLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMobileLaborDtl(requestBody:GetNewMobileLaborDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMobileLaborDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/GetNewMobileLaborDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewMobileLaborDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMobileLaborDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileLaborDtlAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMobileLaborDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileLaborDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMobileLaborDtlAttch(requestBody:GetNewMobileLaborDtlAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMobileLaborDtlAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/GetNewMobileLaborDtlAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewMobileLaborDtlAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMobileLaborDtlComment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileLaborDtlComment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMobileLaborDtlComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileLaborDtlComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMobileLaborDtlComment(requestBody:GetNewMobileLaborDtlComment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMobileLaborDtlComment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/GetNewMobileLaborDtlComment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewMobileLaborDtlComment_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileApproverListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileApproverListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileLaborDtlAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlCommentRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileLaborDtlCommentRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileLaborDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileLaborHedRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileLaborListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileQuickEntryViewRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileQuickEntryViewRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileTimeWeeklyViewRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileTimeWeeklyViewRow,
}

export interface Erp_Tablesets_MobileApproverListRow{
      /**  The status of the current approval task.  */  
   "ApprovalStatus":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Date when the approval task was completed.  */  
   "CompleteDate":string,
      /**  Major component of the foreign key of the related master record. For a task related to an Expense this field would contain the related EmployeeID. For a task related to Labor this field would contain the related LaborHed.  */  
   "Key1":string,
      /**  Second component of the foreign key to the related master record. For a task related to an Expense, this field would contain the related ExpenseID. For a task related to Labor, this field would contain the related LaborDtl.  */  
   "Key2":string,
      /**  The master file to which the task is related.  */  
   "RelatedToFile":string,
      /**  The SalesRep that this task is assigned to.  */  
   "SalesRepCode":string,
      /**  Name corresponding to the SalesRepCode.  */  
   "SalesRepName":string,
      /**  Number used to display the records in their correct sequence in the mobile app.  */  
   "SequenceNum":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MobileLaborDtlAttchRow{
   "Company":string,
   "LaborHedSeq":number,
   "LaborDtlSeq":number,
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

export interface Erp_Tablesets_MobileLaborDtlCommentRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier of the Labor Header the comment relates to.  */  
   "LaborHedSeq":number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   "LaborDtlSeq":number,
      /**  Internal identifier of the comment record.  Used in conjunction with EmpTimeNum to make the record unique.  */  
   "CommentNum":number,
      /**   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  */  
   "CommentType":string,
      /**  The comment text.  */  
   "CommentText":string,
      /**  Userid of the user who created the record.  */  
   "CreatedBy":string,
      /**  The date the record was created.  */  
   "CreateDate":string,
      /**  The time the record was created (in seconds since midnight)  */  
   "CreateTime":number,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date the record was last changed.  */  
   "ChangeDate":string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   "ChangeTime":number,
      /**  The identifier of the Task record the comment is related to.  Can be zero, which indicates the comment is not related to a specific task.  */  
   "TaskSeqNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MobileLaborDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   "EmployeeNum":string,
      /**  Used as the foreign key to the LaborHed record.  */  
   "LaborHedSeq":number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   "LaborDtlSeq":number,
      /**   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   "LaborType":string,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   "LaborTypePseudo":string,
      /**  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  */  
   "ReWork":boolean,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  */  
   "ReworkReasonCode":string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   "JobNum":string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   "AssemblySeq":number,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   "OprSeq":number,
      /**  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  */  
   "JCDept":string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   "ResourceGrpID":string,
      /**  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  */  
   "OpCode":string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   "LaborHrs":number,
      /**  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  */  
   "BurdenHrs":number,
      /**  The Total production quantity reported.  */  
   "LaborQty":number,
      /**  The reported scrap quantity.  */  
   "ScrapQty":number,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  */  
   "ScrapReasonCode":string,
      /**  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  */  
   "SetupPctComplete":number,
      /**  Indicates if this transaction "completes" either the setup or production for this operation.  */  
   "Complete":boolean,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   "IndirectCode":string,
      /**  A short note that the user can make about the labor transaction.  */  
   "LaborNote":string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   "ExpenseCode":string,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   "LaborCollection":boolean,
      /**  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  */  
   "AppliedToSchedule":boolean,
      /**  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  */  
   "ClockInMInute":number,
      /**  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  */  
   "ClockOutMinute":number,
      /**  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  */  
   "ClockInDate":string,
      /**   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  */  
   "ClockinTime":number,
      /**   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  */  
   "ClockOutTime":number,
      /**   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  */  
   "ActiveTrans":boolean,
      /**  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  */  
   "OverRidePayRate":number,
      /**  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  */  
   "LaborRate":number,
      /**  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  */  
   "BurdenRate":number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   "DspClockInTime":string,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   "DspClockOutTime":string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   "ResourceID":string,
      /**  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  */  
   "OpComplete":boolean,
      /**  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  */  
   "EarnedHrs":number,
      /**  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  */  
   "AddedOper":boolean,
      /**  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  */  
   "PayrollDate":string,
      /**   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  */  
   "PostedToGL":boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  */  
   "GLTrans":boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Indicates if the labordtl record inspection has completed.  */  
   "InspectionPending":boolean,
      /**  The service call that this service record belongs to.  */  
   "CallNum":number,
      /**  The line number of the service call this labor detail is for.  */  
   "CallLine":number,
      /**  the service that is being performed on this line.  */  
   "ServNum":number,
      /**  A unique code that identifies the Service  */  
   "ServCode":string,
      /**  Problem reason code from the reason master table. type Service call.  */  
   "ResReasonCode":string,
      /**  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  */  
   "WipPosted":boolean,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   "DiscrepQty":number,
      /**   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  */  
   "DiscrpRsnCode":string,
      /**  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  */  
   "ParentLaborDtlSeq":number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  */  
   "LaborEntryMethod":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  */  
   "BFLaborReq":boolean,
      /**  Reference to the ABT, it is GUID,used in PostingEngine  */  
   "ABTUID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Project Role Code  */  
   "RoleCd":string,
      /**  Time Type Code  */  
   "TimeTypCd":string,
      /**  The Project Billing Invoice Number where these charges were processed.  */  
   "PBInvNum":number,
      /**  The payment method of the time.  */  
   "PMUID":number,
      /**  Link to Task set  */  
   "TaskSetID":string,
      /**  The date the time received final approval.  */  
   "ApprovedDate":string,
      /**  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   "ClaimRef":string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  */  
   "QuickEntryCode":string,
      /**   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   "TimeStatus":string,
      /**  Userid of the user who created the record.  */  
   "CreatedBy":string,
      /**  The date the record was created.  */  
   "CreateDate":string,
      /**  The time the record was created (in seconds since midnight)  */  
   "CreateTime":number,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date the record was last changed.  */  
   "ChangeDate":string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   "ChangeTime":number,
      /**  The Currently active Stage changing task  */  
   "ActiveTaskID":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
      /**  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  */  
   "CreatedViaTEWeekView":boolean,
      /**  The identifier of the workflow stage.  */  
   "CurrentWFStageID":string,
      /**  The identifier of the workflow group  */  
   "WFGroupID":string,
      /**  This indicates if the workflow for this group is complete.  */  
   "WFComplete":boolean,
      /**  Indicates if approval is required for this transaction.  */  
   "ApprovalRequired":boolean,
      /**  The User ID of the submitter.  */  
   "SubmittedBy":string,
      /**  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  */  
   "PBRateFrom":string,
      /**  Project Billing calculation in COSandWIP: Currency code is got from Project  */  
   "PBCurrencyCode":string,
      /**  Project Billing calculation in COSandWIP: Hours used for charge  */  
   "PBHours":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  */  
   "PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  */  
   "PBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  */  
   "DocPBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   "Rpt1PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   "Rpt2PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   "Rpt3PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  */  
   "DocPBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   "Rpt1PBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   "Rpt2PBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   "Rpt3PBChargeAmt":number,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   "Shift":number,
      /**  Links to PActDtl.ActID  */  
   "ActID":number,
      /**  System assigned unique id number for the detail. Links to PActDtl.DetailID  */  
   "DtailID":number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   "ProjProcessed":boolean,
      /**  Used By Project Analysis Process.  */  
   "AsOfDate":string,
      /**  Used By Project Analysis Process.  */  
   "AsOfSeq":number,
      /**  JDFInputFiles  */  
   "JDFInputFiles":string,
      /**  JDFNumberOfPages  */  
   "JDFNumberOfPages":string,
      /**  BatchWasSaved  */  
   "BatchWasSaved":string,
      /**  AssignToBatch  */  
   "AssignToBatch":boolean,
      /**  BatchComplete  */  
   "BatchComplete":boolean,
      /**  BatchRequestMove  */  
   "BatchRequestMove":boolean,
      /**  BatchPrint  */  
   "BatchPrint":boolean,
      /**  BatchLaborHrs  */  
   "BatchLaborHrs":number,
      /**  BatchPctOfTotHrs  */  
   "BatchPctOfTotHrs":number,
      /**  BatchQty  */  
   "BatchQty":number,
      /**  BatchTotalExpectedHrs  */  
   "BatchTotalExpectedHrs":number,
      /**  JDFOpCompleted  */  
   "JDFOpCompleted":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Downtime  */  
   "Downtime":boolean,
      /**  RefJobNum  */  
   "RefJobNum":string,
      /**  RefAssemblySeq  */  
   "RefAssemblySeq":number,
      /**  RefOprSeq  */  
   "RefOprSeq":number,
      /**  Imported  */  
   "Imported":boolean,
      /**  ImportDate  */  
   "ImportDate":string,
      /**   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  */  
   "TimeAutoSubmit":boolean,
      /**  BatchMode  */  
   "BatchMode":boolean,
      /**  BillServiceRate  */  
   "BillServiceRate":number,
      /**  Pay Hours used for HCM  */  
   "HCMPayHours":number,
      /**  True if transaction is related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  Indicates if the labor detail has attachments  */  
   "HasAttachments":boolean,
      /**  Indicates if the labor detail has comments  */  
   "HasComments":boolean,
   "EnableComplete":boolean,
      /**  Indicates if the copy button is enabled  */  
   "EnableCopy":boolean,
      /**  Indicates if the recall button is enabled  */  
   "EnableRecall":boolean,
      /**  Indicates if the submit button is enabled  */  
   "EnableSubmit":boolean,
   "TimeDisableUpdate":boolean,
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   "AllowDirLbr":boolean,
   "TimeDisableDelete":boolean,
      /**  To know if the LaborDtl was created on the current plant  */  
   "EnteredOnCurPlant":boolean,
   "EnableLaborQty":boolean,
   "PendingApprovalBy":string,
   "ApprovedBy":string,
      /**  Indicates if recall is available for an approver  */  
   "EnableRecallAprv":boolean,
      /**  This field is used to get the translated value of JobTypeCode.  */  
   "JobType":string,
      /**   Indicates the type of job. Possible values are:
MFG - Manufacture
SRV - Service
PRJ - Project
MNT - Maintenance  */  
   "JobTypeCode":string,
      /**  Used for the Labor Type grouping. A new column was needed to differentiate between records with the same Labor Type (e.g. Production and Maintenance).  */  
   "GroupByLaborType":string,
      /**  The ID of the Equipment that this "Maintenance Job" is for.  */  
   "EquipID":string,
   "BitFlag":number,
   "EmpBasicName":string,
   "ExpenseCodeDescription":string,
   "IndirectDescription":string,
   "JobAsmblDescription":string,
   "JobAsmblPartNum":string,
   "OpDescOpDesc":string,
   "PhaseIDDescription":string,
   "ProjectDescription":string,
   "ResourceGrpDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MobileLaborHedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The number of the employee that performed the work. This field is directly maintainable. A selection list is provided in labor entry to find the employee by name.  */  
   "EmployeeNum":string,
      /**  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  */  
   "LaborHedSeq":number,
      /**   The Payroll date is the "Logical Day" that labor occurred. In most cases this is the same as the "Physical Day".  But when work is done before and after midnight then "Labor Collection" rolls the physical date forward or backward to create a Logical date. This date will be used to group transactions together by a logical date in order to calculate daily overtime during the transfer to payroll.
It will also be used in the selection criteria logic during the transfer to payroll.  This is duplicated into each LaborDtl.  */  
   "PayrollDate":string,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   "Shift":number,
      /**  The clock in date of the clock in time field. It is created using the ActualDate and may be rolled forward/backward if the clock in time is adjusted across midnight. For example, when an employee clocks in prior to midnight, but shift starts at midnight or later, this situation causes the default to be ActualDateIn + 1.  */  
   "ClockInDate":string,
      /**  The clock in time to be considered for payroll and costing purposes as the time when the employee starts work. Clock in time is stored as Hours.Hundreths. It is created using the ActualClockIn value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockin" is before the shift start time (JCShift.Start) and after ( JCShift. start - JCSyst.Grace) then the system adjusts the clockin time to be the start of the shift. Else it will be set to the actual system time.  */  
   "ClockInTime":number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   "DspClockInTime":string,
      /**  Actual clock in time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocked in. In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.StartTime. Stored as Hours:Hundreths.  */  
   "ActualClockInTime":number,
      /**  The actual date at the time of clockin. Labor Collection uses the system date to create this field.  Labor entry allows entry of this field and then uses it to generate the default for the adjusted  "ClockInDate".  This field is provided mainly for audit purposes.  */  
   "ActualClockinDate":string,
      /**   An internal control byte used by Labor Collection when the system is configured not to take out lunch automatically (JCSyst.AutoLunch = N). It is used determine if what to do when the "Lunch" button is pressed.

The possible values are "N" - No lunch, "O" - Out to Lunch, "R" - Returned from lunch.  */  
   "LunchStatus":string,
      /**   Actual Clock out time for Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchStart as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time for LunchOut.  */  
   "ActLunchOutTime":number,
      /**   Clock out time for Lunch that is used for costing/payroll determination. It is created by adjusting the ActLunchOutTime. . The adjusted time is where the system time is rolled back to the JCShift.LunchStart time when the employee clocks out for lunch after it has started but before it ends.

Stored as Hours.Hundreths.  */  
   "LunchOutTime":number,
      /**   Actual Clock In  time from Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchEnd as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time.  */  
   "ActLunchInTime":number,
      /**   Clock In time from Lunch break that is used for costing/payroll determination. Created by adjusting the ActLunchInTime.
The adjusted time is where the system time is rolled forward to the JCShift.LunchEnd time when the employee clocks in from lunch before the lunch period ends. 
Stored as Hours.Hundreths.  */  
   "LunchInTime":number,
      /**  The clockOut in time to be considered for payroll and costing purposes as the time when the employee stops work. ClockOut time is stored as Hours.Hundreths. It is defaulted using the ActualClockOut value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockOut" is after the shift end time (JCShift.End) and before ( JCShift.End + JC.Syst.Grace) then the system adjusts the ClockOut time to be the end of the shift. Else it will be set to the actual system time.  */  
   "ClockOutTime":number,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   "DspClockOutTime":string,
      /**  Actual clock Out time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocks out.  In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.EndTime. Stored as Hours.Hundreths.  */  
   "ActualClockOutTime":number,
      /**   Hours for payroll.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5. This is calculated when the Start/Stop times are changed in labor entry. It can then be overridden.
The Logic for calculating hours from clockin, clockout is:
If ClockIn > ClockOut Gross Hours = ( (ClockOut + 24.00) - ClockIn) else Gross Hours = ClockOut - ClockIn. 
If LunchOut > LunchIn Lunch Hours = ( (LunchIn +24) - LunchOut )
else Lunch Hours = ( LunchIn - LunchOut ).
PayHours = GRoss Hours - Lunch Hours. 
Remember that the database clockin/clockout fields are stored as hours hundredths, while the entry widgets are either hours.hundreths or Hours:Minutes. So use the database fields in this calculation and there is no need to worry about conversions.  */  
   "PayHours":number,
      /**  Flag that indicates this labor transaction is eligible for transfer to DCD payroll application. The default is set from JCSyst.FeedPayroll.  */  
   "FeedPayroll":boolean,
      /**  Indicates if this transaction has been transferred to payroll. This is updated via the Payroll function to transfer labor.  */  
   "TransferredToPayroll":boolean,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   "LaborCollection":boolean,
      /**  An optional field where the user enters a string of characters that would be used to associate multiple transactions as being part of a transaction set. TranSet will be used for data selection type functions.  */  
   "TranSet":string,
      /**   Used by Labor collection to indicate that this LaborHed record is currently active. When the employee clocks out it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice, displaying which employees are clocked in and which ones have not clocked out. Labor entry can't access a record that is Open.  */  
   "ActiveTrans":boolean,
      /**   Encoded value PRChkDtl.HeadNum + PRChkDtl.LineNum.
Used to relate the labor to the payroll check detail.  */  
   "ChkLink":string,
      /**  BatchTotalHrsDisp  */  
   "BatchTotalHrsDisp":string,
      /**  BatchHrsRemainDisp  */  
   "BatchHrsRemainDisp":string,
      /**  BatchHrsRemainPctDisp  */  
   "BatchHrsRemainPctDisp":string,
      /**  BatchSplitHrsMethod  */  
   "BatchSplitHrsMethod":string,
      /**  BatchAssignTo  */  
   "BatchAssignTo":boolean,
      /**  BatchComplete  */  
   "BatchComplete":boolean,
      /**  BatchStartHrs  */  
   "BatchStartHrs":string,
      /**  BatchEndHrs  */  
   "BatchEndHrs":string,
      /**  BatchTotalHrs  */  
   "BatchTotalHrs":number,
      /**  BatchHrsRemain  */  
   "BatchHrsRemain":number,
      /**  BatchHrsRemainPct  */  
   "BatchHrsRemainPct":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Imported  */  
   "Imported":boolean,
      /**  ImportDate  */  
   "ImportDate":string,
      /**  BatchMode  */  
   "BatchMode":boolean,
      /**  Indicates which type of Pay time calculation will be used when HCM Integration is on.  */  
   "HCMPayHoursCalcType":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MobileLaborListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The number of the employee that performed the work. This field is directly maintainable. A selection list is provided in labor entry to find the employee by name.  */  
   "EmployeeNum":string,
      /**  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  */  
   "LaborHedSeq":number,
      /**   The Payroll date is the "Logical Day" that labor occurred. In most cases this is the same as the "Physical Day".  But when work is done before and after midnight then "Labor Collection" rolls the physical date forward or backward to create a Logical date. This date will be used to group transactions together by a logical date in order to calculate daily overtime during the transfer to payroll.
It will also be used in the selection criteria logic during the transfer to payroll.  This is duplicated into each LaborDtl.  */  
   "PayrollDate":string,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   "Shift":number,
      /**  The clock in date of the clock in time field. It is created using the ActualDate and may be rolled forward/backward if the clock in time is adjusted across midnight. For example, when an employee clocks in prior to midnight, but shift starts at midnight or later, this situation causes the default to be ActualDateIn + 1.  */  
   "ClockInDate":string,
      /**  The clock in time to be considered for payroll and costing purposes as the time when the employee starts work. Clock in time is stored as Hours.Hundreths. It is created using the ActualClockIn value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockin" is before the shift start time (JCShift.Start) and after ( JCShift. start - JCSyst.Grace) then the system adjusts the clockin time to be the start of the shift. Else it will be set to the actual system time.  */  
   "ClockInTime":number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   "DspClockInTime":string,
      /**  Actual clock in time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocked in. In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.StartTime. Stored as Hours:Hundreths.  */  
   "ActualClockInTime":number,
      /**  The actual date at the time of clockin. Labor Collection uses the system date to create this field.  Labor entry allows entry of this field and then uses it to generate the default for the adjusted  "ClockInDate".  This field is provided mainly for audit purposes.  */  
   "ActualClockinDate":string,
      /**   An internal control byte used by Labor Collection when the system is configured not to take out lunch automatically (JCSyst.AutoLunch = N). It is used determine if what to do when the "Lunch" button is pressed.

The possible values are "N" - No lunch, "O" - Out to Lunch, "R" - Returned from lunch.  */  
   "LunchStatus":string,
      /**   Actual Clock out time for Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchStart as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time for LunchOut.  */  
   "ActLunchOutTime":number,
      /**   Clock out time for Lunch that is used for costing/payroll determination. It is created by adjusting the ActLunchOutTime. . The adjusted time is where the system time is rolled back to the JCShift.LunchStart time when the employee clocks out for lunch after it has started but before it ends.

Stored as Hours.Hundreths.  */  
   "LunchOutTime":number,
      /**   Actual Clock In  time from Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchEnd as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time.  */  
   "ActLunchInTime":number,
      /**   Clock In time from Lunch break that is used for costing/payroll determination. Created by adjusting the ActLunchInTime.
The adjusted time is where the system time is rolled forward to the JCShift.LunchEnd time when the employee clocks in from lunch before the lunch period ends. 
Stored as Hours.Hundreths.  */  
   "LunchInTime":number,
      /**  The clockOut in time to be considered for payroll and costing purposes as the time when the employee stops work. ClockOut time is stored as Hours.Hundreths. It is defaulted using the ActualClockOut value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockOut" is after the shift end time (JCShift.End) and before ( JCShift.End + JC.Syst.Grace) then the system adjusts the ClockOut time to be the end of the shift. Else it will be set to the actual system time.  */  
   "ClockOutTime":number,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   "DspClockOutTime":string,
      /**  Actual clock Out time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocks out.  In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.EndTime. Stored as Hours.Hundreths.  */  
   "ActualClockOutTime":number,
      /**   Hours for payroll.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5. This is calculated when the Start/Stop times are changed in labor entry. It can then be overridden.
The Logic for calculating hours from clockin, clockout is:
If ClockIn > ClockOut Gross Hours = ( (ClockOut + 24.00) - ClockIn) else Gross Hours = ClockOut - ClockIn. 
If LunchOut > LunchIn Lunch Hours = ( (LunchIn +24) - LunchOut )
else Lunch Hours = ( LunchIn - LunchOut ).
PayHours = GRoss Hours - Lunch Hours. 
Remember that the database clockin/clockout fields are stored as hours hundredths, while the entry widgets are either hours.hundreths or Hours:Minutes. So use the database fields in this calculation and there is no need to worry about conversions.  */  
   "PayHours":number,
      /**  Flag that indicates this labor transaction is eligible for transfer to DCD payroll application. The default is set from JCSyst.FeedPayroll.  */  
   "FeedPayroll":boolean,
      /**  Indicates if this transaction has been transferred to payroll. This is updated via the Payroll function to transfer labor.  */  
   "TransferredToPayroll":boolean,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   "LaborCollection":boolean,
      /**  An optional field where the user enters a string of characters that would be used to associate multiple transactions as being part of a transaction set. TranSet will be used for data selection type functions.  */  
   "TranSet":string,
      /**   Used by Labor collection to indicate that this LaborHed record is currently active. When the employee clocks out it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice, displaying which employees are clocked in and which ones have not clocked out. Labor entry can't access a record that is Open.  */  
   "ActiveTrans":boolean,
      /**   Encoded value PRChkDtl.HeadNum + PRChkDtl.LineNum.
Used to relate the labor to the payroll check detail.  */  
   "ChkLink":string,
      /**  BatchTotalHrsDisp  */  
   "BatchTotalHrsDisp":string,
      /**  BatchHrsRemainDisp  */  
   "BatchHrsRemainDisp":string,
      /**  BatchHrsRemainPctDisp  */  
   "BatchHrsRemainPctDisp":string,
      /**  BatchSplitHrsMethod  */  
   "BatchSplitHrsMethod":string,
      /**  BatchAssignTo  */  
   "BatchAssignTo":boolean,
      /**  BatchComplete  */  
   "BatchComplete":boolean,
      /**  BatchStartHrs  */  
   "BatchStartHrs":string,
      /**  BatchEndHrs  */  
   "BatchEndHrs":string,
      /**  BatchTotalHrs  */  
   "BatchTotalHrs":number,
      /**  BatchHrsRemain  */  
   "BatchHrsRemain":number,
      /**  BatchHrsRemainPct  */  
   "BatchHrsRemainPct":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Imported  */  
   "Imported":boolean,
      /**  ImportDate  */  
   "ImportDate":string,
      /**  BatchMode  */  
   "BatchMode":boolean,
      /**  Indicates which type of Pay time calculation will be used when HCM Integration is on.  */  
   "HCMPayHoursCalcType":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MobileQuickEntryViewRow{
   "AssemblySeq":number,
   "Company":string,
   "EmpID":string,
   "ExpenseCode":string,
   "IndirectCode":string,
   "JobNum":string,
      /**   Indicates the type of job. Possible values are:
MFG - Manufacture
SRV - Service
PRJ - Project
MNT - Maintenance  */  
   "JobTypeCode":string,
   "LaborHrs":number,
   "LaborType":string,
   "LaborTypePseudo":string,
   "OpCode":string,
      /**  Operation Description  */  
   "OperDesc":string,
   "OprSeq":number,
   "PhaseID":string,
   "ProjectID":string,
   "QuickEntryCode":string,
   "ResourceGrpID":string,
   "ResourceID":string,
   "RoleCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MobileTimeWeeklyViewRow{
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   "AllowDirLbr":boolean,
      /**  Job Assembly description  */  
   "ASMdesc":string,
   "AssemblySeq":number,
   "Company":string,
   "Complete":boolean,
   "DeleteRow":boolean,
   "DisLaborType":boolean,
   "DisPrjRoleCd":boolean,
   "DisTimeTypCd":boolean,
   "EmployeeNum":string,
      /**  Indicates if the copy function is available  */  
   "EnableCopy":boolean,
      /**  Indicates if recall is available  */  
   "EnableRecall":boolean,
      /**  Indicates if submit is available  */  
   "EnableSubmit":boolean,
   "ExpenseCode":string,
   "ExpenseCodeDescription":string,
      /**  HCM Integration Total Weekly Pay Hours  */  
   "HCMTotWeeklyPayHours":number,
   "HoursFri":number,
   "HoursMon":number,
   "HoursSat":number,
   "HoursSun":number,
   "HoursThu":number,
   "HoursTotal":number,
   "HoursTue":number,
   "HoursWed":number,
   "IndirectCode":string,
   "IndirectCodeDescription":string,
   "JCDept":string,
   "JobNum":string,
   "LaborEntryMethod":string,
   "LaborRate":number,
   "LaborType":string,
   "LaborTypePseudo":string,
   "MessageText":string,
      /**  Valid values are "A" for an Add of a new TimeWeeklyView row and "C" for a Copy of an existing TimeWeeklyView row.  */  
   "NewRowType":string,
   "OpCode":string,
   "OpComplete":boolean,
      /**  Operation Description  */  
   "OperDesc":string,
   "OprSeq":number,
   "PhaseID":string,
   "PhaseIDDescription":string,
   "ProjDesc":string,
   "ProjectID":string,
   "QuickEntryCode":string,
   "ResourceGrpID":string,
   "ResourceGrpIDDescription":string,
   "ResourceID":string,
   "ResourceIDDescription":string,
   "RoleCd":string,
   "RoleCdDescription":string,
   "Shift":number,
   "ShiftDescription":string,
      /**   If the Time is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  */  
   "TimeAutoSubmit":boolean,
   "TimeDisableUpdate":boolean,
   "TimeStatus":string,
   "TimeTypCd":string,
   "TimeTypCdDescription":string,
      /**  WBS Phase Project Description  */  
   "WBSPhaseDesc":string,
   "WeekBeginDate":string,
   "WeekDisplayText":string,
   "WeekEndDate":string,
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
      @param salesRepCode
      @param action
      @param comment
      @param ds
   */  
export interface ApproveReject_input{
      /**  The sales Rep Code of the approver.  */  
   salesRepCode:string,
      /**  Action to take A = approver, R = reject.  */  
   action:string,
      /**  Comment text if comments are to be created.  */  
   comment:string,
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface ApproveReject_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   outMessage:string,
}
}

   /** Required : 
      @param salesRepCode
      @param ds
   */  
export interface CheckRecall_input{
      /**  The sales Rep Code of the approver.  */  
   salesRepCode:string,
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface CheckRecall_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   outRecallMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CopyLaborDetail_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface CopyLaborDetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   messageText:string,
}
}

   /** Required : 
      @param laborHedSeq
   */  
export interface DeleteByID_input{
   laborHedSeq:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_MobileApproverListRow{
      /**  The status of the current approval task.  */  
   ApprovalStatus:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Date when the approval task was completed.  */  
   CompleteDate:string,
      /**  Major component of the foreign key of the related master record. For a task related to an Expense this field would contain the related EmployeeID. For a task related to Labor this field would contain the related LaborHed.  */  
   Key1:string,
      /**  Second component of the foreign key to the related master record. For a task related to an Expense, this field would contain the related ExpenseID. For a task related to Labor, this field would contain the related LaborDtl.  */  
   Key2:string,
      /**  The master file to which the task is related.  */  
   RelatedToFile:string,
      /**  The SalesRep that this task is assigned to.  */  
   SalesRepCode:string,
      /**  Name corresponding to the SalesRepCode.  */  
   SalesRepName:string,
      /**  Number used to display the records in their correct sequence in the mobile app.  */  
   SequenceNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileLaborDtlAttchRow{
   Company:string,
   LaborHedSeq:number,
   LaborDtlSeq:number,
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

export interface Erp_Tablesets_MobileLaborDtlCommentRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the Labor Header the comment relates to.  */  
   LaborHedSeq:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**  Internal identifier of the comment record.  Used in conjunction with EmpTimeNum to make the record unique.  */  
   CommentNum:number,
      /**   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  */  
   CommentType:string,
      /**  The comment text.  */  
   CommentText:string,
      /**  Userid of the user who created the record.  */  
   CreatedBy:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date the record was last changed.  */  
   ChangeDate:string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   ChangeTime:number,
      /**  The identifier of the Task record the comment is related to.  Can be zero, which indicates the comment is not related to a specific task.  */  
   TaskSeqNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileLaborDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   EmployeeNum:string,
      /**  Used as the foreign key to the LaborHed record.  */  
   LaborHedSeq:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   LaborType:string,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   LaborTypePseudo:string,
      /**  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  */  
   ReWork:boolean,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  */  
   ReworkReasonCode:string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   JobNum:string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   AssemblySeq:number,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   OprSeq:number,
      /**  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  */  
   JCDept:string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   ResourceGrpID:string,
      /**  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  */  
   OpCode:string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   LaborHrs:number,
      /**  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  */  
   BurdenHrs:number,
      /**  The Total production quantity reported.  */  
   LaborQty:number,
      /**  The reported scrap quantity.  */  
   ScrapQty:number,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  */  
   ScrapReasonCode:string,
      /**  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  */  
   SetupPctComplete:number,
      /**  Indicates if this transaction "completes" either the setup or production for this operation.  */  
   Complete:boolean,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   IndirectCode:string,
      /**  A short note that the user can make about the labor transaction.  */  
   LaborNote:string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   ExpenseCode:string,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   LaborCollection:boolean,
      /**  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  */  
   AppliedToSchedule:boolean,
      /**  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  */  
   ClockInMInute:number,
      /**  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  */  
   ClockOutMinute:number,
      /**  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  */  
   ClockInDate:string,
      /**   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  */  
   ClockinTime:number,
      /**   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  */  
   ClockOutTime:number,
      /**   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  */  
   ActiveTrans:boolean,
      /**  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  */  
   OverRidePayRate:number,
      /**  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  */  
   LaborRate:number,
      /**  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  */  
   BurdenRate:number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockInTime:string,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockOutTime:string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   ResourceID:string,
      /**  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  */  
   OpComplete:boolean,
      /**  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  */  
   EarnedHrs:number,
      /**  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  */  
   AddedOper:boolean,
      /**  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  */  
   PayrollDate:string,
      /**   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  */  
   PostedToGL:boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  */  
   GLTrans:boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Indicates if the labordtl record inspection has completed.  */  
   InspectionPending:boolean,
      /**  The service call that this service record belongs to.  */  
   CallNum:number,
      /**  The line number of the service call this labor detail is for.  */  
   CallLine:number,
      /**  the service that is being performed on this line.  */  
   ServNum:number,
      /**  A unique code that identifies the Service  */  
   ServCode:string,
      /**  Problem reason code from the reason master table. type Service call.  */  
   ResReasonCode:string,
      /**  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  */  
   WipPosted:boolean,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   DiscrepQty:number,
      /**   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  */  
   DiscrpRsnCode:string,
      /**  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  */  
   ParentLaborDtlSeq:number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  */  
   LaborEntryMethod:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  */  
   BFLaborReq:boolean,
      /**  Reference to the ABT, it is GUID,used in PostingEngine  */  
   ABTUID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Project Role Code  */  
   RoleCd:string,
      /**  Time Type Code  */  
   TimeTypCd:string,
      /**  The Project Billing Invoice Number where these charges were processed.  */  
   PBInvNum:number,
      /**  The payment method of the time.  */  
   PMUID:number,
      /**  Link to Task set  */  
   TaskSetID:string,
      /**  The date the time received final approval.  */  
   ApprovedDate:string,
      /**  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   ClaimRef:string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  */  
   QuickEntryCode:string,
      /**   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   TimeStatus:string,
      /**  Userid of the user who created the record.  */  
   CreatedBy:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date the record was last changed.  */  
   ChangeDate:string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   ChangeTime:number,
      /**  The Currently active Stage changing task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  */  
   CreatedViaTEWeekView:boolean,
      /**  The identifier of the workflow stage.  */  
   CurrentWFStageID:string,
      /**  The identifier of the workflow group  */  
   WFGroupID:string,
      /**  This indicates if the workflow for this group is complete.  */  
   WFComplete:boolean,
      /**  Indicates if approval is required for this transaction.  */  
   ApprovalRequired:boolean,
      /**  The User ID of the submitter.  */  
   SubmittedBy:string,
      /**  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  */  
   PBRateFrom:string,
      /**  Project Billing calculation in COSandWIP: Currency code is got from Project  */  
   PBCurrencyCode:string,
      /**  Project Billing calculation in COSandWIP: Hours used for charge  */  
   PBHours:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  */  
   PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  */  
   PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  */  
   DocPBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt1PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt2PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt3PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  */  
   DocPBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt1PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt2PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt3PBChargeAmt:number,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   Shift:number,
      /**  Links to PActDtl.ActID  */  
   ActID:number,
      /**  System assigned unique id number for the detail. Links to PActDtl.DetailID  */  
   DtailID:number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   ProjProcessed:boolean,
      /**  Used By Project Analysis Process.  */  
   AsOfDate:string,
      /**  Used By Project Analysis Process.  */  
   AsOfSeq:number,
      /**  JDFInputFiles  */  
   JDFInputFiles:string,
      /**  JDFNumberOfPages  */  
   JDFNumberOfPages:string,
      /**  BatchWasSaved  */  
   BatchWasSaved:string,
      /**  AssignToBatch  */  
   AssignToBatch:boolean,
      /**  BatchComplete  */  
   BatchComplete:boolean,
      /**  BatchRequestMove  */  
   BatchRequestMove:boolean,
      /**  BatchPrint  */  
   BatchPrint:boolean,
      /**  BatchLaborHrs  */  
   BatchLaborHrs:number,
      /**  BatchPctOfTotHrs  */  
   BatchPctOfTotHrs:number,
      /**  BatchQty  */  
   BatchQty:number,
      /**  BatchTotalExpectedHrs  */  
   BatchTotalExpectedHrs:number,
      /**  JDFOpCompleted  */  
   JDFOpCompleted:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Downtime  */  
   Downtime:boolean,
      /**  RefJobNum  */  
   RefJobNum:string,
      /**  RefAssemblySeq  */  
   RefAssemblySeq:number,
      /**  RefOprSeq  */  
   RefOprSeq:number,
      /**  Imported  */  
   Imported:boolean,
      /**  ImportDate  */  
   ImportDate:string,
      /**   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  */  
   TimeAutoSubmit:boolean,
      /**  BatchMode  */  
   BatchMode:boolean,
      /**  BillServiceRate  */  
   BillServiceRate:number,
      /**  Pay Hours used for HCM  */  
   HCMPayHours:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  Indicates if the labor detail has attachments  */  
   HasAttachments:boolean,
      /**  Indicates if the labor detail has comments  */  
   HasComments:boolean,
   EnableComplete:boolean,
      /**  Indicates if the copy button is enabled  */  
   EnableCopy:boolean,
      /**  Indicates if the recall button is enabled  */  
   EnableRecall:boolean,
      /**  Indicates if the submit button is enabled  */  
   EnableSubmit:boolean,
   TimeDisableUpdate:boolean,
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   AllowDirLbr:boolean,
   TimeDisableDelete:boolean,
      /**  To know if the LaborDtl was created on the current plant  */  
   EnteredOnCurPlant:boolean,
   EnableLaborQty:boolean,
   PendingApprovalBy:string,
   ApprovedBy:string,
      /**  Indicates if recall is available for an approver  */  
   EnableRecallAprv:boolean,
      /**  This field is used to get the translated value of JobTypeCode.  */  
   JobType:string,
      /**   Indicates the type of job. Possible values are:
MFG - Manufacture
SRV - Service
PRJ - Project
MNT - Maintenance  */  
   JobTypeCode:string,
      /**  Used for the Labor Type grouping. A new column was needed to differentiate between records with the same Labor Type (e.g. Production and Maintenance).  */  
   GroupByLaborType:string,
      /**  The ID of the Equipment that this "Maintenance Job" is for.  */  
   EquipID:string,
   BitFlag:number,
   EmpBasicName:string,
   ExpenseCodeDescription:string,
   IndirectDescription:string,
   JobAsmblDescription:string,
   JobAsmblPartNum:string,
   OpDescOpDesc:string,
   PhaseIDDescription:string,
   ProjectDescription:string,
   ResourceGrpDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileLaborHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The number of the employee that performed the work. This field is directly maintainable. A selection list is provided in labor entry to find the employee by name.  */  
   EmployeeNum:string,
      /**  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  */  
   LaborHedSeq:number,
      /**   The Payroll date is the "Logical Day" that labor occurred. In most cases this is the same as the "Physical Day".  But when work is done before and after midnight then "Labor Collection" rolls the physical date forward or backward to create a Logical date. This date will be used to group transactions together by a logical date in order to calculate daily overtime during the transfer to payroll.
It will also be used in the selection criteria logic during the transfer to payroll.  This is duplicated into each LaborDtl.  */  
   PayrollDate:string,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   Shift:number,
      /**  The clock in date of the clock in time field. It is created using the ActualDate and may be rolled forward/backward if the clock in time is adjusted across midnight. For example, when an employee clocks in prior to midnight, but shift starts at midnight or later, this situation causes the default to be ActualDateIn + 1.  */  
   ClockInDate:string,
      /**  The clock in time to be considered for payroll and costing purposes as the time when the employee starts work. Clock in time is stored as Hours.Hundreths. It is created using the ActualClockIn value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockin" is before the shift start time (JCShift.Start) and after ( JCShift. start - JCSyst.Grace) then the system adjusts the clockin time to be the start of the shift. Else it will be set to the actual system time.  */  
   ClockInTime:number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockInTime:string,
      /**  Actual clock in time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocked in. In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.StartTime. Stored as Hours:Hundreths.  */  
   ActualClockInTime:number,
      /**  The actual date at the time of clockin. Labor Collection uses the system date to create this field.  Labor entry allows entry of this field and then uses it to generate the default for the adjusted  "ClockInDate".  This field is provided mainly for audit purposes.  */  
   ActualClockinDate:string,
      /**   An internal control byte used by Labor Collection when the system is configured not to take out lunch automatically (JCSyst.AutoLunch = N). It is used determine if what to do when the "Lunch" button is pressed.

The possible values are "N" - No lunch, "O" - Out to Lunch, "R" - Returned from lunch.  */  
   LunchStatus:string,
      /**   Actual Clock out time for Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchStart as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time for LunchOut.  */  
   ActLunchOutTime:number,
      /**   Clock out time for Lunch that is used for costing/payroll determination. It is created by adjusting the ActLunchOutTime. . The adjusted time is where the system time is rolled back to the JCShift.LunchStart time when the employee clocks out for lunch after it has started but before it ends.

Stored as Hours.Hundreths.  */  
   LunchOutTime:number,
      /**   Actual Clock In  time from Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchEnd as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time.  */  
   ActLunchInTime:number,
      /**   Clock In time from Lunch break that is used for costing/payroll determination. Created by adjusting the ActLunchInTime.
The adjusted time is where the system time is rolled forward to the JCShift.LunchEnd time when the employee clocks in from lunch before the lunch period ends. 
Stored as Hours.Hundreths.  */  
   LunchInTime:number,
      /**  The clockOut in time to be considered for payroll and costing purposes as the time when the employee stops work. ClockOut time is stored as Hours.Hundreths. It is defaulted using the ActualClockOut value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockOut" is after the shift end time (JCShift.End) and before ( JCShift.End + JC.Syst.Grace) then the system adjusts the ClockOut time to be the end of the shift. Else it will be set to the actual system time.  */  
   ClockOutTime:number,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockOutTime:string,
      /**  Actual clock Out time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocks out.  In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.EndTime. Stored as Hours.Hundreths.  */  
   ActualClockOutTime:number,
      /**   Hours for payroll.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5. This is calculated when the Start/Stop times are changed in labor entry. It can then be overridden.
The Logic for calculating hours from clockin, clockout is:
If ClockIn > ClockOut Gross Hours = ( (ClockOut + 24.00) - ClockIn) else Gross Hours = ClockOut - ClockIn. 
If LunchOut > LunchIn Lunch Hours = ( (LunchIn +24) - LunchOut )
else Lunch Hours = ( LunchIn - LunchOut ).
PayHours = GRoss Hours - Lunch Hours. 
Remember that the database clockin/clockout fields are stored as hours hundredths, while the entry widgets are either hours.hundreths or Hours:Minutes. So use the database fields in this calculation and there is no need to worry about conversions.  */  
   PayHours:number,
      /**  Flag that indicates this labor transaction is eligible for transfer to DCD payroll application. The default is set from JCSyst.FeedPayroll.  */  
   FeedPayroll:boolean,
      /**  Indicates if this transaction has been transferred to payroll. This is updated via the Payroll function to transfer labor.  */  
   TransferredToPayroll:boolean,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   LaborCollection:boolean,
      /**  An optional field where the user enters a string of characters that would be used to associate multiple transactions as being part of a transaction set. TranSet will be used for data selection type functions.  */  
   TranSet:string,
      /**   Used by Labor collection to indicate that this LaborHed record is currently active. When the employee clocks out it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice, displaying which employees are clocked in and which ones have not clocked out. Labor entry can't access a record that is Open.  */  
   ActiveTrans:boolean,
      /**   Encoded value PRChkDtl.HeadNum + PRChkDtl.LineNum.
Used to relate the labor to the payroll check detail.  */  
   ChkLink:string,
      /**  BatchTotalHrsDisp  */  
   BatchTotalHrsDisp:string,
      /**  BatchHrsRemainDisp  */  
   BatchHrsRemainDisp:string,
      /**  BatchHrsRemainPctDisp  */  
   BatchHrsRemainPctDisp:string,
      /**  BatchSplitHrsMethod  */  
   BatchSplitHrsMethod:string,
      /**  BatchAssignTo  */  
   BatchAssignTo:boolean,
      /**  BatchComplete  */  
   BatchComplete:boolean,
      /**  BatchStartHrs  */  
   BatchStartHrs:string,
      /**  BatchEndHrs  */  
   BatchEndHrs:string,
      /**  BatchTotalHrs  */  
   BatchTotalHrs:number,
      /**  BatchHrsRemain  */  
   BatchHrsRemain:number,
      /**  BatchHrsRemainPct  */  
   BatchHrsRemainPct:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Imported  */  
   Imported:boolean,
      /**  ImportDate  */  
   ImportDate:string,
      /**  BatchMode  */  
   BatchMode:boolean,
      /**  Indicates which type of Pay time calculation will be used when HCM Integration is on.  */  
   HCMPayHoursCalcType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileLaborListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The number of the employee that performed the work. This field is directly maintainable. A selection list is provided in labor entry to find the employee by name.  */  
   EmployeeNum:string,
      /**  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  */  
   LaborHedSeq:number,
      /**   The Payroll date is the "Logical Day" that labor occurred. In most cases this is the same as the "Physical Day".  But when work is done before and after midnight then "Labor Collection" rolls the physical date forward or backward to create a Logical date. This date will be used to group transactions together by a logical date in order to calculate daily overtime during the transfer to payroll.
It will also be used in the selection criteria logic during the transfer to payroll.  This is duplicated into each LaborDtl.  */  
   PayrollDate:string,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   Shift:number,
      /**  The clock in date of the clock in time field. It is created using the ActualDate and may be rolled forward/backward if the clock in time is adjusted across midnight. For example, when an employee clocks in prior to midnight, but shift starts at midnight or later, this situation causes the default to be ActualDateIn + 1.  */  
   ClockInDate:string,
      /**  The clock in time to be considered for payroll and costing purposes as the time when the employee starts work. Clock in time is stored as Hours.Hundreths. It is created using the ActualClockIn value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockin" is before the shift start time (JCShift.Start) and after ( JCShift. start - JCSyst.Grace) then the system adjusts the clockin time to be the start of the shift. Else it will be set to the actual system time.  */  
   ClockInTime:number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockInTime:string,
      /**  Actual clock in time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocked in. In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.StartTime. Stored as Hours:Hundreths.  */  
   ActualClockInTime:number,
      /**  The actual date at the time of clockin. Labor Collection uses the system date to create this field.  Labor entry allows entry of this field and then uses it to generate the default for the adjusted  "ClockInDate".  This field is provided mainly for audit purposes.  */  
   ActualClockinDate:string,
      /**   An internal control byte used by Labor Collection when the system is configured not to take out lunch automatically (JCSyst.AutoLunch = N). It is used determine if what to do when the "Lunch" button is pressed.

The possible values are "N" - No lunch, "O" - Out to Lunch, "R" - Returned from lunch.  */  
   LunchStatus:string,
      /**   Actual Clock out time for Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchStart as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time for LunchOut.  */  
   ActLunchOutTime:number,
      /**   Clock out time for Lunch that is used for costing/payroll determination. It is created by adjusting the ActLunchOutTime. . The adjusted time is where the system time is rolled back to the JCShift.LunchStart time when the employee clocks out for lunch after it has started but before it ends.

Stored as Hours.Hundreths.  */  
   LunchOutTime:number,
      /**   Actual Clock In  time from Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchEnd as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time.  */  
   ActLunchInTime:number,
      /**   Clock In time from Lunch break that is used for costing/payroll determination. Created by adjusting the ActLunchInTime.
The adjusted time is where the system time is rolled forward to the JCShift.LunchEnd time when the employee clocks in from lunch before the lunch period ends. 
Stored as Hours.Hundreths.  */  
   LunchInTime:number,
      /**  The clockOut in time to be considered for payroll and costing purposes as the time when the employee stops work. ClockOut time is stored as Hours.Hundreths. It is defaulted using the ActualClockOut value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockOut" is after the shift end time (JCShift.End) and before ( JCShift.End + JC.Syst.Grace) then the system adjusts the ClockOut time to be the end of the shift. Else it will be set to the actual system time.  */  
   ClockOutTime:number,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockOutTime:string,
      /**  Actual clock Out time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocks out.  In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.EndTime. Stored as Hours.Hundreths.  */  
   ActualClockOutTime:number,
      /**   Hours for payroll.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5. This is calculated when the Start/Stop times are changed in labor entry. It can then be overridden.
The Logic for calculating hours from clockin, clockout is:
If ClockIn > ClockOut Gross Hours = ( (ClockOut + 24.00) - ClockIn) else Gross Hours = ClockOut - ClockIn. 
If LunchOut > LunchIn Lunch Hours = ( (LunchIn +24) - LunchOut )
else Lunch Hours = ( LunchIn - LunchOut ).
PayHours = GRoss Hours - Lunch Hours. 
Remember that the database clockin/clockout fields are stored as hours hundredths, while the entry widgets are either hours.hundreths or Hours:Minutes. So use the database fields in this calculation and there is no need to worry about conversions.  */  
   PayHours:number,
      /**  Flag that indicates this labor transaction is eligible for transfer to DCD payroll application. The default is set from JCSyst.FeedPayroll.  */  
   FeedPayroll:boolean,
      /**  Indicates if this transaction has been transferred to payroll. This is updated via the Payroll function to transfer labor.  */  
   TransferredToPayroll:boolean,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   LaborCollection:boolean,
      /**  An optional field where the user enters a string of characters that would be used to associate multiple transactions as being part of a transaction set. TranSet will be used for data selection type functions.  */  
   TranSet:string,
      /**   Used by Labor collection to indicate that this LaborHed record is currently active. When the employee clocks out it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice, displaying which employees are clocked in and which ones have not clocked out. Labor entry can't access a record that is Open.  */  
   ActiveTrans:boolean,
      /**   Encoded value PRChkDtl.HeadNum + PRChkDtl.LineNum.
Used to relate the labor to the payroll check detail.  */  
   ChkLink:string,
      /**  BatchTotalHrsDisp  */  
   BatchTotalHrsDisp:string,
      /**  BatchHrsRemainDisp  */  
   BatchHrsRemainDisp:string,
      /**  BatchHrsRemainPctDisp  */  
   BatchHrsRemainPctDisp:string,
      /**  BatchSplitHrsMethod  */  
   BatchSplitHrsMethod:string,
      /**  BatchAssignTo  */  
   BatchAssignTo:boolean,
      /**  BatchComplete  */  
   BatchComplete:boolean,
      /**  BatchStartHrs  */  
   BatchStartHrs:string,
      /**  BatchEndHrs  */  
   BatchEndHrs:string,
      /**  BatchTotalHrs  */  
   BatchTotalHrs:number,
      /**  BatchHrsRemain  */  
   BatchHrsRemain:number,
      /**  BatchHrsRemainPct  */  
   BatchHrsRemainPct:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Imported  */  
   Imported:boolean,
      /**  ImportDate  */  
   ImportDate:string,
      /**  BatchMode  */  
   BatchMode:boolean,
      /**  Indicates which type of Pay time calculation will be used when HCM Integration is on.  */  
   HCMPayHoursCalcType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileLaborListTableset{
   MobileLaborList:Erp_Tablesets_MobileLaborListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MobileLaborTableset{
   MobileLaborHed:Erp_Tablesets_MobileLaborHedRow[],
   MobileLaborDtl:Erp_Tablesets_MobileLaborDtlRow[],
   MobileLaborDtlAttch:Erp_Tablesets_MobileLaborDtlAttchRow[],
   MobileLaborDtlComment:Erp_Tablesets_MobileLaborDtlCommentRow[],
   MobileApproverList:Erp_Tablesets_MobileApproverListRow[],
   MobileQuickEntryView:Erp_Tablesets_MobileQuickEntryViewRow[],
   MobileTimeWeeklyView:Erp_Tablesets_MobileTimeWeeklyViewRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MobileQuickEntryViewRow{
   AssemblySeq:number,
   Company:string,
   EmpID:string,
   ExpenseCode:string,
   IndirectCode:string,
   JobNum:string,
      /**   Indicates the type of job. Possible values are:
MFG - Manufacture
SRV - Service
PRJ - Project
MNT - Maintenance  */  
   JobTypeCode:string,
   LaborHrs:number,
   LaborType:string,
   LaborTypePseudo:string,
   OpCode:string,
      /**  Operation Description  */  
   OperDesc:string,
   OprSeq:number,
   PhaseID:string,
   ProjectID:string,
   QuickEntryCode:string,
   ResourceGrpID:string,
   ResourceID:string,
   RoleCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileTimeWeeklyViewRow{
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   AllowDirLbr:boolean,
      /**  Job Assembly description  */  
   ASMdesc:string,
   AssemblySeq:number,
   Company:string,
   Complete:boolean,
   DeleteRow:boolean,
   DisLaborType:boolean,
   DisPrjRoleCd:boolean,
   DisTimeTypCd:boolean,
   EmployeeNum:string,
      /**  Indicates if the copy function is available  */  
   EnableCopy:boolean,
      /**  Indicates if recall is available  */  
   EnableRecall:boolean,
      /**  Indicates if submit is available  */  
   EnableSubmit:boolean,
   ExpenseCode:string,
   ExpenseCodeDescription:string,
      /**  HCM Integration Total Weekly Pay Hours  */  
   HCMTotWeeklyPayHours:number,
   HoursFri:number,
   HoursMon:number,
   HoursSat:number,
   HoursSun:number,
   HoursThu:number,
   HoursTotal:number,
   HoursTue:number,
   HoursWed:number,
   IndirectCode:string,
   IndirectCodeDescription:string,
   JCDept:string,
   JobNum:string,
   LaborEntryMethod:string,
   LaborRate:number,
   LaborType:string,
   LaborTypePseudo:string,
   MessageText:string,
      /**  Valid values are "A" for an Add of a new TimeWeeklyView row and "C" for a Copy of an existing TimeWeeklyView row.  */  
   NewRowType:string,
   OpCode:string,
   OpComplete:boolean,
      /**  Operation Description  */  
   OperDesc:string,
   OprSeq:number,
   PhaseID:string,
   PhaseIDDescription:string,
   ProjDesc:string,
   ProjectID:string,
   QuickEntryCode:string,
   ResourceGrpID:string,
   ResourceGrpIDDescription:string,
   ResourceID:string,
   ResourceIDDescription:string,
   RoleCd:string,
   RoleCdDescription:string,
   Shift:number,
   ShiftDescription:string,
      /**   If the Time is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  */  
   TimeAutoSubmit:boolean,
   TimeDisableUpdate:boolean,
   TimeStatus:string,
   TimeTypCd:string,
   TimeTypCdDescription:string,
      /**  WBS Phase Project Description  */  
   WBSPhaseDesc:string,
   WeekBeginDate:string,
   WeekDisplayText:string,
   WeekEndDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtMobileLaborTableset{
   MobileLaborHed:Erp_Tablesets_MobileLaborHedRow[],
   MobileLaborDtl:Erp_Tablesets_MobileLaborDtlRow[],
   MobileLaborDtlAttch:Erp_Tablesets_MobileLaborDtlAttchRow[],
   MobileLaborDtlComment:Erp_Tablesets_MobileLaborDtlCommentRow[],
   MobileApproverList:Erp_Tablesets_MobileApproverListRow[],
   MobileQuickEntryView:Erp_Tablesets_MobileQuickEntryViewRow[],
   MobileTimeWeeklyView:Erp_Tablesets_MobileTimeWeeklyViewRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param laborHedSeq
   */  
export interface GetByID_input{
   laborHedSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_MobileLaborTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_MobileLaborTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_MobileLaborTableset[],
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
   returnObj:Erp_Tablesets_MobileLaborListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetMobileLaborDtlAttchs_input{
      /**  Labor Header Seq  */  
   laborHedSeq:number,
      /**  Labor Detail Seq  */  
   laborDtlSeq:number,
}

export interface GetMobileLaborDtlAttchs_output{
   returnObj:Erp_Tablesets_MobileLaborTableset[],
}

   /** Required : 
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetMobileLaborDtlComments_input{
      /**  Labor Header Seq  */  
   laborHedSeq:number,
      /**  Labor Detail Seq  */  
   laborDtlSeq:number,
}

export interface GetMobileLaborDtlComments_output{
   returnObj:Erp_Tablesets_MobileLaborTableset[],
}

   /** Required : 
      @param ds
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetNewMobileLaborDtlAttch_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
   laborHedSeq:number,
   laborDtlSeq:number,
}

export interface GetNewMobileLaborDtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetNewMobileLaborDtlComment_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
   laborHedSeq:number,
   laborDtlSeq:number,
}

export interface GetNewMobileLaborDtlComment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
   */  
export interface GetNewMobileLaborDtl_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
   laborHedSeq:number,
}

export interface GetNewMobileLaborDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewMobileLaborHed_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface GetNewMobileLaborHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param whereClauseMobileLaborHed
      @param whereClauseMobileLaborDtl
      @param whereClauseMobileLaborDtlAttch
      @param whereClauseMobileLaborDtlComment
      @param whereClauseMobileApproverList
      @param whereClauseMobileQuickEntryView
      @param whereClauseMobileTimeWeeklyView
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseMobileLaborHed:string,
   whereClauseMobileLaborDtl:string,
   whereClauseMobileLaborDtlAttch:string,
   whereClauseMobileLaborDtlComment:string,
   whereClauseMobileApproverList:string,
   whereClauseMobileQuickEntryView:string,
   whereClauseMobileTimeWeeklyView:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_MobileLaborTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetVersion_output{
   returnObj:string,
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
      @param docTypeID
      @param parentTable
      @param fileName
      @param data
      @param metadata
   */  
export interface MobileAttachmentUpdate_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Document Type ID  */  
   docTypeID:string,
      /**  Parent Table e.g. LaborDtl  */  
   parentTable:string,
      /**  Physical name of the file  */  
   fileName:string,
      /**  Array of bytes representing the data of the attachment  */  
   data:string,
      /**  Metadata  */  
   metadata:any,      //schema had no properties on an object.
}

export interface MobileAttachmentUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param equipID
      @param ds
   */  
export interface MobileChangeEquipID_input{
      /**  The new equipID  */  
   equipID:string,
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface MobileChangeEquipID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface MobileChangeIndirectCode_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface MobileChangeIndirectCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface MobileChangeLaborType_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface MobileChangeLaborType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param pcResourceID
   */  
export interface MobileChangeResourceId_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  The ID of the machine that was used to do the work  */  
   pcResourceID:string,
}

export interface MobileChangeResourceId_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   pcMsg:string,
}
}

   /** Required : 
      @param ds
      @param ProposedResourceID
   */  
export interface MobileCheckResourceGroup_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Proposed Resource ID  */  
   ProposedResourceID:string,
}

export interface MobileCheckResourceGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface MobileCheckWarnings_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface MobileCheckWarnings_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface MobileDefaultDtlTime_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface MobileDefaultDtlTime_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param indirectCode
   */  
export interface MobileDefaultIndirect_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Proposed change to the indirect code  */  
   indirectCode:string,
}

export interface MobileDefaultIndirect_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param jobNum
   */  
export interface MobileDefaultJobNum_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Proposed change to the JobNum field  */  
   jobNum:string,
}

export interface MobileDefaultJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborHrs
   */  
export interface MobileDefaultLaborHrs_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Proposed Labor Hrs change  */  
   laborHrs:number,
}

export interface MobileDefaultLaborHrs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborQty
   */  
export interface MobileDefaultLaborQty_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Proposed change to LaborQty field  */  
   laborQty:number,
}

export interface MobileDefaultLaborQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param ipLaborType
   */  
export interface MobileDefaultLaborType_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Proposed LaborType change  */  
   ipLaborType:string,
}

export interface MobileDefaultLaborType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param oprSeq
   */  
export interface MobileDefaultOprSeq_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Proposed PhaseOprSeq change  */  
   oprSeq:number,
}

export interface MobileDefaultOprSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param ipPhaseID
   */  
export interface MobileDefaultPhaseID_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Proposed value for ipPhaseID  */  
   ipPhaseID:string,
}

export interface MobileDefaultPhaseID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param idPhaseOprSeq
   */  
export interface MobileDefaultPhaseOprSeq_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Proposed PhaseOprSeq change  */  
   idPhaseOprSeq:number,
}

export interface MobileDefaultPhaseOprSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param LaborHedSeq
      @param LaborDtlSeq
      @param CallFrom
   */  
export interface MobileDeleteLaborDtl_input{
      /**  The LaborHedSeq value for the record to be deleted  */  
   LaborHedSeq:number,
      /**  The LaborDtlSeq value for the record to be deleted  */  
   LaborDtlSeq:number,
      /**  Indicates where this method is called from  */  
   CallFrom:string,
}

export interface MobileDeleteLaborDtl_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface MobileDelete_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface MobileDelete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param key1
      @param key2
      @param approvedBy
      @param pendingApprovalBy
   */  
export interface MobileGetApprovalStatus_input{
   key1:string,
   key2:string,
   approvedBy:string,
   pendingApprovalBy:string,
}

export interface MobileGetApprovalStatus_output{
   returnObj:Erp_Tablesets_MobileLaborTableset[],
}

   /** Required : 
      @param laborHedSeq
   */  
export interface MobileGetByID_input{
      /**  The LaborHed seq value for which the LaborHed record is returned.  */  
   laborHedSeq:number,
}

export interface MobileGetByID_output{
   returnObj:Erp_Tablesets_MobileLaborTableset[],
}

   /** Required : 
      @param employeeID
      @param salesRepCode
      @param numberOfDays
   */  
export interface MobileGetHomePageData_input{
   employeeID:string,
   salesRepCode:string,
   numberOfDays:number,
}

export interface MobileGetHomePageData_output{
parameters : {
      /**  output parameters  */  
   entered:number,
   submitted:number,
   approved:number,
   rejected:number,
   forApproval:number,
   oldestRecordDate:string,
   enteredHours:number,
   submittedHours:number,
   approvedHours:number,
   rejectedHours:number,
   forApprovalHours:number,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface MobileGetNewLaborDtlAttch_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  The Labor Header Seq value for which the LaborDtlComment record is created.  */  
   laborHedSeq:number,
      /**  The Labor Detail Seq value for which the LaborDtlComment record is created.  */  
   laborDtlSeq:number,
}

export interface MobileGetNewLaborDtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface MobileGetNewLaborDtlComment_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  The Labor Header Seq value for which the LaborDtlComment record is created.  */  
   laborHedSeq:number,
      /**  The Labor Detail Seq value for which the LaborDtlComment record is created.  */  
   laborDtlSeq:number,
}

export interface MobileGetNewLaborDtlComment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param employeeNum
      @param shopFloor
      @param ClockInDate
      @param ClockInTime
      @param ClockOutDate
      @param ClockOutTTime
   */  
export interface MobileGetNewLaborDtlNoHdr_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  The Employee for which the record is being generated  */  
   employeeNum:string,
      /**  Indicates whether this is being called from the shop floor labor entry program  */  
   shopFloor:boolean,
      /**  The clock in date  */  
   ClockInDate:string,
      /**  The clock in time  */  
   ClockInTime:number,
      /**  The clock out date  */  
   ClockOutDate:string,
      /**  The clock out time  */  
   ClockOutTTime:number,
}

export interface MobileGetNewLaborDtlNoHdr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
      @param sJobNum
      @param iAssemblySeq
      @param iOprSeq
      @param sResourceGrpID
      @param setupOrProd
   */  
export interface MobileGetNewLaborDtlOnSelectForWork_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  The LaborHed seq value for which the LaborDtl record is created.  */  
   laborHedSeq:number,
      /**  The JobNum that will be linked to the LaborDtl record  */  
   sJobNum:string,
      /**  The Assembly sequence for the LaborDtl record  */  
   iAssemblySeq:number,
      /**  The Operation sequence for the LaborDtl record  */  
   iOprSeq:number,
      /**  The Resource group for the LaborDtl record  */  
   sResourceGrpID:string,
      /**  Setup or Prod value string  */  
   setupOrProd:string,
}

export interface MobileGetNewLaborDtlOnSelectForWork_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   bMachinePrompt:boolean,
}
}

   /** Required : 
      @param ds
      @param ClockInDate
      @param ClockInTime
      @param ClockOutDate
      @param ClockOutTTime
      @param laborHedSeq
   */  
export interface MobileGetNewLaborDtlWithHdr_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  The clock in date  */  
   ClockInDate:string,
      /**  The clock in time  */  
   ClockInTime:number,
      /**  The clock out date  */  
   ClockOutDate:string,
      /**  The clock out time  */  
   ClockOutTTime:number,
      /**  The LaborHed seq value for which the LaborDtl record is created.  */  
   laborHedSeq:number,
}

export interface MobileGetNewLaborDtlWithHdr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
   */  
export interface MobileGetNewLaborDtl_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  The LaborHed seq value for which the LaborDtl record is created.  */  
   laborHedSeq:number,
}

export interface MobileGetNewLaborDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface MobileGetNewLaborHed_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface MobileGetNewLaborHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param ipEmployeeNum
      @param ipDateInWeek
   */  
export interface MobileGetNewTimeWeeklyView_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  The Employee for which the record is being generated  */  
   ipEmployeeNum:string,
      /**  Date within the week for which a new TimeWeeklyView record is to be created  */  
   ipDateInWeek:string,
}

export interface MobileGetNewTimeWeeklyView_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param company
      @param empNum
   */  
export interface MobileGetQuickEntry_input{
   company:string,
   empNum:string,
}

export interface MobileGetQuickEntry_output{
   returnObj:Erp_Tablesets_MobileQuickEntryViewRow[],
}

   /** Required : 
      @param salesRepCode
      @param laborType
      @param laborStatus
      @param fromDate
      @param toDate
      @param employeeName
      @param includeMaintenance
      @param includeProduction
      @param pageSize
      @param absolutePage
   */  
export interface MobileGetRowsPendingApprovalWithFilter_input{
   salesRepCode:string,
   laborType:string,
   laborStatus:string,
   fromDate:string,
   toDate:string,
   employeeName:string,
      /**  Bool to include Maintenance type on the filter  */  
   includeMaintenance:boolean,
      /**  Bool to include Production type on the filter  */  
   includeProduction:boolean,
   pageSize:number,
   absolutePage:number,
}

export interface MobileGetRowsPendingApprovalWithFilter_output{
   returnObj:Erp_Tablesets_MobileLaborTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param salesRepCode
      @param laborType
      @param laborStatus
      @param fromDate
      @param toDate
      @param employeeName
      @param pageSize
      @param absolutePage
   */  
export interface MobileGetRowsPendingApproval_input{
   salesRepCode:string,
   laborType:string,
   laborStatus:string,
   fromDate:string,
   toDate:string,
   employeeName:string,
   pageSize:number,
   absolutePage:number,
}

export interface MobileGetRowsPendingApproval_output{
   returnObj:Erp_Tablesets_MobileLaborTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseMobileLaborHed
      @param whereClauseMobileLaborDtl
      @param whereClauseMobileLaborDtlComment
      @param whereClauseTimeWeeklyView
      @param includeMaintenance
      @param includeProduction
      @param pageSize
      @param absolutePage
   */  
export interface MobileGetRowsWithFilter_input{
      /**  The string containing the where clause for LaborHed  */  
   whereClauseMobileLaborHed:string,
      /**  The string containing the where clause for LaborDtl  */  
   whereClauseMobileLaborDtl:string,
      /**  The string containing the where clause for LaborDtlComment  */  
   whereClauseMobileLaborDtlComment:string,
      /**  The string containing the where clause for TimeWeeklyView  */  
   whereClauseTimeWeeklyView:string,
      /**  Bool to include Maintenance type on the filter  */  
   includeMaintenance:boolean,
      /**  Bool to include Production type on the filter  */  
   includeProduction:boolean,
      /**  The Page Size for the resulting dataset  */  
   pageSize:number,
      /**  The Absolute Page for the resulting dataset  */  
   absolutePage:number,
}

export interface MobileGetRowsWithFilter_output{
   returnObj:Erp_Tablesets_MobileLaborTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseMobileLaborHed
      @param whereClauseMobileLaborDtl
      @param whereClauseMobileLaborDtlComment
      @param whereClauseTimeWeeklyView
      @param pageSize
      @param absolutePage
   */  
export interface MobileGetRows_input{
      /**  The string containing the where clause for LaborHed  */  
   whereClauseMobileLaborHed:string,
      /**  The string containing the where clause for LaborDtl  */  
   whereClauseMobileLaborDtl:string,
      /**  The string containing the where clause for LaborDtlComment  */  
   whereClauseMobileLaborDtlComment:string,
      /**  The string containing the where clause for TimeWeeklyView  */  
   whereClauseTimeWeeklyView:string,
      /**  The Page Size for the resulting dataset  */  
   pageSize:number,
      /**  The Absolute Page for the resulting dataset  */  
   absolutePage:number,
}

export interface MobileGetRows_output{
   returnObj:Erp_Tablesets_MobileLaborTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param mobileLaborWhereClause
      @param pageSize
      @param absolutePage
   */  
export interface MobileLaborGetList_input{
      /**  The string containing the where clause for LaborHed  */  
   mobileLaborWhereClause:string,
      /**  The Page Size for the resulting dataset  */  
   pageSize:number,
      /**  The Absolute Page for the resulting dataset  */  
   absolutePage:number,
}

export interface MobileLaborGetList_output{
   returnObj:Erp_Tablesets_MobileLaborListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface MobileLaborUpdate_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface MobileLaborUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param inOpCode
      @param inResGrpID
   */  
export interface MobileOverrides_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  OpCode to override  */  
   inOpCode:string,
      /**  Resource Group OD to override  */  
   inResGrpID:string,
}

export interface MobileOverrides_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

   /** Required : 
      @param ds
      @param lWeeklyView
   */  
export interface MobileRecallFromApproval_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Is this method being called with WeeklyView records?  */  
   lWeeklyView:boolean,
}

export interface MobileRecallFromApproval_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   cMessageText:string,
}
}

   /** Required : 
      @param company
      @param tableName
      @param sysRowID
   */  
export interface MobileSyncSuccessful_input{
      /**  Company where the record was created  */  
   company:string,
      /**  Name of the table related to the patch field  */  
   tableName:string,
      /**  SysRowID of the record on the Mobile  */  
   sysRowID:string,
}

export interface MobileSyncSuccessful_output{
}

   /** Required : 
      @param tableName
      @param ds
      @param comments
      @param salesRepCode
      @param isWeeklyView
   */  
export interface MobileSync_input{
      /**  Name of the table that is being synchronized.  */  
   tableName:string,
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Comments for approved and rejected records  */  
   comments:string,
      /**  Sales Rep Code  */  
   salesRepCode:string,
      /**  Is this method being called with WeeklyView records?  */  
   isWeeklyView:boolean,
}

export interface MobileSync_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   outMessage:string,
}
}

   /** Required : 
      @param ds
      @param scrapQty
   */  
export interface MobileVerifyScrapQty_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Proposed change to ScrapQty field  */  
   scrapQty:number,
}

export interface MobileVerifyScrapQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param salesRepCode
      @param ds
   */  
export interface RecallTrans_input{
      /**  The sales Rep Code of the approver.  */  
   salesRepCode:string,
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface RecallTrans_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   outMessage:string,
}
}

   /** Required : 
      @param ds
      @param isWeeklyView
   */  
export interface SubmitSelected_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
      /**  Indicates if a WeeklyView is being processed  */  
   isWeeklyView:boolean,
}

export interface SubmitSelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
   outMessage:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtMobileLaborTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtMobileLaborTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_MobileLaborTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileLaborTableset,
}
}

