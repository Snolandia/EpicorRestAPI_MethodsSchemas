import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.LaborSvc
// Description: Labor Entry Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get Labors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Labors
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborHedRow
   */  
export function get_Labors(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Labors
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LaborHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Labors(requestBody:Erp_Tablesets_LaborHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the Labor item
   Description: Calls GetByID to retrieve the Labor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Labor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborHedRow
   */  
export function get_Labors_Company_LaborHedSeq(Company:string, LaborHedSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors(" + Company + "," + LaborHedSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Labor for the service
   Description: Calls UpdateExt to update Labor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Labor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Labors_Company_LaborHedSeq(Company:string, LaborHedSeq:string, requestBody:Erp_Tablesets_LaborHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors(" + Company + "," + LaborHedSeq + ")", {
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
   Summary: Call UpdateExt to delete Labor item
   Description: Call UpdateExt to delete Labor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Labor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Labors_Company_LaborHedSeq(Company:string, LaborHedSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors(" + Company + "," + LaborHedSeq + ")", {
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
   Description: Get LaborDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborDtls1
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlRow
   */  
export function get_Labors_Company_LaborHedSeq_LaborDtls(Company:string, LaborHedSeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors(" + Company + "," + LaborHedSeq + ")/LaborDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborDtl item
   Description: Calls GetByID to retrieve the LaborDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborDtlRow
   */  
export function get_Labors_Company_LaborHedSeq_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors(" + Company + "," + LaborHedSeq + ")/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LaborDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlRow
   */  
export function get_LaborDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LaborDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborDtls(requestBody:Erp_Tablesets_LaborDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LaborDtl item
   Description: Calls GetByID to retrieve the LaborDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborDtlRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborDtl for the service
   Description: Calls UpdateExt to update LaborDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, requestBody:Erp_Tablesets_LaborDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
   Summary: Call UpdateExt to delete LaborDtl item
   Description: Call UpdateExt to delete LaborDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
   Description: Get LaborDtlActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborDtlActions1
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlActionRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborDtlActions(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlActions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborDtlAction item
   Description: Calls GetByID to retrieve the LaborDtlAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlAction1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborDtlActionRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborDtlActions_Company_LaborHedSeq_LaborDtlSeq_ActionSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, ActionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlActions(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + ActionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborDtlActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get LaborDtlComments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborDtlComments1
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlCommentRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborDtlComments(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlComments", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborDtlComment item
   Description: Calls GetByID to retrieve the LaborDtlComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlComment1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborDtlCommentRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company:string, LaborHedSeq:string, LaborDtlSeq:string, CommentNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborDtlCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get LaborEquips items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborEquips1
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborEquipRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborEquips(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborEquipRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborEquips", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborEquipRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborEquip item
   Description: Calls GetByID to retrieve the LaborEquip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborEquip1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborEquipRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborEquips_Company_LaborHedSeq_LaborDtlSeq_EquipID(Company:string, LaborHedSeq:string, LaborDtlSeq:string, EquipID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborEquipRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborEquips(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborEquipRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get LaborParts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborParts1
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborPartRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborParts(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborParts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborPart item
   Description: Calls GetByID to retrieve the LaborPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborPart1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborPartRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborParts_Company_LaborHedSeq_LaborDtlSeq_PartNum(Company:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborParts(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get LbrScrapSerialNumbers items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LbrScrapSerialNumbers1
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LbrScrapSerialNumbersRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LbrScrapSerialNumbers(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LbrScrapSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LbrScrapSerialNumbers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LbrScrapSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LbrScrapSerialNumber item
   Description: Calls GetByID to retrieve the LbrScrapSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LbrScrapSerialNumber1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LbrScrapSerialNumbersRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LbrScrapSerialNumbers_Company_LaborHedSeq_LaborDtlSeq_SerialNumber_AssemblySeq_OprSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, SerialNumber:string, AssemblySeq:string, OprSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LbrScrapSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LbrScrapSerialNumbers(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + SerialNumber + "," + AssemblySeq + "," + OprSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LbrScrapSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get LaborDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborDtlAttches1
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlAttchRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborDtlAttches(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborDtlAttch item
   Description: Calls GetByID to retrieve the LaborDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborDtlAttchRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LaborDtlActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtlActions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlActionRow
   */  
export function get_LaborDtlActions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlActions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtlActions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LaborDtlActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborDtlActions(requestBody:Erp_Tablesets_LaborDtlActionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlActions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LaborDtlAction item
   Description: Calls GetByID to retrieve the LaborDtlAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborDtlActionRow
   */  
export function get_LaborDtlActions_Company_LaborHedSeq_LaborDtlSeq_ActionSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, ActionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlActions(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + ActionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborDtlActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborDtlAction for the service
   Description: Calls UpdateExt to update LaborDtlAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtlAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborDtlActions_Company_LaborHedSeq_LaborDtlSeq_ActionSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, ActionSeq:string, requestBody:Erp_Tablesets_LaborDtlActionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlActions(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + ActionSeq + ")", {
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
   Summary: Call UpdateExt to delete LaborDtlAction item
   Description: Call UpdateExt to delete LaborDtlAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtlAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaborDtlActions_Company_LaborHedSeq_LaborDtlSeq_ActionSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, ActionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlActions(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + ActionSeq + ")", {
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
   Description: Get LaborDtlComments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtlComments
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlCommentRow
   */  
export function get_LaborDtlComments(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlComments", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtlComments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlCommentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LaborDtlCommentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborDtlComments(requestBody:Erp_Tablesets_LaborDtlCommentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlComments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LaborDtlComment item
   Description: Calls GetByID to retrieve the LaborDtlComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlComment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborDtlCommentRow
   */  
export function get_LaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company:string, LaborHedSeq:string, LaborDtlSeq:string, CommentNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborDtlCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborDtlComment for the service
   Description: Calls UpdateExt to update LaborDtlComment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtlComment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlCommentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company:string, LaborHedSeq:string, LaborDtlSeq:string, CommentNum:string, requestBody:Erp_Tablesets_LaborDtlCommentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")", {
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
   Summary: Call UpdateExt to delete LaborDtlComment item
   Description: Call UpdateExt to delete LaborDtlComment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtlComment
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
export function delete_LaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company:string, LaborHedSeq:string, LaborDtlSeq:string, CommentNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")", {
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
   Description: Get LaborEquips items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborEquips
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborEquipRow
   */  
export function get_LaborEquips(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborEquipRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborEquips", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborEquipRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborEquips
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborEquipRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LaborEquipRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborEquips(requestBody:Erp_Tablesets_LaborEquipRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborEquips", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LaborEquip item
   Description: Calls GetByID to retrieve the LaborEquip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborEquip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborEquipRow
   */  
export function get_LaborEquips_Company_LaborHedSeq_LaborDtlSeq_EquipID(Company:string, LaborHedSeq:string, LaborDtlSeq:string, EquipID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborEquipRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborEquips(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborEquipRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborEquip for the service
   Description: Calls UpdateExt to update LaborEquip. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborEquip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborEquipRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborEquips_Company_LaborHedSeq_LaborDtlSeq_EquipID(Company:string, LaborHedSeq:string, LaborDtlSeq:string, EquipID:string, requestBody:Erp_Tablesets_LaborEquipRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborEquips(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")", {
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
   Summary: Call UpdateExt to delete LaborEquip item
   Description: Call UpdateExt to delete LaborEquip item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborEquip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaborEquips_Company_LaborHedSeq_LaborDtlSeq_EquipID(Company:string, LaborHedSeq:string, LaborDtlSeq:string, EquipID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborEquips(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")", {
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
   Description: Get LaborParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborParts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborPartRow
   */  
export function get_LaborParts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborParts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborParts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LaborPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborParts(requestBody:Erp_Tablesets_LaborPartRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborParts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LaborPart item
   Description: Calls GetByID to retrieve the LaborPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborPartRow
   */  
export function get_LaborParts_Company_LaborHedSeq_LaborDtlSeq_PartNum(Company:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborParts(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborPart for the service
   Description: Calls UpdateExt to update LaborPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborParts_Company_LaborHedSeq_LaborDtlSeq_PartNum(Company:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, requestBody:Erp_Tablesets_LaborPartRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborParts(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")", {
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
   Summary: Call UpdateExt to delete LaborPart item
   Description: Call UpdateExt to delete LaborPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaborParts_Company_LaborHedSeq_LaborDtlSeq_PartNum(Company:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborParts(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")", {
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
   Description: Get LbrScrapSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LbrScrapSerialNumbers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LbrScrapSerialNumbersRow
   */  
export function get_LbrScrapSerialNumbers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LbrScrapSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LbrScrapSerialNumbers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LbrScrapSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LbrScrapSerialNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LbrScrapSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LbrScrapSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LbrScrapSerialNumbers(requestBody:Erp_Tablesets_LbrScrapSerialNumbersRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LbrScrapSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LbrScrapSerialNumber item
   Description: Calls GetByID to retrieve the LbrScrapSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LbrScrapSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LbrScrapSerialNumbersRow
   */  
export function get_LbrScrapSerialNumbers_Company_LaborHedSeq_LaborDtlSeq_SerialNumber_AssemblySeq_OprSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, SerialNumber:string, AssemblySeq:string, OprSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LbrScrapSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LbrScrapSerialNumbers(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + SerialNumber + "," + AssemblySeq + "," + OprSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LbrScrapSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LbrScrapSerialNumber for the service
   Description: Calls UpdateExt to update LbrScrapSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LbrScrapSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LbrScrapSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LbrScrapSerialNumbers_Company_LaborHedSeq_LaborDtlSeq_SerialNumber_AssemblySeq_OprSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, SerialNumber:string, AssemblySeq:string, OprSeq:string, requestBody:Erp_Tablesets_LbrScrapSerialNumbersRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LbrScrapSerialNumbers(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + SerialNumber + "," + AssemblySeq + "," + OprSeq + ")", {
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
   Summary: Call UpdateExt to delete LbrScrapSerialNumber item
   Description: Call UpdateExt to delete LbrScrapSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LbrScrapSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LbrScrapSerialNumbers_Company_LaborHedSeq_LaborDtlSeq_SerialNumber_AssemblySeq_OprSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, SerialNumber:string, AssemblySeq:string, OprSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LbrScrapSerialNumbers(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + SerialNumber + "," + AssemblySeq + "," + OprSeq + ")", {
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
   Description: Get LaborDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlAttchRow
   */  
export function get_LaborDtlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtlAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LaborDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborDtlAttches(requestBody:Erp_Tablesets_LaborDtlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LaborDtlAttch item
   Description: Calls GetByID to retrieve the LaborDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborDtlAttchRow
   */  
export function get_LaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborDtlAttch for the service
   Description: Calls UpdateExt to update LaborDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, DrawingSeq:string, requestBody:Erp_Tablesets_LaborDtlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete LaborDtlAttch item
   Description: Call UpdateExt to delete LaborDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtlAttch
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
export function delete_LaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")", {
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
   Description: Get LaborDtlGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtlGroups
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlGroupRow
   */  
export function get_LaborDtlGroups(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlGroups", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtlGroups
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LaborDtlGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborDtlGroups(requestBody:Erp_Tablesets_LaborDtlGroupRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlGroups", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LaborDtlGroup item
   Description: Calls GetByID to retrieve the LaborDtlGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlGroup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmployeeNum Desc: EmployeeNum   Required: True   Allow empty value : True
      @param ClaimRef Desc: ClaimRef   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborDtlGroupRow
   */  
export function get_LaborDtlGroups_Company_EmployeeNum_ClaimRef(Company:string, EmployeeNum:string, ClaimRef:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlGroups(" + Company + "," + EmployeeNum + "," + ClaimRef + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborDtlGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborDtlGroup for the service
   Description: Calls UpdateExt to update LaborDtlGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtlGroup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmployeeNum Desc: EmployeeNum   Required: True   Allow empty value : True
      @param ClaimRef Desc: ClaimRef   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborDtlGroups_Company_EmployeeNum_ClaimRef(Company:string, EmployeeNum:string, ClaimRef:string, requestBody:Erp_Tablesets_LaborDtlGroupRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlGroups(" + Company + "," + EmployeeNum + "," + ClaimRef + ")", {
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
   Summary: Call UpdateExt to delete LaborDtlGroup item
   Description: Call UpdateExt to delete LaborDtlGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtlGroup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmployeeNum Desc: EmployeeNum   Required: True   Allow empty value : True
      @param ClaimRef Desc: ClaimRef   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaborDtlGroups_Company_EmployeeNum_ClaimRef(Company:string, EmployeeNum:string, ClaimRef:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlGroups(" + Company + "," + EmployeeNum + "," + ClaimRef + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectedSerialNumbers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectedSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SNFormats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SNFormats", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
   Description: Get TimeWeeklyViews items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TimeWeeklyViews
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TimeWeeklyViewRow
   */  
export function get_TimeWeeklyViews(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TimeWeeklyViewRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWeeklyViews", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TimeWeeklyViewRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TimeWeeklyViews
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TimeWeeklyViewRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TimeWeeklyViewRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TimeWeeklyViews(requestBody:Erp_Tablesets_TimeWeeklyViewRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWeeklyViews", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the TimeWeeklyView item
   Description: Calls GetByID to retrieve the TimeWeeklyView item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TimeWeeklyView
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmployeeNum Desc: EmployeeNum   Required: True   Allow empty value : True
      @param WeekBeginDate Desc: WeekBeginDate   Required: True   Allow empty value : True
      @param WeekEndDate Desc: WeekEndDate   Required: True   Allow empty value : True
      @param LaborTypePseudo Desc: LaborTypePseudo   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param PhaseID Desc: PhaseID   Required: True   Allow empty value : True
      @param TimeTypCd Desc: TimeTypCd   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param IndirectCode Desc: IndirectCode   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      @param NewRowType Desc: NewRowType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      @param TimeStatus Desc: TimeStatus   Required: True   Allow empty value : True
      @param Shift Desc: Shift   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TimeWeeklyViewRow
   */  
export function get_TimeWeeklyViews_Company_EmployeeNum_WeekBeginDate_WeekEndDate_LaborTypePseudo_ProjectID_PhaseID_TimeTypCd_JobNum_AssemblySeq_OprSeq_IndirectCode_RoleCd_ResourceGrpID_ResourceID_ExpenseCode_NewRowType_QuickEntryCode_TimeStatus_Shift(Company:string, EmployeeNum:string, WeekBeginDate:string, WeekEndDate:string, LaborTypePseudo:string, ProjectID:string, PhaseID:string, TimeTypCd:string, JobNum:string, AssemblySeq:string, OprSeq:string, IndirectCode:string, RoleCd:string, ResourceGrpID:string, ResourceID:string, ExpenseCode:string, NewRowType:string, QuickEntryCode:string, TimeStatus:string, Shift:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TimeWeeklyViewRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWeeklyViews(" + Company + "," + EmployeeNum + "," + WeekBeginDate + "," + WeekEndDate + "," + LaborTypePseudo + "," + ProjectID + "," + PhaseID + "," + TimeTypCd + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + IndirectCode + "," + RoleCd + "," + ResourceGrpID + "," + ResourceID + "," + ExpenseCode + "," + NewRowType + "," + QuickEntryCode + "," + TimeStatus + "," + Shift + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_TimeWeeklyViewRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TimeWeeklyView for the service
   Description: Calls UpdateExt to update TimeWeeklyView. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TimeWeeklyView
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmployeeNum Desc: EmployeeNum   Required: True   Allow empty value : True
      @param WeekBeginDate Desc: WeekBeginDate   Required: True   Allow empty value : True
      @param WeekEndDate Desc: WeekEndDate   Required: True   Allow empty value : True
      @param LaborTypePseudo Desc: LaborTypePseudo   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param PhaseID Desc: PhaseID   Required: True   Allow empty value : True
      @param TimeTypCd Desc: TimeTypCd   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param IndirectCode Desc: IndirectCode   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      @param NewRowType Desc: NewRowType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      @param TimeStatus Desc: TimeStatus   Required: True   Allow empty value : True
      @param Shift Desc: Shift   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TimeWeeklyViewRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TimeWeeklyViews_Company_EmployeeNum_WeekBeginDate_WeekEndDate_LaborTypePseudo_ProjectID_PhaseID_TimeTypCd_JobNum_AssemblySeq_OprSeq_IndirectCode_RoleCd_ResourceGrpID_ResourceID_ExpenseCode_NewRowType_QuickEntryCode_TimeStatus_Shift(Company:string, EmployeeNum:string, WeekBeginDate:string, WeekEndDate:string, LaborTypePseudo:string, ProjectID:string, PhaseID:string, TimeTypCd:string, JobNum:string, AssemblySeq:string, OprSeq:string, IndirectCode:string, RoleCd:string, ResourceGrpID:string, ResourceID:string, ExpenseCode:string, NewRowType:string, QuickEntryCode:string, TimeStatus:string, Shift:string, requestBody:Erp_Tablesets_TimeWeeklyViewRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWeeklyViews(" + Company + "," + EmployeeNum + "," + WeekBeginDate + "," + WeekEndDate + "," + LaborTypePseudo + "," + ProjectID + "," + PhaseID + "," + TimeTypCd + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + IndirectCode + "," + RoleCd + "," + ResourceGrpID + "," + ResourceID + "," + ExpenseCode + "," + NewRowType + "," + QuickEntryCode + "," + TimeStatus + "," + Shift + ")", {
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
   Summary: Call UpdateExt to delete TimeWeeklyView item
   Description: Call UpdateExt to delete TimeWeeklyView item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TimeWeeklyView
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmployeeNum Desc: EmployeeNum   Required: True   Allow empty value : True
      @param WeekBeginDate Desc: WeekBeginDate   Required: True   Allow empty value : True
      @param WeekEndDate Desc: WeekEndDate   Required: True   Allow empty value : True
      @param LaborTypePseudo Desc: LaborTypePseudo   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param PhaseID Desc: PhaseID   Required: True   Allow empty value : True
      @param TimeTypCd Desc: TimeTypCd   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param IndirectCode Desc: IndirectCode   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      @param NewRowType Desc: NewRowType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      @param TimeStatus Desc: TimeStatus   Required: True   Allow empty value : True
      @param Shift Desc: Shift   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TimeWeeklyViews_Company_EmployeeNum_WeekBeginDate_WeekEndDate_LaborTypePseudo_ProjectID_PhaseID_TimeTypCd_JobNum_AssemblySeq_OprSeq_IndirectCode_RoleCd_ResourceGrpID_ResourceID_ExpenseCode_NewRowType_QuickEntryCode_TimeStatus_Shift(Company:string, EmployeeNum:string, WeekBeginDate:string, WeekEndDate:string, LaborTypePseudo:string, ProjectID:string, PhaseID:string, TimeTypCd:string, JobNum:string, AssemblySeq:string, OprSeq:string, IndirectCode:string, RoleCd:string, ResourceGrpID:string, ResourceID:string, ExpenseCode:string, NewRowType:string, QuickEntryCode:string, TimeStatus:string, Shift:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWeeklyViews(" + Company + "," + EmployeeNum + "," + WeekBeginDate + "," + WeekEndDate + "," + LaborTypePseudo + "," + ProjectID + "," + PhaseID + "," + TimeTypCd + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + IndirectCode + "," + RoleCd + "," + ResourceGrpID + "," + ResourceID + "," + ExpenseCode + "," + NewRowType + "," + QuickEntryCode + "," + TimeStatus + "," + Shift + ")", {
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
   Description: Get TimeWorkHours items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TimeWorkHours
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TimeWorkHoursRow
   */  
export function get_TimeWorkHours(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TimeWorkHoursRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWorkHours", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TimeWorkHoursRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TimeWorkHours
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TimeWorkHoursRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TimeWorkHoursRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TimeWorkHours(requestBody:Erp_Tablesets_TimeWorkHoursRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWorkHours", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the TimeWorkHour item
   Description: Calls GetByID to retrieve the TimeWorkHour item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TimeWorkHour
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmployeeNum Desc: EmployeeNum   Required: True   Allow empty value : True
      @param WeekBeginDate Desc: WeekBeginDate   Required: True   Allow empty value : True
      @param WeekEndDate Desc: WeekEndDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TimeWorkHoursRow
   */  
export function get_TimeWorkHours_Company_EmployeeNum_WeekBeginDate_WeekEndDate(Company:string, EmployeeNum:string, WeekBeginDate:string, WeekEndDate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TimeWorkHoursRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWorkHours(" + Company + "," + EmployeeNum + "," + WeekBeginDate + "," + WeekEndDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_TimeWorkHoursRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TimeWorkHour for the service
   Description: Calls UpdateExt to update TimeWorkHour. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TimeWorkHour
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmployeeNum Desc: EmployeeNum   Required: True   Allow empty value : True
      @param WeekBeginDate Desc: WeekBeginDate   Required: True   Allow empty value : True
      @param WeekEndDate Desc: WeekEndDate   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TimeWorkHoursRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TimeWorkHours_Company_EmployeeNum_WeekBeginDate_WeekEndDate(Company:string, EmployeeNum:string, WeekBeginDate:string, WeekEndDate:string, requestBody:Erp_Tablesets_TimeWorkHoursRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWorkHours(" + Company + "," + EmployeeNum + "," + WeekBeginDate + "," + WeekEndDate + ")", {
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
   Summary: Call UpdateExt to delete TimeWorkHour item
   Description: Call UpdateExt to delete TimeWorkHour item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TimeWorkHour
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmployeeNum Desc: EmployeeNum   Required: True   Allow empty value : True
      @param WeekBeginDate Desc: WeekBeginDate   Required: True   Allow empty value : True
      @param WeekEndDate Desc: WeekEndDate   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TimeWorkHours_Company_EmployeeNum_WeekBeginDate_WeekEndDate(Company:string, EmployeeNum:string, WeekBeginDate:string, WeekEndDate:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWorkHours(" + Company + "," + EmployeeNum + "," + WeekBeginDate + "," + WeekEndDate + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseLaborHed:string, whereClauseLaborDtl:string, whereClauseLaborDtlAttch:string, whereClauseLaborDtlAction:string, whereClauseLaborDtlComment:string, whereClauseLaborEquip:string, whereClauseLaborPart:string, whereClauseLbrScrapSerialNumbers:string, whereClauseLaborDtlGroup:string, whereClauseSelectedSerialNumbers:string, whereClauseSNFormat:string, whereClauseTimeWeeklyView:string, whereClauseTimeWorkHours:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseLaborHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborHed=" + whereClauseLaborHed
   }
   if(typeof whereClauseLaborDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborDtl=" + whereClauseLaborDtl
   }
   if(typeof whereClauseLaborDtlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborDtlAttch=" + whereClauseLaborDtlAttch
   }
   if(typeof whereClauseLaborDtlAction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborDtlAction=" + whereClauseLaborDtlAction
   }
   if(typeof whereClauseLaborDtlComment!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborDtlComment=" + whereClauseLaborDtlComment
   }
   if(typeof whereClauseLaborEquip!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborEquip=" + whereClauseLaborEquip
   }
   if(typeof whereClauseLaborPart!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborPart=" + whereClauseLaborPart
   }
   if(typeof whereClauseLbrScrapSerialNumbers!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLbrScrapSerialNumbers=" + whereClauseLbrScrapSerialNumbers
   }
   if(typeof whereClauseLaborDtlGroup!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborDtlGroup=" + whereClauseLaborDtlGroup
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
   if(typeof whereClauseSNFormat!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSNFormat=" + whereClauseSNFormat
   }
   if(typeof whereClauseTimeWeeklyView!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTimeWeeklyView=" + whereClauseTimeWeeklyView
   }
   if(typeof whereClauseTimeWorkHours!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTimeWorkHours=" + whereClauseTimeWorkHours
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method LaborHedPayrollDateChanging
   Description: Called when LaborHed Payroll Date is changing
   OperationID: LaborHedPayrollDateChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LaborHedPayrollDateChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LaborHedPayrollDateChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborHedPayrollDateChanging(requestBody:LaborHedPayrollDateChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LaborHedPayrollDateChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborHedPayrollDateChanging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LaborHedPayrollDateChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultsAddLaborDtlFromCalendar
   OperationID: GetDefaultsAddLaborDtlFromCalendar
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefaultsAddLaborDtlFromCalendar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultsAddLaborDtlFromCalendar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultsAddLaborDtlFromCalendar(requestBody:GetDefaultsAddLaborDtlFromCalendar_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultsAddLaborDtlFromCalendar_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetDefaultsAddLaborDtlFromCalendar", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDefaultsAddLaborDtlFromCalendar_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLaborPartScrapQty
   Description: This method sets Complete checkbox when scrap qty field changes in End Activity.
   OperationID: OnChangeLaborPartScrapQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLaborPartScrapQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLaborPartScrapQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLaborPartScrapQty(requestBody:OnChangeLaborPartScrapQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLaborPartScrapQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/OnChangeLaborPartScrapQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeLaborPartScrapQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLaborPartAttributeSetID
   Description: This method updates the revision field when the attribute ID field changes.
   OperationID: ChangeLaborPartAttributeSetID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLaborPartAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborPartAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborPartAttributeSetID(requestBody:ChangeLaborPartAttributeSetID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLaborPartAttributeSetID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ChangeLaborPartAttributeSetID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeLaborPartAttributeSetID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AfterChangeLaborPartDiscrepQty
   Description: Called after LaborDtl.DiscrepQty has been changed.
   OperationID: AfterChangeLaborPartDiscrepQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AfterChangeLaborPartDiscrepQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterChangeLaborPartDiscrepQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AfterChangeLaborPartDiscrepQty(requestBody:AfterChangeLaborPartDiscrepQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AfterChangeLaborPartDiscrepQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/AfterChangeLaborPartDiscrepQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AfterChangeLaborPartDiscrepQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborHed(requestBody:GetNewLaborHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLaborHed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborDtl(requestBody:GetNewLaborDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLaborDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtlAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborDtlAttch(requestBody:GetNewLaborDtlAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborDtlAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLaborDtlAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborDtlAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborDtlAction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtlAction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborDtlAction(requestBody:GetNewLaborDtlAction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborDtlAction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLaborDtlAction", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborDtlAction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborDtlComment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtlComment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborDtlComment(requestBody:GetNewLaborDtlComment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborDtlComment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLaborDtlComment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborDtlComment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborEquip
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborEquip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborEquip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborEquip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborEquip(requestBody:GetNewLaborEquip_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborEquip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLaborEquip", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborEquip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborPart(requestBody:GetNewLaborPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLaborPart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborDtlGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtlGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborDtlGroup(requestBody:GetNewLaborDtlGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborDtlGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLaborDtlGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborDtlGroup_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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

   /**  
   Summary: Invoke method BuildJobOperPrjRoleList
   Description: This proc will return the whereclause for the role code combo
Customers
   OperationID: BuildJobOperPrjRoleList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildJobOperPrjRoleList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildJobOperPrjRoleList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildJobOperPrjRoleList(requestBody:BuildJobOperPrjRoleList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildJobOperPrjRoleList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/BuildJobOperPrjRoleList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildJobOperPrjRoleList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeEquipID
   Description: This method should call when EquipID is changed
   OperationID: ChangeEquipID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeEquipID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEquipID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEquipID(requestBody:ChangeEquipID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeEquipID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ChangeEquipID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeEquipID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeIndirectCode
   Description: This method clears the JobNumber and Quantity fields when the LaborType changes to Indirect
leaves the values as is if changed between Production and Setup
   OperationID: ChangeIndirectCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeIndirectCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeIndirectCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeIndirectCode(requestBody:ChangeIndirectCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeIndirectCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ChangeIndirectCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeIndirectCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLaborType
   Description: This method clears the JobNumber and Quantity fields when the LaborType changes to Indirect
leaves the values as is if changed between Production and Setup
   OperationID: ChangeLaborType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLaborType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborType(requestBody:ChangeLaborType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLaborType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ChangeLaborType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeLaborType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckResourceId
   Description: Main logic from ChangeResourceId to validate the resource id assigned to a Job.
This method does not depend on a tableset or LaborDtl record.
   OperationID: CheckResourceId
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckResourceId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckResourceId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckResourceId(requestBody:CheckResourceId_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckResourceId_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/CheckResourceId", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckResourceId_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeResourceId
   Description: For use with MES (ShopFloor) only.
This method checks the Resource Group of the proposed Resource, and if it
is different than the current Resource Group, provides a warning question
suitable for presenting to the user.
The UI code should place the user's answer to the question in the
ttLaborDtl.OkToChangeResourceGrpID.
This method should be called prior to calling the DefaultResourceID method.
   OperationID: ChangeResourceId
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeResourceId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResourceId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeResourceId(requestBody:ChangeResourceId_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeResourceId_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ChangeResourceId", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeResourceId_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckEmployeeActivity
   Description: This method checks if the current employee is already working on a Job/Asm/Opr/Resource combination
If he/she is already working on it, the opMessage will be populated with an error message
   OperationID: CheckEmployeeActivity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckEmployeeActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEmployeeActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckEmployeeActivity(requestBody:CheckEmployeeActivity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckEmployeeActivity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/CheckEmployeeActivity", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckEmployeeActivity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckNonConformance
   Description: Check if there are NonConformance records, if they exists it will ask the user for his approval to delete them
   OperationID: CheckNonConformance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckNonConformance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckNonConformance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckNonConformance(requestBody:CheckNonConformance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckNonConformance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/CheckNonConformance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckNonConformance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckFirstArticleWarning
   Description: Performs all First Article Validations
   OperationID: CheckFirstArticleWarning
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckFirstArticleWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFirstArticleWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckFirstArticleWarning(requestBody:CheckFirstArticleWarning_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckFirstArticleWarning_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/CheckFirstArticleWarning", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckFirstArticleWarning_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckInspResults
   Description: This method validates if InspResults has been entered when the Inspection Data is allowed for the current OprSeq.
   OperationID: CheckInspResults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckInspResults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckInspResults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckInspResults(requestBody:CheckInspResults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckInspResults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/CheckInspResults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckInspResults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckResourceGroup
   Description: This method checks to see if the new resource is in the current resource group.
This needs to be run right before the DefaultResourceID.  If the user answers
okay then the group will be changed in the DefaultResourceID method.
   OperationID: CheckResourceGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckResourceGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckResourceGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckResourceGroup(requestBody:CheckResourceGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckResourceGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/CheckResourceGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckResourceGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckWarnings
   Description: This method runs the labor warning routine and returns any warnings the user needs
to be aware of.  This needs to be run right before the update method.  If the user answers
okay to all of the questions, then the update method can be run.  Otherwise the labor record
needs to be corrected
   OperationID: CheckWarnings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckWarnings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckWarnings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckWarnings(requestBody:CheckWarnings_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckWarnings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/CheckWarnings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckWarnings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method chkReportQtyShopWarn
   OperationID: chkReportQtyShopWarn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/chkReportQtyShopWarn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/chkReportQtyShopWarn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_chkReportQtyShopWarn(requestBody:chkReportQtyShopWarn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<chkReportQtyShopWarn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/chkReportQtyShopWarn", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as chkReportQtyShopWarn_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyLaborDetail
   Description: Method to copy the vales from one Labor record to a new Labor record.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/CopyLaborDetail", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method CopyTimeWeeklyView
   Description: Method to copy the vales from one Weekly Time record to a new Weekly Time record.
   OperationID: CopyTimeWeeklyView
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyTimeWeeklyView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyTimeWeeklyView_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyTimeWeeklyView(requestBody:CopyTimeWeeklyView_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyTimeWeeklyView_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/CopyTimeWeeklyView", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CopyTimeWeeklyView_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultAssemblySeq
   Description: This method sets dataset fields when the AssemblySeq field changes
   OperationID: DefaultAssemblySeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultAssemblySeq(requestBody:DefaultAssemblySeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultAssemblySeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultAssemblySeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultAssemblySeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultComplete
   Description: This method updates the dataset after complete flag is set
   OperationID: DefaultComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultComplete(requestBody:DefaultComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultComplete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultComplete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultDate
   Description: This method updates the clock in and clock out dates for the LaborHed and LaborDtl
tables when the payroll date has changed.
   OperationID: DefaultDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultDate(requestBody:DefaultDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultDiscrpRsnCode
   Description: This method defaults fields when the discrepancy reason code field changes.
Also checks for any warnings the user needs to be aware of
   OperationID: DefaultDiscrpRsnCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultDiscrpRsnCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultDiscrpRsnCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultDiscrpRsnCode(requestBody:DefaultDiscrpRsnCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultDiscrpRsnCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultDiscrpRsnCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultDiscrpRsnCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultReworkReasonCode
   Description: This method defaults fields when the discrepancy reason code field changes.
Also checks for any warnings the user needs to be aware of
   OperationID: DefaultReworkReasonCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultReworkReasonCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultReworkReasonCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultReworkReasonCode(requestBody:DefaultReworkReasonCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultReworkReasonCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultReworkReasonCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultReworkReasonCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultDtlTime
   Description: This method updates the hours when a time field changes
   OperationID: DefaultDtlTime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultDtlTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultDtlTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultDtlTime(requestBody:DefaultDtlTime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultDtlTime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultDtlTime", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultDtlTime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultIndirect
   Description: This method defaults the expense code when the indirect code has changed
   OperationID: DefaultIndirect
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultIndirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultIndirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultIndirect(requestBody:DefaultIndirect_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultIndirect_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultIndirect", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultIndirect_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectAllForWork
   Description: This method will take the selected rows from the work queue and process them in one server call.
GetNewLaborDtlOnSelectForWork is called for each work queue row, after that SelectForWork will be called filling required information in all the added LaborDtl rows
If there is any warning that needs user input the method will finish before calling Update and the prompts will be shown to the user, after the UI will call Update to finish.
   OperationID: SelectAllForWork
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectAllForWork_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectAllForWork_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectAllForWork(requestBody:SelectAllForWork_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectAllForWork_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectAllForWork", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SelectAllForWork_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultJobNum
   Description: This method defaults dataset fields when the JobNum field changes
   OperationID: DefaultJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultJobNum(requestBody:DefaultJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultJobNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultLaborHrs
   Description: This method updates the tot hours display field when the labor hours clock in/out
time changes
   OperationID: DefaultLaborHrs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultLaborHrs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultLaborHrs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultLaborHrs(requestBody:DefaultLaborHrs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultLaborHrs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultLaborHrs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultLaborHrs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultLaborQty
   Description: This method defaults fields when the labor qty fields changes.  Also checks
for any labor warnings the user needs to be aware of
   OperationID: DefaultLaborQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultLaborQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultLaborQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultLaborQty(requestBody:DefaultLaborQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultLaborQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultLaborQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultLaborQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultNonConformanceQty
   Description: This method defaults fields when the labor qty fields changes.  Also checks
for any labor warnings the user needs to be aware of
   OperationID: DefaultNonConformanceQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultNonConformanceQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultNonConformanceQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultNonConformanceQty(requestBody:DefaultNonConformanceQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultNonConformanceQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultNonConformanceQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultNonConformanceQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VerifyScrapQty
   Description: This method defaults fields when the scrap qty field changes.  Also checks
for any labor warnings the user needs to be aware of
   OperationID: VerifyScrapQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VerifyScrapQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyScrapQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifyScrapQty(requestBody:VerifyScrapQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VerifyScrapQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/VerifyScrapQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as VerifyScrapQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartQty
   Description: This method sets Complete checkbox when part qty field changes in End Activity.
   OperationID: OnChangePartQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartQty(requestBody:OnChangePartQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/OnChangePartQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePartQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultLaborType
   Description: This method defaults dataset fields when the LaborType field changes.
   OperationID: DefaultLaborType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultLaborType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultLaborType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultLaborType(requestBody:DefaultLaborType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultLaborType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultLaborType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultLaborType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultLunchBreak
   Description: This method defaults the Lunch Time fields when the Lunch Break field changes.
   OperationID: DefaultLunchBreak
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultLunchBreak_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultLunchBreak_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultLunchBreak(requestBody:DefaultLunchBreak_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultLunchBreak_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultLunchBreak", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultLunchBreak_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultNextOprSeq
   Description: This method updates the dataset after next operation seq is set
   OperationID: DefaultNextOprSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultNextOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultNextOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultNextOprSeq(requestBody:DefaultNextOprSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultNextOprSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultNextOprSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultNextOprSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultOpCode
   Description: This method checks for any warnings user needs to know on change of OpCode
   OperationID: DefaultOpCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultOpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultOpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultOpCode(requestBody:DefaultOpCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultOpCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultOpCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultOpCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultOprSeq
   Description: This method defaults fields when Operation sequence changes.  Also returns any
warnings user needs to know.
   OperationID: DefaultOprSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultOprSeq(requestBody:DefaultOprSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultOprSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultOprSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultOprSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborDtlOnSelectForWork
   Description: Call GetNewLaborDtl base method then assign selected values and default values for MES/Work Queue/Select for Work.
ResourceID is defaulted the same way than for MES- Start Production Activity. ResourceID must be required only if Company Configuration MachinePrompt is true, otherwise is optional.
   OperationID: GetNewLaborDtlOnSelectForWork
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlOnSelectForWork_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlOnSelectForWork_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborDtlOnSelectForWork(requestBody:GetNewLaborDtlOnSelectForWork_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborDtlOnSelectForWork_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLaborDtlOnSelectForWork", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborDtlOnSelectForWork_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultPhaseID
   Description: This method defaults dataset fields when the PhaseID field changes.
   OperationID: DefaultPhaseID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultPhaseID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultPhaseID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultPhaseID(requestBody:DefaultPhaseID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultPhaseID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultPhaseID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultPhaseID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultPhaseOprSeq
   Description: This method defaults dataset fields when the PhaseOprSeq field changes.
   OperationID: DefaultPhaseOprSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultPhaseOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultPhaseOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultPhaseOprSeq(requestBody:DefaultPhaseOprSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultPhaseOprSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultPhaseOprSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultPhaseOprSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultProjectID
   Description: This method defaults dataset fields when the ProjectID field changes.
   OperationID: DefaultProjectID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultProjectID(requestBody:DefaultProjectID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultProjectID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultProjectID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultProjectID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultResourceID
   Description: This method updates dataset fields when the ResourceID field changes.
   OperationID: DefaultResourceID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultResourceID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultResourceID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultResourceID(requestBody:DefaultResourceID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultResourceID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultResourceID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultResourceID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultRoleCd
   Description: This method defaults dataset fields when the RoleCd field changes.
   OperationID: DefaultRoleCd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultRoleCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultRoleCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultRoleCd(requestBody:DefaultRoleCd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultRoleCd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultRoleCd", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultRoleCd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultScrapReasonCode
   Description: This method defaults fields when the scrap reason code fields changes.  Also checks
for any labor warnings the user needs to be aware of
   OperationID: DefaultScrapReasonCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultScrapReasonCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultScrapReasonCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultScrapReasonCode(requestBody:DefaultScrapReasonCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultScrapReasonCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultScrapReasonCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultScrapReasonCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultSetupPctComplete
   Description: This method validates and reassigns the setup percent complete field.
   OperationID: DefaultSetupPctComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultSetupPctComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultSetupPctComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultSetupPctComplete(requestBody:DefaultSetupPctComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultSetupPctComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultSetupPctComplete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultSetupPctComplete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultShift
   Description: This method updates clock in/out and lunch in/out fields after shift field changes
   OperationID: DefaultShift
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultShift_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultShift_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultShift(requestBody:DefaultShift_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultShift_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultShift", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultShift_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultTime
   Description: This method updates time and pay hours when a time field changes
   OperationID: DefaultTime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultTime(requestBody:DefaultTime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultTime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultTime", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultTime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultTimeTypCd
   Description: This method defaults dataset fields when the TimeTypCd field changes.
   OperationID: DefaultTimeTypCd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultTimeTypCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultTimeTypCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultTimeTypCd(requestBody:DefaultTimeTypCd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultTimeTypCd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultTimeTypCd", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultTimeTypCd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultWCCode
   Description: This method updates dataset fields when the ResourceGroup field changes.  Also checks
for any warning the user needs to know
   OperationID: DefaultWCCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultWCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultWCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultWCCode(requestBody:DefaultWCCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultWCCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DefaultWCCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultWCCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteLaborDtl
   Description: This method delete records related to HCM PTO.
   OperationID: DeleteLaborDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteLaborDtl(requestBody:DeleteLaborDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteLaborDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/DeleteLaborDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteLaborDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EndActivity
   Description: Method to call to end an activity in Shop Floor.  This method will mark
the EndActivity flag in LaborDtl so when the Update method is run, special
end activity processing can occur.  It will also default values in other
fields that apply to the end activity.  Before this method is called, the
LaborDtl.RowMod value needs to be set to 'U'.
   OperationID: EndActivity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/EndActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EndActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EndActivity(requestBody:EndActivity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<EndActivity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/EndActivity", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as EndActivity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EndActivityComplete
   Description: This method checks for any necessary labor warning when the complete flag is checked in MES End Activity
   OperationID: EndActivityComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/EndActivityComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EndActivityComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EndActivityComplete(requestBody:EndActivityComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<EndActivityComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/EndActivityComplete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as EndActivityComplete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetActiveLaborDtl
   Description: Method to retrieve the active Labor Details and header records by employee.
   OperationID: GetActiveLaborDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetActiveLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActiveLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetActiveLaborDtl(requestBody:GetActiveLaborDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetActiveLaborDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetActiveLaborDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetActiveLaborDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InitiateDowntime
   Description: Method to Begin Downtime for Kinetic MES
   OperationID: InitiateDowntime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InitiateDowntime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitiateDowntime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitiateDowntime(requestBody:InitiateDowntime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InitiateDowntime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/InitiateDowntime", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as InitiateDowntime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EndDowntime
   Description: Method to End Downtime for Kinetic MES
   OperationID: EndDowntime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/EndDowntime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EndDowntime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EndDowntime(requestBody:EndDowntime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<EndDowntime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/EndDowntime", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as EndDowntime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDetail
   Description: Method to call to retrieve the Labor dataset with just the header
and a specific detail record.
   OperationID: GetDetail
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDetail(requestBody:GetDetail_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDetail_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetDetail", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDetail_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method getElapsedTime
   Description: This method gets the elapsed time from a start date-startTime until now
   OperationID: getElapsedTime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/getElapsedTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getElapsedTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getElapsedTime(requestBody:getElapsedTime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<getElapsedTime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/getElapsedTime", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as getElapsedTime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborDtlNoHdr
   Description: This method is called to add a new labor detail without having a
labor header record available
   OperationID: GetNewLaborDtlNoHdr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlNoHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlNoHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborDtlNoHdr(requestBody:GetNewLaborDtlNoHdr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborDtlNoHdr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLaborDtlNoHdr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborDtlNoHdr_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborDtlWithHdr
   Description: This method is called to add a new labor detail without having a
labor header record available
   OperationID: GetNewLaborDtlWithHdr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlWithHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlWithHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborDtlWithHdr(requestBody:GetNewLaborDtlWithHdr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborDtlWithHdr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLaborDtlWithHdr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborDtlWithHdr_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborHed1
   Description: This method to be used in place of GetNewLaborHed.  This method asks for an
employee number to default fields based on the employee.
   OperationID: GetNewLaborHed1
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborHed1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborHed1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborHed1(requestBody:GetNewLaborHed1_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborHed1_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLaborHed1", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborHed1_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLbrScrapSerialNumbers
   Description: Gets a new LbrScrapSerialNumbers record for current LaborDtl
   OperationID: GetNewLbrScrapSerialNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLbrScrapSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLbrScrapSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLbrScrapSerialNumbers(requestBody:GetNewLbrScrapSerialNumbers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLbrScrapSerialNumbers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewLbrScrapSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLbrScrapSerialNumbers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTimeWeeklyView
   Description: Gets a new TimeWeeklyView record for the current week
   OperationID: GetNewTimeWeeklyView
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTimeWeeklyView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTimeWeeklyView_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTimeWeeklyView(requestBody:GetNewTimeWeeklyView_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTimeWeeklyView_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetNewTimeWeeklyView", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewTimeWeeklyView_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCalendarView
   OperationID: GetRowsCalendarView
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsCalendarView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCalendarView_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCalendarView(requestBody:GetRowsCalendarView_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsCalendarView_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetRowsCalendarView", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsCalendarView_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsWhoIsHere
   OperationID: GetRowsWhoIsHere
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsWhoIsHere_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWhoIsHere_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsWhoIsHere(requestBody:GetRowsWhoIsHere_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsWhoIsHere_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetRowsWhoIsHere", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsWhoIsHere_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTERetrieveApproved
   Description: Method to get the value UserFile.TERetrieveApproved
   OperationID: GetTERetrieveApproved
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTERetrieveApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTERetrieveApproved(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTERetrieveApproved_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetTERetrieveApproved", {
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
         resolve(data as GetTERetrieveApproved_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTERetrieveByOption
   Description: Method to get retrieve by options
   OperationID: GetTERetrieveByOption
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTERetrieveByOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTERetrieveByOption(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTERetrieveByOption_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetTERetrieveByOption", {
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
         resolve(data as GetTERetrieveByOption_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTERetrieveEntered
   Description: Method to get the value UserFile.TERetrieveEntered
   OperationID: GetTERetrieveEntered
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTERetrieveEntered_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTERetrieveEntered(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTERetrieveEntered_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetTERetrieveEntered", {
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
         resolve(data as GetTERetrieveEntered_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTERetrievePartiallyApproved
   Description: Method to get the value UserFile.TERetrievePartiallyApproved
   OperationID: GetTERetrievePartiallyApproved
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTERetrievePartiallyApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTERetrievePartiallyApproved(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTERetrievePartiallyApproved_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetTERetrievePartiallyApproved", {
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
         resolve(data as GetTERetrievePartiallyApproved_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTERetrieveRejected
   Description: Method to get the value UserFile.TERetrieveRejected
   OperationID: GetTERetrieveRejected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTERetrieveRejected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTERetrieveRejected(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTERetrieveRejected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetTERetrieveRejected", {
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
         resolve(data as GetTERetrieveRejected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTERetrieveSubmitted
   Description: Method to get the value UserFile.TERetrieveSubmitted
   OperationID: GetTERetrieveSubmitted
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTERetrieveSubmitted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTERetrieveSubmitted(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTERetrieveSubmitted_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetTERetrieveSubmitted", {
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
         resolve(data as GetTERetrieveSubmitted_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsValidAssembly
   Description: Validate if an assembly is valid for a job. if not returns false,
otherwise returns true.
   OperationID: IsValidAssembly
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsValidAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsValidAssembly(requestBody:IsValidAssembly_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsValidAssembly_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/IsValidAssembly", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as IsValidAssembly_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LaborDtlAfterGetRowsWrapper
   Description: Calls LaborDtlAfterGetRows for the passed in LaborDtl row
   OperationID: LaborDtlAfterGetRowsWrapper
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LaborDtlAfterGetRowsWrapper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LaborDtlAfterGetRowsWrapper_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborDtlAfterGetRowsWrapper(requestBody:LaborDtlAfterGetRowsWrapper_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LaborDtlAfterGetRowsWrapper_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlAfterGetRowsWrapper", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LaborDtlAfterGetRowsWrapper_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LaborRateCalc
   OperationID: LaborRateCalc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LaborRateCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LaborRateCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborRateCalc(requestBody:LaborRateCalc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LaborRateCalc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborRateCalc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LaborRateCalc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeClockInDate
   Description: Call this procedure when LaborDtl.ClockInDate changes
   OperationID: OnChangeClockInDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeClockInDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClockInDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeClockInDate(requestBody:OnChangeClockInDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeClockInDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/OnChangeClockInDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeClockInDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCID
   Description: This method validates the PCID
   OperationID: OnChangePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCID(requestBody:OnChangePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/OnChangePCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeQuickEntryCode
   Description: This method validates field QuickEntryCode, and if it is valid, uses the
values from the QuickEntry record to populate the LaborDtl values.
   OperationID: OnChangeQuickEntryCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeQuickEntryCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuickEntryCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeQuickEntryCode(requestBody:OnChangeQuickEntryCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeQuickEntryCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/OnChangeQuickEntryCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeQuickEntryCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeResourceGrpID
   Description: Call this procedure when TimeWeeklyView.ResourceGrpID changes
   OperationID: OnChangeResourceGrpID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeResourceGrpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResourceGrpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeResourceGrpID(requestBody:OnChangeResourceGrpID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeResourceGrpID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/OnChangeResourceGrpID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeResourceGrpID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnLoadEndActivity
   Description: Call this method when loading end activity on Kinetic-MES.
   OperationID: OnLoadEndActivity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnLoadEndActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnLoadEndActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnLoadEndActivity(requestBody:OnLoadEndActivity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnLoadEndActivity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/OnLoadEndActivity", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnLoadEndActivity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Overrides
   Description: Call this procedure to override the Resource Group and Operation Code in a
job.
   OperationID: Overrides
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Overrides_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Overrides_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Overrides(requestBody:Overrides_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Overrides_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Overrides", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Overrides_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OverridesResource
   Description: Call this procedure to override the Resource in a LaborDtl record
   OperationID: OverridesResource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OverridesResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OverridesResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OverridesResource(requestBody:OverridesResource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OverridesResource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/OverridesResource", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OverridesResource_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecallFromApproval
   Description: Method to recall Labor for Approval.
   OperationID: RecallFromApproval
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RecallFromApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallFromApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecallFromApproval(requestBody:RecallFromApproval_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RecallFromApproval_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/RecallFromApproval", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RecallFromApproval_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectForWork
   Description: This method is intended to be used when the MES/ShopFloor user selects an
operation from the WorkQueue to work on.  Use this method in place of the
Update method in this situation.
            
This method expects a LaborDataSet containing a single LaborHed with a
RowMod indicating a changed row, and a LaborDtl row with a RowMod indicating
a changed row.  This can be obtained with a call to Labor.GetRows() with a
whereClauseLaborHed of
ActiveTrans = YES and EmployeeNum = xxxx
substituting the desired employeeNum for the xxxx.
followed by a call to LaborDtlGetNew.
            
After validating the given Job, Assembly, Operation, ResourceID, ResourceGrpID
and LaborType, and additional validations are applied, the LaborDtl is updated.
            
An exception is thrown if:
- a changed Laborhed row is not found.
- the given Job, Assembly and Operation is not valid
- the LaborHed.ActiveTrans = no.  This method is for MES (ShopFloor) use only.
- the given LaborType is not "S" or "P"
   OperationID: SelectForWork
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectForWork_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectForWork_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectForWork(requestBody:SelectForWork_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectForWork_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectForWork", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SelectForWork_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectForWorkCheckWarnings
   Description: This method runs the shop warning routine and returns any warnings the user needs
to be aware of.  This needs to be run right before the SelectForWork method.  If the user answers
okay to all of the questions, then the SelectForWork method can be run.  Otherwise the labor record
needs to be corrected
   OperationID: SelectForWorkCheckWarnings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectForWorkCheckWarnings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectForWorkCheckWarnings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectForWorkCheckWarnings(requestBody:SelectForWorkCheckWarnings_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectForWorkCheckWarnings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectForWorkCheckWarnings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SelectForWorkCheckWarnings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetClockInAndDisplayTimeMES
   Description: Sets the Time Stamp in which the Employee Starts his/her activity and
also populates the field that displays the time correctly.
   OperationID: SetClockInAndDisplayTimeMES
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetClockInAndDisplayTimeMES_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetClockInAndDisplayTimeMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetClockInAndDisplayTimeMES(requestBody:SetClockInAndDisplayTimeMES_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetClockInAndDisplayTimeMES_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SetClockInAndDisplayTimeMES", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetClockInAndDisplayTimeMES_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetTERetrieveApproved
   Description: Method to set the value UserFile.TERetrieveApproved
   OperationID: SetTERetrieveApproved
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetTERetrieveApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetTERetrieveApproved(requestBody:SetTERetrieveApproved_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetTERetrieveApproved_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SetTERetrieveApproved", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetTERetrieveApproved_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetTERetrieveByDay
   Description: Method to set the value for retrieve by day
   OperationID: SetTERetrieveByDay
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetTERetrieveByDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveByDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetTERetrieveByDay(requestBody:SetTERetrieveByDay_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetTERetrieveByDay_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SetTERetrieveByDay", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetTERetrieveByDay_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetTERetrieveByMonth
   Description: Method to set the value for retrieve by month
   OperationID: SetTERetrieveByMonth
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetTERetrieveByMonth_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveByMonth_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetTERetrieveByMonth(requestBody:SetTERetrieveByMonth_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetTERetrieveByMonth_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SetTERetrieveByMonth", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetTERetrieveByMonth_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetTERetrieveByWeek
   Description: Method to set the value for retrieve by week
   OperationID: SetTERetrieveByWeek
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetTERetrieveByWeek_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveByWeek_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetTERetrieveByWeek(requestBody:SetTERetrieveByWeek_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetTERetrieveByWeek_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SetTERetrieveByWeek", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetTERetrieveByWeek_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetTERetrieveEntered
   Description: Method to set the value UserFile.TERetrieveEntered
   OperationID: SetTERetrieveEntered
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetTERetrieveEntered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveEntered_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetTERetrieveEntered(requestBody:SetTERetrieveEntered_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetTERetrieveEntered_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SetTERetrieveEntered", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetTERetrieveEntered_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetTERetrievePartiallyApproved
   Description: Method to set the value UserFile.TERetrievePartiallyApproved
   OperationID: SetTERetrievePartiallyApproved
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetTERetrievePartiallyApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrievePartiallyApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetTERetrievePartiallyApproved(requestBody:SetTERetrievePartiallyApproved_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetTERetrievePartiallyApproved_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SetTERetrievePartiallyApproved", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetTERetrievePartiallyApproved_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetTERetrieveRejected
   Description: Method to set the value UserFile.TERetrieveRejected
   OperationID: SetTERetrieveRejected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetTERetrieveRejected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveRejected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetTERetrieveRejected(requestBody:SetTERetrieveRejected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetTERetrieveRejected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SetTERetrieveRejected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetTERetrieveRejected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetTERetrieveSubmitted
   Description: Method to set the value UserFile.TERetrieveSubmitted
   OperationID: SetTERetrieveSubmitted
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetTERetrieveSubmitted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveSubmitted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetTERetrieveSubmitted(requestBody:SetTERetrieveSubmitted_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetTERetrieveSubmitted_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SetTERetrieveSubmitted", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetTERetrieveSubmitted_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method StartActivity
   Description: Method to call to start an activity in Shop Floor.
   OperationID: StartActivity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/StartActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartActivity(requestBody:StartActivity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<StartActivity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/StartActivity", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as StartActivity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method StartActivityByEmp
   Description: Method to call to start an activity in Shop Floor by Employee.
   OperationID: StartActivityByEmp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/StartActivityByEmp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartActivityByEmp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartActivityByEmp(requestBody:StartActivityByEmp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<StartActivityByEmp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/StartActivityByEmp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as StartActivityByEmp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SubmitForApproval
   Description: Method to submit Labor for Approval.
   OperationID: SubmitForApproval
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SubmitForApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitForApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitForApproval(requestBody:SubmitForApproval_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SubmitForApproval_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SubmitForApproval", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SubmitForApproval_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateIndirectCodeIsDowntime
   Description: This method validates the IndirectCode is marked as Downtime
   OperationID: ValidateIndirectCodeIsDowntime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateIndirectCodeIsDowntime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateIndirectCodeIsDowntime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateIndirectCodeIsDowntime(requestBody:ValidateIndirectCodeIsDowntime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateIndirectCodeIsDowntime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ValidateIndirectCodeIsDowntime", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateIndirectCodeIsDowntime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method validateNonConfProcessed
   Description: This method validates the Non Conformance value and validates if it has already been processed
   OperationID: validateNonConfProcessed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/validateNonConfProcessed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/validateNonConfProcessed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_validateNonConfProcessed(requestBody:validateNonConfProcessed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<validateNonConfProcessed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/validateNonConfProcessed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as validateNonConfProcessed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateProjectClosed
   Description: this method validates if the Project linked to the Job in Labor Detail is closed.
   OperationID: ValidateProjectClosed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateProjectClosed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateProjectClosed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateProjectClosed(requestBody:ValidateProjectClosed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateProjectClosed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ValidateProjectClosed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateProjectClosed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSerialAfterSelect
   Description: Validates after calling SN selection screen
   OperationID: ValidateSerialAfterSelect
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSerialAfterSelect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialAfterSelect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSerialAfterSelect(requestBody:ValidateSerialAfterSelect_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSerialAfterSelect_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ValidateSerialAfterSelect", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateSerialAfterSelect_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSerialScanInterface
   Description: Validates if serial number is valid after selecting SN on scan interface kinetic MES
   OperationID: ValidateSerialScanInterface
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSerialScanInterface_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialScanInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSerialScanInterface(requestBody:ValidateSerialScanInterface_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSerialScanInterface_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ValidateSerialScanInterface", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateSerialScanInterface_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSerialBeforeSelect
   Description: Call before allowing the select of serial numbers
   OperationID: ValidateSerialBeforeSelect
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSerialBeforeSelect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialBeforeSelect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSerialBeforeSelect(requestBody:ValidateSerialBeforeSelect_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSerialBeforeSelect_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ValidateSerialBeforeSelect", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateSerialBeforeSelect_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VerifySerialMatch
   Description: Verifies if the user should enter child serial numbers for the serial numbers
being received depending on the setting of the Serial Number Matching before save.
   OperationID: VerifySerialMatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VerifySerialMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifySerialMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifySerialMatch(requestBody:VerifySerialMatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VerifySerialMatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/VerifySerialMatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as VerifySerialMatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetClockTime
   Description: This method is called to update the values of the Display columns
DspClockInTime and DspClockOutTime
   OperationID: GetClockTime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetClockTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetClockTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetClockTime(requestBody:GetClockTime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetClockTime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetClockTime", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetClockTime_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetDspClockTime
   Description: This method is called to update the values of the Display columns
DspClockInTime and DspClockOutTime
   OperationID: GetDspClockTime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDspClockTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDspClockTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDspClockTime(requestBody:GetDspClockTime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDspClockTime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetDspClockTime", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDspClockTime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReportPartQtyAllowed
   Description: Returns TRUE if Part Quantity Reporting is allowed for a given operation.
   OperationID: ReportPartQtyAllowed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReportPartQtyAllowed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReportPartQtyAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReportPartQtyAllowed(requestBody:ReportPartQtyAllowed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReportPartQtyAllowed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ReportPartQtyAllowed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ReportPartQtyAllowed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExternalMESDowntime
   Description: Methods updates Downtime codes
   OperationID: ExternalMESDowntime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExternalMESDowntime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExternalMESDowntime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExternalMESDowntime(requestBody:ExternalMESDowntime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExternalMESDowntime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ExternalMESDowntime", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExternalMESDowntime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExternalMESEndDowntime
   Description: Methods updates Downtime codes
   OperationID: ExternalMESEndDowntime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExternalMESEndDowntime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExternalMESEndDowntime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExternalMESEndDowntime(requestBody:ExternalMESEndDowntime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExternalMESEndDowntime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ExternalMESEndDowntime", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExternalMESEndDowntime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HCMGetLaborRecords
   Description: Description: Public method which retrieves the labor information HCM third party requires.
   OperationID: HCMGetLaborRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HCMGetLaborRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HCMGetLaborRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HCMGetLaborRecords(requestBody:HCMGetLaborRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HCMGetLaborRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/HCMGetLaborRecords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as HCMGetLaborRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HCMSetLaborStatus
   OperationID: HCMSetLaborStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HCMSetLaborStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HCMSetLaborStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HCMSetLaborStatus(requestBody:HCMSetLaborStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HCMSetLaborStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/HCMSetLaborStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as HCMSetLaborStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateChargeRateForTimeType
   Description: Validates if there is no valid Charge Rate according to selected Time Type.
This validation can also be found on BO/LaborApproval.
   OperationID: ValidateChargeRateForTimeType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateChargeRateForTimeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateChargeRateForTimeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateChargeRateForTimeType(requestBody:ValidateChargeRateForTimeType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateChargeRateForTimeType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ValidateChargeRateForTimeType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateChargeRateForTimeType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReviewIsDocumentLock
   Description: Review if the document is Lock when user tries to recall the record from UI
   OperationID: ReviewIsDocumentLock
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReviewIsDocumentLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReviewIsDocumentLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReviewIsDocumentLock(requestBody:ReviewIsDocumentLock_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReviewIsDocumentLock_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ReviewIsDocumentLock", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ReviewIsDocumentLock_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsHCMEnabledAtCompany
   Description: Returns true if HCM is enable at company level.
   OperationID: IsHCMEnabledAtCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsHCMEnabledAtCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsHCMEnabledAtCompany(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsHCMEnabledAtCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/IsHCMEnabledAtCompany", {
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
         resolve(data as IsHCMEnabledAtCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTimeWeeklyViewWeekBeginDate
   Description: Called when Time Weekly View Week Begin Date is changing
   OperationID: ChangeTimeWeeklyViewWeekBeginDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTimeWeeklyViewWeekBeginDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTimeWeeklyViewWeekBeginDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTimeWeeklyViewWeekBeginDate(requestBody:ChangeTimeWeeklyViewWeekBeginDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTimeWeeklyViewWeekBeginDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ChangeTimeWeeklyViewWeekBeginDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTimeWeeklyViewWeekBeginDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLaborDtlOprSeq
   Description: This method defaults LaborDtl fields when Operation sequence changes.  Also returns any
warnings user needs to know.
   OperationID: ChangeLaborDtlOprSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLaborDtlOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborDtlOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborDtlOprSeq(requestBody:ChangeLaborDtlOprSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLaborDtlOprSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ChangeLaborDtlOprSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeLaborDtlOprSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLaborDtlScrapQty
   Description: This method defaults fields when the scrap qty field changes.
   OperationID: ChangeLaborDtlScrapQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLaborDtlScrapQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborDtlScrapQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborDtlScrapQty(requestBody:ChangeLaborDtlScrapQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLaborDtlScrapQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ChangeLaborDtlScrapQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeLaborDtlScrapQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLaborDtlAttributeSetID
   Description: This method updates the revision field when the attribute ID field changes.
   OperationID: ChangeLaborDtlAttributeSetID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLaborDtlAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborDtlAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborDtlAttributeSetID(requestBody:ChangeLaborDtlAttributeSetID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLaborDtlAttributeSetID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ChangeLaborDtlAttributeSetID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeLaborDtlAttributeSetID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AfterChangeLaborDtlDiscrepQty
   Description: Called after LaborDtl.DiscrepQty has been changed.
   OperationID: AfterChangeLaborDtlDiscrepQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AfterChangeLaborDtlDiscrepQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterChangeLaborDtlDiscrepQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AfterChangeLaborDtlDiscrepQty(requestBody:AfterChangeLaborDtlDiscrepQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AfterChangeLaborDtlDiscrepQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/AfterChangeLaborDtlDiscrepQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AfterChangeLaborDtlDiscrepQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLaborDtlTimeField
   Description: Called when labor clock in or clock out time is changing
   OperationID: ChangeLaborDtlTimeField
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLaborDtlTimeField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborDtlTimeField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborDtlTimeField(requestBody:ChangeLaborDtlTimeField_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLaborDtlTimeField_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ChangeLaborDtlTimeField", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeLaborDtlTimeField_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLaborDtlDspTimeField
   Description: Called when labor display clock in or clock out time is changing
   OperationID: ChangeLaborDtlDspTimeField
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLaborDtlDspTimeField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborDtlDspTimeField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborDtlDspTimeField(requestBody:ChangeLaborDtlDspTimeField_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLaborDtlDspTimeField_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/ChangeLaborDtlDspTimeField", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeLaborDtlDspTimeField_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetJobProductionCompanySettings
   Description: Returns company job production settings for Advance Labor Rate, Clock Format
   OperationID: GetJobProductionCompanySettings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobProductionCompanySettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJobProductionCompanySettings(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetJobProductionCompanySettings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetJobProductionCompanySettings", {
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
         resolve(data as GetJobProductionCompanySettings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SubmitForApprovalBySelected
   Description: Method to submit Labor for Approval using RowSelected flag.
   OperationID: SubmitForApprovalBySelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SubmitForApprovalBySelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitForApprovalBySelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitForApprovalBySelected(requestBody:SubmitForApprovalBySelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SubmitForApprovalBySelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SubmitForApprovalBySelected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SubmitForApprovalBySelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecallFromApprovalBySelected
   Description: Method to recall Labor for Approval using RowSelected flag.
   OperationID: RecallFromApprovalBySelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RecallFromApprovalBySelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallFromApprovalBySelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecallFromApprovalBySelected(requestBody:RecallFromApprovalBySelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RecallFromApprovalBySelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/RecallFromApprovalBySelected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RecallFromApprovalBySelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyLaborDtlBySelected
   Description: Method to copy Labor detail record(s) using RowSelected flag.
   OperationID: CopyLaborDtlBySelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyLaborDtlBySelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyLaborDtlBySelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyLaborDtlBySelected(requestBody:CopyLaborDtlBySelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyLaborDtlBySelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/CopyLaborDtlBySelected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CopyLaborDtlBySelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyTimeWeeklyViewBySelected
   Description: Method to copy TimeWeeklyView record(s) using RowSelected flag.
   OperationID: CopyTimeWeeklyViewBySelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyTimeWeeklyViewBySelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyTimeWeeklyViewBySelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyTimeWeeklyViewBySelected(requestBody:CopyTimeWeeklyViewBySelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyTimeWeeklyViewBySelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/CopyTimeWeeklyViewBySelected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CopyTimeWeeklyViewBySelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsTimeEntry
   Description: Get rows for Time Entry.  This method will consider user time retrieval options for retrieving approved, entered, partially approved, rejected, and submitted records.
   OperationID: GetRowsTimeEntry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsTimeEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsTimeEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsTimeEntry(requestBody:GetRowsTimeEntry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsTimeEntry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetRowsTimeEntry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsTimeEntry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLaborTypeList
   Description: Returns valid labor types based on the employee
   OperationID: GetLaborTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLaborTypeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLaborTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLaborTypeList(requestBody:GetLaborTypeList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLaborTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/GetLaborTypeList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetLaborTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateLbrScrapSerialNumbersFromList
   Description: Create LbrScrapSerialNumbers dataset records from a list of selected serial numbers
   OperationID: CreateLbrScrapSerialNumbersFromList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateLbrScrapSerialNumbersFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateLbrScrapSerialNumbersFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateLbrScrapSerialNumbersFromList(requestBody:CreateLbrScrapSerialNumbersFromList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateLbrScrapSerialNumbersFromList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/CreateLbrScrapSerialNumbersFromList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateLbrScrapSerialNumbersFromList_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlActionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborDtlActionRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborDtlAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlCommentRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborDtlCommentRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlGroupRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborDtlGroupRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborEquipRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborEquipRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborHedListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborHedRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborPartRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborPartRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LbrScrapSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LbrScrapSerialNumbersRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TimeWeeklyViewRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TimeWeeklyViewRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TimeWorkHoursRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TimeWorkHoursRow,
}

export interface Erp_Tablesets_LaborDtlActionRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Used as the foreign key to the LaborDtl record.  */  
   "LaborHedSeq":number,
      /**  Used as the foreign key to the LaborDtl record.  */  
   "LaborDtlSeq":number,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   "ActionSeq":number,
      /**  Description of Action.  */  
   "ActionDesc":string,
      /**  Indicated if this Action must be completed before Operation can be completed.  */  
   "Required":boolean,
      /**  Indicates if this Action was completed.  */  
   "Completed":boolean,
      /**  The number of the employee that performed the work.  */  
   "CompletedBy":string,
      /**  Date the Action was completed.  */  
   "CompletedOn":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
   "EmpBasicName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborDtlAttchRow{
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

export interface Erp_Tablesets_LaborDtlCommentRow{
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
   "DspChangeTime":string,
   "DspCreateTime":string,
   "TreeNodeImageName":string,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
      /**  List of valid comment types for Time Entry  */  
   "TimeEntryCommentTypeList":string,
   "CommentTypeDesc":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborDtlGroupRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are

concurrently active for an employee in order to distribute the labor hours.  */  
   "EmployeeNum":string,
      /**  Brief description of the expense.  Can be used to expenses together, for example, all expenses incurred on the same trip can be assigned the same reference.  */  
   "ClaimRef":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborDtlRow{
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
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  */  
   "DiscrepAttributeSetID":number,
      /**  The unique identifier of the related Dynamic Attribute Set for the Labor Qty  */  
   "LaborAttributeSetID":number,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  */  
   "ScrapAttributeSetID":number,
      /**  PCID  */  
   "PCID":string,
      /**  NonConfPCID  */  
   "NonConfPCID":string,
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   "AllowDirLbr":boolean,
      /**  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalPhaseDesc":string,
      /**  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalPhaseID":string,
      /**  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalProjectDesc":string,
      /**  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalProjectID":string,
   "ApprovedBy":string,
      /**  Used in approval entry.  Indicates if the approver has an open task or not.  */  
   "ApprvrHasOpenTask":boolean,
      /**  Company Base currency code description for display in LaborDtl grid.  */  
   "BaseCurrCodeDesc":string,
      /**  calculated field: BurdenHrs * BurdenRate  */  
   "BurdenCost":number,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "CallCode":string,
   "CapabilityDescription":string,
   "CapabilityID":string,
      /**  Charge rate calculated for Time and Expense approval  */  
   "ChargeRate":number,
      /**  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  */  
   "ChargeRateSRC":string,
      /**  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  */  
   "ChgRateCurrDesc":string,
   "CompleteFlag":boolean,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "ContractCode":string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "ContractNum":number,
      /**  Unit of Measure used for DiscrepQty  */  
   "DiscrepUOM":string,
      /**  Field that indicates if field DisLaborTypeshould be disabled.  */  
   "DisLaborType":boolean,
   "DisplayJob":string,
      /**  Field that indicates if field PrjRoleCd should be disabled.  */  
   "DisPrjRoleCd":boolean,
      /**  Field that indicates if field TimeTypCd should be disabled.  */  
   "DisTimeTypCd":boolean,
   "DowntimeTotal":number,
   "DspChangeTime":string,
   "DspCreateTime":string,
   "DspTotHours":string,
   "DtClockIn":string,
   "DtClockOut":string,
      /**  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  */  
   "EfficiencyPercentage":number,
      /**  Labor Detail Employee Name  */  
   "EmployeeName":string,
   "EnableComplete":boolean,
      /**  Indicates if the copy button is enabled  */  
   "EnableCopy":boolean,
   "EnableDiscrepQty":boolean,
   "EnableInspection":boolean,
   "EnableLaborQty":boolean,
   "EnableNextOprSeq":boolean,
   "EnablePrintTagsList":boolean,
      /**  Indicates if the recall button is enabled  */  
   "EnableRecall":boolean,
      /**  Indicates if recall is available for an approver  */  
   "EnableRecallAprv":boolean,
   "EnableRequestMove":boolean,
   "EnableResourceGrpID":boolean,
   "EnableScrapQty":boolean,
      /**  Enable the SN Button?  */  
   "EnableSN":boolean,
      /**  Indicates if the submit button is enabled  */  
   "EnableSubmit":boolean,
   "EndActivity":boolean,
      /**  To know if the LaborDtl was created on the current plant  */  
   "EnteredOnCurPlant":boolean,
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
   "FSComplete":boolean,
      /**  GL Journal Source Transaction Amount  */  
   "GLTranAmt":number,
      /**  GL Journal Source Transaction Date  */  
   "GLTranDate":string,
      /**  Indicates if the user has access to the row  */  
   "HasAccessToRow":boolean,
      /**  Indicates if the labor detail has comments  */  
   "HasComments":boolean,
      /**  To tell the bo that this transaction was being modified from HH.  */  
   "HH":boolean,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
      /**  Indicates if the job operation is marked as fixed hours and quantity only.  */  
   "ISFixHourAndQtyOnly":boolean,
   "JCSystReworkReasons":boolean,
   "JCSystScrapReasons":boolean,
   "JobOperComplete":boolean,
   "JobType":string,
      /**  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  */  
   "JobTypeCode":string,
      /**  calculated field: LaborHrs * LaborRate  */  
   "LaborCost":number,
      /**  Unit of Measure used for LaborQty  */  
   "LaborUOM":string,
      /**  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  */  
   "LbrDay":string,
      /**  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  */  
   "LbrMonth":string,
      /**  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  */  
   "LbrWeek":string,
   "MES":boolean,
   "MultipleEmployeesText":string,
   "NewDifDateFlag":number,
      /**  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  */  
   "NewPrjRoleCd":string,
      /**  Holds the description for NewPrjRoleCd  */  
   "NewRoleCdDesc":string,
   "NextAssemblySeq":number,
   "NextOperDesc":string,
   "NextOprSeq":number,
   "NextResourceDesc":string,
      /**  To evaluate if the NonComformance has been already processed in inspection and no changes can be applied on LaborDtl then.  */  
   "NonConfProcessed":boolean,
   "NotSubmitted":boolean,
      /**  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  */  
   "OkToChangeResourceGrpID":boolean,
   "PartDescription":string,
   "PartNum":string,
   "PBAllowModify":boolean,
   "PendingApprovalBy":string,
      /**  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  */  
   "PhaseJobNum":string,
      /**  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  */  
   "PhaseOprSeq":number,
   "PrintNCTag":boolean,
   "PrjUsedTran":string,
   "ProdDesc":string,
   "ProjPhaseID":string,
   "RequestMove":boolean,
   "ResourceDesc":string,
   "RoleCdDisplayAll":boolean,
      /**  Unit of Measure used for ScrapQty.  */  
   "ScrapUOM":string,
      /**  Flag field to identify if the row is being sent from MES  */  
   "SentFromMES":boolean,
   "StartActivity":boolean,
   "TimeDisableDelete":boolean,
   "TimeDisableUpdate":boolean,
   "TreeNodeImageName":string,
   "UnapprovedFirstArt":boolean,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   "WarrantyCode":string,
   "WeekDisplayText":string,
      /**  EnablePCID  */  
   "EnablePCID":boolean,
      /**  The output bin from the resource  */  
   "OutputBin":string,
      /**  The output warehouse from the resource  */  
   "OutputWarehouse":string,
      /**  Internal flag used for the row rules to control whether the Lot columns should be enabled.  */  
   "EnableLot":boolean,
      /**  Lot number that is to be added to the PCID  */  
   "LotNum":string,
      /**  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  */  
   "PrintPCIDContents":boolean,
      /**  Indicates if the labor detail has attachments  */  
   "HasAttachments":boolean,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set for DiscrepQty  */  
   "DiscrepAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set for DiscrepQty  */  
   "DiscrepAttributeSetShortDescription":string,
      /**  The Full Description of the Attribute Set for ScrapQty  */  
   "ScrapAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set for ScrapQty  */  
   "ScrapAttributeSetShortDescription":string,
      /**  The Full Description of the Attribute Set for LaborQty  */  
   "LaborAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set for LaborQty  */  
   "LaborAttributeSetShortDescription":string,
      /**  Indicates if recall and delete should be disabled  */  
   "DisableRecallAndDelete":boolean,
      /**  List of available role codes  */  
   "RoleCdList":string,
      /**  Indicates if the row is selected for submit, recall, or copy  */  
   "RowSelected":boolean,
      /**  Start date/time for calendar appoinment  */  
   "AppointmentStart":string,
      /**  End date/time for calendar appoinment  */  
   "AppointmentEnd":string,
      /**  Title to display for the calendar appointment  */  
   "AppointmentTitle":string,
      /**  PDF Form Template linked to the Job Operation  */  
   "TemplateID":string,
      /**  Flag to validate if the transaction includes WIP  */  
   "WIPTransaction":boolean,
      /**  Revision for DiscrepQty  */  
   "DiscrepRevision":string,
      /**  Revision for LaborQty  */  
   "LaborRevision":string,
      /**  Revision for ScrapQty  */  
   "ScrapRevision":string,
   "TrackInventoryByRevision":boolean,
      /**  Indicates whether co-parts can be entered  */  
   "ReportPartQtyAllowed":boolean,
   "BitFlag":number,
   "DiscrpRsnDescription":string,
   "EmpBasicLastName":string,
   "EmpBasicFirstName":string,
   "EmpBasicName":string,
   "ExpenseCodeDescription":string,
   "HCMIntregationHCMEnabled":boolean,
   "HCMStatusStatus":string,
   "IndirectDescription":string,
   "JCDeptDescription":string,
   "JobAsmblPartNum":string,
   "JobAsmblDescription":string,
   "MachineDescription":string,
   "OpCodeOpDesc":string,
   "OpDescOpDesc":string,
   "PayMethodType":number,
   "PayMethodSummarizePerCustomer":boolean,
   "PayMethodName":string,
   "PhaseIDDescription":string,
   "ProjectDescription":string,
   "ResourceGrpDescription":string,
   "ResReasonDescription":string,
   "ReWorkReasonDescription":string,
   "RoleCdRoleDescription":string,
   "ScrapReasonDescription":string,
   "ShiftDescription":string,
   "TimeTypCdDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborEquipRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Used as the foreign key to the LaborHed record.  */  
   "LaborHedSeq":number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   "LaborDtlSeq":number,
      /**  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  */  
   "EquipID":string,
      /**  Hours that will be added to Equip.CurrentMeter.  Relevant only when the related Equip.LaborOpt = "Hrs"  */  
   "Hours":number,
      /**  Quantity that will be added to Equip.CurrentMeter.  Relevant only when the related Equip.LaborOpt = "Qty"  */  
   "Qty":number,
      /**  Current Meter reading which will update the Equip.CurrentMeter. Relevant only when the related Equip.LaborOpt = "Mtr"  */  
   "CurrentMeter":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "EquipLaborMeterOpt":string,
   "EquipDescription":string,
   "EquipMeterUOM":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborHedListRow{
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "TotLbrHrs":number,
   "TotBurHrs":number,
   "WipPosted":boolean,
      /**  Full Path of Employee PhotoFile  */  
   "ImagePath":string,
      /**  Indicates if a lunch break is part of the shift  */  
   "LunchBreak":boolean,
      /**  Normal work shift from EmpBasic  */  
   "EmpBasicShift":number,
      /**  The ID of the supervisor for the employee  */  
   "EmpBasicSupervisorID":string,
      /**  For display purposes  */  
   "DspPayHours":number,
   "GetNewNoHdr":boolean,
   "TimeDisableUpdate":boolean,
   "TimeDisableDelete":boolean,
   "MES":boolean,
      /**  Last name of employee  */  
   "EmployeeNumLastName":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "EmployeeNumName":string,
      /**  First name of employee.  */  
   "EmployeeNumFirstName":string,
      /**  A concatenation of Start + End time.  */  
   "ShiftDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborHedRow{
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
      /**  Normal work shift from EmpBasic  */  
   "EmpBasicShift":number,
      /**  The ID of the supervisor for the employee  */  
   "EmpBasicSupervisorID":string,
   "GetNewNoHdr":boolean,
      /**  HCM Integration, Display the Total of Pay Hours of the Labor Details.  */  
   "HCMTotPayHours":number,
      /**  Full Path of Employee PhotoFile  */  
   "ImagePath":string,
      /**  Indicates if a lunch break is part of the shift  */  
   "LunchBreak":boolean,
   "MES":boolean,
      /**  Temporal field that stores patch field value: HDR, DTL, NON  */  
   "PayrollValuesForHCM":string,
   "TimeDisableDelete":boolean,
   "TimeDisableUpdate":boolean,
   "TotBurHrs":number,
   "TotLbrHrs":number,
   "WipPosted":boolean,
      /**  For display purposes  */  
   "DspPayHours":number,
      /**  Indicates if all labor has been posted  */  
   "FullyPosted":boolean,
      /**  Indicates if some labor has been posted  */  
   "PartiallyPosted":boolean,
   "HCMExistsWithStatus":boolean,
      /**  Payroll date for record navigation  */  
   "PayrollDateNav":string,
   "BitFlag":number,
   "EmployeeNumFirstName":string,
   "EmployeeNumName":string,
   "EmployeeNumLastName":string,
   "HCMStatusStatus":string,
   "PRSystHCMEnabled":boolean,
   "ShiftDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborPartRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Used as the foreign key to the LaborHed record.  */  
   "LaborHedSeq":number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   "LaborDtlSeq":number,
      /**  Part number of the manufactured item that the quantity is for. Must be defined on the Job in the JobPart table.  */  
   "PartNum":string,
      /**  The number of individual parts completed on this labor transaction. Updates the JobPart.QtyCompleted.  */  
   "PartQty":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   "DiscrepQty":number,
      /**  Discrepant Reason Code  */  
   "DiscrpRsnCode":string,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  */  
   "DiscrpAttributeSetID":number,
      /**  The reported scrap quantity.  */  
   "ScrapQty":number,
      /**  Scrap Reason Code  */  
   "ScrapReasonCode":string,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  */  
   "ScrapAttributeSetID":number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   "NonConfTranID":number,
      /**  The unique identifier of the related Dynamic Attribute Set for the PartQty  */  
   "LaborAttributeSetID":number,
      /**  UI Sets this to true when processing from MES Labor Entry.  The BL uses this to determine if PartWip/MtlQueue logic should be performed.  */  
   "MESProcessing":boolean,
   "RequestMove":boolean,
      /**  Unit of Measure for the Part defined on the Operation  */  
   "PartUOM":string,
   "PartDescription":string,
   "RevisionNum":string,
      /**  Unit of Measure used for DiscrepQty  */  
   "DiscrepUOM":string,
      /**  Unit of Measure used for ScrapQty.  */  
   "ScrapUOM":string,
      /**  The Full Description of the Attribute Set for DiscrepQty  */  
   "DiscrepAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set for DiscrepQty  */  
   "DiscrepAttributeSetShortDescription":string,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set for PartQty  */  
   "LaborAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set for PartQty  */  
   "LaborAttributeSetShortDescription":string,
      /**  The Full Description of the Attribute Set for ScrapQty  */  
   "ScrapAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set for ScrapQty  */  
   "ScrapAttributeSetShortDescription":string,
      /**  Revision for DiscrepQty  */  
   "DiscrepRevision":string,
      /**  Revision for ScrapQty  */  
   "ScrapRevision":string,
      /**  Allow input of discrepant (nonconformance) quantity  */  
   "EnableDiscrpQty":boolean,
      /**  Allow input of scrap quantity  */  
   "EnableScrapQty":boolean,
   "BitFlag":number,
   "DiscrpRsnDescription":string,
   "ScrapReasonDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LbrScrapSerialNumbersRow{
      /**  Company  */  
   "Company":string,
      /**  LaborHedSeq of the related LaborDtl  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq of the related LaborDtl  */  
   "LaborDtlSeq":number,
      /**  Serial Number  */  
   "SerialNumber":string,
      /**  Part Number  */  
   "PartNum":string,
      /**  Job Number  */  
   "JobNum":string,
      /**  AssemblySeq this scrap serial number is for  */  
   "AssemblySeq":number,
      /**  OprSeq this scrap serial number is for  */  
   "OprSeq":number,
      /**  Indicates whether the Status field can be updated.  */  
   "EnableStatus":boolean,
      /**  New status for the serial number. This field will require Code/Desc definition: REJECTED`Scrap INSPECTION`Nonconformance WIP`WIP  */  
   "SNStatus":string,
      /**  The SNStatus description ? set same as SerialNo.SNStatusTrans  */  
   "SNStatusDesc":string,
      /**  Serial Number Selected for process  */  
   "Selected":boolean,
   "SysRowID":string,
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

export interface Erp_Tablesets_TimeWeeklyViewRow{
   "Company":string,
   "EmployeeNum":string,
   "WeekBeginDate":string,
   "WeekEndDate":string,
   "QuickEntryCode":string,
   "WeekDisplayText":string,
   "LaborType":string,
   "ProjectID":string,
   "PhaseID":string,
   "TimeTypCd":string,
   "JobNum":string,
   "AssemblySeq":number,
   "OprSeq":number,
   "RoleCd":string,
   "IndirectCode":string,
   "HoursSun":number,
   "HoursMon":number,
   "HoursTue":number,
   "HoursWed":number,
   "HoursThu":number,
   "HoursFri":number,
   "HoursSat":number,
   "TimeTypCdDescription":string,
   "RoleCdDescription":string,
   "IndirectCodeDescription":string,
   "PhaseIDDescription":string,
   "HoursTotal":number,
   "ExpenseCode":string,
   "Complete":boolean,
   "ResourceGrpID":string,
   "ResourceID":string,
   "OpCode":string,
   "OpComplete":boolean,
   "LaborEntryMethod":string,
   "LaborRate":number,
   "ResourceGrpIDDescription":string,
   "JCDept":string,
   "TimeDisableUpdate":boolean,
   "ResourceIDDescription":string,
   "ExpenseCodeDescription":string,
   "LaborTypePseudo":string,
   "Shift":number,
   "ShiftDescription":string,
   "MessageText":string,
      /**  Valid values are "A" for an Add of a new TimeWeeklyView row and "C" for a Copy of an existing TimeWeeklyView row.  */  
   "NewRowType":string,
   "DisPrjRoleCd":boolean,
   "DisTimeTypCd":boolean,
   "DisLaborType":boolean,
      /**  Indicates if submit is available  */  
   "EnableSubmit":boolean,
      /**  Indicates if the copy function is available  */  
   "EnableCopy":boolean,
      /**  Indicates if recall is available  */  
   "EnableRecall":boolean,
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   "AllowDirLbr":boolean,
   "TimeStatus":string,
   "ProjDesc":string,
      /**  WBS Phase Project Description  */  
   "WBSPhaseDesc":string,
      /**  Operation Description  */  
   "OperDesc":string,
      /**  Job Assembly description  */  
   "ASMdesc":string,
      /**   If the Time is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  */  
   "TimeAutoSubmit":boolean,
   "DeleteRow":boolean,
      /**  HCM Integration Total Weekly Pay Hours  */  
   "HCMTotWeeklyPayHours":number,
      /**  List of avaialble role codes  */  
   "RoleCdList":string,
      /**  Indicates if the row is selected for submit, recall, or copy.  */  
   "RowSelected":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TimeWorkHoursRow{
   "Company":string,
   "CalendarID":string,
   "WeekBeginDate":string,
   "WeekEndDate":string,
   "SunDisplayDate":string,
   "MonDisplayDate":string,
   "TueDisplayDate":string,
   "WedDisplayDate":string,
   "ThuDisplayDate":string,
   "FriDisplayDate":string,
   "SatDisplayDate":string,
   "WeekDisplayText":string,
   "SunWorkHours":number,
   "MonWorkHours":number,
   "TueWorkHours":number,
   "WedWorkHours":number,
   "ThuWorkHours":number,
   "FriWorkHours":number,
   "SatWorkHours":number,
   "SunBookedHours":number,
   "MonBookedHours":number,
   "WedBookedHours":number,
   "ThuBookedHours":number,
   "FriBookedHours":number,
   "SunDiffHours":number,
   "MonDiffHours":number,
   "SatBookedHours":number,
   "TueBookedHours":number,
   "TueDiffHours":number,
   "WedDiffHours":number,
   "ThuDiffHours":number,
   "FriDiffHours":number,
   "SatDiffHours":number,
   "EmployeeNum":string,
   "CalendarDescription":string,
   "TotalWorkHours":number,
   "TotalBookedHours":number,
   "TotalDiffHours":number,
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
   */  
export interface AfterChangeLaborDtlDiscrepQty_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface AfterChangeLaborDtlDiscrepQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   message:string,
}
}

   /** Required : 
      @param ds
   */  
export interface AfterChangeLaborPartDiscrepQty_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface AfterChangeLaborPartDiscrepQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   message:string,
}
}

   /** Required : 
      @param ipJobNum
      @param ipAssemblySeq
      @param ipOprSeq
      @param ipEmpID
   */  
export interface BuildJobOperPrjRoleList_input{
      /**  JobNum  */  
   ipJobNum:string,
      /**  AssemblySeq  */  
   ipAssemblySeq:number,
      /**  OprSeq  */  
   ipOprSeq:number,
      /**  EmpID  */  
   ipEmpID:string,
}

export interface BuildJobOperPrjRoleList_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   whereClause:string,
}
}

   /** Required : 
      @param equipID
      @param ds
   */  
export interface ChangeEquipID_input{
      /**  equipID  */  
   equipID:string,
   ds:Erp_Tablesets_LaborTableset[],
}

export interface ChangeEquipID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeIndirectCode_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface ChangeIndirectCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param attributeSetID
      @param type
   */  
export interface ChangeLaborDtlAttributeSetID_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed change to ScrapQty field  */  
   attributeSetID:number,
      /**  Discrep, Scrap or Labor  */  
   type:string,
}

export interface ChangeLaborDtlAttributeSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param fieldName
      @param timeValue
      @param ds
   */  
export interface ChangeLaborDtlDspTimeField_input{
      /**  The name of the field that is changing  */  
   fieldName:string,
      /**  The new time value  */  
   timeValue:string,
   ds:Erp_Tablesets_LaborTableset[],
}

export interface ChangeLaborDtlDspTimeField_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param oprSeq
   */  
export interface ChangeLaborDtlOprSeq_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed oprSeq change  */  
   oprSeq:number,
}

export interface ChangeLaborDtlOprSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   message:string,
}
}

   /** Required : 
      @param ds
      @param scrapQty
   */  
export interface ChangeLaborDtlScrapQty_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed change to ScrapQty field  */  
   scrapQty:number,
}

export interface ChangeLaborDtlScrapQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param fieldName
      @param timeValue
      @param ds
   */  
export interface ChangeLaborDtlTimeField_input{
      /**  The name of the field that is changing  */  
   fieldName:string,
      /**  The new time value  */  
   timeValue:number,
   ds:Erp_Tablesets_LaborTableset[],
}

export interface ChangeLaborDtlTimeField_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param attributeSetID
      @param type
   */  
export interface ChangeLaborPartAttributeSetID_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed change to ScrapQty field  */  
   attributeSetID:number,
      /**  Discrep, Scrap or Labor  */  
   type:string,
}

export interface ChangeLaborPartAttributeSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeLaborType_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface ChangeLaborType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param pcResourceID
   */  
export interface ChangeResourceId_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  The ID of the machine that was used to do the work.  */  
   pcResourceID:string,
}

export interface ChangeResourceId_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   pcMsg:string,
}
}

   /** Required : 
      @param ds
      @param weekBeginDate
   */  
export interface ChangeTimeWeeklyViewWeekBeginDate_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed week begin date  */  
   weekBeginDate:string,
}

export interface ChangeTimeWeeklyViewWeekBeginDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ipEmpID
      @param ipLaborHedSeq
      @param ipJobNum
      @param ipAsmSeq
      @param ipOprSeq
      @param ipResourceID
   */  
export interface CheckEmployeeActivity_input{
      /**  The current Employee ID  */  
   ipEmpID:string,
      /**  LaborHed Sequence  */  
   ipLaborHedSeq:number,
      /**  Job Number  */  
   ipJobNum:string,
      /**  Assembly Sequence  */  
   ipAsmSeq:number,
      /**  Operation Sequence  */  
   ipOprSeq:number,
      /**  Resource ID  */  
   ipResourceID:string,
}

export interface CheckEmployeeActivity_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckFirstArticleWarning_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface CheckFirstArticleWarning_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   pcMsg:string,
}
}

   /** Required : 
      @param ipJobNum
      @param ipAssemblySeq
      @param ipOprSeq
   */  
export interface CheckInspResults_input{
      /**  Current Job  */  
   ipJobNum:string,
      /**  Current AssembleSeq  */  
   ipAssemblySeq:number,
      /**  Current OprSeq  */  
   ipOprSeq:number,
}

export interface CheckInspResults_output{
parameters : {
      /**  output parameters  */  
   inspectionOK:boolean,
}
}

   /** Required : 
      @param jobNum
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface CheckNonConformance_input{
      /**  JobNumber  */  
   jobNum:string,
      /**  LaborHedSeq  */  
   laborHedSeq:number,
      /**  LaborDtlSeq  */  
   laborDtlSeq:number,
}

export interface CheckNonConformance_output{
parameters : {
      /**  output parameters  */  
   pcMsg:string,
}
}

   /** Required : 
      @param ds
      @param ProposedResourceID
   */  
export interface CheckResourceGroup_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed Resource ID  */  
   ProposedResourceID:string,
}

export interface CheckResourceGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param resourceGrpId
      @param proposedResId
   */  
export interface CheckResourceId_input{
      /**  Resource Group of the Job  */  
   resourceGrpId:string,
      /**  Proposed Resource ID to assign.  */  
   proposedResId:string,
}

export interface CheckResourceId_output{
parameters : {
      /**  output parameters  */  
   pcMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckWarnings_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface CheckWarnings_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CopyLaborDetail_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface CopyLaborDetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   cMessageText:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CopyLaborDtlBySelected_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface CopyLaborDtlBySelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   messageText:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CopyTimeWeeklyViewBySelected_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface CopyTimeWeeklyViewBySelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   messageText:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CopyTimeWeeklyView_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface CopyTimeWeeklyView_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   cMessageText:string,
}
}

   /** Required : 
      @param serialNumberList
      @param partNumList
      @param ds
   */  
export interface CreateLbrScrapSerialNumbersFromList_input{
      /**  Serial Number List  */  
   serialNumberList:string,
      /**  Part Number List  */  
   partNumList:string,
   ds:Erp_Tablesets_LaborTableset[],
}

export interface CreateLbrScrapSerialNumbersFromList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param assemblySeq
   */  
export interface DefaultAssemblySeq_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed AssemblySeq change  */  
   assemblySeq:number,
}

export interface DefaultAssemblySeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param cmplete
   */  
export interface DefaultComplete_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed change to the Complete field  */  
   cmplete:boolean,
}

export interface DefaultComplete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param payrollDate
   */  
export interface DefaultDate_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed Payroll Date change  */  
   payrollDate:string,
}

export interface DefaultDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param ProposedDiscrpRsnCode
   */  
export interface DefaultDiscrpRsnCode_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed discrepancy reason  */  
   ProposedDiscrpRsnCode:string,
}

export interface DefaultDiscrpRsnCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface DefaultDtlTime_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface DefaultDtlTime_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param indirectCode
   */  
export interface DefaultIndirect_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed change to the indirect code  */  
   indirectCode:string,
}

export interface DefaultIndirect_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param jobNum
   */  
export interface DefaultJobNum_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed change to the JobNum field  */  
   jobNum:string,
}

export interface DefaultJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborHrs
   */  
export interface DefaultLaborHrs_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed Labor Hrs change  */  
   laborHrs:number,
}

export interface DefaultLaborHrs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborQty
   */  
export interface DefaultLaborQty_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed change to LaborQty field  */  
   laborQty:number,
}

export interface DefaultLaborQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param ipLaborType
   */  
export interface DefaultLaborType_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed LaborType change  */  
   ipLaborType:string,
}

export interface DefaultLaborType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface DefaultLunchBreak_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface DefaultLunchBreak_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param ProposedNextOprSeq
   */  
export interface DefaultNextOprSeq_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed next operation sequence  */  
   ProposedNextOprSeq:number,
}

export interface DefaultNextOprSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param nonConformanceQty
   */  
export interface DefaultNonConformanceQty_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed change to LaborQty field  */  
   nonConformanceQty:number,
}

export interface DefaultNonConformanceQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param opCode
   */  
export interface DefaultOpCode_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed OpCode field change  */  
   opCode:string,
}

export interface DefaultOpCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param oprSeq
   */  
export interface DefaultOprSeq_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed oprSeq change  */  
   oprSeq:number,
}

export interface DefaultOprSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param ipPhaseID
   */  
export interface DefaultPhaseID_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed PhaseID change  */  
   ipPhaseID:string,
}

export interface DefaultPhaseID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param ipPhaseOprSeq
   */  
export interface DefaultPhaseOprSeq_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed PhaseOprSeq change  */  
   ipPhaseOprSeq:number,
}

export interface DefaultPhaseOprSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param ipProjectID
   */  
export interface DefaultProjectID_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed ProjectID change  */  
   ipProjectID:string,
}

export interface DefaultProjectID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param ProposedResourceID
   */  
export interface DefaultResourceID_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  The proposed resource id  */  
   ProposedResourceID:string,
}

export interface DefaultResourceID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param ProposedReworkReasonCode
   */  
export interface DefaultReworkReasonCode_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed discrepancy reason  */  
   ProposedReworkReasonCode:string,
}

export interface DefaultReworkReasonCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param ipRoleCd
   */  
export interface DefaultRoleCd_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed RoleCd change  */  
   ipRoleCd:string,
}

export interface DefaultRoleCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param ProposedScrapReasonCode
   */  
export interface DefaultScrapReasonCode_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed scrap reason  */  
   ProposedScrapReasonCode:string,
}

export interface DefaultScrapReasonCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param PercentComplete
   */  
export interface DefaultSetupPctComplete_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed percent complete  */  
   PercentComplete:number,
}

export interface DefaultSetupPctComplete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param shift
   */  
export interface DefaultShift_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed Shift field change  */  
   shift:number,
}

export interface DefaultShift_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param ipTimeTypCd
   */  
export interface DefaultTimeTypCd_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed TimeTypCd change  */  
   ipTimeTypCd:string,
}

export interface DefaultTimeTypCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param cFieldName
      @param timeValue
   */  
export interface DefaultTime_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  name of field being changed  */  
   cFieldName:string,
      /**  proposed time change  */  
   timeValue:number,
}

export interface DefaultTime_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param wcCode
   */  
export interface DefaultWCCode_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed WorkCenter Code change  */  
   wcCode:string,
}

export interface DefaultWCCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
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

   /** Required : 
      @param LaborHedSeq
      @param LaborDtlSeq
      @param CallFrom
   */  
export interface DeleteLaborDtl_input{
      /**  LaborHedSeq  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq  */  
   LaborDtlSeq:number,
      /**  Proposed value to filter logic for HCM  */  
   CallFrom:string,
}

export interface DeleteLaborDtl_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param cmplete
   */  
export interface EndActivityComplete_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed change to the Complete field  */  
   cmplete:boolean,
}

export interface EndActivityComplete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface EndActivity_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface EndActivity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param employeeNum
   */  
export interface EndDowntime_input{
      /**  Employee Number  */  
   employeeNum:string,
}

export interface EndDowntime_output{
}

export interface Erp_Tablesets_HCMLaborDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   EmployeeNum:string,
      /**  Used as the foreign key to the LaborHed record.  */  
   LaborHedSeq:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   LaborTypePseudo:string,
      /**  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  */  
   JCDept:string,
      /**  A short note that the user can make about the labor transaction.  */  
   LaborNote:string,
      /**  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  */  
   ClockInDate:string,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockInTime:string,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockOutTime:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   Shift:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   PayHours:number,
      /**  String value which contains the values for the HCM Integration, HDR (Header) DTL (Detail). Those values help to know the source of the payHours.  */  
   HCMEnabledAt:string,
      /**  Sent (S) = Submitted to HCM  Received (R) = Received from HCM  Error (E) = Error Submitting to HCM In Progress (IP) = In Progress  */  
   Status:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HCMLaborDtlSyncRow{
      /**  Company  */  
   Company:string,
      /**  Field to Link the SysRowID with HCMLaborDtlSync record.  */  
   LaborDtlSysRowID:string,
      /**  Sent (S) = Submitted to HCM  Received (R) = Received from HCM  Error (E) = Error Submitting to HCM In Progress (IP) = In Progress  */  
   Status:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  String value which indicates if the status should be applied to the header or the detail (HDR/DTL)  */  
   LaborSource:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HCMLaborDtlTableset{
   HCMLaborDtl:Erp_Tablesets_HCMLaborDtlRow[],
   HCMLaborDtlSync:Erp_Tablesets_HCMLaborDtlSyncRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LaborDtlActionRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Used as the foreign key to the LaborDtl record.  */  
   LaborHedSeq:number,
      /**  Used as the foreign key to the LaborDtl record.  */  
   LaborDtlSeq:number,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   ActionSeq:number,
      /**  Description of Action.  */  
   ActionDesc:string,
      /**  Indicated if this Action must be completed before Operation can be completed.  */  
   Required:boolean,
      /**  Indicates if this Action was completed.  */  
   Completed:boolean,
      /**  The number of the employee that performed the work.  */  
   CompletedBy:string,
      /**  Date the Action was completed.  */  
   CompletedOn:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
   EmpBasicName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborDtlAttchRow{
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

export interface Erp_Tablesets_LaborDtlCommentRow{
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
   DspChangeTime:string,
   DspCreateTime:string,
   TreeNodeImageName:string,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  List of valid comment types for Time Entry  */  
   TimeEntryCommentTypeList:string,
   CommentTypeDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborDtlGroupRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are

concurrently active for an employee in order to distribute the labor hours.  */  
   EmployeeNum:string,
      /**  Brief description of the expense.  Can be used to expenses together, for example, all expenses incurred on the same trip can be assigned the same reference.  */  
   ClaimRef:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborDtlRow{
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
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  */  
   DiscrepAttributeSetID:number,
      /**  The unique identifier of the related Dynamic Attribute Set for the Labor Qty  */  
   LaborAttributeSetID:number,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  */  
   ScrapAttributeSetID:number,
      /**  PCID  */  
   PCID:string,
      /**  NonConfPCID  */  
   NonConfPCID:string,
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   AllowDirLbr:boolean,
      /**  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalPhaseDesc:string,
      /**  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalPhaseID:string,
      /**  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalProjectDesc:string,
      /**  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalProjectID:string,
   ApprovedBy:string,
      /**  Used in approval entry.  Indicates if the approver has an open task or not.  */  
   ApprvrHasOpenTask:boolean,
      /**  Company Base currency code description for display in LaborDtl grid.  */  
   BaseCurrCodeDesc:string,
      /**  calculated field: BurdenHrs * BurdenRate  */  
   BurdenCost:number,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   CallCode:string,
   CapabilityDescription:string,
   CapabilityID:string,
      /**  Charge rate calculated for Time and Expense approval  */  
   ChargeRate:number,
      /**  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  */  
   ChargeRateSRC:string,
      /**  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  */  
   ChgRateCurrDesc:string,
   CompleteFlag:boolean,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   ContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   ContractNum:number,
      /**  Unit of Measure used for DiscrepQty  */  
   DiscrepUOM:string,
      /**  Field that indicates if field DisLaborTypeshould be disabled.  */  
   DisLaborType:boolean,
   DisplayJob:string,
      /**  Field that indicates if field PrjRoleCd should be disabled.  */  
   DisPrjRoleCd:boolean,
      /**  Field that indicates if field TimeTypCd should be disabled.  */  
   DisTimeTypCd:boolean,
   DowntimeTotal:number,
   DspChangeTime:string,
   DspCreateTime:string,
   DspTotHours:string,
   DtClockIn:string,
   DtClockOut:string,
      /**  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  */  
   EfficiencyPercentage:number,
      /**  Labor Detail Employee Name  */  
   EmployeeName:string,
   EnableComplete:boolean,
      /**  Indicates if the copy button is enabled  */  
   EnableCopy:boolean,
   EnableDiscrepQty:boolean,
   EnableInspection:boolean,
   EnableLaborQty:boolean,
   EnableNextOprSeq:boolean,
   EnablePrintTagsList:boolean,
      /**  Indicates if the recall button is enabled  */  
   EnableRecall:boolean,
      /**  Indicates if recall is available for an approver  */  
   EnableRecallAprv:boolean,
   EnableRequestMove:boolean,
   EnableResourceGrpID:boolean,
   EnableScrapQty:boolean,
      /**  Enable the SN Button?  */  
   EnableSN:boolean,
      /**  Indicates if the submit button is enabled  */  
   EnableSubmit:boolean,
   EndActivity:boolean,
      /**  To know if the LaborDtl was created on the current plant  */  
   EnteredOnCurPlant:boolean,
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
   FSComplete:boolean,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  Indicates if the user has access to the row  */  
   HasAccessToRow:boolean,
      /**  Indicates if the labor detail has comments  */  
   HasComments:boolean,
      /**  To tell the bo that this transaction was being modified from HH.  */  
   HH:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  Indicates if the job operation is marked as fixed hours and quantity only.  */  
   ISFixHourAndQtyOnly:boolean,
   JCSystReworkReasons:boolean,
   JCSystScrapReasons:boolean,
   JobOperComplete:boolean,
   JobType:string,
      /**  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  */  
   JobTypeCode:string,
      /**  calculated field: LaborHrs * LaborRate  */  
   LaborCost:number,
      /**  Unit of Measure used for LaborQty  */  
   LaborUOM:string,
      /**  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  */  
   LbrDay:string,
      /**  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  */  
   LbrMonth:string,
      /**  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  */  
   LbrWeek:string,
   MES:boolean,
   MultipleEmployeesText:string,
   NewDifDateFlag:number,
      /**  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  */  
   NewPrjRoleCd:string,
      /**  Holds the description for NewPrjRoleCd  */  
   NewRoleCdDesc:string,
   NextAssemblySeq:number,
   NextOperDesc:string,
   NextOprSeq:number,
   NextResourceDesc:string,
      /**  To evaluate if the NonComformance has been already processed in inspection and no changes can be applied on LaborDtl then.  */  
   NonConfProcessed:boolean,
   NotSubmitted:boolean,
      /**  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  */  
   OkToChangeResourceGrpID:boolean,
   PartDescription:string,
   PartNum:string,
   PBAllowModify:boolean,
   PendingApprovalBy:string,
      /**  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  */  
   PhaseJobNum:string,
      /**  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  */  
   PhaseOprSeq:number,
   PrintNCTag:boolean,
   PrjUsedTran:string,
   ProdDesc:string,
   ProjPhaseID:string,
   RequestMove:boolean,
   ResourceDesc:string,
   RoleCdDisplayAll:boolean,
      /**  Unit of Measure used for ScrapQty.  */  
   ScrapUOM:string,
      /**  Flag field to identify if the row is being sent from MES  */  
   SentFromMES:boolean,
   StartActivity:boolean,
   TimeDisableDelete:boolean,
   TimeDisableUpdate:boolean,
   TreeNodeImageName:string,
   UnapprovedFirstArt:boolean,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   WarrantyCode:string,
   WeekDisplayText:string,
      /**  EnablePCID  */  
   EnablePCID:boolean,
      /**  The output bin from the resource  */  
   OutputBin:string,
      /**  The output warehouse from the resource  */  
   OutputWarehouse:string,
      /**  Internal flag used for the row rules to control whether the Lot columns should be enabled.  */  
   EnableLot:boolean,
      /**  Lot number that is to be added to the PCID  */  
   LotNum:string,
      /**  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  */  
   PrintPCIDContents:boolean,
      /**  Indicates if the labor detail has attachments  */  
   HasAttachments:boolean,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set for DiscrepQty  */  
   DiscrepAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set for DiscrepQty  */  
   DiscrepAttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set for ScrapQty  */  
   ScrapAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set for ScrapQty  */  
   ScrapAttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set for LaborQty  */  
   LaborAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set for LaborQty  */  
   LaborAttributeSetShortDescription:string,
      /**  Indicates if recall and delete should be disabled  */  
   DisableRecallAndDelete:boolean,
      /**  List of available role codes  */  
   RoleCdList:string,
      /**  Indicates if the row is selected for submit, recall, or copy  */  
   RowSelected:boolean,
      /**  Start date/time for calendar appoinment  */  
   AppointmentStart:string,
      /**  End date/time for calendar appoinment  */  
   AppointmentEnd:string,
      /**  Title to display for the calendar appointment  */  
   AppointmentTitle:string,
      /**  PDF Form Template linked to the Job Operation  */  
   TemplateID:string,
      /**  Flag to validate if the transaction includes WIP  */  
   WIPTransaction:boolean,
      /**  Revision for DiscrepQty  */  
   DiscrepRevision:string,
      /**  Revision for LaborQty  */  
   LaborRevision:string,
      /**  Revision for ScrapQty  */  
   ScrapRevision:string,
   TrackInventoryByRevision:boolean,
      /**  Indicates whether co-parts can be entered  */  
   ReportPartQtyAllowed:boolean,
   BitFlag:number,
   DiscrpRsnDescription:string,
   EmpBasicLastName:string,
   EmpBasicFirstName:string,
   EmpBasicName:string,
   ExpenseCodeDescription:string,
   HCMIntregationHCMEnabled:boolean,
   HCMStatusStatus:string,
   IndirectDescription:string,
   JCDeptDescription:string,
   JobAsmblPartNum:string,
   JobAsmblDescription:string,
   MachineDescription:string,
   OpCodeOpDesc:string,
   OpDescOpDesc:string,
   PayMethodType:number,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodName:string,
   PhaseIDDescription:string,
   ProjectDescription:string,
   ResourceGrpDescription:string,
   ResReasonDescription:string,
   ReWorkReasonDescription:string,
   RoleCdRoleDescription:string,
   ScrapReasonDescription:string,
   ShiftDescription:string,
   TimeTypCdDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborEquipRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Used as the foreign key to the LaborHed record.  */  
   LaborHedSeq:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  */  
   EquipID:string,
      /**  Hours that will be added to Equip.CurrentMeter.  Relevant only when the related Equip.LaborOpt = "Hrs"  */  
   Hours:number,
      /**  Quantity that will be added to Equip.CurrentMeter.  Relevant only when the related Equip.LaborOpt = "Qty"  */  
   Qty:number,
      /**  Current Meter reading which will update the Equip.CurrentMeter. Relevant only when the related Equip.LaborOpt = "Mtr"  */  
   CurrentMeter:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   EquipLaborMeterOpt:string,
   EquipDescription:string,
   EquipMeterUOM:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborHedListRow{
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   TotLbrHrs:number,
   TotBurHrs:number,
   WipPosted:boolean,
      /**  Full Path of Employee PhotoFile  */  
   ImagePath:string,
      /**  Indicates if a lunch break is part of the shift  */  
   LunchBreak:boolean,
      /**  Normal work shift from EmpBasic  */  
   EmpBasicShift:number,
      /**  The ID of the supervisor for the employee  */  
   EmpBasicSupervisorID:string,
      /**  For display purposes  */  
   DspPayHours:number,
   GetNewNoHdr:boolean,
   TimeDisableUpdate:boolean,
   TimeDisableDelete:boolean,
   MES:boolean,
      /**  Last name of employee  */  
   EmployeeNumLastName:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   EmployeeNumName:string,
      /**  First name of employee.  */  
   EmployeeNumFirstName:string,
      /**  A concatenation of Start + End time.  */  
   ShiftDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborHedListTableset{
   LaborHedList:Erp_Tablesets_LaborHedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LaborHedRow{
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
      /**  Normal work shift from EmpBasic  */  
   EmpBasicShift:number,
      /**  The ID of the supervisor for the employee  */  
   EmpBasicSupervisorID:string,
   GetNewNoHdr:boolean,
      /**  HCM Integration, Display the Total of Pay Hours of the Labor Details.  */  
   HCMTotPayHours:number,
      /**  Full Path of Employee PhotoFile  */  
   ImagePath:string,
      /**  Indicates if a lunch break is part of the shift  */  
   LunchBreak:boolean,
   MES:boolean,
      /**  Temporal field that stores patch field value: HDR, DTL, NON  */  
   PayrollValuesForHCM:string,
   TimeDisableDelete:boolean,
   TimeDisableUpdate:boolean,
   TotBurHrs:number,
   TotLbrHrs:number,
   WipPosted:boolean,
      /**  For display purposes  */  
   DspPayHours:number,
      /**  Indicates if all labor has been posted  */  
   FullyPosted:boolean,
      /**  Indicates if some labor has been posted  */  
   PartiallyPosted:boolean,
   HCMExistsWithStatus:boolean,
      /**  Payroll date for record navigation  */  
   PayrollDateNav:string,
   BitFlag:number,
   EmployeeNumFirstName:string,
   EmployeeNumName:string,
   EmployeeNumLastName:string,
   HCMStatusStatus:string,
   PRSystHCMEnabled:boolean,
   ShiftDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborPartRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Used as the foreign key to the LaborHed record.  */  
   LaborHedSeq:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**  Part number of the manufactured item that the quantity is for. Must be defined on the Job in the JobPart table.  */  
   PartNum:string,
      /**  The number of individual parts completed on this labor transaction. Updates the JobPart.QtyCompleted.  */  
   PartQty:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   DiscrepQty:number,
      /**  Discrepant Reason Code  */  
   DiscrpRsnCode:string,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  */  
   DiscrpAttributeSetID:number,
      /**  The reported scrap quantity.  */  
   ScrapQty:number,
      /**  Scrap Reason Code  */  
   ScrapReasonCode:string,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  */  
   ScrapAttributeSetID:number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   NonConfTranID:number,
      /**  The unique identifier of the related Dynamic Attribute Set for the PartQty  */  
   LaborAttributeSetID:number,
      /**  UI Sets this to true when processing from MES Labor Entry.  The BL uses this to determine if PartWip/MtlQueue logic should be performed.  */  
   MESProcessing:boolean,
   RequestMove:boolean,
      /**  Unit of Measure for the Part defined on the Operation  */  
   PartUOM:string,
   PartDescription:string,
   RevisionNum:string,
      /**  Unit of Measure used for DiscrepQty  */  
   DiscrepUOM:string,
      /**  Unit of Measure used for ScrapQty.  */  
   ScrapUOM:string,
      /**  The Full Description of the Attribute Set for DiscrepQty  */  
   DiscrepAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set for DiscrepQty  */  
   DiscrepAttributeSetShortDescription:string,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set for PartQty  */  
   LaborAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set for PartQty  */  
   LaborAttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set for ScrapQty  */  
   ScrapAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set for ScrapQty  */  
   ScrapAttributeSetShortDescription:string,
      /**  Revision for DiscrepQty  */  
   DiscrepRevision:string,
      /**  Revision for ScrapQty  */  
   ScrapRevision:string,
      /**  Allow input of discrepant (nonconformance) quantity  */  
   EnableDiscrpQty:boolean,
      /**  Allow input of scrap quantity  */  
   EnableScrapQty:boolean,
   BitFlag:number,
   DiscrpRsnDescription:string,
   ScrapReasonDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborTableset{
   LaborHed:Erp_Tablesets_LaborHedRow[],
   LaborDtl:Erp_Tablesets_LaborDtlRow[],
   LaborDtlAttch:Erp_Tablesets_LaborDtlAttchRow[],
   LaborDtlAction:Erp_Tablesets_LaborDtlActionRow[],
   LaborDtlComment:Erp_Tablesets_LaborDtlCommentRow[],
   LaborEquip:Erp_Tablesets_LaborEquipRow[],
   LaborPart:Erp_Tablesets_LaborPartRow[],
   LbrScrapSerialNumbers:Erp_Tablesets_LbrScrapSerialNumbersRow[],
   LaborDtlGroup:Erp_Tablesets_LaborDtlGroupRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   TimeWeeklyView:Erp_Tablesets_TimeWeeklyViewRow[],
   TimeWorkHours:Erp_Tablesets_TimeWorkHoursRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LbrScrapSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  LaborHedSeq of the related LaborDtl  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl  */  
   LaborDtlSeq:number,
      /**  Serial Number  */  
   SerialNumber:string,
      /**  Part Number  */  
   PartNum:string,
      /**  Job Number  */  
   JobNum:string,
      /**  AssemblySeq this scrap serial number is for  */  
   AssemblySeq:number,
      /**  OprSeq this scrap serial number is for  */  
   OprSeq:number,
      /**  Indicates whether the Status field can be updated.  */  
   EnableStatus:boolean,
      /**  New status for the serial number. This field will require Code/Desc definition: REJECTED`Scrap INSPECTION`Nonconformance WIP`WIP  */  
   SNStatus:string,
      /**  The SNStatus description ? set same as SerialNo.SNStatusTrans  */  
   SNStatusDesc:string,
      /**  Serial Number Selected for process  */  
   Selected:boolean,
   SysRowID:string,
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

export interface Erp_Tablesets_TimeWeeklyViewRow{
   Company:string,
   EmployeeNum:string,
   WeekBeginDate:string,
   WeekEndDate:string,
   QuickEntryCode:string,
   WeekDisplayText:string,
   LaborType:string,
   ProjectID:string,
   PhaseID:string,
   TimeTypCd:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   RoleCd:string,
   IndirectCode:string,
   HoursSun:number,
   HoursMon:number,
   HoursTue:number,
   HoursWed:number,
   HoursThu:number,
   HoursFri:number,
   HoursSat:number,
   TimeTypCdDescription:string,
   RoleCdDescription:string,
   IndirectCodeDescription:string,
   PhaseIDDescription:string,
   HoursTotal:number,
   ExpenseCode:string,
   Complete:boolean,
   ResourceGrpID:string,
   ResourceID:string,
   OpCode:string,
   OpComplete:boolean,
   LaborEntryMethod:string,
   LaborRate:number,
   ResourceGrpIDDescription:string,
   JCDept:string,
   TimeDisableUpdate:boolean,
   ResourceIDDescription:string,
   ExpenseCodeDescription:string,
   LaborTypePseudo:string,
   Shift:number,
   ShiftDescription:string,
   MessageText:string,
      /**  Valid values are "A" for an Add of a new TimeWeeklyView row and "C" for a Copy of an existing TimeWeeklyView row.  */  
   NewRowType:string,
   DisPrjRoleCd:boolean,
   DisTimeTypCd:boolean,
   DisLaborType:boolean,
      /**  Indicates if submit is available  */  
   EnableSubmit:boolean,
      /**  Indicates if the copy function is available  */  
   EnableCopy:boolean,
      /**  Indicates if recall is available  */  
   EnableRecall:boolean,
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   AllowDirLbr:boolean,
   TimeStatus:string,
   ProjDesc:string,
      /**  WBS Phase Project Description  */  
   WBSPhaseDesc:string,
      /**  Operation Description  */  
   OperDesc:string,
      /**  Job Assembly description  */  
   ASMdesc:string,
      /**   If the Time is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  */  
   TimeAutoSubmit:boolean,
   DeleteRow:boolean,
      /**  HCM Integration Total Weekly Pay Hours  */  
   HCMTotWeeklyPayHours:number,
      /**  List of avaialble role codes  */  
   RoleCdList:string,
      /**  Indicates if the row is selected for submit, recall, or copy.  */  
   RowSelected:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TimeWorkHoursRow{
   Company:string,
   CalendarID:string,
   WeekBeginDate:string,
   WeekEndDate:string,
   SunDisplayDate:string,
   MonDisplayDate:string,
   TueDisplayDate:string,
   WedDisplayDate:string,
   ThuDisplayDate:string,
   FriDisplayDate:string,
   SatDisplayDate:string,
   WeekDisplayText:string,
   SunWorkHours:number,
   MonWorkHours:number,
   TueWorkHours:number,
   WedWorkHours:number,
   ThuWorkHours:number,
   FriWorkHours:number,
   SatWorkHours:number,
   SunBookedHours:number,
   MonBookedHours:number,
   WedBookedHours:number,
   ThuBookedHours:number,
   FriBookedHours:number,
   SunDiffHours:number,
   MonDiffHours:number,
   SatBookedHours:number,
   TueBookedHours:number,
   TueDiffHours:number,
   WedDiffHours:number,
   ThuDiffHours:number,
   FriDiffHours:number,
   SatDiffHours:number,
   EmployeeNum:string,
   CalendarDescription:string,
   TotalWorkHours:number,
   TotalBookedHours:number,
   TotalDiffHours:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtLaborTableset{
   LaborHed:Erp_Tablesets_LaborHedRow[],
   LaborDtl:Erp_Tablesets_LaborDtlRow[],
   LaborDtlAttch:Erp_Tablesets_LaborDtlAttchRow[],
   LaborDtlAction:Erp_Tablesets_LaborDtlActionRow[],
   LaborDtlComment:Erp_Tablesets_LaborDtlCommentRow[],
   LaborEquip:Erp_Tablesets_LaborEquipRow[],
   LaborPart:Erp_Tablesets_LaborPartRow[],
   LbrScrapSerialNumbers:Erp_Tablesets_LbrScrapSerialNumbersRow[],
   LaborDtlGroup:Erp_Tablesets_LaborDtlGroupRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   TimeWeeklyView:Erp_Tablesets_TimeWeeklyViewRow[],
   TimeWorkHours:Erp_Tablesets_TimeWorkHoursRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WorkQueueRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  */  
   JCDept:string,
      /**   Indicates if this operation is completed. This is normally set to complete via labor entry transactions.   Not maintainable by Job Entry. It can't be reset to "No" if the JobHead.Complete = Yes.
Labor entry setting logic is: If SetUpComplete = Yes and  EstProdHours = 0 or ProdComplete = Yes and EstSetHours = 0 or both ProdComplete = Yes and SetupComplete = Yes  then OpComplete = Yes.
This field is also set by PO receipt entry "issue complete" for subcontract operations.  */  
   OpComplete:boolean,
      /**  Job Number  */  
   JobNum:string,
      /**  Assembly Sequence # that this Operation is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  The total operation quantity. This is a calculated field.  */  
   OprQty:number,
      /**  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  */  
   EstSetHours:number,
      /**   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  */  
   EstProdHours:number,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   SchedCode:string,
   SetupLoadHrs:number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
   ProdLoadHrs:number,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  1=CurrentWork, 2=AvailableWork, 3=ExpectedWork  */  
   RegionCode:number,
      /**  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   StartDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   StartHour:number,
      /**  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   DueHour:number,
   SortDate:string,
   WIPQty:number,
      /**  Number Of Employees Now Working On This Operation  */  
   CrewCount:number,
   QtyLeft:number,
   SetupLeft:number,
      /**  TRUE indicates there are WIP Qty Details available (i.e. the Staged Details button should be enabled)  */  
   WIPQtyDetails:boolean,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   Machines:number,
      /**  TRUE indicates the current employee is authorized to Request Material  */  
   CanRequest:boolean,
      /**  TRUE indicates the current employee can select this operation to work on (i.e. the Select For Work button should be enabled).  */  
   CanSelect:boolean,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Part number of the manufactured item.  */  
   JobHeadPartNum:string,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  The description of the part that is to be manufactured.  */  
   JobHeadPartDescription:string,
      /**   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  */  
   QtyCompleted:number,
      /**  Editor widget for Job operation comments.  */  
   OprCommentText:string,
      /**  Editor widget for Job header comments.  */  
   AsmCommentText:string,
      /**  Editor widget for Job header comments.  */  
   JobHeadCommentText:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  "Current Work", "Available Work", or "Expected Work" as indicated by the RegionCode.  */  
   RegionDescription:string,
      /**  Uniquely identifies an OpDtl.  System assigned.  */  
   OpDtlSeq:number,
      /**  Description is initially created when the JobOpDtl is created.  */  
   OpDtlDescription:string,
      /**  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  */  
   PartNum:string,
      /**  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "Setup", "Production", or "Both".  */  
   OpDtlType:string,
      /**  Description used only for subcontract operations  */  
   Description:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   SortHour:number,
      /**  Editor widget for Job operation comments.  */  
   CommentText:string,
      /**  Used by the UI to allow selection of rows  */  
   Selected:boolean,
      /**   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   RunQty:number,
      /**  Description for PartNum  */  
   PartDescription:string,
      /**  Delimited list of resources oper is schedueld to  */  
   SchResourceList:string,
      /**  Current Production Qty (for user reporting qty)  */  
   CurQty:number,
      /**  Qty currently being completed  */  
   LaborQty:number,
      /**  Scrap Qty currently being entered  */  
   ScrapQty:number,
      /**  Discrep Qty currently being entered  */  
   DiscrepQty:number,
      /**  Reason code for discrep qty currently being entered  */  
   DiscrepRsnCode:string,
      /**  Reason code for scrap currently being entered  */  
   ScrapRsnCode:string,
      /**  Description for ScrapRsnCode  */  
   ScrapRsnDesc:string,
      /**  Description for DescrepRsnCode  */  
   DiscrepRsnDesc:string,
      /**  Operation complete  */  
   Complete:boolean,
   ResourceID:string,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  CustNum from first order  */  
   FirstCustNum:number,
   FirstCustID:string,
   FirstCustName:string,
   FirstShipViaCode:string,
   FirstShipViaDesc:string,
   SetupGrpDesc:string,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RequestMove  */  
   RequestMove:boolean,
   ResourceGrpID:string,
   SetupOrProd:string,
      /**  Used to checks if the StartDate has a value or is null to later permit a Sorting of the records By the StartDate field , positioning the null values at the end.  */  
   StartDateNullCheck:boolean,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
   CheckBox05:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
      /**  Used for caching pagination in UI  */  
   PageNum:number,
      /**  Used for caching pagination in UI  */  
   TotalRecords:number,
      /**  Used for caching pagination in UI  */  
   MorePages:boolean,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) , "B" - Backflush or "X" - Time and Backflush Qty.  */  
   LaborEntryMethodDesc:string,
   EnableLaborQty:boolean,
   EnableScrapQty:boolean,
   EnableDiscrepQty:boolean,
      /**  Resource Group Description.  */  
   ResourceGrpDesc:string,
      /**  Operation Code Description.  */  
   OpCodeOpDesc:string,
      /**  Unit of Measure used for editable quantity fields on the WorkQueue.  */  
   LaborUOM:string,
   LaborType:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ds
      @param indirectCode
      @param downtimeNote
   */  
export interface ExternalMESDowntime_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  IndirectCode  */  
   indirectCode:string,
      /**  Downtime Note  */  
   downtimeNote:string,
}

export interface ExternalMESDowntime_output{
}

   /** Required : 
      @param ds
   */  
export interface ExternalMESEndDowntime_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface ExternalMESEndDowntime_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param employeeNum
   */  
export interface GetActiveLaborDtl_input{
      /**  The Employee Num  */  
   employeeNum:string,
}

export interface GetActiveLaborDtl_output{
   returnObj:Erp_Tablesets_LaborTableset[],
}

   /** Required : 
      @param laborHedSeq
   */  
export interface GetByID_input{
   laborHedSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_LaborTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_LaborTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_LaborTableset[],
}

   /** Required : 
      @param dspClckTm
   */  
export interface GetClockTime_input{
      /**  The clock time to be parsed as Decimal  */  
   dspClckTm:string,
}

export interface GetClockTime_output{
parameters : {
      /**  output parameters  */  
   clckTm:number,
}
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
      @param empID
      @param calendarStartDateTime
      @param calendarEndDateTime
   */  
export interface GetDefaultsAddLaborDtlFromCalendar_input{
   empID:string,
   calendarStartDateTime:string,
   calendarEndDateTime:string,
}

export interface GetDefaultsAddLaborDtlFromCalendar_output{
parameters : {
      /**  output parameters  */  
   laborHedSeq:number,
   startDate:string,
   startTime:number,
   endDate:string,
   endTime:number,
}
}

   /** Required : 
      @param iLaborHedSeq
      @param iLaborDtlSeq
   */  
export interface GetDetail_input{
      /**  The LaborHedSeq of the LaborHed record to retrieve  */  
   iLaborHedSeq:number,
      /**  The LaborDtlSeq of the LaborDtl record to retrieve  */  
   iLaborDtlSeq:number,
}

export interface GetDetail_output{
   returnObj:Erp_Tablesets_LaborTableset[],
}

   /** Required : 
      @param clckTm
   */  
export interface GetDspClockTime_input{
      /**  The clock time to be formatted  */  
   clckTm:number,
}

export interface GetDspClockTime_output{
parameters : {
      /**  output parameters  */  
   dspClckTm:string,
}
}

export interface GetJobProductionCompanySettings_output{
parameters : {
      /**  output parameters  */  
   advanceLaborRate:boolean,
   clockFormat:string,
}
}

   /** Required : 
      @param employeeNum
   */  
export interface GetLaborTypeList_input{
      /**  Employee Number  */  
   employeeNum:string,
}

export interface GetLaborTypeList_output{
parameters : {
      /**  output parameters  */  
   laborTypeList:string,
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
   returnObj:Erp_Tablesets_LaborHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetNewLaborDtlAction_input{
   ds:Erp_Tablesets_LaborTableset[],
   laborHedSeq:number,
   laborDtlSeq:number,
}

export interface GetNewLaborDtlAction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetNewLaborDtlAttch_input{
   ds:Erp_Tablesets_LaborTableset[],
   laborHedSeq:number,
   laborDtlSeq:number,
}

export interface GetNewLaborDtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetNewLaborDtlComment_input{
   ds:Erp_Tablesets_LaborTableset[],
   laborHedSeq:number,
   laborDtlSeq:number,
}

export interface GetNewLaborDtlComment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param employeeNum
   */  
export interface GetNewLaborDtlGroup_input{
   ds:Erp_Tablesets_LaborTableset[],
   employeeNum:string,
}

export interface GetNewLaborDtlGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param EmployeeNum
      @param ShopFloor
      @param ClockInDate
      @param ClockInTime
      @param ClockOutDate
      @param ClockOutTime
   */  
export interface GetNewLaborDtlNoHdr_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  The employee id for this labor record  */  
   EmployeeNum:string,
      /**  Indicates whether this is being called from the shop floor
            labor entry program  */  
   ShopFloor:boolean,
      /**  The clock in date  */  
   ClockInDate:string,
      /**  The clock in time  */  
   ClockInTime:number,
      /**  The clock out date  */  
   ClockOutDate:string,
      /**  The clock out time  */  
   ClockOutTime:number,
}

export interface GetNewLaborDtlNoHdr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
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
export interface GetNewLaborDtlOnSelectForWork_input{
   ds:Erp_Tablesets_LaborTableset[],
   laborHedSeq:number,
   sJobNum:string,
   iAssemblySeq:number,
   iOprSeq:number,
   sResourceGrpID:string,
   setupOrProd:string,
}

export interface GetNewLaborDtlOnSelectForWork_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   bMachinePrompt:boolean,
}
}

   /** Required : 
      @param ds
      @param ipClockInDate
      @param ipClockInTime
      @param ipClockOutDate
      @param ipClockOutTime
      @param ipLaborHedSeq
   */  
export interface GetNewLaborDtlWithHdr_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  The clock in date  */  
   ipClockInDate:string,
      /**  The clock in time  */  
   ipClockInTime:number,
      /**  The clock out date  */  
   ipClockOutDate:string,
      /**  The clock out time  */  
   ipClockOutTime:number,
      /**  Unique identifier of the LaborHed  */  
   ipLaborHedSeq:number,
}

export interface GetNewLaborDtlWithHdr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
   */  
export interface GetNewLaborDtl_input{
   ds:Erp_Tablesets_LaborTableset[],
   laborHedSeq:number,
}

export interface GetNewLaborDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetNewLaborEquip_input{
   ds:Erp_Tablesets_LaborTableset[],
   laborHedSeq:number,
   laborDtlSeq:number,
}

export interface GetNewLaborEquip_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param EmployeeNum
      @param ShopFloor
      @param payrollDate
   */  
export interface GetNewLaborHed1_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  The employee id for this labor record  */  
   EmployeeNum:string,
      /**  Indicates whether this is being called from the shop floor
            labor entry program  */  
   ShopFloor:boolean,
      /**  Payroll Date for this labor record  */  
   payrollDate:string,
}

export interface GetNewLaborHed1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewLaborHed_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface GetNewLaborHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetNewLaborPart_input{
   ds:Erp_Tablesets_LaborTableset[],
   laborHedSeq:number,
   laborDtlSeq:number,
}

export interface GetNewLaborPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewLbrScrapSerialNumbers_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface GetNewLbrScrapSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param ipEmployeeNum
      @param ipDateInWeek
   */  
export interface GetNewTimeWeeklyView_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  The employee id for this labor record  */  
   ipEmployeeNum:string,
      /**  Date within the week for which a new TimeWeeklyView record is to be created  */  
   ipDateInWeek:string,
}

export interface GetNewTimeWeeklyView_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param whereClauseLaborHed
      @param whereClauseLaborDtl
      @param whereClauseLaborDtlAttach
      @param whereClauseLaborDtlAction
      @param whereClauseLaborDtlCom
      @param whereClauseLaborEquip
      @param whereClauseLaborPart
      @param whereClauseLbrScrapSerialNumbers
      @param whereClauseTimeWorkHours
      @param whereClauseTimeWeeklyView
      @param whereClauseLaborDtlGroup
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
      @param ipEmployeeNum
      @param ipCalendarStartDate
      @param ipCalendarEndDate
   */  
export interface GetRowsCalendarView_input{
   whereClauseLaborHed:string,
   whereClauseLaborDtl:string,
   whereClauseLaborDtlAttach:string,
   whereClauseLaborDtlAction:string,
   whereClauseLaborDtlCom:string,
   whereClauseLaborEquip:string,
   whereClauseLaborPart:string,
   whereClauseLbrScrapSerialNumbers:string,
   whereClauseTimeWorkHours:string,
   whereClauseTimeWeeklyView:string,
   whereClauseLaborDtlGroup:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   pageSize:number,
   absolutePage:number,
   ipEmployeeNum:string,
   ipCalendarStartDate:string,
   ipCalendarEndDate:string,
}

export interface GetRowsCalendarView_output{
   returnObj:Erp_Tablesets_LaborTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseLaborHed
      @param whereClauseLaborDtl
      @param whereClauseLaborDtlAttach
      @param whereClauseLaborDtlAction
      @param whereClauseLaborDtlCom
      @param whereClauseLaborEquip
      @param whereClauseLaborPart
      @param whereClauseLbrScrapSerialNumbers
      @param whereClauseTimeWorkHours
      @param whereClauseTimeWeeklyView
      @param whereClauseLaborDtlGroup
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
      @param employeeNum
      @param calendarStartDate
      @param calendarEndDate
   */  
export interface GetRowsTimeEntry_input{
      /**  LaborHed where clause  */  
   whereClauseLaborHed:string,
      /**  LaborDtl where clause  */  
   whereClauseLaborDtl:string,
      /**  LaborDtlAttach where clause  */  
   whereClauseLaborDtlAttach:string,
      /**  LaborDtlAction where clause  */  
   whereClauseLaborDtlAction:string,
      /**  LaborDtlCom where clause  */  
   whereClauseLaborDtlCom:string,
      /**  LaborEquip where clause  */  
   whereClauseLaborEquip:string,
      /**  LaborPart where clause  */  
   whereClauseLaborPart:string,
      /**  LbrScrapSerialNumbers where clause  */  
   whereClauseLbrScrapSerialNumbers:string,
      /**  LaborTimeWorkHours where clause  */  
   whereClauseTimeWorkHours:string,
      /**  LaborTimeWeeklyView where clause  */  
   whereClauseTimeWeeklyView:string,
      /**  LaborDtlGroup where clause  */  
   whereClauseLaborDtlGroup:string,
      /**  SelectedSerialNumbers where clause  */  
   whereClauseSelectedSerialNumbers:string,
      /**  SNFormat where clause  */  
   whereClauseSNFormat:string,
      /**  Page size  */  
   pageSize:number,
      /**  Absolute page  */  
   absolutePage:number,
      /**  Employee number  */  
   employeeNum:string,
      /**  Calendar start date  */  
   calendarStartDate:string,
      /**  Calendar end date  */  
   calendarEndDate:string,
}

export interface GetRowsTimeEntry_output{
   returnObj:Erp_Tablesets_LaborTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseLaborHed
      @param whereClauseLaborDtl
      @param whereClauseLaborDtlCom
      @param whereClauseLaborEquip
      @param whereClauseLaborPart
      @param whereClauseLbrScrapSerialNumbers
      @param whereClauseTimeWorkHours
      @param whereClauseTimeWeeklyView
      @param whereClauseLaborDtlGroup
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
      @param ipSupervisorID
   */  
export interface GetRowsWhoIsHere_input{
   whereClauseLaborHed:string,
   whereClauseLaborDtl:string,
   whereClauseLaborDtlCom:string,
   whereClauseLaborEquip:string,
   whereClauseLaborPart:string,
   whereClauseLbrScrapSerialNumbers:string,
   whereClauseTimeWorkHours:string,
   whereClauseTimeWeeklyView:string,
   whereClauseLaborDtlGroup:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   pageSize:number,
   absolutePage:number,
   ipSupervisorID:string,
}

export interface GetRowsWhoIsHere_output{
   returnObj:Erp_Tablesets_LaborTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseLaborHed
      @param whereClauseLaborDtl
      @param whereClauseLaborDtlAttch
      @param whereClauseLaborDtlAction
      @param whereClauseLaborDtlComment
      @param whereClauseLaborEquip
      @param whereClauseLaborPart
      @param whereClauseLbrScrapSerialNumbers
      @param whereClauseLaborDtlGroup
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param whereClauseTimeWeeklyView
      @param whereClauseTimeWorkHours
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseLaborHed:string,
   whereClauseLaborDtl:string,
   whereClauseLaborDtlAttch:string,
   whereClauseLaborDtlAction:string,
   whereClauseLaborDtlComment:string,
   whereClauseLaborEquip:string,
   whereClauseLaborPart:string,
   whereClauseLbrScrapSerialNumbers:string,
   whereClauseLaborDtlGroup:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   whereClauseTimeWeeklyView:string,
   whereClauseTimeWorkHours:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_LaborTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetTERetrieveApproved_output{
parameters : {
      /**  output parameters  */  
   opTERetrieveApproved:boolean,
}
}

export interface GetTERetrieveByOption_output{
parameters : {
      /**  output parameters  */  
   opTERetrieveByDay:boolean,
   opTERetrieveByWeek:boolean,
   opTERetrieveByMonth:boolean,
}
}

export interface GetTERetrieveEntered_output{
parameters : {
      /**  output parameters  */  
   opTERetrieveEntered:boolean,
}
}

export interface GetTERetrievePartiallyApproved_output{
parameters : {
      /**  output parameters  */  
   opTERetrievePartiallyApproved:boolean,
}
}

export interface GetTERetrieveRejected_output{
parameters : {
      /**  output parameters  */  
   opTERetrieveRejected:boolean,
}
}

export interface GetTERetrieveSubmitted_output{
parameters : {
      /**  output parameters  */  
   opTERetrieveSubmitted:boolean,
}
}

   /** Required : 
      @param employeeNum
      @param startDate
      @param endDate
      @param includeStatus
   */  
export interface HCMGetLaborRecords_input{
      /**  String value with the list of employees  */  
   employeeNum:string,
      /**  Start Date  */  
   startDate:string,
      /**  End Date  */  
   endDate:string,
      /**  String value with status value  */  
   includeStatus:string,
}

export interface HCMGetLaborRecords_output{
   returnObj:Erp_Tablesets_HCMLaborDtlTableset[],
}

   /** Required : 
      @param hcmDs
   */  
export interface HCMSetLaborStatus_input{
   hcmDs:Erp_Tablesets_HCMLaborDtlTableset[],
}

export interface HCMSetLaborStatus_output{
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
      @param employeeNum
      @param indirectCode
      @param indirectNote
   */  
export interface InitiateDowntime_input{
      /**  Employee Number  */  
   employeeNum:string,
      /**  Indirect Code  */  
   indirectCode:string,
      /**  Indirect Labor Note  */  
   indirectNote:string,
}

export interface InitiateDowntime_output{
}

export interface IsHCMEnabledAtCompany_output{
   returnObj:boolean,
}

   /** Required : 
      @param pcJobNum
      @param piAssemblySeq
   */  
export interface IsValidAssembly_input{
      /**  Job number to which this labor transaction applies.  */  
   pcJobNum:string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to.  */  
   piAssemblySeq:number,
}

export interface IsValidAssembly_output{
parameters : {
      /**  output parameters  */  
   plFound:boolean,
}
}

   /** Required : 
      @param laborDtlRow
   */  
export interface LaborDtlAfterGetRowsWrapper_input{
   laborDtlRow:Erp_Tablesets_LaborDtlRow[],
}

export interface LaborDtlAfterGetRowsWrapper_output{
parameters : {
      /**  output parameters  */  
   laborDtlRow:Erp_Tablesets_LaborDtlRow,
}
}

   /** Required : 
      @param payrollDate
      @param ds
   */  
export interface LaborHedPayrollDateChanging_input{
      /**  Payroll Date  */  
   payrollDate:string,
   ds:Erp_Tablesets_LaborTableset[],
}

export interface LaborHedPayrollDateChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface LaborRateCalc_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface LaborRateCalc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param ipClockInDate
   */  
export interface OnChangeClockInDate_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed Clock In Date  */  
   ipClockInDate:string,
}

export interface OnChangeClockInDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param scrapQty
      @param sysRowID
   */  
export interface OnChangeLaborPartScrapQty_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed change to PartQty field  */  
   scrapQty:number,
      /**  sysRowID of line updated in LaborPart  */  
   sysRowID:string,
}

export interface OnChangeLaborPartScrapQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param pcid
      @param isNonConformance
      @param ds
   */  
export interface OnChangePCID_input{
      /**  PCID to validate  */  
   pcid:string,
      /**  Is this the NonConformance PCID  */  
   isNonConformance:boolean,
   ds:Erp_Tablesets_LaborTableset[],
}

export interface OnChangePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param partQty
      @param sysRowID
   */  
export interface OnChangePartQty_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed change to PartQty field  */  
   partQty:number,
      /**  sysRowID of line updated in LaborPart  */  
   sysRowID:string,
}

export interface OnChangePartQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ipEmpID
      @param ipQuickEntryCode
      @param ds
   */  
export interface OnChangeQuickEntryCode_input{
      /**  Proposed EmpID value  */  
   ipEmpID:string,
      /**  Proposed QuickEntryCode value  */  
   ipQuickEntryCode:string,
   ds:Erp_Tablesets_LaborTableset[],
}

export interface OnChangeQuickEntryCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param ipResourceGrpID
   */  
export interface OnChangeResourceGrpID_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed Resource Group  */  
   ipResourceGrpID:string,
}

export interface OnChangeResourceGrpID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param iLaborHedSeq
      @param iLaborDtlSeq
   */  
export interface OnLoadEndActivity_input{
      /**  The LaborHedSeq of the LaborHed record to retrieve  */  
   iLaborHedSeq:number,
      /**  The LaborDtlSeq of the LaborDtl record to retrieve  */  
   iLaborDtlSeq:number,
}

export interface OnLoadEndActivity_output{
   returnObj:Erp_Tablesets_LaborTableset[],
}

   /** Required : 
      @param ds
      @param ProposedResourceID
   */  
export interface OverridesResource_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  The proposed resource id  */  
   ProposedResourceID:string,
}

export interface OverridesResource_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param inOpCode
      @param inResGrpID
   */  
export interface Overrides_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  OpCode to override  */  
   inOpCode:string,
      /**  Resource Group OD to override  */  
   inResGrpID:string,
}

export interface Overrides_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param weeklyView
   */  
export interface RecallFromApprovalBySelected_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Is this method being called with WeeklyView records?  */  
   weeklyView:boolean,
}

export interface RecallFromApprovalBySelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   messageText:string,
}
}

   /** Required : 
      @param ds
      @param lWeeklyView
   */  
export interface RecallFromApproval_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Is this method being called with WeeklyView records?  */  
   lWeeklyView:boolean,
}

export interface RecallFromApproval_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   cMessageText:string,
}
}

   /** Required : 
      @param ip_JobNum
      @param ip_AssemblySeq
      @param ip_OprSeq
   */  
export interface ReportPartQtyAllowed_input{
      /**  Job number  */  
   ip_JobNum:string,
      /**  Assembly Sequence number  */  
   ip_AssemblySeq:number,
      /**  Operation Sequence number  */  
   ip_OprSeq:number,
}

export interface ReportPartQtyAllowed_output{
   returnObj:boolean,
}

   /** Required : 
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface ReviewIsDocumentLock_input{
      /**  Labor Hed Sequence  */  
   laborHedSeq:string,
      /**  Labor Detail Sequence  */  
   laborDtlSeq:string,
}

export interface ReviewIsDocumentLock_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

   /** Required : 
      @param laborDS
      @param selectedWorkQueueRows
      @param empID
      @param resourceGrpID
      @param resourceID
      @param laborType
   */  
export interface SelectAllForWork_input{
   laborDS:Erp_Tablesets_LaborTableset[],
      /**  Selected rows from Work Queue / type WorkQueueTable  */  
   selectedWorkQueueRows:Erp_Tablesets_WorkQueueRow[],
      /**  Employee ID which is starting the activities.  */  
   empID:string,
      /**  Resource Group ID for all activities.  */  
   resourceGrpID:string,
      /**  Resource used for all activities.  */  
   resourceID:string,
      /**  Labor Type, can be 'P' for Production or 'S' for Setup  */  
   laborType:string,
}

export interface SelectAllForWork_output{
parameters : {
      /**  output parameters  */  
   laborDS:Erp_Tablesets_LaborTableset,
   warningsMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface SelectForWorkCheckWarnings_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface SelectForWorkCheckWarnings_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param pcResourceGrpId
      @param pcResourceId
      @param pcLaborType
   */  
export interface SelectForWork_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  The Resource Group id for this work.  */  
   pcResourceGrpId:string,
      /**  The Resource id for this work.  */  
   pcResourceId:string,
      /**  Labor Type: S=Setup, P=Production  */  
   pcLaborType:string,
}

export interface SelectForWork_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface SetClockInAndDisplayTimeMES_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface SetClockInAndDisplayTimeMES_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ipTERetrieveApproved
   */  
export interface SetTERetrieveApproved_input{
      /**  Value to set UserFile.TERetrieveApproved Yes/No  */  
   ipTERetrieveApproved:boolean,
}

export interface SetTERetrieveApproved_output{
}

   /** Required : 
      @param ipTERetrieveByDay
   */  
export interface SetTERetrieveByDay_input{
      /**  Value to set the by day option Yes/No  */  
   ipTERetrieveByDay:boolean,
}

export interface SetTERetrieveByDay_output{
}

   /** Required : 
      @param ipTERetrieveByMonth
   */  
export interface SetTERetrieveByMonth_input{
      /**  Value to set the by month option Yes/No  */  
   ipTERetrieveByMonth:boolean,
}

export interface SetTERetrieveByMonth_output{
}

   /** Required : 
      @param ipTERetrieveByWeek
   */  
export interface SetTERetrieveByWeek_input{
      /**  Value to set the by week option Yes/No  */  
   ipTERetrieveByWeek:boolean,
}

export interface SetTERetrieveByWeek_output{
}

   /** Required : 
      @param ipTERetrieveEntered
   */  
export interface SetTERetrieveEntered_input{
      /**  Value to set UserFile.TERetrieveEntered Yes/No  */  
   ipTERetrieveEntered:boolean,
}

export interface SetTERetrieveEntered_output{
}

   /** Required : 
      @param ipTERetrievePartiallyApproved
   */  
export interface SetTERetrievePartiallyApproved_input{
      /**  Value to set UserFile.TERetrievePartiallyApproved Yes/No  */  
   ipTERetrievePartiallyApproved:boolean,
}

export interface SetTERetrievePartiallyApproved_output{
}

   /** Required : 
      @param ipTERetrieveRejected
   */  
export interface SetTERetrieveRejected_input{
      /**  Value to set UserFile.TERetrieveRejected Yes/No  */  
   ipTERetrieveRejected:boolean,
}

export interface SetTERetrieveRejected_output{
}

   /** Required : 
      @param ipTERetrieveSubmitted
   */  
export interface SetTERetrieveSubmitted_input{
      /**  Value to set UserFile.TERetrieveSubmitted Yes/No  */  
   ipTERetrieveSubmitted:boolean,
}

export interface SetTERetrieveSubmitted_output{
}

   /** Required : 
      @param employeeID
      @param startType
      @param ds
   */  
export interface StartActivityByEmp_input{
      /**  Employee ID  */  
   employeeID:string,
      /**  The type of activity being started.
            Values are: P - Production
            I - Indirect
            S - Setup
            R - Rework  */  
   startType:string,
   ds:Erp_Tablesets_LaborTableset[],
}

export interface StartActivityByEmp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param LaborHedSeq
      @param StartType
      @param ds
   */  
export interface StartActivity_input{
      /**  The labor header sequence  */  
   LaborHedSeq:number,
      /**  The type of activity being started.
            Values are: P - Production
            I - Indirect
            S - Setup
            R - Rework  */  
   StartType:string,
   ds:Erp_Tablesets_LaborTableset[],
}

export interface StartActivity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
      @param weeklyView
   */  
export interface SubmitForApprovalBySelected_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Is this method being called with WeeklyView records?  */  
   weeklyView:boolean,
}

export interface SubmitForApprovalBySelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   messageText:string,
}
}

   /** Required : 
      @param ds
      @param lWeeklyView
   */  
export interface SubmitForApproval_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Is this method being called with WeeklyView records?  */  
   lWeeklyView:boolean,
}

export interface SubmitForApproval_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   cMessageText:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtLaborTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtLaborTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateChargeRateForTimeType_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface ValidateChargeRateForTimeType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param indirectCode
   */  
export interface ValidateIndirectCodeIsDowntime_input{
   indirectCode:string,
}

export interface ValidateIndirectCodeIsDowntime_output{
}

   /** Required : 
      @param projectID
      @param jobNum
      @param laborTypePseudo
   */  
export interface ValidateProjectClosed_input{
   projectID:string,
   jobNum:string,
   laborTypePseudo:string,
}

export interface ValidateProjectClosed_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
   */  
export interface ValidateSerialAfterSelect_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface ValidateSerialAfterSelect_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateSerialBeforeSelect_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface ValidateSerialBeforeSelect_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   notEnoughSerials:string,
   totSNReq:number,
   totNewSNReq:number,
}
}

   /** Required : 
      @param jobNum
      @param assemblySeq
      @param partNum
      @param proposedSN
      @param oprSeq
      @param laborHedSeq
      @param laborDtlSeq
      @param rework
   */  
export interface ValidateSerialScanInterface_input{
      /**  JobNum of the SN  */  
   jobNum:string,
      /**  AssemblySeq of the SN  */  
   assemblySeq:number,
      /**  PartNum of the SN  */  
   partNum:string,
      /**  Proposed SN  */  
   proposedSN:string,
      /**  Operation sequence of the labor detail  */  
   oprSeq:number,
      /**  Labor Head sequence of the labor detail  */  
   laborHedSeq:number,
      /**  Labor Detail sequence of the labor detail  */  
   laborDtlSeq:number,
      /**  Indicates if labor record is rework  */  
   rework:boolean,
}

export interface ValidateSerialScanInterface_output{
}

   /** Required : 
      @param ds
      @param scrapQty
   */  
export interface VerifyScrapQty_input{
   ds:Erp_Tablesets_LaborTableset[],
      /**  Proposed change to ScrapQty field  */  
   scrapQty:number,
}

export interface VerifyScrapQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface VerifySerialMatch_input{
   ds:Erp_Tablesets_LaborTableset[],
}

export interface VerifySerialMatch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   pcMsg:string,
   piMsgType:number,
}
}

   /** Required : 
      @param company
      @param jobNum
      @param assemblySeq
      @param oprSeq
      @param empID
      @param activeTrans
   */  
export interface chkReportQtyShopWarn_input{
      /**  Company ID in ReportQty record  */  
   company:string,
      /**  Job Number in ReportQty record  */  
   jobNum:string,
      /**  Assembly Sequence Number in ReportQty record  */  
   assemblySeq:number,
      /**  Operation Sequence Number in ReportQty record  */  
   oprSeq:number,
      /**  Employee ID in ReportQty record  */  
   empID:string,
      /**  Active Transaction FLAG in ReportQty record  */  
   activeTrans:boolean,
}

export interface chkReportQtyShopWarn_output{
parameters : {
      /**  output parameters  */  
   pcMsg:string,
}
}

   /** Required : 
      @param startDate
      @param startTime
   */  
export interface getElapsedTime_input{
      /**  Initial Date  */  
   startDate:string,
      /**  Initial Time  */  
   startTime:number,
}

export interface getElapsedTime_output{
   returnObj:number,
}

   /** Required : 
      @param ds
      @param laborHedSeq
      @param laborDtlSeq
      @param vDiscrepQty
   */  
export interface validateNonConfProcessed_input{
   ds:Erp_Tablesets_LaborTableset[],
   laborHedSeq:number,
   laborDtlSeq:number,
   vDiscrepQty:number,
}

export interface validateNonConfProcessed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LaborTableset,
   vMessage:string,
}
}

